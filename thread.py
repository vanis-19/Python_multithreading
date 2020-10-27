import threading
def square(n):
    print(n*n)
def cube(n):
    print(n*n*n)


t1=threading.Thread(target=square, args=(10,))
t2=threading.Thread(target=cube, args=(5,)) 

t1.start()
t2.start()