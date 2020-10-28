import threading
class MyThread1(threading.Thread):
    def run(self):
        print('morning')
class MyThread2(threading.Thread):
    def run(self):
        print('evening')



t1=MyThread1()
t2=MyThread2()
t1.start()
t2.start()
