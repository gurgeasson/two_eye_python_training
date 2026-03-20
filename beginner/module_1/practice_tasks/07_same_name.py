'''
Instructions

    1) Define the function to accept two strings, your_name and my_name.
    2) Test if the two strings are equal.
    3) Return True if they are equal, otherwise return False.
'''

def same_name(name1, name2):
    if name1 == name2:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(same_name("Colby", "Colby"))
    print(same_name("Tina", "Amber"))
