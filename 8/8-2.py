import threading
import time

# def thread_1():
#     while True:
#         print("Thread-1")
#         time.sleep(1.0)
#
# def thread_2():
#     while True:
#         print("Thread-2")
#         time.sleep(2.0)

def sum(name, value):
    for i in range(value):
        print(f'{name} and it'f's value is {i}')

t1 = threading.Thread(target=sum, args=('Thread#1', 100))
t2 = threading.Thread(target=sum, args=('Thread#2', 120))

# t1 = threading.Thread(target=thread_1)
# t2 = threading.Thread(target=thread_2)

t1.daemon = True
t2.daemon = True

t1.start()
t2.start()

while True:
    print("Main Threaad")
    time.sleep(1.5)

