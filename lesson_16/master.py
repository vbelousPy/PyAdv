# 3 slave 1 2 3
# 3 sec if close -> print (procces_id + sum)

import subprocess
import time

for i in range(3):
    p = subprocess.Popen("python slave.py 1 10 2", shell=True)
    p.wait()
    print("pid =", p.pid)
    print(p)
    time.sleep(3)
