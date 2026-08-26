from datetime import datetime
import colorama
import fs
import climage
import CLI
isRun=True
build_no=0.1
version=1
os_name="VOS"
class LoggerService:
    @staticmethod
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
class Main:
    def __init__(self):
        self.exitCode=0
        colorama.init(autoreset=True)
        LoggerService.log("Kernel Starting...")
        CLI.cli()
        self.isRun=True
    def Shutdown(self):
        LoggerService.log(self.exitCode," Shutdown")
        
if __name__ == "__main__":
    krnl = Main()