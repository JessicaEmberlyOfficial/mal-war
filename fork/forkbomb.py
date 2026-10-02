import os
import random
number = 0
file = open("domains.txt", "r")
content = file.readlines()
for line in content:
  os.system("xdg-open https://" + line)
