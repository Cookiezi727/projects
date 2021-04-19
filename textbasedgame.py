# Adventure game by group flying tuna
# Feel free to edit the storyline
"""
# Daniel
Current Story:
Wake up in dungeon/cave, pick up some flint, a torch and a knife. After wandering around, you hear something large approaching you
  RUN:
  you run, the dungeon splits into two
      LEFT: You run, and then you hit a dead end. The thing that was chasing you was a large, drolling troll. you:
          FIGHT: You stand your ground
          # Mini fight even, check fight()
              You will fight and keep on dying until RNG decides to let you win. You them meet up with TERRY, a young man who decides to take you somewhere
              (not coded) You are given various dialogue options, each with their seperate responses, but in the end, you are taken to a settlement inside the dungeon.
              It turns out that people are periodically dropped into this dungeon, with no recollection of their past. The dungeon spawns monsters, who strength ranges from annoying
              to if-it-sees-you-your-good-as-dead.
      RIGHT: You bump into a dwarf that guards the gates. You must play Rock-Paper-scissors with the troll, best out of three. If you win, the dwarf lets you through and shuts 
              the gate behind him, allowing you to escape
              If you tie, then the dwarf will let you through, but will also let the troll through, forcing you to fight time # same mini fight event as above
              If you lose, the troll does not let you through, and you die
"""

import time, random, sys

def slowprint(string):  # prints text slowly for dramatic effect
    for i in string + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1 / 50)


def talk(name, dialogue):
    sys.stdout.write(f"{name}: ")
    slowprint(f"\"{dialogue}\"")
    time.sleep(1 / 2)



def info():
    option_a = True
    option_b = True
    option_c = True
    while True:
        if option_a:
            print("a) \"Dropped? What does that mean?\"")
        if option_b:
            print("b) \"Tell me more about this \'home\'\"")
        if option_c:
            print("c) \"How did you get here?\"")
        print("d) Exit from dialogue")
        while True:
            user_input = input(">> ").lower()
            if user_input == "a" or user_input == "b" or user_input == "c" or user_input == "d":
                break
            else:
                slowprint("Invalid input")
        if user_input == "a" and option_a:
            talk("Terry",
                 """Yeah, that's what we say when people like you are thrown into the dungeon. "Dropped" is simply a word that we use because none of us remember how we got here. Most of us just kinda woke up in a dark corner and started to wander the dungeon until someone picked us up.""")

            time.sleep(2)

            talk("Terry",
                 """Usually people are dropped pretty close to home, but you're way farther than normal. Most people are found a stone's throw outside of out perimeters. Right now we're more than half a day out.""")
            option_a = False

        elif user_input == "b" and option_b:
            talk("Terry",
                 """Home is the one truly safe place in this dungeon for people like you and me. We're dropped into this place that we call the dungeon, filled with a thousand different things that can kill you. It's quite a large place, something like a village, whatever that means. No monsters spawn within or around it's perimeters, allowing us to sleep and eat in peace.""")
            option_b = False

        elif user_input == "c" and option_c:
            talk("Terry",
                 "I was dropped in here just like you. Dunno where I am, or why I'm here. Honestly it scared the crap out of me...")
            talk("Terry",
                 "Though once I met some of the guys at Home, it became a bit easier to get used to this place. Honestly most people back at home are great guys. I'm sure you'll get along with them")
            option_c = False

        else:
            slowprint("""You both fall silent, not because there isn't more to talk about, but because I'm too lazy to come up with more dialogue options.
            Let's assume that half a day has passed and now you and Terry know each very well.
            """)
            time.sleep(1)
            slowprint(
                """Your legs are starting to feel soft from all the walking, climbing, and running you've been doing. You want to talk a break, but Terry taps you on the shoulder""")
            talk("Terry", "Hey, we're here now")
            slowprint("""You can hear the sound of running water in the distance. A stream perhaps? 
            As you go forward, a large, iron gate comes into view, flanked by two lamps. Warm, yellow light spills from the crack between the two doors. Terry bangs on the door twice before standing back.""")
            talk("Terry", "We're home now. Try not to get too excited, the place is a bit dazzling.")
            slowprint(
                """You can hear the gears creaking, and the door opens outwards. Terry did warn you that the place was dazzling, but nothing could've prepared you for this... """)

            print("############################################")
            print("Thanks for playing! And thanks for making it this far.")
            time.sleep(1)
            slowprint("Credits:")
            time.sleep(2 / 3)
            slowprint("Daniel Zhu")
            time.sleep(1 / 3)
            print("Part 2 coming out never, because I need more coding experience to make an actually good game")
            break


