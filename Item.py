import random

class Item:

    """
    Represents an item in roleplay game, which is only a weapon. Contains 
    variables storing a weapons damage, how much protection is provided, and 
    the weapons name, which is auto-generated.
    """

    """
    Contructor for Item class. Instantiates instance variables and auto-generates
    a name.
    Parameters:
    int damage - amount of damage an item can inflict
    int protection - amount of protection provided by item
    """
    def __init__(self, damage, protection):
        self.damage = damage
        self.protection = protection
        self.name = self.__itemNameGenerator()
    
    """
    Private method. Auto-generates a name from two preset arrays (More than a hundred combos)
    Returns:
    name from f-string
    """
    def __itemNameGenerator(self):
        itemTypes = ["Sword", "Dagger", "Bow", "Broadsword", "Longsword",
                     "Trident", "Spear", "Crossbow", "Wand", "Staff"]
        itemDescriptors = ["Fury", "Destruction", "Friendship", "Cloaking", "Fortitude",
                           "Legitimacy", "Good Grades", "Freedom", "Dehydration", "Hardcore-ness"]
        randIndex1 = random.randint(0, 9)
        randIndex2 = random.randint(0, 9)
        return f"{itemTypes[randIndex1]} of {itemDescriptors[randIndex2]}"

    """ Getter for Item damage, returns int damage """
    def getDamage(self):
        return self.damage

    """ Getter for Item protection, returns int protection """
    def getProtection(self):
        return self.protection

    """ Getter for Item name, returns String name """
    def getName(self):
        return self.name

    """ Setter for Item damage, parameter int newDamage """
    def setDamage(self, newDamage):
        self.damage = newDamage
    
    """ Setter for Item protection, parameter in newProtection """
    def setProtection(self, newProtection):
        self.protection = newProtection
