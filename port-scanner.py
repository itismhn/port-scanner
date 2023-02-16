import os,socket,sys,time
from queue import Queue
import threading
from datetime import datetime

os.system('cls')


def input_validation():
    print("[~]Enter 1 for scan [1-1024] ports\n[~]Enter 2 for scan [1-65535] ports\n[~]Enter 3 for scan custom ports")
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
        

def option_1():
    print(1)

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
    print(input_start,input_end)
    
    
input_validation()