def win():
    global user_input
    slowprint("You Win!")
    slowprint("""You stand over the dead body of the large troll, your arms and legs burning from exhaustion. You sheath your bloody dagger and tentatively step over the corpse. Your vision's starting to blur, and you suddenly feel very, very tired.
    You stagger away from the troll, and you start to wander away
""")
    time.sleep(1)
    slowprint("""
a flurry of footsteps echo in the distance, but your too disorientated to tell where they're coming from. More monsters? It can't be...
You fumble for your knife, but your fingers feel weak and numb. 
""")
    time.sleep(1 / 2)
    sys.stdout.write("voice in the distance: ")
    slowprint("""\"I think the troll went this way. It couldn't of gone -\""
    """)
    time.sleep(1 / 2)
    slowprint("""You come face-to-face with a young man, clad in plate armour. He has a dark complexion and short, curly hair. He has a shortsword in one hand, and a roundshield in the other.
    You look at each other for a second, and then he turns around to shout to someone you can't see.""")
    time.sleep(1 / 2)
    slowprint("\"We got another one!\"")
    time.sleep(0.5)
    sys.stdout.write("voice 1 in the distance: ")
    slowprint("\"Another one?\"")
    time.sleep(0.5)
    sys.stdout.write("voice 2 in the distance: ")
    slowprint("\"What the fuck is doing all the way out here?\"")
    time.sleep(0.5)
    slowprint("""The young man turns his attention back to you""")
    sys.stdout.write("The young man: ")
    slowprint("""\"Hey, it's going to be alright. All of this is probably very confusing for you,
    but don't worry, we'll explain everything to you. But first, drop the dagger\"""")
    slowprint("You realise that your holding a bloody dagger in your hand. You sheath it.")
    sys.stdout.write("The young man: ")
    slowprint("""That's better, we're making progress. My name is Terry, what's yours?""")
    time.sleep(0.5)
    name = input(">> ").upper()
    sys.stdout.write("Terry: ")
    slowprint(f"""\"Hey {name}, nice to meet you. Follow, me, I'll take you somewhere safe.\""
    He shouts at someone in the distance: \"I'll take care of the newbie, you guys head home!\""
    """)
    time.sleep(0.5)
    sys.stdout.write("voice 1 in the distance: ")
    slowprint("""Roger That!""")
    time.sleep(0.5)
    sys.stdout.write("Terry: ")
    slowprint(f"""By the way {name}, did you take out that troll by yourself? """)
    slowprint("He gestures towards the troll carcass")

    print("a) \"Yeah I did\"")
    print("b) \"No, it clubbed itself to death\"")
    print("c) \"Where am I?\"")
    notvalidinput = True
    while notvalidinput:
        user_input = input(">> ").lower()
        if user_input == "a" or user_input == "b" or user_input == "c":
            notvalidinput = False
        else:
            slowprint("Invalid input")
            notvalidinput = True
    if user_input == "a":
        talk("Terry", """Impressive! I don't many people could've of survived againsed a troll on their first day.""")
    elif user_input == "b":
        slowprint("He chuckles to himself")
        talk("Terry", "Yeah, that was a bit of stupid question, wasn't it?")
    else:
        slowprint("He quickly nods his head once.")
        talk("Terry", "Yeah, I'd be asking the same question if I were you...")

    talk("Terry", "Here follow me, we'll talk on the way back. ")
    talk("Terry", """But first, tell me a bit about yourself, or at least, what you remember about yourself? """)
    slowprint("""You realize that besides your name, you can't really remember anything. Did I have parents?""")
    time.sleep(1)
    slowprint("Siblings?")
    time.sleep(1)
    slowprint("What was my life like? Who am I?")
    time.sleep(1 / 2)
    slowprint("You close your eyes. Fuzzy faces flit in and out of your minds eye, but nothing tangible comes up.")

    print("a) \"I can't remember anything\"")
    print(f"b) \"My name is... {name}...\"")
    print("c) \"Think harder\"")

    notvalidinput = True
    while notvalidinput:
        user_input = input(">> ").lower()
        if user_input == "a" or user_input == "b" or user_input == "c":
            notvalidinput = False
        else:
            slowprint("Invalid input")
            notvalidinput = True

    if user_input == "a":
        talk("Terry", """Figures, nobody here really remembers where they came from.""")

    elif user_input == "b":
        slowprint("Terry chuckles good-naturedly")
        talk("Terry", "Don't worry, nobody remembers anything besides their name.")

    elif user_input == "c":
        slowprint("...")
        time.sleep(3)
        talk("Terry", "Honestly, It's not a big deal if you can't remember anything. Nobody remembers anything")
    else:
        talk("Terry", "Under construction")
    slowprint("\"\'Nobody\'? You mean there are other people here?\"")
    time.sleep(1 / 2)
    talk("Terry", """Yeah, they pop up around the Labryith, but it's usually to Home. 
    You dropped way outside of the normal radius.""")
    info()


