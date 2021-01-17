import subprocess
import os
from scapy.all import *
import netaddr
import collections

def detector(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated

def main():
    #print('list of all networks\n\n')

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
    #print(ssids)
    i = 0
    while i < len(ssids):
        if len(ssids[i].split(':')) > 1:
            retVal += ssids[i].split(':')[1][1:]
            retVal += '\n'
        i += 1
    detect = retVal.split('\n')
    if len(detector(detect)):
        print("Warning: two networks by names", detector(detect), ". Recommention: Do not connect to any of them.\n")
    else:
        print("Everything's OK\n")

if __name__ == "__main__":
    main()


"""import subprocess
import ctypes
import webbrowser

#Define filename to write SSIDs/Keys to
FNAME = 'keys.txt'

#Define function that gathers list of profiles from host machine
def nabProfiles():
	#Set cmd to netsh profile query shell, pass it to shell
	cmd = "netsh wlan show profiles"
	output = subprocess.check_output(cmd)
	temp = output.decode() 
	print(temp)
	output2 = output.decode('utf-8').split("\r\n")
	
	#init list of profiles, load them into list
	profileList = []
	for i in range(0,len(output2)):
		#Check for existence of phrase "Profile" in return line, split off after colon, take right side of split into list
		if ("Profile" in output2[i]):
			if not ("Profiles" in output2[i]):
				profileName = output2[i].split(": ")
				profileList.append(profileName[1])
	#Send back the parsed list of profile names
	return profileList

#Define function that checks wlan profiles based on gathered list of profile names
def nabKeys(profileList):
	#init local function variables
	entry = []
	bulkout = []
	WEP = False
	textout = []
	#iterate list of profiles, return output of each profile
	for i in range(0,len(profileList)):
		cmd = 'netsh wlan show profile name="' + profileList[i] + '" key=clear'
		output = subprocess.check_output(cmd)
		#begin parsing out nonsense, starting at line breaks
		output = output.split("\r\n")
		for j in range(0,len(output)):
			#check for SSID name phrase, if so, parse, load into output list
			if ("SSID name" in output[j]):
				output[j] = output[j].replace("    ","")
				textout.append(output[j])
			#do same for phrase WEP, also, set bool to True to check for WEP key and decode into ASCII
			if ("WEP" in output[j]):
				WEP = True
			if ("Key Content" in output[j]):
				output[j] = output[j].split(": ")[1]
				if WEP:
					WEP = False
					textout.append("WEP KEY: \nHex:" + output[j] + "\nASCII: "+output[j].decode("hex"))
				else:
					textout.append("WPA KEY: " + output[j])
			#if no authentication for profile, no key info will exist
			if ("None" in output[j]):
				textout.append("No key information for this profile.")
	return textout

#Define function to collect profile names, keys, and return data
def gatherInfo():
	profiles = nabProfiles()
	textout = nabKeys(profiles)
	return textout

#Define function that gathers input from shell, writes to keyfile
def writeInfo():
	textout = gatherInfo()
	texto = ""
	f = open(FNAME,'w')
	f.write('SSID/Keys:\n====================\n\n')
	for i in range(0,len(textout)):
		f.write(textout[i]+'\n')
		texto = texto + textout[i] + "\n"
		texto = textout[i]
		if not ("SSID" in textout[i]):
			f.write('\n=================\n\n')
	ctypes.windll.user32.MessageBoxA(0, 'SSID Keys written to file '+FNAME,'SSID Keys',0)
	
writeInfo()
webbrowser.open(FNAME)
"""