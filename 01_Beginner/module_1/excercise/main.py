'''The Great Morning Scramble!'''

count = 0

while True:
    if count == 3:
        print("\n" *10)
        print("too late, you're late... probably best if you call in sick")
        break
    if count == 0:
        print("You're late for work and your door key has vanished into thin air!")
    else:
        print("You're still late, hurry up, you don't have much time left")

    choice = input("Where do you want to look?\n" \
        "1. Check in your wellies\n" \
        "2. Check onder the mat\n" \
        "3. Check in the rubbish bin\n" \
        "Choos 1, 2, or 3: ")

    match choice:
        case "1" | "1.":
            print("\n" *10)
            print("no luck mate, just a single selly sock with a mouldy apple core")
        case "2" | "2.":
            print("\n" *10)
            print("no key, just a bunch of slaters scatter around")
        case "3" | "3.":
            print("\n" *10)
            print("who put it in there?... your're the only one in the house")
            break
        case _:
            print("\n" *10)
            print("not a valid option")

    count += 1
