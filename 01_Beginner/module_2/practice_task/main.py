'''
Mood Diary
this script asks some questions about your mood, 
than saves the answers and some other info as a new text file.
Name of new file is today's date. New file is based on 'diaryTemplate' text file.
'''

import datetime

date_and_time = datetime.datetime.now()
new_file_name = f"{date_and_time.year}-{date_and_time.month}-{date_and_time.day}.txt"

new_file_contents = ""

name = input("Hello there! What's your name? Type it here: ")
mood = input(f"Good on ya {name}. How are you felling? Type it here: ")

try:
    # TODO: fix location
    with open("01_Beginner/module_2/practice_task/diaryTemplate.txt", "r") as template:
        template_contents = template.read()
        new_file_contents = template_contents.replace("YOURNAME", name)
        new_file_contents = new_file_contents.replace("YOURMOODHERE", mood)
except FileNotFoundError:
    print("diaryTemplate.txt does not exist at run location")

try:
    with open(f"01_Beginner/module_2/practice_task/{new_file_name}", "w") as new_entry_file:
        new_entry_file.write(new_file_contents)
except:
    print("something went wrong")

try:
    with open(f"01_Beginner/module_2/practice_task/{new_file_name}", "r") as recent_file:
        print(recent_file.read())
except:
    print("something went wrong")