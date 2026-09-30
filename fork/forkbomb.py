def forkbomb():
  mal = True
  number = 0
  while mal == True:
    os.system("xdg-open https://www.facebook.com")
    number += 1
    if number == 100:
      mal = False
  if mal == False:
    number = 0
    mal = True
