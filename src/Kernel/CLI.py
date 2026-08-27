import os
from .Logger import log,logBool,clear
import time
from .OSDATA import os_name,os_version
import colorama 
from .Auth import getPassword,getUsername,getPermState,CheckAuth,Login,Register
from .Power import Reboot
colorama.init(autoreset=True)
is_run=True

def main(foundRec=False):
    clear()
    time.sleep(2)
    print(f"Welcome to {os_name}")
    
    
    if CheckAuth():
        is_run=Login()
        while(is_run):
            prompt = str(input(f"{colorama.Fore.BLUE}{getUsername()}{colorama.Fore.YELLOW}@{colorama.Fore.CYAN}{getPermState()} {colorama.Fore.GREEN}$~ {colorama.Fore.WHITE}"))
        if(is_run):
            log("Acces Granted")
        else:
            log("Acces Deneid")
            Reboot()
    else:
        Register()
        Reboot()

    clear()

    