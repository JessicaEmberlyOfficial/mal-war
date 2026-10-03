import os
import atexit
os.system("python _run.py & python bomb.py &")

@atexit.register
def goodbye():
  os.system("python atexit.py &")
