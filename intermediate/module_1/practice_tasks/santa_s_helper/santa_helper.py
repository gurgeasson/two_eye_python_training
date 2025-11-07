'''
Santa is running late this year in fulfilling his order of toys before Christmas arrives. 
You're task is to help Santa meet his quota of toy's by building some more using a generator function. To complete this exercise there are several sub tasks:

1) Create a basic function that accepts a single integer.
2) Add a generator by utilising the 'yield' key word.
3) Call your new generator function and utilise the 'next()' function to return the following yield value.

'''

def toy_constructor(toy_amount):
    for i in range(1, toy_amount + 1):
        print('Working on toy...')
        yield f'Toy #{i} is ready to be wrapped up and sent for delivery'

toy = toy_constructor(7)
print(next(toy))
print(next(toy))
print(next(toy))
print(next(toy))
print(next(toy))
print(next(toy))
print(next(toy))
# print(next(toy))
