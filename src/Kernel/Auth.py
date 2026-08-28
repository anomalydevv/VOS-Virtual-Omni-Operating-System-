from .fsManager import ReadDisk
from .Logger import logBool,log
import json

data=ReadDisk()

def CheckAuth() -> bool:
    if data.get("AuthManager") is not None:
        logBool("Record found", True)
        return True
    else:
        logBool("Record not found", False)
        return False

def Register():
    log("Please create a user account. Warning: This account inherently default holds operator privileges.")
    print("sign in username")
    username = input(": ")
    print("sign in password")
    password = input(": ")
    
    
    if "AuthManager" not in data:
        data["AuthManager"] = {}

    data["AuthManager"]["USERNAME"]=username
    data["AuthManager"]["PASSWORD"]=str(password)
    data["AuthManager"]["PERM"]="OPERATOR"
    with open("src/Kernel/Device/VOSdisk.vofs", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Register Succes")

def Login():
    log("Please log in to your user account . . .")
    print("sign in username")
    username = input(": ")
    print("sign in password")
    password = input(": ")

    if(data.get("AuthManager") and data["AuthManager"].get("USERNAME")==username and data["AuthManager"].get("PASSWORD")==str(password)):
        print("Login Succesful")
        return True
    else:
        print("Login Fail")
        return False
    
def getUsername()->str:
    return data["AuthManager"].get("USERNAME")
def getPassword()->str:
    return data["AuthManager"].get("PASSWORD")
def getPermState()->str:
    return data["AuthManager"].get("PERM")