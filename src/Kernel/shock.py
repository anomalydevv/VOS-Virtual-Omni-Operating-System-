import sys
import time
from src.Kernel.Logger import log


def call(exception: Exception = None, err_code: int = 45650):
    """VOS Kernel Shock Handler.

    Çekirdek seviyesinde yakalanmayan kritik hataları işler ve ekrana basar.
    """
    print("\n")
    log("VOS --shocked", 2)
    log(
        "Your system encountered a problem and processes were stopped, which"
        " is why your system will restart . . .",
        2,
    )

    if exception:
        log(f"Error Cause: {exception}", 2)

    log(f"ERRCODE: {err_code}\n", 2)

    try:
        time.sleep(3)
    except KeyboardInterrupt:
        pass

    sys.exit(1)