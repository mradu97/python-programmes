from threading import*
import time
def display():
    print(current_thread().getName(),"started\n")
    time.sleep(3)
    print(current_thread().getName(),"ended\n")
print("active threads\n",active_count())
t1=Thread(target=display,name="child thread\n")
t2=Thread(target=display,name="chil2\n")
t3=Thread(target=display,name="chil3\n")
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
    print("thread name",t.name)
time.sleep(5)
l=enumerate()
for t in l:
    print("threadname",t.name)
