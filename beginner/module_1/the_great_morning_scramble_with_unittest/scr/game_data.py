class Game_data:
    def __init__(self, location_dict):
        self.location_dict = location_dict
        self.question = self.assemble_question(location_dict)

    def assemble_question(self, location_dict):
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

    def search_location(self, location):
        if location in self.location_dict:
            print("\n" *10)
            print(self.location_dict[location][1])
            return self.location_dict[location][2]
        else:
            print("\n" *10)
            print("not a valid option")
            return False

if __name__ == "__main__":
    raise Exception("Don't run this module, go to project root and run main.py instead")
