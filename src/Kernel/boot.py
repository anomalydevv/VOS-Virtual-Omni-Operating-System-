from .Logger import log,clear ,logBool
import time
from pathlib import Path
import os
import json
from .Auth import Register ,CheckAuth,Login
from .fsManager import CreateDisk
from .CLI import main

foundRec=False

def init():
    global foundRec

    logBool("Boot Starting . . .")
    log("Checking for disk existence")
    disk = Path("src/Kernel/Device/VOSdisk.vofs")
    time.sleep(1)
    
    
    if disk.exists() and disk.is_file() and disk.stat().st_size != 0:
        try:
            with open("src/Kernel/Device/VOSdisk.vofs", "r", encoding="utf-8") as f:
                data = json.load(f)
            logBool("Disk found",True)
        except (json.JSONDecodeError, FileNotFoundError):
            logBool("Disk not found", False)
            CreateDisk()
        
    else:
        logBool("Disk not found", False)
        CreateDisk()

    if(CheckAuth()):
        foundRec=True
    else:
        foundRec=False

    time.sleep(1.5)
    clear()
    
    main(foundRec)