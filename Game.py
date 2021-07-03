from Character import Character
from Item import Item
import random
from os import system, name
from time import sleep

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
        print("\n" + ("-" * 40) + "\n Round " + str(roundCounter) + "\n" + ("-" * 40))
        
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
        retVal = " (Hey same name how fun)"
    else:
        retVal = ""

    return retVal


#Not actually used yet, I'm not sure where to have clears...or whether I like it or not
def clear():
    """
    Clears terminal screen for you viewing pleasure
    """
    system('cls' if name == 'nt' else 'clear')


#Character objects
#You
warrior = Character(random.randint(100, 150), random.randint(10, 20), None)
warriorWeapon = None

#Not so friendly guys
goblin = Character(random.randint(20, 40), random.randint(5, 10), getName())
troll = Character(random.randint(60, 100), random.randint(10, 15), getName())
wyvern = Character(random.randint(150, 200), random.randint(20, 25), 'Masteme') #Spoiler alert

#Beginning of game
print(
      "\n\tWelcome brave warrior! I am Masteme, the chief of Feirytic, and my people need your help."
      "\n\tIn the woods surrounding our town, lie three ferocious monsters that terrorize us. I am"
      "\n\ttoo old to face them, and we have no one else strong enough. Will you help rid us of our"
      "\n\tplague, so that we may be free once again?"
      )

startGame = input("\n\nWill you help Masteme and his people? (Press enter to help, type 'N' or 'no' to leave the town of Feirytic to ruin): ")
if startGame.lower() == 'n' or startGame.lower() == 'no':
    print("\n\nThen why are you even here, what a jerk...")
    exit()

#clear()

#Our hero agrees to the challenge...
print(
      "\n\n\tThank you great warrior! What should we call you?"
      )
warriorName = input("\n\nWhat is you name? (Type a name here, or press enter for an auto generated one): ")
if warriorName == '':
    warriorName = getName()

#Add name to character
warrior.setName(warriorName)

#Now that everyone is acquainted...

print(    
      f"\n\n\tVery good, {warrior.getName()}, thank you again for your help. Your first foe will be {goblin.getName()} the goblin{sameNameDialogue(warrior, goblin)}. They are quick"
      "\n\tand sly, never let them leave your sight for a moment. You will find their little cave over the hill" 
      "\n\teast of here. If you succeed, come find me and I will direct you to your next target. Good luck hero."
      )

input("\n\nPress enter")

#Round 1, fight!
print(
      "\n\n\tFollowing Masteme's directions, you head east to find the nasty goblin. After exiting the town,"
      "\n\tyou find a lightly worn trail through the woods. With the late afternoon sun on your back, you"
      "\n\tfollow it, tensing at every creek and groan coming from the woods around you. After about an hour,"
      "\n\tyou finally make it to the hill. You climb to the top to see if you can locate the cave ... and"
      "\n\tthen the top of the hill crumbles beneath you. A trap! You are suddenly in the dark, where you hear"
      "\n\ta voice croak:"

            "\n\n\t\t'Finally, a snack - must eat it while it's still fresh!'"

      f"\n\n\tLittle does {goblin.getName()} know, this snack doesn't smile back..."
      )

startFight = input("\n\nReady to fight? (Press enter to continue, or type 'Run' or 'R' to flee): ")

#Ensures an identified input
while startFight.lower() != '' and startFight.lower() != 'run' and startFight.lower() != 'r':
    startFight = input("That wasn't an option, try again (Press enter to continue, or type 'Run' or 'R' to flee): ")

#Can't run from this fight, get admonished
if startFight.lower() == 'run' or startFight.lower() == 'r':
    print("\n\n\tReally? Some hero you are. Remember, you fell into a hill, so you're kind of stuck. Maybe you guys can make friendship bracelets together...")
    print("\n\t\x1B[3mThere is no escape\x1B[0m")
    input("\n\nPress enter")


outcome = fight(warrior, goblin, canFlee=False)

#You die
if outcome == 1:
    print()
    print(
          f"\n\tWell, Masteme wasn't kidding - {goblin.getName()} is a slimy fella. They dashed between you legs, cutting your"
          "\n\tgreat saphenous vein. You might know too much about anatomy and physiology, but all that knowledge"
          f"\n\tisn't very helpful when you bleeding out, stuck on the inside of the mountain. {goblin.getName()} continued to cut"
          "\n\tyou here, and as you begin to faint the last image is their gleaming smile, as they ready themselves"
          "\n\tfor a warm meal..."

          "\n\n\tDon't be discouraged, it happens to the best of us."
          )

    #Game over
    exit()

