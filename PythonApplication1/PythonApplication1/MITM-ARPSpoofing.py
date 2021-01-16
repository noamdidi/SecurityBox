from scapy.all import Ether, ARP, srp, sniff, conf
import socket
import os
import subprocess
from subprocess import check_output
from xml.etree.ElementTree import fromstring
from ipaddress import IPv4Interface, IPv6Interface

def getNics() :

    cmd = 'wmic.exe nicconfig where "IPEnabled  = True" get ipaddress,MACAddress,IPSubnet,DNSHostName,Caption,DefaultIPGateway /format:rawxml'
    xml_text = check_output(cmd, creationflags=8)
    xml_root = fromstring(xml_text)

    nics = []
    keyslookup = {
        'DNSHostName' : 'hostname',
        'IPAddress' : 'ip',
        'IPSubnet' : '_mask',
        'Caption' : 'hardware',
        'MACAddress' : 'mac',
        'DefaultIPGateway' : 'gateway',
    }

    for nic in xml_root.findall("./RESULTS/CIM/INSTANCE") :
        # parse and store nic info
        n = {
            'hostname':'',
            'ip':[],
            '_mask':[],
            'hardware':'',
            'mac':'',
            'gateway':[],
        }
        for prop in nic :
            name = keyslookup[prop.attrib['NAME']]
            if prop.tag == 'PROPERTY':
                if len(prop):
                    for v in prop:
                        n[name] = v.text
            elif prop.tag == 'PROPERTY.ARRAY':
                for v in prop.findall("./VALUE.ARRAY/VALUE") :
                    n[name].append(v.text)
        nics.append(n)

        # creates python ipaddress objects from ips and masks
        for i in range(len(n['ip'])) :
            arg = '%s/%s'%(n['ip'][i],n['_mask'][i])
            if ':' in n['ip'][i] : n['ip'][i] = IPv6Interface(arg)
            else : n['ip'][i] = IPv4Interface(arg)
        del n['_mask']

    return nics

def get_mac(ip):
    """
    Returns the MAC address of `ip`, if it is unable to find it
    for some reason, throws `IndexError`
    """
    p = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    result = srp(p, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc

def process(packet):
    # if the packet is an ARP packet
    if packet.haslayer(ARP):
        # if it is an ARP response (ARP reply)
        print("ccc")
        if packet[ARP].op == 2:
            try:
                # get the real MAC address of the sender
                real_mac = get_mac(packet[ARP].psrc)
                # get the MAC address from the packet sent to us
                response_mac = packet[ARP].hwsrc
                # if they're different, definetely there is an attack
                if real_mac != response_mac:
                    print(f"[!] You are under attack, REAL-MAC: {real_mac.upper()}, FAKE-MAC: {response_mac.upper()}")
            except IndexError:
                # unable to find the real mac
                # may be a fake IP or firewall is blocking packets
                pass

if __name__ == "__main__":
    import sys
    nics = getNics()
    for nic in nics :
        for k,v in nic.items() :
            #print('%s : %s'%(k,v))
            if 'Wireless' in v:
                wifiIface = v
        
    wifiIface = wifiIface[11:]
    try:
        iface = wifiIface
        print(iface)
    except IndexError:
        print('e')
        iface = conf.iface

    sniff(store=False, prn=process, iface=iface)
