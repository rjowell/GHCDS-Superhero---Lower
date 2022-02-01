from superhero import Superhero
from enemy import Enemy
#def __init__(self,_name,_superpower,_hp,_isHuman):
#self,_name,_superpower,_hp,_isHuman):
#(self,_name,_evilPower,_hp,_isHuman):
print("Welcome to PYTHON BATTLE!")

heroName = input("Enter your hero's name")
heroSuperpower = input("What is your hero's superpower")
hpInput = int(input("How many Hit Points does your hero have?"))
isHuman = input("Is your hero human? Y/N")

heroHuman = True

if isHuman == "N":
  heroHuman = False

Player = Superhero(heroName,heroSuperpower,hpInput,heroHuman)
ComputerPlayer = Enemy("Jamal","Shoot Webs",420,True)

while Player.dead == False and ComputerPlayer.dead == False:
  userAction = input("Press X to fight the enemy")
  if userAction == "X":
    Player.fight(Enemy, 20)

  ComputerPlayer.fight(Player, 32)

if Player.dead == True:
  print("The Enemy Has Won")
else:
  print("The hero has won!")


