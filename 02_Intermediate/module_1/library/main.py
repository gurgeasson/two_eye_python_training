import os

PROJECT_PATH = os.path.dirname(__file__)
DATA_FOLDER_NAME = 'data'
FILENAME = 'down_the_rabbit-hole.txt'

from data.chapters import chapters

for chapter_number, chapter in enumerate(chapters, start=1):
    print(f"{chapter_number}: {chapter}")

try:
    with open(os.path.join(PROJECT_PATH, DATA_FOLDER_NAME, FILENAME), "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print(f"{FILENAME} does not exist.")
except PermissionError:
    print(f"You don't have permission to access {FILENAME}.")
except OSError as e:
    print(f"OS error occurred: {e}")
except UnicodeDecodeError:
    print("Failed to decode the file with UTF-8 encoding.")
