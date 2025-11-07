'''
You're task is to create a coffee machine by extending the base 
function(coffee machine) using decorators. A decorator is a way of 
extending a base function without modifying it.

To complete this exercise there are 4 sub tasks:

1) Create a basic function that prints out a string such as: "Here is your coffee".

2) Create a decorator by nesting a wrapper function within it.

3) Add the decorator to the base function.

4) Add arguments to your base function by utilising 'args & kwargs', 
then set up your wrapper function to accept arguments.
'''


def add_coffee(func):
    def wrapper(*args, **kwargs):
        if args[0] == 'tea':
            print('You add a tea bag')
        else:
            print('You add ground coffee')
        result = func(*args, **kwargs)
        return result
    return wrapper

def add_water(func):
    def wrapper(*args, **kwargs):
        print('You add water')
        result = func(*args, **kwargs)
        return result
    return wrapper

def add_milk(func):
    def wrapper(*args, **kwargs):
        print('You add milk')
        result = func(*args, **kwargs)
        return result
    return wrapper

def stir(func):
    def wrapper(*args, **kwargs):
        print('You stir it all')
        result = func(*args, **kwargs)
        return result
    return wrapper

@add_coffee
@add_water
@add_milk
@stir
def get_coffee_from_machine(drink):
    return f'Here is your {drink}, enjoy!'

print(get_coffee_from_machine('tea'))
print(get_coffee_from_machine('cappuccino'))

input("press 'enter' to continue...")
