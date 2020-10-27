import threading
import time
def disp1():
    print('morning')
    time.sleep(2)
    print('evening')


t1=threading.Thread(target=disp1)

t1.start()