# Author: NJK (AMDG) 10/7/20

game = int(input("How many points did the team score? "))

if game >= 15:
    print("They got a gold medal")
else:
    if game >= 12:
        print("They got a silver medal")
    else: 
        if game < 9:
            print("They got no medal")
        else:
            print("They got a bronze medal")
