'''
Instructions

    Create an empty dictionary called students.
    Define a function called add_student that takes two arguments: name & info. Using dictionary notation, assign name & info as the new key : value pair to the existing students dictionary and print a message to show student has been added.
    Create dictionaries for individual students containing "grade" and "DOB".
'''

'''
pimp my script: to practice OOP I added classes
'''

class Student:
    def __init__(self, first_name, dob):
        self.first_name = first_name
        self.date_of_birth = dob

    def __str__(self):
        return f"first name: {self.first_name}, DOB: {self.date_of_birth}"

class Exam:
    student_dictionary = {}

    def __str__(self):
        string = "no names in results"
        if len(self.student_dictionary) > 0:
            string = ""
            for i in self.student_dictionary:
                string += (f"student first_name: {i}, student data: {self.student_dictionary[i]}\n")
        return string

    def add_student(self, student, grade):
        self.student_dictionary[student.first_name] = {"grade": grade, "DOB": student.date_of_birth}
        print(f"Student added with key:value pair as {student.first_name} : {self.student_dictionary[student.first_name]}")

if __name__ == "__main__":
    alex = Student("Alex", "10/10/1995")
    alex_grade = 88
    alice = Student("Alice", "11/05/2003")
    alice_grade = 100
    james = Student("James", "11/09/2013")
    james_grade = 47

    end_of_year_exam_2026 = Exam()
    
    print(end_of_year_exam_2026)

    print("adding students to Exam instance:")
    end_of_year_exam_2026.add_student(alex, alex_grade)
    end_of_year_exam_2026.add_student(alice, alice_grade)
    end_of_year_exam_2026.add_student(james, james_grade)

    print("print 'student_dictionary' of my class instance:")
    print(end_of_year_exam_2026)

