def assemble_question(location_dict):
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
        #     raise MyCustomError("formatting of locations.py is not correct!")
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
