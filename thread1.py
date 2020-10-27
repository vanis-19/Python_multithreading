import threading
def disp1():
    for _ in range(10):
        print('hello')
def disp2():
    for _ in range(10):
        print('hi')


t1=threading.Thread(target=disp1)
t2=threading.Thread(target=disp2) 

t1.start()
t2.start()