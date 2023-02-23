import threading
import time

def thread1():
    while True:
        i = 1
        print("Thread-1")
        time.sleep(1.0)

t1 = threading.Thread(target=thread1)
t1.daemon = True
t1.start()

while True:
    print("Main Process")
    time.sleep(2.0)

