'''
Instructions

    Define the function to accept two strings, your_name and my_name.
    Test if the two strings are equal.
    Return True if they are equal, otherwise return False.
'''

def same_name(name1, name2):
    if name1 == name2:
        return True
    else:
        return False

print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))
