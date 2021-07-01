class Character:
    """
    TODO: Documentation
    
    """

    def __init__(self, health, maxDamage, name):
        self.health = health
        self.__updateMaxDamage(maxDamage)
        self.name = name

    def __updateMaxDamage(self, newMaxDamage):
        if newMaxDamage > 0:
            self.maxDamage = newMaxDamage
        else:
            raise ValueError("int maxDamage can't be negative")

    def getHealth(self):
        return self.health 

    def getMaxDamage(self):
        return self.maxDamage 

    def getName(self):
        return self.name

    def setHealth(self, newHealth):
        self.health = newHealth

    def setMaxDamage(self, newMaxDamage):
        self.__updateMaxDamage(newMaxDamage)

    def setName(self, newName):
        self.name = newName

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

    def hurt(self, damage):
        self.health -= damage
