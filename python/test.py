import threading
import time
def worker(num):
    time.sleep(5 - num)
    print(num ** 2, end='')
t1 = threading.Thread(target=worker, args=(1,))
t2 = threading.Thread(target=worker, args=(2,))
t1. start()
t2.start()
t1.join()
t2. join()