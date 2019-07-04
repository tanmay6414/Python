import threading
import os
import sys
 
# global variable x
x = 0
 
def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1
 
def thread_task(lock):
    """
    task for thread
    calls increment function 10000 times.
    """
    for _ in range(int(a)):
        lock.acquire()
        increment()
        lock.release()

def thread_tasks(lock):
    """
    task for thread
    calls increment function 10000 times.
    """
    for _ in range(10000):
        lock.acquire()
        increment()
        lock.release()
 
def main_task(b):
    global x
    # setting global variable x as 0
    x = 0
    # creating a lock
    lock = threading.Lock()
    # creating threads
    #for loop for creating 20threds for 20 persons
    for i in range(int(sys.argv[2])):
        t = threading.Thread(target=thread_task, args=(lock,))
        # start threads
        t.start()
        # wait until threads finish their job
        t.join()

def main_tasks():
    global x
    # setting global variable x as 0
    x = 0
    # creating a lock
    lock = threading.Lock()
    # creating threads
    #for loop for creating 20threds for 20 persons
    for i in range(20):
        t = threading.Thread(target=thread_tasks, args=(lock,))
        # start threads
        t.start()
        # wait until threads finish their job
        t.join()




print "\n1. By default\t2. By using given commandline arg"
ch = input("Enter your choise : ")
if ch == 1:
    #this is for by default taking n = 20 and p = 100
    for i in range(100):
        main_tasks()
        print("Person {0} Flipped coin {1} times".format(i+1,x))

elif ch == 2:
    #thid take user input for number of coin and number of person
    a = sys.argv[1]
    b = sys.argv[2]
    for i in range(int(sys.argv[3])):
        main_task(b)
        print("Person {0} Flipped coin {1} times".format(i+1,x))





import threading
import os
import sys
 
# global variable x
x = 0
 
def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1
 
def thread_task(lock):
    """
    task for thread
    calls increment function 10000 times.
    """
    for _ in range(int(a)):
        lock.acquire()
        increment()
        lock.release()

def thread_tasks(lock):
    """
    task for thread
    calls increment function 10000 times.
    """
    for _ in range(10000):
        lock.acquire()
        increment()
        lock.release()
 
def main_task(b):
    global x
    # setting global variable x as 0
    x = 0
    # creating a lock
    lock = threading.Lock()
    # creating threads
    #for loop for creating 20threds for 20 persons
    for i in range(int(sys.argv[2])):
        t = threading.Thread(target=thread_task, args=(lock,))
        # start threads
        t.start()
        # wait until threads finish their job
        t.join()

def main_tasks():
    global x
    # setting global variable x as 0
    x = 0
    # creating a lock
    lock = threading.Lock()
    # creating threads
    #for loop for creating 20threds for 20 persons
    for i in range(20):
        t = threading.Thread(target=thread_tasks, args=(lock,))
        # start threads
        t.start()
        # wait until threads finish their job
        t.join()




print "\n1. By default\t2. By using given commandline arg"
ch = input("Enter your choise : ")
if ch == 1:
    #this is for by default taking n = 20 and p = 100
    for i in range(100):
        main_tasks()
        print("Person {0} Flipped coin {1} times".format(i+1,x))

elif ch == 2:
    #thid take user input for number of coin and number of person
    a = sys.argv[1]
    b = sys.argv[2]
    for i in range(int(sys.argv[3])):
        main_task(b)
        print("Person {0} Flipped coin {1} times".format(i+1,x))





