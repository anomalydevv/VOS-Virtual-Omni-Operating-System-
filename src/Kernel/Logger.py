import time,colorama,os
from datetime import datetime

def clear():
     os.system('cls' if os.name == 'nt' else 'clear')
     
def log(text, loglevel=0):
    
    now = datetime.now()
    zaman_str = now.strftime("%H:%M:%S")
    
    if loglevel == 0:
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{zaman_str}] {colorama.Fore.CYAN}{text}{colorama.Fore.WHITE}")
    if loglevel == 1:
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{zaman_str}] {colorama.Fore.YELLOW}{text}{colorama.Fore.WHITE}")
    if loglevel == 2:
            print(f"{colorama.Fore.LIGHTBLACK_EX}[{zaman_str}] {colorama.Fore.RED}{text}{colorama.Fore.WHITE}")
def logBool(text,__BOOL__=True):
    now = datetime.now()
    zaman_str = now.strftime("%H:%M:%S")
    if(__BOOL__):
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{zaman_str}] {colorama.Fore.WHITE}[{colorama.Fore.GREEN} OK {colorama.Fore.WHITE}] {text}")
    else:
        print(f"{colorama.Fore.LIGHTBLACK_EX}[{zaman_str}] {colorama.Fore.WHITE}[{colorama.Fore.RED} FAIL {colorama.Fore.WHITE}] {text}")