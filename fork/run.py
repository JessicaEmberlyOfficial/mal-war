import os
import platform
from android import android
from linux import linux
os = ""
if platform.system() == "Android":
  os = "android"
elif platform.system() == "Linux":
  os = "linux"
else:
  pass
while True:
  os.system("python fork.py")
  if os == "android":
    android()
  elif os == "linux":
    linux()
  else:
    pass