#Goblin is killed
elif outcome == 0:
    print(
          f"\n\tAlas, the foe is vanquished. {goblin.getName()} was fast, but not fast enough. As they ran from your sweeping blade, they"
          "\n\ttripped and landed on their bloodied face, promptly breaking their own neck with a hearty \x1B[3mCrunch!\x1B[0m -"
          "\n\ta fitting end for such a slimy creature. On your way out of the hole, you stumble upon a chest in the rubble..."
          )
    
    playerMove = input("\n\nWhat do you do? (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

    #Ensures an identified input
    while playerMove.lower() != 'examine' and playerMove.lower() != 'e' and playerMove.lower() != 'ignore' and playerMove.lower() != 'i':
        playerMove = input("\n\nThat wasn't an option, try again (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

    #Item found
    if playerMove.lower() == 'examine' or playerMove.lower() == 'e':
        warriorWeapon = Item(random.randint(5, 15), random.randint(0, 10))
        print(
              "\n\n\tYou begin to dig out the chest, and find it unlocked. You found a new weapon! You throw aside your rusty" 
              f"\n\tsword for this new companion. You find it's name engraved on the side: '{warriorWeapon.getName()}'. A proper"
              "\n\tname for a real weapon. You feel more confident about the remaining two enemies that lie on the horizon."
              )

    elif playerMove.lower() == 'ignore' or playerMove.lower() == 'i':
        print(
              "\n\n\tIt looks intriguing, but judging by the surrounding of the cave, it's probably just trash. You stumble"
              "\n\tyour way out of the cave and into the sunlight."
             )

    input("\n\nPress enter")

#Dialogue before fight 2
print(
      "\n\n\tBy the time you've dug your way out of the rubble that once was a hill, the sun has just reached the horizon in"
      "\n\ta brilliant sunset. Reorienting yourself, you begin to make your way back to the village. The sunset"
      "\n\tcreates long shadows along the ground, making it difficult to figure out if what your seeing are trees or your"
      "\n\tnext foe - you do still have two left."

      "\n\n\tAfter awhile, you realize you're thoughouly lost. You begin to stumble around the slowly darkening forest,"
      "\n\ttrying to find the path that brought you to the hill. Eventually, you do find a path, but this one is much more"
      "\n\tovergrown. You decide to follow it, hoping that it will bring you back to the village. You pick up the pace,"
      "\n\tavoiding mouse holes and roots as you walk. A clearing appear in front of you, and your path leads to a bridge"
      "\n\tcrossing a long dried up river bed."
     )

input("\n\nPress Enter")

clear()

print(
      "\n\n\tMaking you way across the bridge, you begin to realize that it looks ... weird. The cobblestones look more like grey,"
      "\n\tdried skin than stones. And it's not quite as hard as you would have thought, since it's supposed to be"
      "\n\tstone. And that's when it hits you - literally and figuratively - as the bridge begins to rise and grunt. Hitchiker's"
      "\n\tGuide to the Galaxy comes to mind, with a very apt quote, 'Oh no, not again...'"

      "\n\n\tAs the bridge continues to rise, you begin to make out a peaceful, but rather grotesque face of a troll."
      "\n\tIn the process of standing up, it tosses you off of it's back (Oof) and begins to yawn."

      f"\n\n\t\t'Who dares to awaken {troll.getName()}{sameNameDialogue(warrior, troll)} from their beauty sleep!! A few more centuries and I would have been irresitable!'"

      "\n\n\tThe troll looks around, and eventually locks onto you." 

      "\n\n\t\t'You! I'm gonna kick your mildly handsome face in!'"
      
      "\n\n\tMildly handsome, that's kind of a low blow..."
      )

startFight = input("\n\nReady to fight? (Press enter to continue, or type 'Run' or 'R' to flee): ")

#Ensures an identified input
while startFight.lower() != '' and startFight.lower() != 'run' and startFight.lower() != 'r':
    startFight = input("\n\nThat wasn't an option, try again (Press enter to continue, or type 'Run' or 'R' to flee): ")


if startFight.lower() == 'run' or startFight.lower() == 'r':
    print( 
          "\n\n\tThe troll charges towards you, but apparently it's a little groggy from it's slumber. It slams it's"
          "\n\tbig toe into a rock, and screams in pain. In their moment of distraction, you slip away. That was a close one!"
          )
else:
    #Fight two sequence
    outcome = fight(warrior, troll, canFlee=True)

    #You died
    if outcome == 1:
        print(
              "\n\n\tYou begin to slow as you battered by the trolls blows - for having just woken up, the troll is suprisingly aware and agile."
              "\n\tMust be all that rage, just as good as a morning cup of coffee. Consciousness begins to fade in and out as you try to dodge"
              "\n\tand inevitably end up in the trolls grasp once again. The troll reaches down to grab you - you try to avaid but all your strength"
              "\n\tbegins to leave you." 

              "\n\n\t\t'Your not looking so good, maybe you should think twice before waking up a troll smarty pants'"

              f"\n\n\t{troll.getName()} then crushes you skull like a grape between there fingers. Your brains splatter everywhere."
                  
              "\n\n\tHonestly, I'm just impressed you had any at all..."
              )

        #Game over
        exit()

    #You kill weird bridge troll guy
    elif outcome == 0:
        print( 
              f"\n\n\tThe {troll.getName()} the troll begins to look dazzed - probably from the loss of blood. Eventually, the troll falls to their"
              "\n\tknees, too weak to continue fighting. They lower their head:"

              "\n\n\t\t'I stand defeated, have mercy and finish of my mildly attractive being'"

              "\n\n\tAs you approach to strike the final blow, in a blur the troll moves to make one final strike. But you"
              "\n\twere expecting this - you dodge them and strike back, killing them instantly. As the troll falls to the"
              "\n\tside, you notice a bag on their neck."
              )

        playerMove = input("\n\nWhat do you do? (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

        #Ensures an identified input
        while playerMove.lower() != 'examine' and playerMove.lower() != 'e' and playerMove.lower() != 'ignore' and playerMove.lower() != 'i':
            playerMove = input("\n\nThat wasn't an option, try again (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

        if playerMove.lower() == 'examine' or playerMove.lower() == 'e':
            #You found a new weapon!
            newWeapon = Item(random.randint(10, 20), random.randint(5, 15))
            print(
                  "\n\n\tYou approach to cooling corpse, and pull the bag off of their neck. In the last remaining light, you"
                  "\n\tsee the something glimmer from within. A weapon!"
                  )

            print(
                  "\n\nWeapon Comparison:"

                  f"\n\n\t\x1B[3m{warriorWeapon.getName()}\x1B[0m stats:"
                  f"\n\tDamage - {warriorWeapon.getDamage()}"
                  f"\n\tProtection - {warriorWeapon.getProtection()}"

                  f"\n\n\t\x1B[3m{newWeapon.getName()}\x1B[0m stats:"
                  f"\n\tDamage - {newWeapon.getDamage()}"
                  f"\n\tProtection - {newWeapon.getProtection()}"
                  )

            keepWeapon = input("\n\nWhat do you do? (Type 'Take' or 'T' to take the new weapon, 'Keep' or 'K' to keep the old weapon): ")

            #Ensures an identified input
            while keepWeapon.lower() != 'take' and keepWeapon.lower() != 't' and keepWeapon.lower() != 'keep' and keepWeapon.lower() != 'k':
                keepWeapon = input("\n\nThat wasn't an option, try again (Type 'Take' or 'T' to take the new weapon, 'Keep' or 'K' to keep the old weapon): ")
            
            if keepWeapon.lower() == 'take' or keepWeapon.lower() == 't':
                print(
                      f"\n\n\tYou take {newWeapon.getName()} into your hand, casting aside {warriorWeapon.getName()} - it served you well in this last battle, but your going to need something more"
                      "\n\n\tsubstantial for the final foe."
                      )
                      
                #Update weapon
                warriorWeapon = newWeapon

            elif keepWeapon.lower() == 'keep' or keepWeapon.lower() == 'k':
                print(
                      f"\n\n\tThis new weapon is good, but nothing compares to {warriorWeapon.getName()}. Plus, it's just proven itself in battle. Better stick to ol'"
                      "\n\treliable. "
                      )

            playerMove = input("\n\nContinue searching the bag? (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on):")

            #Ensures an identified input
            while playerMove.lower() != 'examine' and playerMove.lower() != 'e' and playerMove.lower() != 'ignore' and playerMove.lower() != 'i':
                playerMove = input("\n\nThat wasn't an option, try again (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

            if playerMove.lower() == 'examine' or playerMove.lower() == 'e':
                print(
                      "\n\n\tSomething in your gut tells you that weapon wasn't the only thing hiding in that pouch. And sure enough, reaching your"
                      "\n\tarm deeper into the bag you pull out a vial filled with a chunky, vaguely red fluid(?). The label reads '\x1B[3mFor Emergencies"
                      "\n\tOnly\x1B[0m'. Kind of hard to tell if it was meant to heal or kill you..."
                      )
                
                toDrink = input("\n\nWhat do you do? (Type 'Drink' or 'D' to drink, 'Pass' or 'P' to do the smart things): ")
                
                #Ensures an identified input
                while toDrink.lower() != 'drink' and toDrink.lower() != 'd' and toDrink.lower() != 'pass' and toDrink.lower() != 'p':
                    toDrink = input("\n\nThat wasn't an option, try again (Type 'Drink' or 'D' to drink, 'Pass' or 'P' to do the smart things): ")

                #Drink potion, get healed
                if toDrink.lower() == 'drink' or toDrink.lower() == 'd':
                    print(
                          "\n\n\t'Yah know what, what do I have to lose?' You uncap the vial, and take a swig - it smells worse than it looks. You feel"
                          "\n\ta funny feeling in your stomach, and realize that drinking a questionable fluid from a trolls bag may have been illadvised."
                          "\n\tThe queesy feeling continues but as you look at your arms the cuts and bruises start to fade. Your being healed! Looks like"
                          "\n\tit was worth it after all.."

                          "\n\n\t\x1B[3mHealth increased + 40pts\x1B[0m"
                          )

                    #Warrior healed
                    warrior.setHealth(warrior.getHealth() + 40)

                #Only the bold are rewarded...
                elif toDrink.lower() == 'pass' or toDrink.lower() == 'p':
                    print(
                          "\n\n\tWhy in God's name would I drink a questionable fluid from a trolls' bag? Did my parents teach me nothing? You cast the vial aside,"
                          "\n\twhere it shatters on the ground, spreading it's foul smelling contents across the forgotten river bed. Good ridance."
                          )

        elif playerMove.lower() == 'ignore' or playerMove.lower() == 'i':
            print("\n\n\tIt's probably just weird troll garbage. Maybe it's even troll makeup... you shudder at the thought and go on your way.")

input("\n\nPress Enter")

#TODO: split this in half to that you find something in the dark woods, and if you examine it you loose either health or you weapon, at random
#then you do the battle totally boned lol
print(
      "\n\n\tIn the darkness, you climb back into the woods, leaving the river bed behind you. in the distance you can make out a red glimmer - "
      "\n\tthat must be the town! You head towards it with a warm meal in mind."

      "\n\n\tAs you walk, you here a creak come from your left. You turn to look, but don't see anything."
      )

playerMove = input("\n\nWhat do you do? (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

#Ensures an identified input
while playerMove.lower() != 'examine' and playerMove.lower() != 'e' and playerMove.lower() != 'ignore' and playerMove.lower() != 'i':
    playerMove = input("\n\nThat wasn't an option, try again (Type 'Examine' or 'E' to look, 'Ignore' or 'I' to move on): ")

if playerMove.lower() == 'examine' or playerMove.lower() == 'e':
    outcome = random.randint(0,1)

    #You loose your weapon
    if outcome == 0:
        print(
              "\n\n\tSo far today, you've been pretty lucky when you've examined stuff, why not again? You walk toward where the sound came from."
              "\n\tAs you approach, a blinding light comes from behind a log. As you lift you arm up to avoid it, you feel something pass you."
              "\n\tYou begin to regan your vision, franticly trying to assess the situation. You reach down to draw your weapon, but where it was"
              "\n\tis now a ... branch. You've been robbed - and you have no idea how! Off in the distance, you see a white glimmer and the faint"
              "\n\tsound of giggling. To tired to pursue, you turn back towards the village."

              "\n\n\t\x1B[3mYou have lost your weapon\x1B[0m"
              )

        #No weapon for you
        warriorWeapon = None

    #Loose health
    elif outcome == 1:
        #Health adjustment
        lostHealth = warrior.getHealth() // 4
        warrior.setHealth(warrior.getHealth() - lostHealth)

        print(
              "\n\n\tYou strike off towards the sound, reading your weapon just in case it's the final foe. As you approach, you hear more rustling ..."
              "\n\tand then a wolf jumps from the bushes! You try to draw your weapon, but before you can the wolf leaps and bites you leg. You scream in pain,"
              "\n\tand before you can strike back the wolf rushes off into the night. You sit there, dazzed and in pain. You grab a nearby branch to use as a"
              "\n\tcan. Hopefully the village has a good doctor."

              f"\n\n\t\x1B[3mYou lost {lostHealth}pts from you health\x1B[0m"
              )  
    elif playerMove.lower() == 'ignore' or playerMove.lower() == 'i':
        print("\n\n\tWeird noises in the woods? No thank you. You continue on you way.")

#Dialogue before final fight
print(
      "\n\n\tAs you get closer to the village, you realize that the red glow isn't laterns - the village is ablaze! You pick up your pace. This must"
      "\n\tbe the last foe Masteme warned you of. You break into a clearing, and the village comes into view, engulfed in flames. No one is in"
      "\n\tsight, not even the culprit. As you examine the flames, you feel a strong grasp upon the back of your shirt. You feel your feet"
      "\n\tleave the ground as you are picked up and flung. As you hit the ground you let out a grunt, and when you roll over to face your attacker"
      "\n\tyou see Masteme, his face emotionless and his eyes glowing an amber red, like hot coals. Not only that, but his eyes are..."
      "\n\trepitlian. Before you can say anything, he hisses..."

      "\n\n\t\t'I thought those fools would have killed you, but apparently I have to do everything on my own.'"

      "\n\n\tAs he speaks, his skin begins to split as the body underneath writhes and expands into a giant *wyvern! Masteme is a wyvern\u203D But he's"
      "\n\tthe chieftan, why would he destroy his village...and then it dawns on you. You never actually saw anyone else - it was all a setup. You"
      "\n\tbegin to stand, and Masteme laughs, smoke billowing from his scaly nostrils."

      "\n\n\t\t'Fool! Face me and you will perish - I've never been bested, and I do not imagine today will be any different'"

      "\n\n\tF$#kin cocky bastard..."

      "\n\n\x1B[3m*A wyvern is a bipedal dragon with wings as arms. I did this because I can.\x1B[0m"
      )

startFight = input("\n\nReady to fight? (Press enter to continue, or type 'Run' or 'R' to flee): ")

#Ensures an identified input
while startFight.lower() != '' and startFight.lower() != 'run' and startFight.lower() != 'r':
    startFight = input("\n\nThat wasn't an option, try again (Press enter to continue, or type 'Run' or 'R' to flee): ")

if startFight.lower() == 'run' or startFight.lower() == 'r':
    print("\n\n\tSo Masteme has wings. And he can breathe fire. You run and you a nice flame broiled chicken breast...")
    print("\n\t\x1B[3mThere is no escape\x1B[0m")
    input("\n\nPress enter")

#Final battle
outcome = fight(warrior, wyvern, canFlee=False)

#You die
if outcome == 1:
    print(
          "\n\n\tBloodied and burned, you make one last charge, trying to slice at Masteme's legs. Your weapon makes contact, and your stomach"
          "\n\tas it shatters on the hardened scales. Masteme chuckles above you."

          "\n\n\t'That was ill advised my friend."

          "\n\n\tYou feel one of his talons grab your back, flinging you high up into the air. The last thing you see is Masteme's"
          "\n\tsly smirk as he swallows you whole."

          "\n\n\tI don't know who had it worse, you or Noah..."
          )

    #Game over
    exit()

#You win, Masteme defeated
elif outcome == 0:
    print(
          "\n\n\tMasteme might be big and firebreathing, but he has seriously underestimated you. Dodging his over confident strikes, you manage to grab"
          "\n\this wing and swing onto his back. He tries to grab at you, but you've managed to stay just out of reach. You examine his hide for a weakness."
          "\n\tJust above his right wing, there's a slight gap when he flaps. Timing your strike just right, plunge your weapon into his side. Masteme begins"
          "\n\tto stagger."

          "\n\n\t\t'What is this...feeling? Is this pain? What a stranger it has been all these centuries.'"

          "\n\n\tHe staggers forward, falling onto his chest. You slide off as the great beast goes limp. Victory! You sit on the ground, letting your weapon"
          "\n\tfall by your side. Exhaustion takes over, and you pass out by the corpse of you foe."
          )

