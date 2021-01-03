
import sys
import subprocess
from subprocess import *
import os
from scapy.all import *
import netaddr

def findNets():
    print('list of all networks\n\n')

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
    print(ssids)
    i = 0
    while i < len(ssids):
        if len(ssids[i].split(':')) > 1:
            retVal += ssids[i].split(':')[1][1:]
            retVal += '\n'
        i += 1
    return retVal

def main():
    nets = ''
    netToConnect = 0
    nets = findNets()
    nets = nets.split('\n')
    print(nets)
    netToConnect = input("choose network by number: ")
    sCommand = ["netsh","wlan","Connect",nets[int(netToConnect) - 1]]
    SUInfo = subprocess.STARTUPINFO()
    SUInfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
    SUInfo.sShowWindow = SW_HIDE
    Popen(sCommand,startupinfo=SUInfo)

if __name__ == "__main__":
    main()