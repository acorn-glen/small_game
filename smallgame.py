#Characters: Dungeon Masta, [player = Eugene]

print "\tWELCOME TO DUNGEON KNOCK OFF!"

import time
time.sleep(1)

user_name = raw_input("Enter your name: ")

time.sleep(1)

print "\tSo... you're name is {name}?".format(name = user_name)

raw_input("Y/N: ")

x = 0
while x < 3:
    time.sleep(.7)
    print ".",
    x = x + 1
time.sleep(0.4)

print
print "\tAhh! You're name is Eugene! Wonderful!"
time.sleep(2)

print
print "\tWell, Eugene, you are here to test your wits!"
time.sleep(3)

print"\tTo challenge your brain! To think, not just type nonsense and hope it works!"
time.sleep(2)

print
print "\tI hope you are ready for this ordeal?"
time.sleep(2)

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

time.sleep(1)

print
print "You are making your way to your one true love's abode."

time.sleep(1)

print
print "You come to a fork in the road."

time.sleep(2)

print
print "You see that if you go one way, you will enter a dark entrance in the side of a mountain."

time.sleep(1)

print
print "But the other way continues up the mountain to your one true love's house."

print "Which way do you go?"

choice_fork = raw_input("'UP' or 'THROUGH': ")

if choice_fork == "UP":
    # This marks a split in the paths. This needs to be directed towards the code AFTER the IF statement.
    print
    print "You went up the mountain."
elif choice_fork == "THROUGH":
    print
    print "You went into the mountain."
else:
    print
    print "You typed a command in wrong. Congratulations. Now the program's broken." 
    
    time.sleep(2)
    
    print
    print "Let's just keep going, shall we?"
    
    time.sleep(2)
    
    print
    print "You end up going into the mountain. Easy passage through? Nope. Chuck Testa."
    
    time.sleep(2)
    
    print
    print "You look around you."
    raw_input("Type 'Look around': ")
    
    time.sleep(2)
    
    print
    print "You see something glitter in the wall."

    time.sleep(2)

    print
    print "You are curious. You should totally walk over there."

    total_control = raw_input("But do whatever you want. You're the one playing this game.\nNow, I give you full reign over the commands. Type \"HELP\" for a list of commands\n>")
    
    x = 0
    
    while x < 3:
        time.sleep(.7)
        print ".",
        x = x + 1
    
    time.sleep(1)
    
    if total_control == "HELP":
        print
        print "Haha, screw you!"
        
        time.sleep(1)
        
    elif total_control == "no":
        print
        print "yes"
        
        time.sleep(1)
    
    print
    print "You go walk to the glittering object."
    
    time.sleep(2)
    
    print
    print "It is so shiny. You want to touch it."
    object_touch = raw_input("To touch it, type 'TOUCH': ")    
    
    time.sleep(1)
    
    print
    print "*Rumble*",
    
    time.sleep(3)
    
    print "*Rumble*",
    
    time.sleep(1)
    
    print "*RUMBLE*"
    
    time.sleep(2)
    
    print "RRRRRRRRRUUUUUUUUUUUMMMMMMMMMMMBBBBBBBBBBBBLLLLLLLLLLEEEEEEEEEEEE!!!!"
    
# Boss fight starts here, and it's NOT in the IF statement. This is the end for ALL the outcomes.