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
    time.sleep(1)
    print ".",
    x = x + 1

time.sleep(0.4)

print
print "\tAhh! You're name is Eugene! Wonderful!"

time.sleep(2)
print
print """\tWell, Eugene, you are here to test your wits!
\tTo challenge your brain! To think, not just type nonsense!"""
