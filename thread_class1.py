import threading
class MyThread(threading.Thread):
    def run(self):
        for _ in range(3):
            print('hi')
t1=MyThread()
t2=MyThread()
t3=MyThread()
t1.start()  
t2.start()
t3.start()
print(threading.active_count())      