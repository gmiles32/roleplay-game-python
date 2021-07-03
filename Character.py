class Character:
    """
    Represents a character, either hero or enemy, in roleplay game. Acts as convenient
    storage for character stats, including character name, health, and maximum amount
    of damage the character is capable of.
    
    """

    """
    Constructor for Character class. Creates character object, and ensures
    values meet contraints, specifically that maxDamage is non-negative.
    Parameters:
    int health - Character's health
    int maxDamage - Maximum amount of damage a character can do (non-negative)
    String name - Character's name
    """
    def __init__(self, health, maxDamage, name):
        self.health = health
        self.__updateMaxDamage(maxDamage)
        self.name = name

    """
    Private method, ensures maxDamage is non-negative
    Parameters:
    int newMaxDamage - new non-negative value for maxDamage
    """
    def __updateMaxDamage(self, newMaxDamage):
        if newMaxDamage > 0:
            self.maxDamage = newMaxDamage
        else:
            raise ValueError("int maxDamage can't be negative")

    """ Getter for health, returns int health """
    def getHealth(self):
        return self.health 

    """ Getter for maxDamage, returns int maxDamage """
    def getMaxDamage(self):
        return self.maxDamage 

    """ Getter for name, returns String name """
    def getName(self):
        return self.name

    """ Setter for health, parameter int newHealth"""
    def setHealth(self, newHealth):
        self.health = newHealth

    """ Setter for maxDamage, parameter int newMaxDamage"""
    def setMaxDamage(self, newMaxDamage):
        self.__updateMaxDamage(newMaxDamage)

    """ Setter for name, parameter String newName """
    def setName(self, newName):
        self.name = newName

    """
    Checks if health is postive, or character is alive.
    Returns:
    True if health is positive else False
    """
    def isAlive(self):
        if self.health > 0:
            return True
        else:
            return False

    """
    Decrements health by amount of damage inflicted
    Parameters:
    int damage - amount of damage to inflict
    """
    def hurt(self, damage):
        self.health -= damage
