def favourite_things(*args):
    for index, i in enumerate(args, start=1):
        if i.endswith("s"):
            verb = "are"
        else:
            verb = "is"

        if index == 1:
            print(f"One of my favourite things {verb} {i}")
        else:
            print(f"Another of my favourite things {verb} {i}")
    if len(args) > 1:
        sentence_start = "These are"
    else:
        sentence_start = "This is"
    print(f"{sentence_start} {len(args)} of my favourite things")

# favourite_things("chocolate", "videogames", "holidays", "relaxing")
# favourite_things("chocolate")

def favourite_things_2(*args, **kwargs):
    if len(kwargs) != 0:
        if len(kwargs) == 1:
            for i in kwargs:
                print(f"My most favourite thing is:\n {kwargs[i]}")
        else:
            print(f"My most favourite things are:")
            for i in kwargs:
                print(f" {i}: {kwargs[i]}")

    if len(args) != 0:
        if len(kwargs) > 0:
            print("Some of my other favourite things are:")
        else:
            print("Some of my favourite things are:")
        for i in args:
            print(f" {i}")


favourite_things_2("chocolate", "videogames")
favourite_things_2("chocolate", "videogames", First="holidays")
favourite_things_2("chocolate", "videogames", First="holidays", Second="relaxing")
