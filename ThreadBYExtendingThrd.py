from threading import*

class trd(Thread):
    def run(self):
        for i in range(5):
            print("Thread 1\n")

t = trd()
t.start()

for j in range(5):
    print("Main thread\n")
