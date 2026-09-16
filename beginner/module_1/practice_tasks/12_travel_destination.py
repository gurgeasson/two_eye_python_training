'''
Instructions

    1) Create an empty dictionary called travel_destinations.
    2) Define a function called add_destination that takes two arguments: name
        and info.
    3) Using dictionary notation, assign name and info as the new key-value
        pair to the existing travel_destinations dictionary. After that,
        print a message to show the destination has been added.
    4) Create dictionaries for individual destinations containing "country",
        "population_millions", and "landmarks".

'''

travel_destinations = {}

def add_destination(name, info):
    travel_destinations[name] = info
    print(f"Destination {name} has been added with info: {info}")

edinburgh = {
    "country" : "Scotland",
    "population_millions" : 0.5,
    "landmarks" : "piles of rubbish everywhere, the last remaining building that is not an airBnB, Bobby"
    }
