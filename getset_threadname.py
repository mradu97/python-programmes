from threading import*
print(current_thread().getName())
current_thread().setName("new thread")
print(current_thread().getName())
print(current_thread().name)
