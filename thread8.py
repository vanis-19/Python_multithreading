import threading
import time
def disp1():
    print('morning')
    time.sleep(2)
    print('evening')
threads=[]
for _ in range(5):
    t1=threading.Thread(target=disp1)
    threads.append(t1)
    t1.start()
    time.sleep(4)
    print(threads)