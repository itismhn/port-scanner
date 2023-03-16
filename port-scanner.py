import os,socket,sys,time
import ipaddress
#v2.2 modules
from stem import Signal
from stem.control import Controller
from urllib.request import urlopen

os.system('cls')
def ip_validator(ip):
    try:
        address = ipaddress.ip_address(ip)
        tor_func()
    except ValueError:
        print("IP address {} is not valid".format(ip)) 

#-----tor-----

controller = Controller.from_port(port=9051)

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def renewTor():
    controller.authenticate("123")
    controller.signal(Signal.NEWNYM)

def showIP():
    print(urlopen('http://icanhazip.com').read())

def tor_func():
    tor=input("[~]Integrate with TOR [Y/N]:")
    global tor_flag
    if(tor=='y' or tor=='Y'):
        tor_flag=1
        input_validation()
    elif (tor=='n' or tor=='N'):
        tor_flag=0
        input_validation()

#-----tor-----

def input_validation():
    time.sleep(1)
    print("\n[~]Enter 1 for scan [1-1024] ports\n[~]Enter 2 for scan [1-65535] ports\n[~]Enter 3 for scan custom ports")
    while True:
        try:   
            input_option =int(input("[~]Enter Number:"))
            if input_option in [1,2,3]:
                if input_option==1:
                    option_1()
                elif input_option==2:
                    option_2()
                elif input_option==3:
                    option_3()
                    break
            else:
                print('[~]please choose valid option\n')
        except KeyboardInterrupt:
            break
        except :
            print('[~]oops! Enter a valid Charecters!\n')
    
def scan(num,host,portStart,portEnd):
    if (tor_flag==1):
        pass
    elif (tor_flag==0):

        print('\nscanning started...\n')
        open_ports=[]
        if num == 1:
            portRange=range(1,1025)
        elif num == 2:
            portRange=range(1,65536)
        else:
            portRange=range(portStart,portEnd+1)
        for port in portRange:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
                    scan.settimeout(1)
                    print(f"(~)Scanning port {port} on target:{host}")
                    scan.connect((host, port))
                    open_ports.append(port)
            except KeyboardInterrupt:
                print("\nExiting...")
                for port in open_ports:
                    print(f"Port {port} is OPEN on {host}")
                sys.exit()
            except:
                pass
        print('\n')
        for port in open_ports:
                print(f"Port {port} is OPEN on {host}.")



def option_1():
    scan(1,ip,0,0)

def option_2():
    scan(2,ip,0,0)

def option_3():
    time.sleep(0.8)
    os.system('cls')
    try:   
        input_start =int(input("[~]Enter Start PortNumber:"))
        input_end =int(input("[~]Enter End PortNumber:"))
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    except:
        print('[~]oops! Enter a valid Charecter!\n')
        time.sleep(1)
        option_3()
        return()
    scan(3,ip,input_start,input_end)    
ip=input("[~]Enter Ip:")
ip_validator(ip)