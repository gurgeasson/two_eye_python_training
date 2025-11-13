'''
Instructions

    Define the function header to accept one input num.
    Calculate the remainder of the input divided by 10 (use modulus).
    Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False.
'''

def divisible_by_ten(num):
    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":    
    print(divisible_by_ten(20))
    print(divisible_by_ten(25))
