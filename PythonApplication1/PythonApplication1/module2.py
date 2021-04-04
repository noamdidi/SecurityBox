import requests

url = 'http://216.58.192.142'

def internet_on():
    try:
        html = requests.get(url)
        print(html)
        return True
    except: 
        return False

i = internet_on()
print(i)