import json
from pathlib import Path
from src.Kernel.Logger import log, logBool

disk = Path("src/Kernel/Device/VOSdisk.vofs")

def CreateDisk():
    log("Disk wizard is creating the disk . . .", 1)

    
    with open(disk, "w", encoding="utf-8") as f:
        json.dump({}, f, indent=4)

    logBool("Disk is ready, closing wizard . . .", True)

def ReadDisk():
    with open(disk,"r") as f:
        return json.load(f)