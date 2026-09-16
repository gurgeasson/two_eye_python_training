'''
Define a function called contains_true.
Accept a list of booleans called values.
Return True if at least one value is True.
Otherwise return False.
Fix 3 bugs.
Optional: Improve the code using simple best practices.
'''

def contains_true(values):
    for v in values:
        if v is True:       #use 'is True' to check identity rather than equality
            return True
    else:
        return False


if __name__ == "__main__":
    print(contains_true([2, False, True]))
    print(contains_true([9, False, 'False', 'True', 0, -1, 6.9]))

'''
bugs found:
def contains_true(values):
    for v in values:
        if v = True:            - '=' assigns value, '==' is a comparator
            return "True"       - returns the text True and not the boolean True
        else:                   - if the first value is not True, the next step is to return False without checking any of the other values
            return False
'''
