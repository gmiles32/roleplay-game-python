class Character:
    """
    TODO: Documentation
    
    """

    def __init__(self, health, maxDamage):
        self.health = health
        self.__updateMaxDamage(maxDamage)

    def __updateMaxDamage(self, newMaxDamage):
        if newMaxDamage > 0:
            self.maxDamage = newMaxDamage
        else:
            raise ValueError("int maxDamage can't be negative")

    def getHealth(self):
        return self.health 

    def getMaxDamage(self):
        return self.maxDamage 
    
    def setHealth(self, newHealth):
        self.health = newHealth

    def setMaxDamage(self, newMaxDamage):
        self.__updateMaxDamage(newMaxDamage)

    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

    def hurt(self, damage):
        self.health -= damage

    


     

    