import fs
import Kernel
import sys
class Auth:
    def __init__(self):
        disk = fs.read()
        if disk.get("USER") is None or disk.get("PASSWORD") is None:
            print("No records found")
            print("\n -------------")
            print("sign in username")
            username = input(": ")
            fs.dataOBJ("USER",username)
            print("sign in password")
            password = input(": ")
            fs.dataOBJ("PASSWORD",password)
        else:
            print("Welcome Again please sign in username")
            loginUsername= input(": ")
            print("Sign in password")
            loginPass=input(": ")
            if(loginUsername==disk.get("USER") and loginPass==disk.get("PASSWORD")):
                print("Login Succesful")
            else:
                print("Login Fail")
                sys.exit(20)
    
    