# Daniel
def combatdead():
    slowprint("Your have 0 hitpoints. You are dead!")
    slowprint("Try again? Y/N")
    tryagain = input(">> ").upper()
    if tryagain == "Y":
        fight()
    else:
        slowprint("Thanks for playing!")



def dead():
    print()
    time.sleep(1)
    slowprint("You have died")
    time.sleep(2)
    slowprint("Play again? Y/N")

    user_input = input(">> ").upper()

    if user_input == "Y" or user_input == "YES":
        start()
    elif user_input == "N" or user_input == "NO":
        slowprint("Thanks for playing!")
    else:
        print("Please enter a valid response")
        time.sleep(1)
        dead()


def bleed(hitpoints, localturn, turn):
    turnstobleed = localturn + 3
    # print (turnstobleed, localTurn, turn)
    if turnstobleed > turn:
        hitpoints = hitpoints - 33
        print("TROLL is BLEEDING, he takes 33 damage")
        turnstobleed -= 1
    else:
        print("BLEED has worn off")
        localturn = None
    return hitpoints, localturn



def trollattack():
    global statuseffect
    ismiss = False
    damagegiven = 0
    hitormiss = random.randint(1, 6)
    if hitormiss == 1:
        statuseffect = None
        iscrit = False
        ismiss = True
    else:
        crit = random.randint(1, 10)
        if crit < 3:
            iscrit = True
            statuseffect = "Dizzy"
            damagegiven = random.randint(10, 80)
        else:
            iscrit = False
            statuseffect = None
            damagegiven = random.randint(10, 80)
    return damagegiven, statuseffect, iscrit, ismiss


# Daniel, rock weapon
def rock(statuseffect):
    statuseffectgiven = None
    iscrit = False
    ismiss = False
    damagegiven = 0
    if statuseffect == "Dizzy":
        hitormiss = random.randint(1, 3)
        if hitormiss == 1:
            ismiss = True
        else:
            crit = random.randint(1, 8)
            if crit == 1:
                damagegiven = random.randint(50, 110)
                iscrit = True
                statuseffectgiven = "Stunned"
            else:
                damagegiven = random.randint(50, 110)

    else:
        hitormiss = random.randint(1, 6)
        if hitormiss == 1:
            ismiss = True
        else:
            crit = random.randint(1, 5)
            if crit == 1:
                damagegiven = random.randint(70, 130)
                statuseffectgiven = "Stunned"
                iscrit = True
            else:
                damagegiven = random.randint(70, 130)

    return damagegiven, statuseffectgiven, iscrit, ismiss


def dagger(statuseffect):
    global statuseffectgiven
    damagegiven = 0
    statuseffectgiven = None
    iscrit = False
    ismiss = False
    if statuseffect == "Dizzy":
        hitormiss = random.randint(1, 5)
        if hitormiss == 1:
            ismiss = True
        else:
            crit = random.randint(1, 5)
            if crit == 1:
                statuseffectgiven = "Bleed"
                damagegiven = random.randint(30, 90)
            else:
                damagegiven = random.randint(30, 90)
    else:
        hitormiss = random.randint(1, 10)
        if hitormiss == 1:
            ismiss = True
        else:
            crit = random.randint(1, 3)
            if crit == 1:
                damagegiven = random.randint(40, 100)
                iscrit = True
                statuseffectgiven = "Bleed"
            else:
                damagegiven = random.randint(40, 100)
    return damagegiven, statuseffectgiven, iscrit, ismiss



def endfight(trollhitpoints, userhitpoints):
    if trollhitpoints < 0:
        win()
        return False
    elif userhitpoints < 0:
        combatdead()
        return False
    else:
        return True


