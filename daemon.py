import threading
m=threading.currentThread()
print(m.isDaemon())
print(m.daemon)