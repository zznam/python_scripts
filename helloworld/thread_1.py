#!/usr/bin/python3

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.delay, 5)
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)

print ("threading.activeCount() before two threads started", threading.activeCount())
# Start new Threads
thread1.start()
thread2.start()
thread3.start()
print ("threading.activeCount() after two threads started:", threading.activeCount())
print ("threading.currentThread() after two threads started:", threading.currentThread())
print ("threading.enumerate() after two threads started:", threading.enumerate())
thread1.join()
thread2.join()
thread3.join()
print("Exiting Main Thread")
