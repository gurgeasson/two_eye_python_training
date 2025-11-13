class Game:
    count = 0
    def __init__(self, locations):
        self.locations = locations
    
    def run_game(self):
        while True:
            if self.count == 3:
                print("\n" *10)
                print("too late, you're late... probably best if you call in sick")
                break    
            elif self.count == 0:
                print("You're late for work and your door key has vanished into thin air!")
            else:
                print("You're still late, hurry up, you don't have much time left")
            
            if self.locations.search_location(int(input(self.locations.question))):
                print("Congrats, you found the key. you should be get to work on time today... though before you go out the door. Where are your pants?")
                break

            self.count += 1

if __name__ == "__main__":
    raise Exception("Don't run this module, go to project root and run main.py instead")
