from Character import Character
from Item import Item
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
        
        #Checks if warrior has found a weapon, and adds damage and removes protection if present
        if warriorWeapon != None:
            maxWarriorDamage = warrior.getMaxDamage() + warriorWeapon.getDamage()
            maxEnemyDamage = enemy.getMaxDamage() - warriorWeapon.getProtection()
        else:
            maxWarriorDamage = warrior.getMaxDamage()
            maxEnemyDamage = enemy.getMaxDamage()
        
        #Gets random damage values
        warriorDamage = doDamage(maxWarriorDamage)
        enemyDamage = doDamage(maxEnemyDamage)

        #Warriors turn
        print()
        print("\x1B[3mWarrior strikes first!\x1B[0m")
        enemy.hurt(warriorDamage)
        print()

        input("Press enter")
        print()

        if 0 < warriorDamage and warriorDamage < maxWarriorDamage // 3:
            print("Ow! Looks like you did " + str(warriorDamage) + " damage to the enemy. Wimp...")
        elif maxWarriorDamage // 3 <= warriorDamage and warriorDamage < 2 * (maxWarriorDamage // 3):
            print("Wabam! Looks like you did " + str(warriorDamage) + " damage to the enemy. Not bad...")
        elif 2 * (maxWarriorDamage // 3) <= warriorDamage and warriorDamage <= maxWarriorDamage:
            print("Holy cow! Looks like you did " + str(warriorDamage) + " damage to the enemy. Remind me not to get on your bad side...")
        elif warriorDamage == 0:
            print("Yikes, looks like you missed.")
        else:
            print("Looks like you did " + str(warriorDamage) + " damage to the enemy.")
        
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

        if 0 < enemyDamage and enemyDamage < 10:
            print("Ouch? Looks like they did " + str(enemyDamage) + " damage to you. Thought they would hit harder...")
        elif 10 <= enemyDamage and enemyDamage < 20:
            print("Pow! Looks like they did " + str(enemyDamage) + " damage to you. Gonna feel that one in the morning...")
        elif 20 <= enemyDamage and enemyDamage <= 25:
            print("Holy S#$T! Looks like they did " + str(enemyDamage) + " damage to you. Medic, where's a medic...")
        elif 0 == enemyDamage:
            print("Nice dodge!")
        else:
            print("Looks like they did " + str(enemyDamage) + " damage to you.")
        
        print()
        if warrior.isAlive():
            print('End of enemy\'s turn')
            print("-------------------\n|  Your health: " + str(warrior.getHealth()) + " |\n-------------------")
        else:
            #print("You're lookin pretty dead guy, better luck next time.")
            outcome = 1
            break

        #Allows player to flee
        fightStatus = input("Would you like to continue? (Press enter to keep fighting, type 'Run' or 'R' to flee): ")
        print()
        if fightStatus.lower() == 'run' or fightStatus.lower() =='r':
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


def sameNameDialogue(warrior, enemy):

    """
    Returns a fun blurp if names are same

    *Note: would prefer to do this with a lambda function like this - 
    lambda x : "(Hey same name, how fun)" if warrior.getName() == goblin.getName() else ""
    """
    if warrior.getName() == enemy.getName():
        retVal = "(Hey same name how fun)"
    else:
        retVal = ""

    return retVal

#Character objects
#You
warrior = Character(random.randint(100, 150), random.randint(10, 20), None)
warriorWeapon = None

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
      Very good, %s, thank you again for your help. Your first foe will be %s the goblin %s. They are quick
      and sly, never let them leave your sight for a moment. You will find their little cave over the hill 
      east of here. If you succeed, come find me and I will direct you to your next target. Good luck hero.
      """ % (warrior.getName(), goblin.getName(), sameNameDialogue(warrior, goblin)))
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

startFight = input("Ready to fight? (Press enter to continue, or type 'Run' or 'R' to flee): ")
print()
if startFight.lower() == 'run' or startFight.lower() == 'r':
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
      a fitting end for such a slimy creature. On your way out of the hole, you stumble upon a chest in the rubble...
      """ % goblin.getName())
print()
playerMove = input("What do you do? (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")
print()

