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
class NormalInfantry(Enemy):
    BASE_HP = 100
    BASE_ATK = 25

    def __init__(self, hp, attack):
        self._hp = hp + NormalInfantry.BASE_HP
        self._attack = attack + NormalInfantry.BASE_ATK

    def attack(self):
        print(f"Infantry(Normal) attacks and dealt damage {self._attack}")
    def status(self):
        print(f"Infantry(Normal) HP: {self._hp}, Attk: {self._attack}")


class NormalTank(Enemy):
    BASE_HP = 500
    BASE_ATK = 50

    def __init__(self, hp, attack):
        self._hp = hp + NormalTank.BASE_HP
        self._attack = attack + NormalTank.BASE_ATK

    def attack(self):
        print(f"Tank(Normal) attacks and dealt damage {self._attack}")
    def status(self):
        print(f"Tank(Normal) HP: {self._hp}, Attk: {self._attack}")


class HardInfantry(Enemy):
    BASE_HP = 200
    BASE_ATK = 50

    def __init__(self, hp, attack):
        self._hp = hp + HardInfantry.BASE_HP
        self._attack = attack + HardInfantry.BASE_ATK

    def attack(self):
        print(f"Infantry(Hard) attacks and dealt damage {self._attack}")
    def status(self):
        print(f"Infantry(Hard) HP: {self._hp}, Attk: {self._attack}")


class HardTank(Enemy):
    BASE_HP = 750
    BASE_ATK = 100

    def __init__(self, hp, attack):
        self._hp = hp + HardTank.BASE_HP
        self._attack = attack + HardTank.BASE_ATK

    def attack(self):
        print(f"Tank(Hard) attacks and dealt damage {self._attack}")
    def status(self):
        print(f"Tank(Hard) HP: {self._hp}, Attk: {self._attack}")



###################
# Abstract Factory
###################
class EnemyFactory:
    def createInfantry(self): pass
    def createTank(self): pass
    def createEnemies(self, size): pass

#####################
# Concrete Factory
#####################
class NormalModeEnemyFactory(EnemyFactory):
    def createInfantry(self):
        return NormalInfantry( random.randrange(50, 100), random.randrange(10, 20) )

    def createTank(self):
        return NormalTank( random.randrange(100, 250), random.randrange(30, 60) )

    def createEnemies(self, size):
        return [ random.choice( (self.createInfantry, self.createTank) )() for i in range(size) ]


class HardModeEnemyFactory(EnemyFactory):
    def createInfantry(self):
        return HardInfantry(random.randrange(150, 250), random.randrange(30, 60))

    def createTank(self):
        return HardTank(random.randrange(250, 400), random.randrange(50, 100))

    def createEnemies(self, size):
        return [random.choices((self.createInfantry, self.createTank), (0.3, 0.7))[0]() for i in range(size)]




if __name__ == '__main__':
    normal_factory = NormalModeEnemyFactory()
    hard_factory = HardModeEnemyFactory()

    print("Normal Factory")
    for enemy in normal_factory.createEnemies(10):
        enemy.status()

    print("\nHard Factory")
    for enemy in hard_factory.createEnemies(10):
        enemy.status()
