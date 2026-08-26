import os
import Kernel
import time
import sys
import Auth
import User
import fs
import colorama 

colorama.init(autoreset=True)
class cli:
    def __init__(self):
        def clearScreen():
            os.system('cls' if os.name == 'nt' else 'clear')
        print("""
 ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
 ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
  ▐░▌         ▐░▌  ▐░▌       ▐░▌▐░▌          
   ▐░▌       ▐░▌   ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
    ▐░▌     ▐░▌    ▐░▌       ▐░▌▐░░░░░░░░░░░▌
     ▐░▌   ▐░▌     ▐░▌       ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
      ▐░▌ ▐░▌      ▐░▌       ▐░▌          ▐░▌
       ▐░▐░▌       ▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄▄▄▄▄█░▌
        ▐░▌        ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
         ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                                             """)
        time.sleep(3)
        Auth.Auth()
        clearScreen()
        while(Kernel.isRun):
            prompt = input(f"{colorama.Fore.GREEN}{fs.read().get('USER')}{colorama.Fore.CYAN}@{colorama.Fore.GREEN}{User.user}{colorama.Style.RESET_ALL}:{colorama.Fore.BLUE}~{colorama.Style.RESET_ALL}$ ")
            if(prompt=="shutdown"):
                time.sleep(0.4)
                clearScreen()
                time.sleep(0.2)
                Kernel.LoggerService.log("Shutdown",1)
                time.sleep(2)
                sys.exit(1)
            elif(prompt.startswith("run")):
                code=prompt[4:].strip()
                exec(code)
            
            elif(prompt.startswith("mirror")):
                text=prompt[7:]
                print(text)
            elif(prompt=="sysinfo"):
                print(f"""
                OS : {Kernel.os_name} 
                Version: {Kernel.version}
                """)
            else:
                Kernel.LoggerService.log(f""" "{prompt}" Unknow Command""",2)
                