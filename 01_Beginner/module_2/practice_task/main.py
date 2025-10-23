'''
Mood Diary
this script asks some questions about your mood, 
than saves the answers and some other info as a new text file.
Name of new file is today's date. New file is based on 'diaryTemplate' text file.
'''

name = input("Hello there! What's your name? Type it here: ")
mood = input(f"Good on ya {name}. How are you felling? Type it here: ")
try:
    # TODO: fix location
    with open("01_Beginner/module_2/practice_task/diaryTemplate.txt", "r") as template:
        template_contents = template.read()
        print(template_contents)
        template_contents = template_contents.replace("YOURNAME", name)
        template_contents = template_contents.replace("YOURMOODHERE", mood)
        print(template_contents)
except FileNotFoundError:
    print("diaryTemplate.txt does not exist at run location")
