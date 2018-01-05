from random import *
x = randint(1,3)

from time import *

class Human:
  health = 30
  name = ""
  def __init__(self, name):
      self.name = name

  def eat(self):
      self.health+=5

myHuman = Human("Hassan")
myHuman.eat()
print("Hassan eats",myHuman.health)

class Ninja(Human):
    health = 10
    def __init__(self, name):
        Human.__init__(self, name)
    
    def meditate(self):
        self.health+=5
    
    def backstab(self, obj):
        obj.health -= 10

kevTheNinja = Ninja("Kevin")

kevTheNinja.eat()
print("kevin eats", kevTheNinja.health)

kevTheNinja.meditate()
print("kevin meditates", kevTheNinja.health)

kevTheNinja.backstab(myHuman)
print("Hassan's health after being stabbed", myHuman.health)

class Wizard(Human):
    health = 25
    magicPower = 0
    def __init__(self, name):
        Human.__init__(self, name)

    def study(self):
        marieTheWizard.magicPower += x

    def burn(self, obj):
        # obj.health -= 1
        burn_time = 3
        while burn_time:
            sleep(1)
            obj.health -= 1 # self.magicPower
            print("{} has {} health points".format(obj.name, obj.health))
            # print(f"{obj.name} has {obj.health} health points")
            burn_time -= 1
    def fireball(self, obj):
        obj.health -= self.magicPower
        self.burn(obj)

marieTheWizard = Wizard("Marie")

marieTheWizard.study()
print("Marie studies", marieTheWizard.health)

marieTheWizard.fireball(myHuman)
print("Hassan after being hit by a fireball", myHuman.health)

class Warrior(Human):
    health = 40
    armor = 10
    def __init__(self, name):
        Human.__init__(self, name)
    
    def armorUp(self):
        charlotteTheWarrior.armorUp += 5

    def shieldAlly(self, obj):
        myHuman.shieldAlly += 5
        myHuman.health -= 5

charlotteTheWarrior = Warrior("Charlotte")

charlotteTheWarrior.armorUp()
print("Charlotte armor's up", charlotteTheWarrior.health)



