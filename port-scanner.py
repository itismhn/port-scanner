import os,socket,sys,time
from queue import Queue
import threading
from datetime import datetime
import ipaddress

os.system('cls')

def ip_validator(ip):
    try:
        address = ipaddress.ip_address(ip)
        input_validation()
    except ValueError:
        print("IP address {} is not valid".format(ip)) 

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
    print('starting scan')
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
                print(host,port)
                scan.connect((host, port))
                open_ports.append(port)
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()
        except:
            pass
    for port in open_ports:
            print(f"Port {port} is OPEN on {host}.")



def option_1():
    scan(1,ip,0,0)

def option_2():
    print(2)

def option_3():
    time.sleep(1)
    os.system('cls')
    try:   
        input_start =int(input("[~]Enter Start PortNumber:"))
        input_end =int(input("[~]Enter End PortNumber:"))
    except KeyboardInterrupt:
        return()
    except:
        print('[~]oops! Enter a valid Charecter!\n')
        time.sleep(1)
        option_3()
        return()
    scan(3,ip,input_start,input_end)    
ip=input("[~]Enter Ip:")
ip_validator(ip)