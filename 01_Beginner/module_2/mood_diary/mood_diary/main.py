'''
Mood Diary
this script asks some questions about your mood, 
than saves the answers and some other info as a new text file.
Name of new file is today's date. New file is based on 'diaryTemplate' text file.
'''

import datetime
import os
import sys

PROJECT_PATH = os.path.dirname(__file__)
DIARY_TEMPLATE_FILE_PATH = os.path.join(PROJECT_PATH, "diaryTemplate.txt")
date_and_time = datetime.datetime.now()
NEW_FILE_NAME = f"{date_and_time.year}-{date_and_time.month}-{date_and_time.day}.txt"
NEW_FILE_PATH = os.path.join(PROJECT_PATH, NEW_FILE_NAME)

new_file_contents = ""

name = input("Hello there! What's your name? Type it here: ")
mood = input(f"Good on ya {name}. How are you felling? Type it here: ")

try:
    with open(DIARY_TEMPLATE_FILE_PATH, "r", encoding="utf-8") as template:
        template_contents = template.read()
        new_file_contents = template_contents.replace("YOURNAME", name)
        new_file_contents = new_file_contents.replace("YOURMOODHERE", mood)
except FileNotFoundError:
    print(f"diaryTemplate.txt does not exist at {DIARY_TEMPLATE_FILE_PATH}")
    sys.exit(1)

try:
    with open(NEW_FILE_PATH, "x", encoding="utf-8") as new_entry_file:
        new_entry_file.write(new_file_contents)
except FileExistsError:
    print(f"{NEW_FILE_NAME} already exist, you already made a diary entry today.")
    sys.exit(1)
except  PermissionError:
    print(f"You don't have permission to create {NEW_FILE_PATH}.")
    sys.exit(1)
except OSError as e:
    print(f"OS error occured: {e}")
    sys.exit(1)

try:
    with open(NEW_FILE_PATH, "r", encoding="utf-8") as recent_file:
        print(recent_file.read())
except FileNotFoundError:
    print(f"the new file with file name {NEW_FILE_NAME} does not exist at {PROJECT_PATH}")
except PermissionError:
    print(f"You don't have permission to access {NEW_FILE_NAME}.")
except OSError as e:
    print(f"OS error occured: {e}")
except UnicodeDecodeError:
    print("Failed to decode the file with UTF-8 encoding.")