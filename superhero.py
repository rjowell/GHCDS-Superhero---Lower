class Superhero:

  dead = False
  
  def fly(self):
    print("flying now")

  def recharge(self):
    print("I'm coming back to life")

  def playerDied(self):
    self.dead = True
    print(self.name + "is dead")
  
  def fight(self,victim,damage):
    victim.takeDamage(damage)

  def takeDamage(self,amountOfDamage):
    if self.hitPoints - amountOfDamage <= 0:
      self.playerDied()
    else:
      self.hitPoints -= amountOfDamage
      print(self.name + " now has "+str(self.hitPoints)+ "HP left")

  #initialize
  def __init__(self,_name,_superpower,_hp,_isHuman):
    self.name = _name
    self.superpower = _superpower
    self.hitPoints = _hp
    self.human = _isHuman










# This thing is called what?

'''
HOW CAN WE CUSTOMIZE OUR SUPERHERO?
Special Moves
Costume
Name
Height
Hair Color
The Way They Are Built
Body Type
Species - Human/Cyborg
Number of Hit Points
weakensses

'''