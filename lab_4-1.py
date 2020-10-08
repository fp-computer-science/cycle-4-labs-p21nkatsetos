# Author: NJK (AMDG) 10/8/20

magic_charge = int(input("What is your magic charge power? "))
shield_charge = int(input("What is your shield charge power? "))
if not (magic_charge >= 90 and shield_charge >= 75): 
    print("The dragon burns you to a crisp. ")
else:
    print("You defeated the dragon! but the princess is in another castle.")
