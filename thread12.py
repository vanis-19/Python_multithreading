import threading
def disp():
    print('child thread')
t=threading.Thread(target=disp)
t.start()
print('main thread identification:', threading.currentThread().ident)
print('child thread:', t.ident)   