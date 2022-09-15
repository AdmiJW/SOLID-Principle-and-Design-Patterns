import random


#################
# Abstract Enemy
#################
class Enemy:
    def attack(self): pass
    def status(self): pass

####################
# Concrete Enemy
####################
class Infantry(Enemy):
    BASE_HP = 100
    BASE_ATK = 25

    def __init__(self, hp, attack):
        self._hp = hp + Infantry.BASE_HP
        self._attack = attack + Infantry.BASE_ATK

    def attack(self):
        print(f"Infantry attacks and dealt damage {self._attack}")
    def status(self):
        print(f"Infantry HP: {self._hp} Attk: {self._attack}")

class Tank(Enemy):
    BASE_HP = 500
    BASE_ATK = 50

    def __init__(self, hp, attack):
        self._hp = hp + Tank.BASE_HP
        self._attack = attack + Tank.BASE_ATK

    def attack(self):
        print(f"Tank attacks and dealt damage {self._attack}")
    def status(self):
        print(f"Tank HP: {self._hp} Attk: {self._attack}")



###################
# Abstract Factory
###################
class EnemyFactory:
    def createEnemy(self): pass


#####################
# Concrete Factory
#####################
class NormalModeEnemyFactory(EnemyFactory):
    def createEnemy(self):
        ChosenEnemyClass = random.choice( (Infantry, Tank) )
        return ChosenEnemyClass( random.randrange(50, 100), random.randrange(10, 30) )

class HardModeEnemyFactory(EnemyFactory):
    def createEnemy(self):
        ChosenEnemyClass = random.choices( (Infantry, Tank), (0.3, 0.7) )[0]
        return ChosenEnemyClass( random.randrange(100, 200), random.randrange(30, 50) )




if __name__ == '__main__':
    normal_factory = NormalModeEnemyFactory()
    hard_factory = HardModeEnemyFactory()

    print("Normal Factory")
    for enemy in [ normal_factory.createEnemy() for i in range(10) ]:
        enemy.status()

    print("\nHard Factory")
    for enemy in [hard_factory.createEnemy() for i in range(10)]:
        enemy.status()