def trollturn(enstatuseffect, userhitpoints):
    hits = trollattack()
    statuseffect = None
    if enstatuseffect == "Stunned":
        slowprint("TROLL is STUNNED, so he missed!")
    else:
        if hits[2]:
            slowprint("Critical Hit!")
            userhitpoints = userhitpoints - hits[0] * 1.5
            slowprint(f"He deals {hits[0] * 1.5} damage")
            slowprint("You are now DIZZY, so your attack will be weaker next turn. ")
            statuseffect = "Dizzy"
        else:
            if hits[3]:
                slowprint("TROLL has missed! ")
            else:
                userhitpoints = userhitpoints - hits[0]
                slowprint(f"He deals {hits[0]} damage")
    return userhitpoints, statuseffect

  
def talk():
  
    slowprint("You: Hi....Hello??.... ")

    time.sleep(1/3)

   # While loop here
    while True:
        # Ask question
        print("What do you want to do next", end = "\n")

        print("a) Continue asking")
        print("b) Keep hiding ")

        # Obtain input: a for ask, b for hide
        ask_or_hide = input("Your answer (a/b) >> ").lower()

        # Handle "ask" below
        if ask_or_hide == "a":
            slowprint("You start talking and ask what he wants ")
            time.sleep(1)

            slowprint("You: ...What do you want from me?... ")
            time.sleep(1)

            slowprint("Monster talks slowly: gerrr you huamn have been killing the forest ")
            slowprint("Monster talks slowly: Now we have no where to live ")
            time.sleep(1)

            # Next decision to make
            print("What do you need to do next", end = "\n")

            # While loop here
            while True:
                print("a) Comfort and appease Monster")
                print("b) Fight back with your words ")

                # Get input, a for conmfort talking, b for hard words
                comfort_or_hard = input(">> ").lower()

                # Comfort talking
                if comfort_or_hard == "a":
                    slowprint("We realized that has been a problem and tried to fix it... ")
                    time.sleep(1)

                    slowprint("You have successfully convinced the monster and left safely ")
                    time.sleep(1)

                    # You win!!!
                    win_1()
                    break

                # Hard words to monster
                elif comfort_or_hard == "b":
                    slowprint("So What??! This has nothing to do with me!! ")
                    time.sleep(1)
                    slowprint("It is triggered by your speech and killed you")
                    time.sleep(1)

                    # You died, sorry...
                    dead()
                    break

                # Valid answer must be given
                else:
                    print("Please enter a or b")
                    time.sleep(1)
                    continue

            # break the loop
            break
           
        # Handle "hide"
        elif ask_or_hide == "b":
            slowprint("You decided to keep hiding to see what will happen... ")
            time.sleep(1)

            slowprint("The monstor eventually found you and killed you before you said anything... ")

            # You died, too bad
            dead()
            
            # break the loop
            break 

        else:
            # Valid answer must be given, go back to loop again
            print("Please enter a or b")
            time.sleep(1)
            continue

            
def hide2():
    slowprint("You decided to stay hidden behind the rocks.")
    time.sleep(1)
    slowprint("You went deeper inside the piles of rocks. You hear something ruffling behind you and you thought it was a troll but.....")
    time.sleep(1)
    slowprint("but there was a human as you also hiding from troll. He was squatting down behind the rocks.")
    time.sleep(1)
    slowprint("would you like to go talk to him or ignore.")
    time.sleep(1)
    print('\n' * 0)

    while True :
        print("a) Go talk to him.")
        print("b) Ignore him.")

        user_input = input("Enter a or b >> ").lower()
        if user_input == "a" :
            slowprint("You decided to go talk to him.")
            time.sleep(1)
            slowprint("He said his name is Michael and a geographer. He came to this dungeon to solve the mystery that was unsolved since before 100 years.")
            time.sleep(1)
            slowprint("He ask for help to get out of this place together. Would you be alone or together.")
            time.sleep(1)
            print('\n' * 0)

            while True :
                print("a) Alone")
                print("b) Together")

                user_input = input("Enter a or b >> ").lower()
                if user_input == "a":
                    slowprint("You chose to be alone. You are now finding any other gates to outside. Suddenly, you heavy footsteps get closer and faster to you. When you turned to see where it was coming, troll was already behind you. You are going to fight.")
                    time.sleep(1)
                    fight()
                    break 

                elif user_input == "b":
                    slowprint("You are now going to find the gate to outside with Michael. You walked and walked and walked..")
                    time.sleep(1)
                    slowprint("Finally you find bright beam of light, it was a hole to the outside. You and Michael decided to go out. Mihcael stepped out and went out of the dungeon already. ")
                    time.sleep(1)
                    slowprint("As soon as you was going to go out, you were caught by the troll. As soon as you were caught by the troll, Michael ran away and left me alone. There was no choice but fight or die.")
                    time.sleep(1)
                    print('\n' * 0)
                    break 

                    while True :
                        print("a) Fight")
                        print("b) Just lie down and die")

                        user_input = input("Enter a or b >> ").lower()
                        if user_input == "a":
                            fight()
                            break 

                        elif user_input == "b":
                            dead()
                            break

                        else:
                            print("Please enter a valid answer.")
                            continue 
                            
                else:
                    print("Please enter a valid answer.")
                    continue 
                    
            break 
            
        elif user_input == "b":
            slowprint("You decided to ignore him. You are now going to walk alone and find a way out. However, you meet the troll right infront of it. You are going to fight with it.")
            time.sleep(1)
            fight()   
            break 
                  
        else:
            print("Please enter a valid answer.")
            continue 


