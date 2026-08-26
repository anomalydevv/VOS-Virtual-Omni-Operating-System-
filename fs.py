import Kernel
import json

fs_name="VOFS"
disk = "VOSdisk.vofs"

class dataOBJ:
    def __init__(self,key,val):
        self.data= {}
        self.key=key
        self.val = val
        try:
            with open(disk,"r",encoding="utf-8") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
        self.data[str(key)]=val
        with open(disk,"w",encoding="utf-8") as f:
            json.dump(self.data, f)

    def toStr(self):
        return f"VAL({type(self.val)}) : {self.val} ---> {self.key}"


def Create():
    with open(disk, "w", encoding="utf-8") as f:
        json.dump({}, f)

def read():
    readed_data={}
    with open(disk, "r", encoding="utf-8") as f:
            readed_data=json.load(f)
    
    return readed_data