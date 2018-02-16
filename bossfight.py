'''
this is the bossfight for small_game
'''
import time

print "You see a gigantic rock golem stand up in front of you 20 yards",
time.sleep(1),
raw_input()
print "do you wish to engage the golem in a battle?"
print "Y/N:",
time.sleep(2),
print "\nToo late! mr.golem blasted a rock at you",
time.sleep(1),
raw_input()
print "you take 999 damage",
time.sleep(1),
raw_input()

for x in range (0, 1001):
    if x < 900:
        time.sleep(0.003)
        print "\r{0}" .format (1000 - x+1),
    else:
        time.sleep(0.01)
        print "\r{0}" .format (1000 - x+1),

print "\n"
print "ba-bump",
time.sleep(1),
print "ba-bump",
time.sleep(1),
print "ba-bump",
time.sleep(1),
raw_input()
print "You have one HP left!",
time.sleep(1),
raw_input()
print "He is hard as rock",
time.sleep(1),
raw_input()
print "Throw a rock at the golem?"
print "Y/N:",
raw_input()

for x in range (0, 3):
    time.sleep(0.5)
    print ".",

print "\n"
print "You run up the hill to your right over to a ledge above the golem -",
time.sleep(1),
raw_input()
print "and push a large boulder over the ledge and onto the golem",
time.sleep(1),
raw_input()
print "It's a one hit KO!",
time.sleep(1)
raw_input()
print "-------------- THE END --------------"

#optional faintedness

print "you wobble over to a safe looking area and pass out"