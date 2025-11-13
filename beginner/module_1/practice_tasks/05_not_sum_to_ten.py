'''
Instructions

    Define the function to accept two parameters, num1 and num2.
    Add the two parameters together.
    Test if the result is not equal to 10.
    If the sum is not equal, return True, otherwise, return False.
'''

def not_sum_to_ten(num1, num2):
    sum = num1 + num2
    if sum != 10:
        return True
    else:
        return False
    
if __name__ == "__main__":    
    print(not_sum_to_ten(9, -1))
    print(not_sum_to_ten(9, 1))
    print(not_sum_to_ten(5, 5))
