# main.py
import sys
import os 
os.system('cls' if os.name == 'nt' else 'clear')
try:
    
    from src.Kernel.shock import call
    from src.Kernel.entry import Main
    
    Main()

except BaseException as e:
    
    try:
        from src.Kernel.shock import call
        call(e)
        sys.exit(int(abs(hash(type(e).__name__)) % 100000))
    except Exception:
        print(f"[CKS] {e}")
        sys.exit(-233)