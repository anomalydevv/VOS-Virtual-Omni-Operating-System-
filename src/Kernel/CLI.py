import os
from .Logger import log, logBool, clear
import time
from .OSDATA import os_name, os_version,build_no
import colorama
from .Auth import getPassword, getUsername, getPermState, CheckAuth, Login, Register
from .Power import Reboot

colorama.init(autoreset=True)

is_run = True


def main(foundRec=False):
    global is_run

    clear()
    time.sleep(2)

    print(f"Welcome to {os_name}")

    if CheckAuth():
        is_run = Login()
        time.sleep(1.5)
        clear()
        print("Welcome To ",os_name,os_version, "Build NO: ",build_no)
        while is_run:
            prompt = str(
                input(
                    f"{colorama.Fore.BLUE}{getUsername()}"
                    f"{colorama.Fore.YELLOW}@"
                    f"{colorama.Fore.CYAN}{getPermState()} "
                    f"{colorama.Fore.GREEN}$~ "
                    f"{colorama.Fore.WHITE}"
                )
            )

        if is_run:
            log("Acces Granted")
        else:
            log("Acces Deneid")
            Reboot()

    else:
        Register()
        Reboot()

    clear()
