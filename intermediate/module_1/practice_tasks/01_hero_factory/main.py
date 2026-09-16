'''You are a scientist known across the land for creating the best and most powerful superheros.
    It's another day at the lab and you now have all the tools to create the ultimate superhero.

    - Create a class for your superhero and define its stats for strength, speed and whether it can fly or not
    - Create a function perform_ability() that defines what happens when your hero uses their special power
    - Create an instance of the class to make the hero come to life
    - Feel free to add as many abilities to your hero as you like and create multiple heroes to practice inheritance
'''

class Superhero:
    def __init__(self, name, ability, strength, speed):
        self.name = name
        self.ability = ability
        self.strength = strength # 1 - 10
        self.speed = speed # 1 - 10

    def __repr__(self):
        return f'Superhero data(name="{self.name}", ability="{self.ability}", strength={self.strength}, speed={self.speed})'
    
    def __add__(self, other):
        if not isinstance(other, Superhero):
            return NotImplemented
        else:
            return f'The combined strength of these superheroes is: {self.strength} + {other.strength}'
        
    def __iter__(self):
        yield self.name
        yield self.ability
        yield self.strength
        yield self.speed

    def __str__(self):
        return f'{my_superhero.name} is a superhero with a strength of {my_superhero.strength} and a speed of {my_superhero.speed}, who\'s super power is their {my_superhero.ability}.'

    def perform_ability(self):
        print(f'{self.name} using their super power, {self.ability}.')

class Flying_hero(Superhero):
        def __str__(self):
            return f'{super().__str__()} They can fly.'

class Not_flying_hero(Superhero):
        def __str__(self):
            return f'{super().__str__()} They can\'t fly.'

if __name__ == "__main__":
    my_superhero = Not_flying_hero('Samantha Smell' ,'super sense of smell', 3, 2)

    my_superhero.perform_ability()
    print(my_superhero)
    print(repr(my_superhero))