def hide():
    slowprint("Hide quickly behind rock and plan next ")    
    time.sleep(1)

    while True:
        # Ask question
        print("What do you want to do next", end = "\n")

        print("a) Ask what he wants")
        print("b) Stay hidden")
   
        talk_or_hide = input("Please answer a/b >> ").lower()
        
        if talk_or_hide == 'a':
            talk()
            break
            
        elif talk_or_hide == 'b':
            hide2()
            break
        
        else:
            print("Please enter valid answer, a or b.")

def start():
    slowprint("""You wake up in a completely dark, damp dungeon, with little to no recollection of what placed you here.""")
    time.sleep(1/3)
    print()
    slowprint("""Feeling the cold, rocky floor with your hands, you find a torch, a knife and some flint. Getting out of here is a reasonably good idea, given the situation, so you light the torch, and start to traverse down the damp and musty corridors.""")
    print()
    time.sleep(1/3)
    for i in range(3):
        time.sleep(1)
        print("tip...")
        time.sleep(1)
        print("tap...")
    time.sleep(1)
    slowprint("""You hear heavy footsteps in the distance. Something big is coming, and it's approaching fast. Do you:
    a) run
    b) hide""")
    # Verification
    notvalidinput = True
    while notvalidinput:
        user_input = input(">> ").lower()
        if user_input == "a" or user_input == "run" or user_input == "b" or user_input == "hide":
            notvalidinput = False
        else:
            slowprint("Invalid input")
            notvalidinput = True 
        
    if user_input == "a" or user_input == "run":
        slowprint("You turn tail and run as fast as you can. You can feel your heart heart beating frantically in your chest while you weave through tunnels and climb up staircases. Eventually you face a split in the tunnel. Do you turn left or turn right? L/R")
        print()
        run()
        notvalidinput = False
    else: 
        hide()


def run():
    notvalidinput = True
    while notvalidinput:
        user_input = input(">> ").lower()
        if user_input == "l" or user_input == "r":
            notvalidinput = False
        else:
            slowprint("Invalid input")
            notvalidinput = True

    if user_input == "l":
        slowprint(
            """The left path looks better, so you bolt left. The sound behind you is getting louder and louder. You make a right, but alas, it's a dead end! """)
        time.sleep(1 / 3)
        print()
        slowprint(
            """The the heavy footsteps are now right behind you, finally allowing you to get a good look at your pursuer""")
        time.sleep(1 / 3)
        print()
        slowprint("""It's a large, slobering troll! With a splintered wooden club in his hand, it stares you down. Do you:
        a) fight
        b) pray
        c) run
        """)
        notvalidinput = True
        while notvalidinput:
            user_input = input(">> ").lower()

            if user_input == "a" or user_input == "fight" or user_input == "b" or user_input == "pray" or user_input == "c" or user_input == "run":
                notvalidinput = False
            else:
                notvalidinput = True
                print("Invalid input")

        if user_input == "a" or user_input == "fight":
            slowprint("""This is not time to pray, nor is a time to run. You must FIGHT! Alas, you don't have many weapons, and the troll looks like it wants to crush you with that bludgeon in it's hand. Into battle!
                """)
            print()
            fight()
        elif user_input == "b" or user_input == "pray":
            slowprint(
                "You get on your knees to pray, but before you can even utter a single prayer, The troll brings his club down on you, and everything goes dark")
            dead()
        elif user_input == "c" or user_input == "run":
            slowprint(
                """You try to get around the troll with your speed. It's quite big, so it's probably slow, right? """)
            time.sleep(1 / 3)
            print()
            slowprint(
                """But even a large, lumbering fool can guard a dead end, and as soon as you try to run around him, he swats his mighty blugeon, turning you into a stain on the dungeon wall """)
            dead()
        else:
            print("Please enter a valid response")

    elif user_input == "r":
        slowprint("""You sprint down the right path as fast as you can, and you can hear it catching up with you.""")
        time.sleep(2)
        slowprint("""After running for a bit, you reach a large, ironclad door, guarded by a stout dwarf
        \n" please, let me through, """)
        rps()
    else:
        print("Please enter  a valid response")
        time.sleep(1)
        run()


