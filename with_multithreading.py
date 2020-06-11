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
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("total time=",time.time()-begintime)
print(t1.getName())
t1.setName("Thread one")
print(t1.getName())
