'''The Great Morning Scramble!'''

# from custom_error import MyCustomError
from scr.modules import *
from data.locations import locations_and_outcomes

count = 0

while True:
    if count == 3:
        print("\n" *10)
        print("too late, you're late... probably best if you call in sick")
        break    
    elif count == 0:
        print("You're late for work and your door key has vanished into thin air!")
    else:
        print("You're still late, hurry up, you don't have much time left")
    
    if search_location(int(input(assamble_question(locations_and_outcomes))), locations_and_outcomes):
        print("Congrats, you found the key. you should be get to work on time today... though before you go out the door. Where are your pants?")
        break

    count += 1