def fight():
    trollhitpoints = 600
    userhitpoints = 200
    dodge = False
    statuseffect = None
    enstatuseffect = None
    localturn = None
    turn = 1
    print("############################################################")
    while trollhitpoints > 0 and userhitpoints > 0:
        print()
        print(f"Your HP: {userhitpoints}                TROLL's HP: {trollhitpoints}")
        slowprint("Your turn to attack! What is your move?")
        print()
        print("Stab with Dagger")
        print("Hurl a rock")
        print("Dodge")
        print()
        notvalidinput = True
        while notvalidinput:
            playermove = input(">> ").lower()
            if playermove in ["stab", "with", "dagger"] or playermove in ["hurl", "a", "rock"] or playermove == "dodge":
                notvalidinput = False
            else:
                notvalidinput = True
                print("Invalid input")

        if playermove in ["stab", "with", "dagger"]:
            hits = dagger(statuseffect)
            enstatuseffect = hits[1]
            if hits[2]:
                if dodge:
                    damage = hits[0] * 4
                    trollhitpoints = trollhitpoints - damage
                else:
                    damage = hits[0] * 2

                    trollhitpoints = trollhitpoints - damage
                slowprint(f"You have stabbed TROLL, dealing {damage} damage!")
                localturn = turn
                slowprint("Critical hit! TROLL is now bleeding, and will take damage for the next three turns. ")
            else:
                if hits[3]:
                    slowprint("You have missed! ")
                else:
                    if dodge:
                        damage = hits[0] * 2
                        trollhitpoints = trollhitpoints - damage
                    else:
                        damage = hits[0]
                        trollhitpoints = trollhitpoints - damage
                    slowprint(f"You have stabbed TROLL, dealing {damage} damage!")
                    enstatuseffect = None

            dodge = False

        elif playermove in ["hurl", "a", "rock"]:
            rockhits = rock(statuseffect)
            enstatuseffect = rockhits[1]
            if rockhits[2]:
                if dodge:
                    damage = rockhits[0] * 4
                    trollhitpoints = trollhitpoints - damage
                else:
                    damage = rockhits[0] * 2
                    trollhitpoints = trollhitpoints - damage

                slowprint(f"You have thrown a rock at TROLL, dealing {damage} damage!")
                slowprint("Critical hit! TROLL is now STUNNED, and will miss his next turn. ")

            else:
                if rockhits[3]:
                    slowprint("You have missed!")
                else:
                    if dodge:
                        damage = rockhits[0] * 2
                        trollhitpoints = trollhitpoints - damage
                    else:
                        damage = rockhits[0]
                        trollhitpoints = trollhitpoints - damage
                slowprint(f"You have thrown a rock at TROLL, dealing {damage} damage!")

            dodge = False

        elif playermove == "dodge":
            dodge = True
            statuseffect = None

        if endfight(trollhitpoints, userhitpoints):
            slowprint("TROLL attacks; he swings his mighty stick at you. ")

            if dodge:
                if statuseffect == "Dizzy":
                    isdodge = random.randint(4, 10)
                    if isdodge < 4:
                        slowprint("You tried to dodge, but you wern't fast enough! ")
                    else:
                        slowprint("You managed to dodge his attack, and your next attack will be stronger!")

                else:
                    isdodge = random.randint(1, 10)
                    if isdodge == 1:
                        slowprint("You tried to dodge, but you wern't fast enough! ")
                        stats = trollturn(enstatuseffect, userhitpoints)
                        userhitpoints = stats[0]
                        statuseffect = stats[1]
                    else:
                        slowprint("You managed to dodge his attack, and your next attack will be stronger!")

            else:
                stats = trollturn(enstatuseffect, userhitpoints)
                userhitpoints = stats[0]
                statuseffect = stats[1]

            if localturn is not None:
                bleeding = bleed(trollhitpoints, localturn, turn)
                trollhitpoints = bleeding[0]
                localturn = bleeding[1]
            turn += 1
            endfight(trollhitpoints, userhitpoints)
        else:
            break
