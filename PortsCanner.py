import socket
import pyfiglet
from colorama import Fore, Back, Style
from datetime import datetime

def get_ports(_input):
    if(_input.isnumeric()):
        return int(_input)
    elif("-" in _input):
        r = _input.split("-",1)
        return range(int(r[0]),int(r[1])+1)
    else:
        raise SystemExit("Please input a valid port number [0 - 65535]")

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.7)
    result = sock.connect_ex((ip,port))
    if not result:
        print(f"Discovered open port {port}")
    sock.close()

def main():
    greenplus = f"{Fore.GREEN}[+]{Style.RESET_ALL}"
    redminus = f"{Fore.LIGHTRED_EX}[-]{Style.RESET_ALL}"
    print(Fore.YELLOW + "\n"+pyfiglet.figlet_format("PortScanner", font="computer"))
    print(Fore.GREEN + "\t\tScan Ports Easier Than Nmap\n")

    try:
        host = input(f"{greenplus} Target ip/hostname: ")
        ports = input(f"{greenplus} Port/Ports to scan [0 - 65535]: ")

        target = socket.gethostbyname(host)
        print(f"Starting scan of {target}")
        print(f"Time started {str(datetime.now())}")

        _ports = get_ports(ports)
        if isinstance(_ports, int):
            scan_port(target,_ports)
        elif isinstance(_ports,range):
            for port in _ports:
                scan_port(target, port)
            print(f"{greenplus} Completed!")
    
    except KeyboardInterrupt:
        print("\r\aQuitting!")
    except ValueError:
        print(f"{redminus} Please enter a valid integer number!")
    except socket.gaierror:
        print(f"{redminus} Could not resolve the hostname!")
    except socket.error:
        print(f"{redminus} Could not connect to the host!")



if __name__=="__main__":
    main()
