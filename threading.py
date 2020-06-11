from threading import*
def display1():
    for i in range (1,5):
        print("child1 thread\n")
def display2():
    for i in range (1,5):
        print("child2 thread\n")
def display3():
    for i in range (1,5):
        print("child3 thread\n")

t1=Thread(target=display1)
t2=Thread(target=display2)
t3=Thread(target=display3)
t1.start()
t2.start()
t3.start()
