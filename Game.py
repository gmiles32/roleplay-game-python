from Character import Character
import random

warrior = Character(150, 5)
enemy = Character(100, 15)


def doDamage(characterMaxDamage):
    """
    Returns a random integer value within the range
    0 <= i <= characterMaxDamage, used as damage 
    value for that turn.
    """
    return random.randint(0, characterMaxDamage)


def fight(warrior, enemy):
    roundCounter = 1
    while warrior.isAlive and enemy.isAlive():
        print("\n-----------------------------\n Round " + str(roundCounter) + "\n" + "-----------------------------")
        warriorDamage = doDamage(warrior.getMaxDamage())
        enemyDamage = doDamage(enemy.getMaxDamage())

        #Warriors turn
        print()
        print("Warrior strikes first!")
        enemy.hurt(warriorDamage)
        print()
        if 0 <= warriorDamage and warriorDamage < warrior.getMaxDamage() // 3:
            print("Ow! Looks like you did " + str(warriorDamage) + " damage to the enemy. Wimp...")
        elif warrior.getMaxDamage() // 3 <= warriorDamage and warriorDamage < 2 * (warrior.getMaxDamage() // 3):
            print("Wabam! Looks like you did " + str(warriorDamage) + " damage to the enemy. Not bad...")
        elif 2 * (warrior.getMaxDamage() // 3) <= warriorDamage and warriorDamage <= warrior.getMaxDamage():
            print("Holy cow! Looks like you did " + str(warriorDamage) + " damage to the enemy. Remind me not to get on your bad side...")
        
        print()
        if enemy.isAlive():
            print('End of warrior\'s turn')
            print("-------------------\n|Enemy's health: " + str(enemy.getHealth()) + "|\n-------------------")
        else:
            print("Enemy has been vanquished, you have succeded in your quest!")
            break

        #Enemies turn
        print()
        print("Enemy strikes back!")
        warrior.hurt(enemyDamage)
        print()
        if 0 <= enemyDamage and enemyDamage < enemy.getMaxDamage() // 3:
            print("Ouch? Looks like they did " + str(enemyDamage) + " damage to you. Thought they would hit harder...")
        elif enemy.getMaxDamage() // 3 <= enemyDamage and enemyDamage < 2 * (enemy.getMaxDamage() // 3):
            print("Pow! Looks like they did " + str(enemyDamage) + " damage to you. Gonna feel that one in the morning...")
        elif 2 * (enemy.getMaxDamage() // 3) <= enemyDamage and enemyDamage <= enemy.getMaxDamage():
            print("Mother of G$@! Looks like they did " + str(enemyDamage) + " damage to you. Medic, where's a medic...")
        
        print()
        if warrior.isAlive():
            print('End of enemy\'s turn')
            print("-------------------\n|  Your health: " + str(warrior.getHealth()) + " |\n-------------------")
        else:
            print("You're lookin pretty dead guy, better luck next time.")
            break

        #Allows player to flee
        fightStatus = input("Would you like to continue? (Press enter to keep fighting, type 'Run' to flee:")
        if fightStatus.lower() == 'run':
            print("You ran away! That was a close one...")
            break

        roundCounter += 1




