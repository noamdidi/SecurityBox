#---------------------- working ----------------------#

import subprocess
import os
from scapy.all import *
import netaddr

def main():
    print('list of all networks\n\n')

    results = subprocess.check_output(["netsh", "wlan", "show", "network"])

    results = results.decode("ascii") # needed in python 3
    results = results.replace("\r","")
    ls = results.split("\n")
    ls = ls[4:]
    ssids = []
    ssidsNumber = []
    x = 0
    retVal = ''
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1
    print(ssids)
    i = 0
    while i < len(ssids):
        if len(ssids[i].split(':')) > 1:
            retVal += ssids[i].split(':')[1][1:]
            retVal += '\n'
        i += 1
    print(retVal)

if __name__ == "__main__":
    main()