import os
import time
import random
def forkbomb():
  number = 0
  file = open("domains.txt", "r")
  content = file.readlines()
  while mal == True:
    line = random.randint(0, len(content))
    time.sleep(5)
    os.system("xdg-open https://" + content(line))
