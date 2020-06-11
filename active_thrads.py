from threading import*
import time
def display():
    print(current_thread().getName(),"fvf\n")
    time.sleep(3)
    print(current_thread().getName(),"hey\n")
print("active threads\n",active_count())
t1=Thread(target=display,name="child thread\n")
t2=Thread(target=display,name="chil2\n")
t3=Thread(target=display,name="chil3\n")
t1.start()
t2.start()
t3.start()
print("num of active threads=",active_count(),"\n")
time.sleep(5)
print("the num of active threads:",active_count(),"\n")
