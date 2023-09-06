#!/usr/bin/python3
#Coded by Morbius.os

import os
try:
    import json
except:
    os.system('pip install json')
try:
    import requests
except:
    os.system('pip install requests')
try:
    from urllib.request import urlopen
except:
    os.system('pip install urllib.request')
    
AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

def animasyon(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(10. / 100)

def hızlı_ani(yazi):
     for u in yazi + '\n' :
         sys.stdout.write(u)
         sys.stdout.flush()
         time.sleep(10. / 250)
         
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'#


def banner():
    print(f"""
{YELLOW} __  __            _     _            {RED} ___         _____        
{YELLOW}|  \/  | ___  _ __| |__ (_)_   _ ___  {RED}|_ _|_ __   |_   _|__        
{YELLOW}| |\/| |/ _ \| '__| '_ \| | | | / __|  {RED}| || '_ \    | |/ _ \        
{YELLOW}| |  | | (_) | |  | |_) | | |_| \__ \  {RED}| || |_) |   | | (_) |        
{YELLOW}|_|  |_|\___/|_|  |_.__/|_|\__,_|___/ {RED}|___| .__/    |_|\___/        
                                          |_|            
{BLUE}             _                    _   _                        
            | |    ___   ___ __ _| |_(_) ___  _ __        
            | |   / _ \ / __/ _` | __| |/ _ \| '_ \        
            | |__| (_) | (_| (_| | |_| | (_) | | | |        
            |_____\___/ \___\__,_|\__|_|\___/|_| |_|        
  
{GREEN}Author: {AUTHOR}
Instagram: {INSTAGRAM}
Github: {GİTHUB} 
{END}
""")

banner()

query = input('''
{}┌──({}root㉿m-scan{})-[{}ToolMenu{}]
└─{}# {}m-location '''.format(BLUE,RED,BLUE,END,BLUE,RED,END))

URL = 'http://ip-api.com/json/{}'.format(query)
r = requests.get(URL)
y = json.loads(r.text)
               
URL2 = 'https://proxycheck.io/v2/{}?vpn=1&asn=1'.format(query)
r2 = requests.get(URL2)
y2 = json.loads(r2.text)
a = y2

with open(".veriler.txt", "w") as veriFile:
    json.dump(a, veriFile)               

with open(".veriler.txt", "r") as veriFile:
    veriler = json.load(veriFile)               

               
GoogleMapsLink = 'http://www.google.com/maps/place/{0},{1}/@{0},{1},16z'.format(y["lat"],y["lon"],y["lat"],y["lon"])
               
print('''{}{}
Target: {}
Country: {}
Country Code: {}
City: {}
City Code: {}
ZİP Code: {}
Timezone: {}
ISP: {}
Internet Service Provider: {}
Internet Service: {}
Autonomous System Number: {}
Google Maps Link: {}{}{}{}{}

{}Proxy İnformation:
'''.format(GREEN,BOLD,y['query'],y['country'],y["countryCode"],y["regionName"],y["region"],y["city"],y["zip"],y['timezone'],y['org'],y['isp'],y['as'],UNDERLINE,GoogleMapsLink,END,GREEN,END,BOLD))

if query in veriler:
                   birinci = veriler[query]
                   proxy = birinci.get('proxy')
                   ikinci = birinci['currency']
                   tip = birinci.get('type')

if proxy is not None:
    print('{}{}Proxy : {}'.format(GREEN,BOLD,proxy))

if tip is not None:
                print('{}{}Proxy Type: {}'.format(GREEN,BOLD,tip))
                
os.remove(".veriler.txt")
print(END+BOLD+'\nWhois İnformation:\n'+GREEN)
try:
    os.system('whois {}'.format(query))
except:
    os.system('apt install whois')
time.sleep(10)