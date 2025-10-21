'''
Instructions

    Define our function with two inputs num1 and num2.
    Multiply the second input by 2.
    Use an if statement to compare the result of the last calculation with the first input.
    If num1 is greater, then return True. Otherwise, return False.
'''

def twice_as_large(num1, num2):
    num2_doubled = num2 * 2
    if num1 > num2_doubled:
        return True
    else:
        return False
    
print(twice_as_large(11, 5))
print(twice_as_large(10, 5))
