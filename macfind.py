import getmac
import requests
import time
import winwifi
import subprocess as S


txt = S.check_output(["netsh", "wlan", "show", "networks"])
print (txt.decode())

#winwifi.WinWiFi.connect('Cohen1')

import os

class Finder:
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

    def run(self):
        command = """iwlist wlp2s0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        result = os.popen(command.format(self.server_name))
        result = list(result)

        if "Device or resource busy" in result:
                return None
        else:
            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
            print("Successfully get ssids {}".format(str(ssid_list)))

        for name in ssid_list:
            try:
                result = self.connection(name)
            except Exception as exp:
                print("Couldn't connect to name : {}. {}".format(name, exp))
            else:
                if result:
                    print("Successfully connected to {}".format(name))

    def connection(self, name):
        try:
            os.system("nmcli d wifi connect {} password {} iface {}".format(name,
       self.password,
       self.interface_name))
        except:
            raise
        else:
            return True

def get_devices_data():
    data_string = ""
    URL = "https://api.macvendors.com/"
    for i in range (0, 20):
        gen_ip = "10.100.102." + str(i)
        print(i)
        if(getmac.get_mac_address(ip=gen_ip) != None):
            print("IP ADDRESS: " + gen_ip)
            print("MAC ADDRESS: " + getmac.get_mac_address(ip=gen_ip))
            data_string += gen_ip 
            data_string += "#"
            data_string += getmac.get_mac_address(ip=gen_ip)
            data_string += "#"
            URL += getmac.get_mac_address(ip=gen_ip)
            r = requests.get(url = URL) 
            #print(r.url)
            if "error" in r.text:
                pass
            else:
                print("MANIFACTURER: " + r.text)
                data_string += r.text
                data_string += "#"
            URL = "https://api.macvendors.com/"
            time.sleep(0.1)
    print(data_string[:-1])

if __name__ == "__main__":
    # Server_name is a case insensitive string, and/or regex pattern which demonstrates
    # the name of targeted WIFI device or a unique part of it.
    #server_name = ""
    #password = ""
    #interface_name = "wlp2s0" # i. e wlp2s0  
    #F = Finder(server_name=server_name,
               #password=password,
               #interface=interface_name)
    #F.run()
    get_devices_data()
