'''
Instructions

    Define the function to accept five parameters starting with budget then food_bill, electricity_bill, internet_bill and rent.
    Calculate the sum of the last four parameters.
    Use if and else statements to test if the budget is less than the sum of the calculated sum from the previous step.
    If the condition is true, return True, otherwise return False.
'''

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    expenses = food_bill + electricity_bill + internet_bill + rent
    if budget < expenses:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(over_budget(80, 20, 30, 10, 30))
    print(over_budget(100, 20, 30, 10, 40))
