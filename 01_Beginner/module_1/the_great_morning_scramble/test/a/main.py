'''The Great Morning Scramble!'''

# from custom_error import MyCustomError
from locations import locations_and_outcomes

count = 0

def assamble_question(location_dict):
    count = 0
    number_of_locations = len(location_dict)
    question = "Where do you want to look?\n"
    help_text = "Type "
    for location in location_dict:
        count += 1
        if location == count:
            question += f"{count}. Check {location_dict[location][0]}\n"
            if count < number_of_locations:
                help_text += f"{count}, "
            elif count == number_of_locations:
                help_text += f"or {count}: "
        # else:
            # raise MyCustomError("formatting of locations.py is not correct!")
    question += help_text
    return question

def search_location(location, locations_and_outcomes):
    if location in locations_and_outcomes:
        print("\n" *10)
        print(locations_and_outcomes[location][1])
        return locations_and_outcomes[location][2]
    else:
        print("\n" *10)
        print("not a valid option")
        return False

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
