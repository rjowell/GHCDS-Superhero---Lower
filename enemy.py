class Enemy:

  dead = False
  
  def teleport(self):
    print("teleporting now")

  def recharge(self):
    print("I'm coming back to life")

  def playerDied(self):
    print(self.name + "is dead")
    self.dead = True
  
  def fight(self,victim,damage):
    victim.takeDamage(damage)

  def takeDamage(self,amountOfDamage):
    if self.hitPoints - amountOfDamage <= 0:
      self.playerDied()
    else:
      self.hitPoints -= amountOfDamage
      print(self.name + " now has "+str(self.hitPoints)+ "HP left")

  #initialize
  def __init__(self,_name,_evilPower,_hp,_isHuman):
    self.name = _name
    self.evilPower = _evilPower
    self.hitPoints = _hp
    self.human = _isHuman