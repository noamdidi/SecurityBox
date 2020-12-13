import getmac
import requests
import time

URL = "https://api.macvendors.com/"
for i in range (0, 255):
    gen_ip = "10.100.102." + str(i)
    if(getmac.get_mac_address(ip=gen_ip) != None):
        print("IP ADDRESS: " + gen_ip)
        print("MAC ADDRESS: " + getmac.get_mac_address(ip=gen_ip))
        #PARAMS = {"":getmac.get_mac_address(ip=gen_ip)}
        URL += getmac.get_mac_address(ip=gen_ip)
        r = requests.get(url = URL) 
        print(r.url)
        print("MANIFACTURER: " + r.text)
        URL = "https://api.macvendors.com/"
        time.sleep(1)
