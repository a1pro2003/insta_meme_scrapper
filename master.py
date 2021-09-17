import os
from multiprocessing import Process

def script1():
    os.system("saver.py")     
def script2():
    os.system("server.py") 

if __name__ == '__main__':
    p = Process(target=script1)
    q = Process(target=script2)
    p.start()
    q.start()
    p.join()
    q.join()
    