#Ensures an identified input
while playerMove.lower() != 'examine' and playerMove.lower() != 'e' and playerMove.lower() != 'ignore' and playerMove.lower() != 'i':
    playerMove = input("That wasn't an option, try again (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

#Item found
if playerMove.lower() == 'examine' or playerMove.lower() == 'e':
    warriorWeapon = Item(random.randint(5, 15), random.randint(0, 10))
    print("""
      You begin to dig out the chest, and find it unlocked. You found a new weapon! You throw aside your rusty 
      sword for this new companion. You find it's name engraved on the side: '%s'. A proper
      name for a real weapon. You feel more confident about the remaining two enemies that lie on the horizon.
          """ % warriorWeapon.getName())
elif playerMove.lower() == 'ignore' or playerMove.lower() == 'i':
    print("""
      It looks intriguing, but judging by the surrounding of the cave, it's probably just trash. You stumble
      your way out of the cave and into the sunlight.
          """)

input("Press enter")
print()

#Dialogue before fight 2
print("""
      By the time you've dug your way out of the rubble that once was a hill, the sun has just reached the horizon in 
      a brilliant sunset. Reorienting yourself, you begin to make your way back to the village. The sunset
      creates long shadows along the ground, making it difficult to figure out if what your seeing are trees or your
      next foe - you do still have two left. 

      After awhile, you realize you're thoughouly lost. You begin to stumble around the slowly darkening forest,
      trying to find the path that brought you to the hill. Eventually, you do find a path, but this one is much more
      overgrown. You decide to follow it, hoping that it will bring you back to the village. You pick up the pace,
      avoiding mouse holes and roots as you walk. A clearing appear in front of you, and your path leads to a bridge
      crossing a long dried up river bed. 
      """)

print()
input("Press Enter")
print()

print("""
      Making you way across the bridge, you begin to realize that it looks ... weird. The cobblestones look more like grey,
      dried skin than stones. And it's not quite as hard as you would have thought, since it's supposed to be
      stone. And that's when it hits you - literally and figuratively - as the gridge begins to rise and grunt. Hitchiker's
      Guide to the Galaxy comes to mind, with a very apt quote, 'Oh no, not again...'

      As the bridge continues to rise, you begin to make out a peaceful, but rather grotesque face of a troll.
      In the process of standing up, it tosses you off of it's back (Oof) and begins to yawn.

        'Who dares to awaken %s the troll from their beauty sleep!! A few more centuries and I would have been 
        irresitable!'

      The troll looks around, and eventually locks onto you. 

        'You! I'm gonna kick your mildly handsome face in!'
      
      Mildly handsome, that's kind of a low blow...
      """ % troll.getName())

print()
startFight = input("Ready to fight? (Press enter to continue, or type 'Run' or 'R' to flee): ")
print()

if startFight.lower() == 'run' or startFight.lower() == 'r':
    print(""" 
      The troll charges towards you, but apparently it's a little groggy from it's slumber. It slams it's 
      big toe into a rock, and screams in pain. In their moment of distraction, you slip away. That was a close one!
          """)
else:
    outcome = fight(warrior, troll, True)

    print()

    #If warrior wins
    if outcome == 0:
        print(""" 
      The %s the troll begins to look dazzed - probably from the loss of blood. Eventually, the troll falls to their 
      knees, too weak to continue fighting. They lower their head:

        'I stand defeated, have mercy and finish of my mildly attractive being'

      As you approach to strike the final blow, in a blur the troll moves to make one final strike. But you
      were expecting this - you dodge them and strike back, killing them instantly. As the troll falls to the 
      side, you notice a bag on their neck.
              """ % troll.getName())

        print()
        playerMove = input("What do you do? (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")
        print()

        #Ensures an identified input
        while playerMove.lower() != 'examine' and playerMove.lower() != 'e' and playerMove.lower() != 'ignore' and playerMove.lower() != 'i':
            playerMove = input("That wasn't an option, try again (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

        if playerMove.lower() == 'examine' or playerMove.lower() == 'e':
            #You found a new weapon!
            newWeapon = Item(random.randint(10, 20), random.randint(5, 15))
            print("""
      You approach to cooling corpse, and pull the bag off of their neck. In the last remaining light, you
      see the something glimmer from within. A weapon!
                  """)

            print()
            print("""
      Weapon Comparison:
      %s stats:
      Damage - %i
      Protection - %i

      %s stats:
      Damage - %i
      Protection - %i
                  """ % (warriorWeapon.getName(), warriorWeapon.getDamage(), warriorWeapon.getProtection(),
                  newWeapon.getName(), newWeapon.getDamage(), newWeapon.getProtection()))

            print()
            keepWeapon = input("What do you do? (Type 'Take' or 'T' to take the new weapon, 'Keep' or 'K' to keep the old weapon): ")
            print()

            #Ensures an identified input
            while keepWeapon.lower() != 'take' and keepWeapon.lower() != 't' and keepWeapon.lower() != 'keep' and keepWeapon.lower() != 'k':
                keepWeapon = input("That wasn't an option, try again (Type 'Take' or 'T' to take the new weapon, 'Keep' or 'K' to keep the old weapon): ")
            
            if keepWeapon.lower() == 'take' or keepWeapon.lower() == 't':
                print("""
      You take %s into your hand, casting aside %s - it served you well in this last battle, but your going to need something more
      substantial for the final foe.
                      """ % (newWeapon.getName(), warriorWeapon.getName()))
                      
                #Update weapon
                warriorWeapon = newWeapon

            elif keepWeapon.lower() == 'keep' or keepWeapon == 'k':
                print("""
      This new weapon is good, but nothing compares to %s. Plus, it's just proven itself in battle. Better stick to ol'
      reliable. 
                      """ % warriorWeapon.getName())

            print()
            playerMove = input("Continue searching the bag? (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on):")
            print()

            #Ensures an identified input
            while playerMove.lower() != 'examine' and playerMove.lower() != 'e' and playerMove.lower() != 'ignore' and playerMove.lower() != 'i':
                playerMove = input("That wasn't an option, try again (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

            if playerMove.lower() == 'examine' or playerMove.lower() == 'e':
                print("""
      Something in your gut tells you that weapon wasn't the only thing hiding in that pouch. And sure enough, reaching your
      arm deeper into the bag you pull out a vial filled with a chunky, vaguely red fluid(?). The label reads '\x1B[3mFor Emergencies
      Only\x1B[0m'. Kind of hard to tell if it was meant to heal or kill you...
                      """)
                
                print()
                toDrink = input("What do you do? (Type 'Drink' or 'D' to drink, 'Pass' or 'P' to do the smart things): ")
                print()

                #Ensures an identified input
                while toDrink.lower() != 'drink' and toDrink.lower() != 'd' and toDrink.lower() != 'pass' and toDrink.lower() != 'p':
                    toDrink = input("That wasn't an option, try again (Type 'Drink' or 'D' to drink, 'Pass' or 'P' to do the smart things): ")

                if toDrink.lower() == 'drink' or toDrink.lower() == 'd':
                    print("""
      'Yah know what, what do I have to lose?' You uncap the vial, and take a swig - it smells worse than it looks. You feel
      a funny feeling in your stomach, and realize that drinking a questionable fluid from a trolls bag might have been illadvised.
      The queesy feeling continues but as you look at your arms the cuts and bruises start to fade. Your being healed! Looks like
      it was worth it after all..

      \x1B[3mHealth increased + 40pts\x1B[0m
                          """)

                    #Warrior healed
                    warrior.setHealth(warrior.getHealth() + 40)
                elif toDrink.lower() == 'pass' or toDrink.lower() == 'p':
                    print("""
      Why in God's name would I drink a questionable fluid from a trolls' bag? Did my parents teach me nothing? You cast the vial aside,
      where it shatters on the ground, spreading it's foul smelling contents across the forgotten river bed. Good ridance.
                          """)
        elif playerMove.lower() == 'ignore' or playerMove.lower() == 'i':
            print("""
      It's probably just weird troll garbarge. Maybe it's even troll makeup... you shudder at the thought and go on your way.
                  """)

    #You died
    elif outcome == 1:
        print("""
      You begin to slow as you battered by the trolls blows - for having just woken up, the troll is suprisingly aware and agile.
      Must be all that rage, just as good as a morning cup of coffee. Consciousness begins to fade in and out as you try to dodge
      and inevitably end up in the trolls grasp once again. The troll reaches down to grab you - you try to avaid but all your strength
      begins to leave you. 

        'Your not looking so good, maybe you should think twice before waking up a troll smarty pants'

      %s then crushes you skull like a grape between there fingers. Your brains splatter everywhere. 
                  
      Honestly, I'm just impressed you had any at all...
              """ % troll.getName())

        exit()

print()
input("Press Enter")
print()

#Dialogue before final fight
print("""
      In the darkness, you climb back into the woods, leaving the river bed behind you.
      """)
