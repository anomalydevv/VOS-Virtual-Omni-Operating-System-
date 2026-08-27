import time
import sys
import os

from src.Kernel.Logger import log, clear

def Shutdown(e=0):
    clear()
    time.sleep(1)
    log("Shutdown . . .")
    sys.stdout.flush()
    time.sleep(2)
    clear()
    sys.exit(e)

def Reboot(e=0):
    clear()
    time.sleep(1)
    log("Rebooting . . .")
    sys.stdout.flush()
    time.sleep(2)
    clear()
    
    python = sys.executable
    os.execv(python, [python] + sys.argv)