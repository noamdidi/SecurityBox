import socket
import getmac
import os
import sys
import requests
import time
import threading
#import subprocess      # currently in check
from subprocess import *
from scapy.all import *
import netaddr
import netifaces
from subprocess import check_output
from xml.etree.ElementTree import fromstring
from ipaddress import IPv4Interface, IPv6Interface

LISTEN_PORT = 447
data_strings = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

class myThread (threading.Thread):
   def __init__(self, threadID, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.counter = counter
   def run(self):
      get_some_devices_data(self.counter, self.counter+16, self.threadID)

# NETS DETECT DECTION:

def find_nets():
    #print('list of all networks\n\n')

    results = subprocess.check_output(["netsh", "wlan", "show", "network"])

    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    x = 0
    retVal = ''
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    #print(ssids)
    i = 0
    while i < len(ssids):
        if len(ssids[i].split(':')) > 1:
            retVal += ssids[i].split(':')[1][1:]
            retVal += '\n'
        i += 1
    return retVal

def get_nets():
    nets = ''
    #netToConnect = 0
    nets = find_nets()
    nets = nets.split('\n')
    #return '#'.join(nets)[:-1]
    return nets
    

def login_net(nets, netToConnect):
    #netToConnect = input("choose network by number: ")
    sCommand = ["netsh","wlan","Connect",nets[int(netToConnect) - 1]]
    SUInfo = subprocess.STARTUPINFO()
    SUInfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
    SUInfo.sShowWindow = SW_HIDE
    Popen(sCommand,startupinfo=SUInfo)

# DEVICES DETECT SECTION:

def get_some_devices_data(strt, fnsh, place):
    URL = "https://api.macvendors.com/"
    for i in range (strt, fnsh):
        global data_strings
        gen_ip = "10.100.102." + str(i)
        #print(i)
        if(getmac.get_mac_address(ip=gen_ip) != None):
            #print("IP ADDRESS: " + gen_ip)
            #print("MAC ADDRESS: " + getmac.get_mac_address(ip=gen_ip))
            
            URL += getmac.get_mac_address(ip=gen_ip)
            r = requests.get(url = URL) 
            #print(r.url)
            if "error" in r.text:
                pass
            else:
                #print("MANIFACTURER: " + r.text)
                if gen_ip and getmac.get_mac_address(ip=gen_ip) and r.text:
                    data_strings[place] += gen_ip 
                    data_strings[place] += "#"
                    data_strings[place] += getmac.get_mac_address(ip=gen_ip)
                    data_strings[place] += "#"
                    data_strings[place] += r.text
                    data_strings[place] += "#"
            URL = "https://api.macvendors.com/"
            time.sleep(0.1)
    #print(data_string[:-1])

def get_all_devices_data():
    threads_list = []
    count = 0
    for place in range (0, 16):
        threads_list.append(myThread(place, count))
        threads_list[place].start()
        count += 16
    for t in threads_list:
        t.join()
    fake_data_strings = data_strings
    for s in data_strings:
        s = ""
    
    #print("".join(fake_data_strings)[:-1])
    return "".join(fake_data_strings)[:-1]

# EVIL TWIN DETECTOR SECTION:

def et_detector(x):
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated

def et_results():
    #print('list of all networks\n\n')

    results = subprocess.check_output(["netsh", "wlan", "show", "network"])

    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    
    x = 0
    retVal = ''
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    #print(ssids)
    i = 0
    while i < len(ssids):
        if len(ssids[i].split(':')) > 1:
            retVal += ssids[i].split(':')[1][1:]
            retVal += '\n'
        i += 1
    detect = retVal.split('\n')
    if len(et_detector(detect)):
        return "Warning: two networks by names" + " | ".join(et_detector(detect)) + ". Recommendation: Do not connect to any of them."
    else:
        return "Everything's OK"

# MAN IN THE MIDDLE DETECT SECTION:

def mitm_get_nics() :

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

def mitm_get_mac(ip):
    """
    Returns the MAC address of `ip`, if it is unable to find it
    for some reason, throws `IndexError`
    """
    p = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    result = srp(p, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc

def mitm_process(packet):
    # if the packet is an ARP packet
    if packet.haslayer(ARP):
        # if it is an ARP response (ARP reply)
        if packet[ARP].op == 2:
            try:
                # get the real MAC address of the sender
                real_mac = mitm_get_mac(packet[ARP].psrc)
                # get the MAC address from the packet sent to us
                response_mac = packet[ARP].hwsrc
                # if they're different, definetely there is an attack
                if real_mac != response_mac:
                    #return "[!] You are under attack, REAL-MAC: {" + real_mac.upper() + "}, FAKE-MAC: {" + response_mac.upper() + "}"
                    return "[!] You are under attack"
            except IndexError:
                # unable to find the real mac
                # may be a fake IP or firewall is blocking packets
                pass
            
def mitm_detector():
    nics = mitm_get_nics()

    for nic in nics :
        for k,v in nic.items() :
            #print('%s : %s'%(k,v))
            if 'Wireless' in v:
                wifiIface = v
    wifiIface = wifiIface[11:]
    try:
        iface = wifiIface
        #print(iface)
    except IndexError:
        print('e')
        iface = conf.iface
        
    return sniff(store=False, prn=mitm_process, iface=iface, timeout=5)

def server_manage(instruct, additional_param): # if there is no need in additonal parameter, let additonal_param = NULL
    #manage = {
        #1: get_nets,
        #2: login_net,
        #3: get_all_devices_data,
        #4: "April",
        #5: "May",
    #}
    #func = manage.get(instruct, lambda: "Invalid Command")
    #func()
    if instruct == 1:
        return '#'.join(get_nets())[:-1]
    elif instruct == 2:
        login_net(get_nets(), int(additional_param))
        return "logged successfully"
    elif instruct == 3:
        #start = time.time() OPTIONAL
        return get_all_devices_data()
        #end = time.time()   OPTIONAL
        #print(end - start)  OPTIONAL
    elif instruct == 4:
        return et_results()
    elif instruct == 5:
        return mitm_detector()

if __name__ == "__main__":
    
    # Create a TCP/IP socket
    listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding to local port 447
    server_address = ('', LISTEN_PORT)
    listening_sock.bind(server_address)

    while(True):
        # Listen for incoming connections
        listening_sock.listen(1)

        # Create a new conversation socket
        client_soc, client_address = listening_sock.accept()

        client_msg = client_soc.recv(1024)
        client_msg = client_msg.decode()
        data_recvd = client_msg.split('#')

        msg = server_manage(int(data_recvd[0]), data_recvd[1])
        client_soc.sendall(msg.encode())



    
