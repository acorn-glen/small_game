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