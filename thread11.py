import threading
def disp():
    for _ in range(5):
        print('child thread')
t=threading.Thread(target=disp)
t.start()
for _ in range(5):
    print('main thread')    