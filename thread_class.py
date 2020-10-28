import threading
class MyThread(threading.Thread):
    def run(self):
        print('hi')
t=MyThread()
t.start()        