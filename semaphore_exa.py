
import threading
import random
import time
from threading import Lock, Thread

maxThreads = 2
semaphore = threading.BoundedSemaphore(maxThreads)

def task(x,  y):
    semaphore.acquire()
    print(f'start task {x}, {y} {time.ctime(time.time())}')
    sum = x+y
    time.sleep(random.randint(1,3))
    print(f'task result  {sum} {time.ctime(time.time())}')
    semaphore.release()

for i in range(1,20):
    t = Thread(target=task, args=(i,i+1))
    t.start()
    #print(f'{t.name} started')
    time.sleep((0.5))