#_______________________________________ end of fight()


def decide_dwarfinput(last):
    i = random.randint(1, 3)
    while i == last:
        i = random.randint(1, 3)
    return i


  
def decide_winner(user, troll):
    if user == troll:
        return 0
    elif user-1 == troll:
        return 1
    elif user == 1 and troll == 3:
        return 1
    return 2



def rps():
    score_player = 0
    score_dwarf = 0
    last = -1
    slowprint("In order to pass the door, you must defeat dwarf in a game of rock paper scissors. But the drawf isnt very smart, he will not use whatever he used last time")
    
    for i in range(3):
        print(f"round {i+1}")
        print("(a) rock")
        print("(b) paper")
        print("(c) scissors")
        
        drawf_input = decide_dwarfinput(last)
        last = drawf_input
        
        notvalidinput = True
        while notvalidinput:
            choice = input("choose the option you want to use: ").lower()
            if choice == "a" or choice == "b" or choice == "c":
                notvalidinput = False
            else:
                slowprint("Please enter a valid response")
                notvalidinput = True
        
        if choice == 'a':
            user_input = 1
        elif choice == 'b':
            user_input = 2
        else:
            user_input = 3 
        
        situation = decide_winner(user_input, drawf_input)
        if situation == 1:
            score_player += 1
            print("you have won this round")
        elif situation == 0:
            print("It is a draw")
        else:
            score_dwarf += 1
            print("you have lost this round")
        print()
    
    if score_dwarf > score_player:
        slowprint("You have lost the match against the old dwarf, so he doesn't let you through.") 
        slowprint("You beg and you plead him to let you pass, but before you know it, the sounds are already right behind you, and everything goes black.")
        dead()
    elif score_player > score_dwarf:
        slowprint("You have defeated the dwarf, as promised, he allows you pass.") 
        slowprint("The dwarf locks the gate behind you, and you can hear the angered cries of the monster as he bangs againsed the bars.")
        run2()
    else:
        slowprint("It's a draw, so the dwarf refuses to allow you pass. However, he shows you a good hiding spot nearby that might help in escaping the monster")
        hide()
        

def run2():
    slowprint("Walking down the path at the dwarf had opened for you. The sound behind you is getting louder and louder. You make a right, but alas, it's a dead end! ")
    time.sleep(1/3)
    slowprint("The the heavy footsteps are now right behind you and you get a good look at your pursuer")
    time.sleep(1/3)
    slowprint("It's a large, slobering troll! With a splintered wooden club in his hand, it stares you down. Do you:")
    slowprint("(a) fight")
    slowprint("(b) pray")
    slowprint("(c) run")
    
    notvalidinput = True
    while notvalidinput:
        user_input = input(">> ").lower()
        if user_input == "a" or user_input == "fight" or user_input == "b" or user_input == "pray" or user_input == "c" or user_input =="run":
            notvalidinput = False
        else:
            slowprint("Please enter a valid response")
            notvalidinput = True
    
    if user_input == "a" or user_input == "fight":
            slowprint("This is not time to pray, nor is a time to run. You must FIGHT! Alas, you don't have many weapons, and the troll looks like it wants to crush you with that bludgeon in it's RIGHT hand. Into battle")
            fight()
    elif user_input == "b" or user_input == "pray":
            slowprint("You get on your knees to pray, but before you can even utter a single prayer, The troll brings his club down on you.")
            dead()
    elif user_input == "c" or user_input =="run":
            slowprint("You try to get around the troll with your speed. It's quite big, so it's probably slow, right? ")
            time.sleep(1/3)
            slowprint("But even a large, lumbering fool can guard a dead end, and as soon as you try to run around him, he swats his mighty blugeon, turning you into a stain on the dungeon wall ")
            dead()
   

  
start()
