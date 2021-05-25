#!/usr/bin/python3

import socket
import pyfiglet
from colorama import Fore, Back, Style


banner = pyfiglet.figlet_format("PortsCanner", font="computer")
print(Fore.YELLOW + banner)
print(Fore.GREEN + "		  Scan Ports Easier Than Nmap	       \n")


ipaddress = input('''[+] INPUT THE IP OF THE TARGET: ''')
port = int(input('''[+] INPUT THE PORT TO SCAN: '''))

try:
    sock = socket.socket()
    sock.settimeout(0.5)
    sock.connect((ipaddress, port))
    print("[+] Port " + str(port) + " is open")

except:
      print("[+] Port " + str(port) + " is close")
