import subprocess

def finder(x):
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated

def detector():
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
    if len(finder(detect)):
        return "Warning: two networks by names" + " | ".join(finder(detect)) + ". Recommendation: Do not connect to any of them."
    else:
        return "Everything's OK"