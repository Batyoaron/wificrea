import random
import time
import string
import os
import pyfiglet
import random
import string
os.system('clear')
def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    # print random string
    print(result_str)
    
random_string = "result_str"
result_str = "password"

# string of length 8

print("\033[1;31;40m \n")
ascii_banner = pyfiglet.figlet_format("wificrea-py")
print(ascii_banner)
print("\033[1;33;40m \n")
print('                                   by: BatyoAron')
print('                                   update version: 2')
print("\033[1;32;40m \n")
print('')
print("\033[1;36;40m \n")
print('dont forget to turn wifi on (NO MOBILE WIFI)')
import requests
print('')
url = "http://www.kite.com"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print("\033[1;31;40m \n")
    
	print("turn off the mobile net/ or disconnect from the wifi and try again")
	exit()
except (requests.ConnectionError, requests.Timeout) as exception:
	print("\033[1;32;40m \n")
	print("everything looks good")
print('')
print("\033[1;33;40m \n")
# import module

import os
 
# function to establish a new connection

def createNewConnection(name, SSID, password):

    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">

    <name>"""+name+"""</name>

    <SSIDConfig>

        <SSID>

            <name>"""+SSID+"""</name>

        </SSID>

    </SSIDConfig>

    <connectionType>ESS</connectionType>

    <connectionMode>auto</connectionMode>

    <MSM>

        <security>

            <authEncryption>

                <authentication>WPA2PSK</authentication>

                <encryption>AES</encryption>

                <useOneX>false</useOneX>

            </authEncryption>

            <sharedKey>

                <keyType>passPhrase</keyType>

                <protected>false</protected>

                <keyMaterial>"""+password+"""</keyMaterial>

            </sharedKey>

        </security>

    </MSM>
</WLANProfile>"""

    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"

    with open(name+".xml", 'w') as file:

        file.write(config)

    os.system(command)
 
# function to connect to a network    

def connect(name, SSID):

    command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"

    os.system(command)
 
# function to display avavilabe Wifi networks    

def displayAvailableNetworks():

    command = "netsh wlan show networks interface=Wi-Fi"

    os.system(command)
 
 
# display available netwroks
displayAvailableNetworks()
 
# input wifi name and password

name = input("Name of Wi-Fi: ")
time.sleep(3)
count = 0
while (count < 100):

 count = count + 1
 print("\033[1;32;40m \n")
 get_random_string(5000)
 print('')
 print('looks good')
time.sleep(3)
 

 
# establish new connection




import secrets

os.system('clear')
password_length = 13
password_lenght =7
print(secrets.token_urlsafe(password_length))
print(secrets.
token_urlsafe(password_length))
time.sleep(0.5)
count = 0

while (count < 100000):    

    count = count + 1
     
    print("\033[1;32;40m \n")
    get_random_string(5)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    
    print("\033[1;32;40m \n")
    get_random_string(6)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    print("\033[1;32;40m \n")
    get_random_string(7)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    print("\033[1;32;40m \n")
    get_random_string(8)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    print("\033[1;32;40m \n")
    get_random_string(9)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    print("\033[1;32;40m \n")
    get_random_string(10)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    print("\033[1;32;40m \n")
    get_random_string(11)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    print("\033[1;32;40m \n")
    get_random_string(12)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    print("\033[1;32;40m \n")
    get_random_string(13)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    print("\033[1;32;40m \n")
    get_random_string(14)
    time.sleep(1)
    print("\033[1;31;40m \n")
    print('wrong password')
    url = "http://www.kite.com"
    try:
        request = requests.get(url, timeout=timeout)
        print('password cracked with one of the last 15 password you see/or connected to the wifi')
        exit()
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("still nothing")



    
    
 
# connect to the wifi network
    
    
    
print("\033[1;31;40m \n")
print("password is too powerful to crack / the internet is not turned on ):") 
