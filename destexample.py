import time
import gc
class A:
    def __init__(self):
        print("Constructor executed ")

    def __del__(self):
        print("Destructor executed ")

aobj = A()
gc.enable()
rint("Hey, ")

time.sleep(4)
del aobj
print("How r u ")
