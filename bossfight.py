'''
this is the bossfight for small_game
'''
import time

clear_line = "\r{0}" .format(" " * 20)

print "You see a gigantic rock golem stand up in front of you 20 yards"
raw_input()
print "do you wish to engage the golem in a battle?"
print "Y/N:",
time.sleep(2)
print "\nToo late! mr.golem blasted a rock at you"
raw_input()
print "you take 755 damage"
raw_input()

for x in range (0, 755):
    time.sleep(0.005)
    print "\r {0}" .format (1000 - x),
    print clear_line,

print "He is hard as rock"
raw_input()
print "Throw a rock at the golem?"
print "Y/N:",
raw_input()

for x in range (0, 2):
    time.sleep(0.5)
    print ".",

print "You run up the hill to your right over to a ledge above the golem"
print "and push a large boulder over the ledge and onto the golem"