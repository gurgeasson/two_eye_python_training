'''
Instructions

    Define a function that has three input parameters, num1, num2, and num3.
    Test if num1 is greater than the other two numbers. If so, return num1.
    Test if num2 is greater than the other two numbers. If so, return num2.
    Test if num3 is greater than the other two numbers. If so, return num3.
    If there was a tie between the two largest numbers, then return "It's a tie!"
'''

def max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    if num2 > num1 and num2 > num3:
        return num2
    if num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"
    
    
if __name__ == "__main__":    
    print(max_number(-10, 0, 10))
    print(max_number(-10, 5, -30))
    print(max_number(-5, -10, -10))
    print(max_number(2, 3, 3))

