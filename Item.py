import random

class Item:

    """
    TODO: Documentation
    """

    def __init__(self, damage, protection):
        self.damage = damage
        self.protection = protection
        self.name = self.__itemNameGenerator()
    
    def __itemNameGenerator(self):
        itemTypes = ["Sword", "Dagger", "Bow", "Broadsword", "Longsword",
                     "Trident", "Spear", "Crossbow", "Wand", "Staff"]
        itemDescriptors = ["Fury", "Destruction", "Friendship", "Cloaking", "Fortitude",
                           "Legitimacy", "Good Grades", "Freedom", "Dehydration", "Hardcore-ness"]
        randIndex1 = random.randint(0, 9)
        randIndex2 = random.randint(0, 9)
        return "%s of %s" % (itemTypes[randIndex1], itemDescriptors[randIndex2])

    def getDamage(self):
        return self.damage

    def getProtection(self):
        return self.protection

    def getName(self):
        return self.name

    def setDamage(self, newDamage):
        self.damage = newDamage
    
    def setProtection(self, newProtection):
        self.protection = newProtection
