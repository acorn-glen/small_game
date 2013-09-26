print "WELCOME TO DUNGEON KNOCK OFF!"
import time
time.sleep(1)

user_name = raw_input("Enter your name: ")

time.sleep(1)

print "So... you're name is {name}?".format(name = user_name)

raw_input("Y/N: ")

x = 0
while x < 3:
    time.sleep(1)
    print ".",
    x = x + 1

time.sleep(0.4)

print
print "Ahh! You're name is Eugene! Wonderful!"

time.sleep(2)
print
print "Well, Eugene, you are here to test your wits! To challenge your brain! To think, not just type in nonsense!"