'''
Instructions

    Create an empty dictionary called students.
    Define a function called add_student that takes two arguments: name & info. Using dictionary notation, assign name & info as the new key : value pair to the existing students dictionary and print a message to show student has been added.
    Create dictionaries for individual students containing "grade" and "DOB".
'''

student_dictionary = {}

alex = {'grade': 88, 'DOB': '10/10/1995'}
alice = {'grade': 100, 'DOB': '11/05/2003'}
james = {'grade': 47, 'DOB': '11/09/2013'}

def add_student(name, info):
    student_dictionary[name] = info
    print(f"Student added with key:value pair as {name} : {student_dictionary[name]}")



add_student("Alex", alex)
add_student("Alice", alice)
add_student("James", james)
