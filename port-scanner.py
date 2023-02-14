def input_validation():
    print("[~]Enter 1 for scan [1-1024] ports\n[~]Enter 2 for scan [1-65535] ports\n[~]Enter 3 for scan custom ports")
    option =int(input("Enter Number:"))
    if option in [1,2,3]:
        print('ok')
    else:
        print('please choose valid option')

input_validation()
