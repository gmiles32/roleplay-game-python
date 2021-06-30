from Character import Character
import random

def doDamage(characterMaxDamage):
    """
    Returns a random integer value within the range
    0 <= i <= characterMaxDamage, used as damage 
    value for that turn.
    """
    return random.randint(0, characterMaxDamage)


def fight(warrior, enemy, canFlee):

    """
    Generic fight sequence. Has dialogue for each hit done by enemy and warrior, varying by 
    what percent of maxDamage the attack falls into. Will break loop once either the warrior or
    enemy dies. If canFlee=False, there is no escape from this fight.
    Parameters:
    Character warrior - your character
    Character enemy - you foe for this fight
    Boolean canFlee - indicates whether you can escape from this fight
    Returns:
    int Outcome - int flag, 0 if warrior won, 1 if enemy won
    """

    roundCounter = 1
    while warrior.isAlive and enemy.isAlive():
        print("\n-----------------------------\n Round " + str(roundCounter) + "\n" + "-----------------------------")
        warriorDamage = doDamage(warrior.getMaxDamage())
        enemyDamage = doDamage(enemy.getMaxDamage())

        #Warriors turn
        print()
        print("\x1B[3mWarrior strikes first!\x1B[0m")
        enemy.hurt(warriorDamage)
        print()

        input("Press enter")
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
            #print("Enemy has been vanquished, you have succeded in your quest!"
            outcome = 0
            break

        print()
        input("Press enter")

        #Enemies turn
        print()
        print("\x1B[3mEnemy strikes back!\x1B[0m")
        warrior.hurt(enemyDamage)
        print()

        input("Press enter")
        print()

        if 0 <= enemyDamage and enemyDamage < 10:
            print("Ouch? Looks like they did " + str(enemyDamage) + " damage to you. Thought they would hit harder...")
        elif 10 <= enemyDamage and enemyDamage < 20:
            print("Pow! Looks like they did " + str(enemyDamage) + " damage to you. Gonna feel that one in the morning...")
        elif 20 <= enemyDamage and enemyDamage <= 25:
            print("Holy S#$T! Looks like they did " + str(enemyDamage) + " damage to you. Medic, where's a medic...")
        
        print()
        if warrior.isAlive():
            print('End of enemy\'s turn')
            print("-------------------\n|  Your health: " + str(warrior.getHealth()) + " |\n-------------------")
        else:
            #print("You're lookin pretty dead guy, better luck next time.")
            outcome = 1
            break

        #Allows player to flee
        fightStatus = input("Would you like to continue? (Press enter to keep fighting, type 'Run' to flee): ")
        print()
        if fightStatus.lower() == 'run':
            if canFlee == False:
                print("\x1B[3mThere is no escape\x1B[0m")
                print()
                input("Press enter")
            else:
                print("You ran away! That was a close one...")
                break
    

        roundCounter += 1

    return outcome


def getName():
    """
    Returns a name from a random index
    """
    names = ["Glozzom", "Buglead", "Brarter", "Unkifto", "Houtal", 
            "Feprit", "Pirend", "Declain", "Mushreher", "Foyertly",
            "Proscled", "Togrash", "Jackinna", "Breater", "Weepeggle"]
    randIndex = random.randint(0, len(names) - 1)
    return names[randIndex]


#Character objects
#You
warrior = Character(random.randint(100, 150), random.randint(10, 20), None)

#Not so friendly guys
goblin = Character(random.randint(20, 40), random.randint(5, 10), getName())
troll = Character(random.randint(60, 100), random.randint(10, 15), getName())
wyvern = Character(random.randint(150, 200), random.randint(20, 25), getName())



#Beginning of game
print("""
      Welcome brave warrior! I am Masteme, the chief of Feirytic, and my people need your help.
      In the woods surrounding our town, lie three ferocious monsters that terrorize us. I am
      too old to face them, and we have no one else strong enough. Will you help rid us of our
      plague, so that we may be free once again?
      """)

startGame = input("Will you help Masteme and his people? (Press enter to help, type 'N' or 'no' to leave the town of Feirytic to ruin): ")
if startGame.lower() == 'n' or startGame.lower() == 'no':
    print("Then why are you even here, what a jerk...")
    exit()

print()

#Our hero agrees to the challenge...
print("""
      Thank you great warrior! What should we call you?
      """)
warriorName = input("What is you name? (Type a name here, or press enter for an auto generated one): ")
if warriorName == '':
    warriorName = getName()

#Add name to character
warrior.setName(warriorName)

print()

#Now that everyone is acquainted...
print("""      
      Very good, %s, thank you again for your help. Your first foe will be %s the goblin. They are quick
      and sly, never let them leave your sight for a moment. You will find their little cave over the hill 
      east of here. If you succeed, come find me and I will direct you to your next target. Good luck hero.
      """ % (warrior.getName(), goblin.getName()))
print()
input("Press enter")
print()

#Round 1, fight!
print("""
      Following Masteme's directions, you head east to find the nasty goblin. After exiting the town,
      you find a lightly worn trail through the woods. With the late afternoon sun on your back, you
      follow it, tensing at every creek and groan coming from the woods around you. After about an hour,
      you finally make it to the hill. You climb to the top to see if you can locate the cave ... and
      then the top of the hill crumbles beneath you. A trap! You are suddenly in the dark, where you hear
      a voice croak:

            'Finally, a snack - must eat it while it's still fresh!'

      Little does %s know, this snack doesn't smile back...
      """ % goblin.getName())

startFight = input("Ready to fight? (Press enter to continue, or type 'Run' to flee): ")
print()
if startFight.lower() == 'run':
    print("Really? Some hero you are. Remember, you fell into a hill, so you're kind of stuck. Maybe you guys can make friendship bracelets together...")
    print("\x1B[3mThere is no escape\x1B[0m")
    print()
    input("Press enter")


outcome = fight(warrior, goblin, False)

if outcome == 1:
    print()
    print("""
          Well, Masteme wasn't kidding - %s is a slimy fella. They dashed between you legs, cutting your
          great saphenous vein. You might know too much about anatomy and physiology, but all that knowledge
          isn't very helpful when you bleeding out, stuck on the inside of the mountain. %s continued to cut
          you here, and as you begin to faint the last image is their gleaming smile, as they ready themselves
          for a warm meal...

          Don't be discouraged, it happens to the best of us.
          """ % goblin.getName())

print()
print("""
      Alas, the foe is vanquished. %s was fast, but not fast enough. As they ran from your sweeping blade, they
      tripped and landed on their bloodied face, promptly breaking their own neck with a hearty \x1B[3mCrunch!\x1B[0m - 
      a fitting end for such a slimy creature. On your way out of the hole, you stumble upon an chest in the rubble...
      """)
print()
input("What do you do? (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

#TODO: Make item class, fill in dialogue

