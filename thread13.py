import threading
import time
def disp1():
    print(threading.currentThread().getName(),'Started')
    time.sleep(2)
    print(threading.currentThread().getName(),'evening')


t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp1)

t1.start()
t2.start()

print(t1.name ,'isAlive:',t1.isAlive())
print(t2.name ,'isAlive:',t2.isAlive())
time.sleep(2)
print(t1.name ,'isAlive:',t1.isAlive())
print(t2.name ,'isAlive:',t2.isAlive())

