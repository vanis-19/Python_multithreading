import threading
def f1():
    print('Thread-name', threading.currentThread().getName())
def f2():
    print('Thread-name', threading.currentThread().getName())    

t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)
 
t1.start()
t2.start()