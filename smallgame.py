#Characters: Dungeon Masta, [player = Eugene]
import time

print "\tWELCOME TO DUNGEON KNOCK OFF!"

time.sleep(2)

user_name = raw_input("Enter your name: ")

time.sleep(2)

print "\tSo... your name is {name}?".format(name = user_name)

raw_input("Y/N: ")

x = 0
while x < 3:
    time.sleep(.7)
    print ".",
    x = x + 1
time.sleep(0.4)

print
print "\tAhh! You're name is Eugene! Wonderful!",
raw_input()
print
print "\tWell, Eugene, you are here to test your wits!",
raw_input()

print "\tTo challenge your brain! To think, not just type nonsense and hope it works!",
raw_input()

print
print "\tI hope you are ready for this ordeal?"


raw_input("Y/N: ")

while x < 3:
    time.sleep(.7)
    print ".",
    x = x + 1
    
print "\tGood, good!"

time.sleep(2)

print "\tNOW...",

time.sleep(.5)

print "LET THE FUN BEGIN!"

time.sleep(1.3)

print
print "______________________________________________________________________________"
print
print """DISCLAIMER: If you have epilepsy, you should be fine playing this game,
 but if you die while playing it, we are definitely not responsible. In fact, 
 if anything bad happens to you while playing this complex and challenging game,
 IT'S NOT OUR FAULT. If you are playing copyrighted music while playing this game,
 turn it off, because it is probably really bad."""
print "______________________________________________________________________________"

time.sleep(6)

print "\nTHE STORY:\n\n"
print "You are on a journey."
print

raw_input()

print
print "You are making your way to your one true love's abode."

raw_input()

print
print "You come to a fork in the road."

raw_input()

print
print "You see that if you go one way, you will enter a dark entrance in the side of a mountain."

raw_input()

print
print "But the other way continues up the mountain to your one true love's house."

print "Which way do you go?"

choice_fork = raw_input("'up' or 'through': ")

if choice_fork == "up":
    # This marks a split in the paths. This needs to be directed towards the code AFTER the IF statement.
    print
    print "You went up the mountain.",
    raw_input()
    print
    print "On your way up, you soak in the sunrays, feel the cool breeze, and whistle a tuneless song.", raw_input()
    print
    print "Gravel crunching beneath your shoes, you think about that dream you had last night.", raw_input()
    print
    print "Weird wasn't it? Some dis-embodied voice asked you what your name was and then comepletely ignored what you said.", raw_input()
    print
    print "You know your name though. It's {name}.".format(name = user_name), raw_input()
    print
    print "You notice something unusual on the side of the road."
    print
    print "HINT: to look at your surroundings, type \"look\"."
    player_look = raw_input('> ')
    if player_look == "look":
        print "It's a goblin.", raw_input()
        print
        print "Funny... they don't usually go romping around in broad daylight.", raw_input()
        print
        print "\"I don't like this,\" you say \"but I don't have the tools to deal with that yet.\"", raw_input()
        encounter_choice = raw_input("To encounter goblin, type \"encounter\". To move on, just press ENTER.\n> ") 
        if encounter_choice == "encounter":
            print "You approach the goblin.", raw_input()
            print
            print "It eyes you warily as you approach.", raw_input()
            print
            print "It bears its teeth. It's hide is as thick as rock.", raw_input()
            print
            print "Are you sure you want to fight him?"
            are_you_sure = raw_input("yes/no\n> ")
            if are_you_sure == "yes":
                print
                print "You strike with lighting fast punches.", raw_input()
                print
                print "The goblin is surprised.", raw_input()
                print
                print "He didn't think you would be so stupid.", raw_input()
                print
                print "And frankly, I didn't either.", raw_input()
                print
                print "I knew you were stupid... but I didn't know you were THIS dumb.", raw_input()
                print
                print "The goblin took no damage.", raw_input()
                print
                print "Bet you feel pretty smart NOW, eh {name}?".format(name = user_name), raw_input()
                print
                print "The goblin shakes you down steals, your money, and runs off, howling with laughter.", raw_input()
                print
                print "You look like a complete idiot.", raw_input()
                print
                print "Because you are.", raw_input()
                print
                print "You return to the road.", raw_input()
            else:
                print "{name} pales at those rows of sharp teeth.".format(name = user_name), raw_input()
                print
                print "You run away like a wimp.", raw_input()
                print
                print "Because you are.", raw_input()
                print
                print "You return to the road.", raw_input()
                print
        else:
            print "{name} passes".format(name = user_name), raw_input()
            print
            print "on the other side of the road", raw_input()
            print
            print "like a coward.", raw_input()
            print
            print "Because that's exactly what you are.", raw_input()
            print
            print "You continue down the road.", raw_input()
            print
    else:
        print "You choose not to look at your surroundings.", raw_input()
        print
        print "Because you're an idiot", raw_input()
        print
        print "You're probably fat too."
                
elif choice_fork == "through":
    print
    print "You went into the mountain."
else:
    print
    print "You typed a command in wrong. Congratulations. Now the program's broken.",
    
    raw_input()
    
    print
    print "Let's just keep going, shall we?",
    
    raw_input()
    
    print
    print "You end up going into the mountain. Easy passage through? Nope. Chuck Testa.",
    
    raw_input()
    
    print
    print "You look around you."
    raw_input("Type 'look around': ")
    
    time.sleep(1)
    
    print
    print "You see something glitter in the wall."

    time.sleep(1)

    print
    print "You are curious. You should totally walk over there."

    total_control = raw_input("But do whatever you want. You're the one playing this game.\nNow, I give you full reign over the commands. Type \"HELP\" for a list of commands.\n>")
    
    x = 0
    
    while x < 3:
        time.sleep(.7)
        print ".",
        x = x + 1
    
    time.sleep(1)
    
    if total_control == "HELP":
        print
        print "Haha, screw you!",
        
        raw_input()
        
    elif total_control == "no":
        print
        print "yes",
        
        raw_input()
    
    print
    print "You go walk to the glittering object.",
    
    raw_input()
    
    print
    print "It is so shiny. You want to touch it."
    object_touch = raw_input("To touch it, type 'touch': ")
    
    time.sleep(1)
    
    print
    print "*Rumble*",
    
    time.sleep(3)
    
    print "*Rumble*",
    
    time.sleep(1)
    
    print "*RUMBLE*",
    
    time.sleep(2)
    
    print "RRRRRRRRRUUUUUUUUUUUMMMMMMMMMMMBBBBBBBBBBBBLLLLLLLLLLEEEEEEEEEEEE!!!!"
    
# Boss fight starts here, and it's NOT in the IF statement. This is the end for ALL the outcomes.