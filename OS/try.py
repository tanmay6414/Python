from threading import Thread, Condition
import time
import random
queue = []
MAX_NUM = int(input("input length of producer queue:"))
condition = Condition()
class ProducerThread(Thread):
    def run(self):
        nums = range(5)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print "Queue full, producer is waiting\n"
                condition.wait()
                print "Space in queue, Consumer notified the producer\n"
            num = random.choice(nums)
            while len(queue)!=10:
            	queue.append(num)
            	print "producer queue:",queue
            	print "current length of queue",len(queue)
            	condition.notify()#Wake up a thread waiting on this condition, if any. This must only be called when the calling thread has acquired the lock
            	condition.release()#Release the underlying lock. This method calls the corresponding method on the underlying lock; there is no return value. 
            	time.sleep(random.random())
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()#Acquire the underlying lock. This method calls the corresponding method on the underlying lock; the return value is whatever that method returns.
            if not queue:
                print "Nothing in queue, consumer is waiting\n"
                condition.wait()#Wait until notified or until a timeout occurs. This must only be called when the calling thread has acquired the lock
                print "Producer added something to queue and notified the consumer\n"
            while len(queue)!=0:
            	num = queue.pop(0)

            	print "Consumed number", num
            	condition.notify()
            	condition.release()
            	time.sleep(random.random())



ProducerThread().start()
ConsumerThread().start()
