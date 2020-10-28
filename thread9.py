import threading
import time
def disp1():
    for _ in range(10):
        print('hello')
        time.sleep(2)
def disp2():
    for _ in range(10):
        print('hi')
        time.sleep(2)


t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2) 

t1.start()
t1.join()
t2.start()
t2.join()