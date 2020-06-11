from threading import *
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("doubles:",2*n)
def squares(numnbers):
    for n in numbers:
        time.sleep(1)
        print("squares:",n*n)
numbers=[1,2,3,4,5,6]
begintime=time.time()
doubles(numbers)
squares(numbers)
print("total time=",time.time()-begintime)
