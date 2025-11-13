'''
Instructions

    Define the function to accept three numbers as parameters.
    Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound.
    If this is true, return True, otherwise, return False.
'''

def in_range(num, lower_bound, upper_bound):
    if (num >= lower_bound and num <= upper_bound):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(in_range(10, 10, 10)) # Expected outcome: True
    print(in_range(5, 10, 20))  # Expected outcome: False
