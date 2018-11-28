import threading
import time


def some_def(start, end):
    time.sleep(1)
    while start < end:
        time.sleep(1)
        print(start)
        start += 1


for i in range(0, 51, 10):
    t = threading.Thread(target=some_def, args=(i, i + 10))
    time.sleep(0.1)
    t.start()
