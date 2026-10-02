import os
import random
def forkbomb():
  mal = True
  number = 0
  file = open("domains.txt")
  content = file.readlines()
  num = random.randint(0, len(content))
  os.system("xdg-open https://" + content[num])
