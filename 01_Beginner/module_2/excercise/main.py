'''
Log Detective
this script takes all text files from a directory and produces a report that summarises the 'critical' and 'error' entries from the files and saves the report in 'summary_report.txt'
'''

import glob
import os

PROJECT_PATH = os.path.dirname(__file__)
REPORT_FILE_PATH = os.path.join(PROJECT_PATH, "./report/report.txt")

KEYWORDS = ["error", "critical"]

def create_new_file(file_name):
    try:
        with open(file_name, "x", encoding="utf-8") as file:
            pass
    except PermissionError:
        print(f"No permission to write file: {file_name}")
    except FileExistsError:
        print(f"File already exist: {file_name}")
    except OSError as e:
            print(f"OS error occured while saving file {file_name}: {e}")

def process_log_file(file_name):
    print(f"Start processing file: {file_name}")
    results = {"file_name": file_name,
               "line_count": 0,
               "keywords": {}}
    for keyword in KEYWORDS:
        results["keywords"][keyword] = {}
        results["keywords"][keyword]["entry_count"] = 0
        results["keywords"][keyword]["entries"] = []

    try:
        with open(file_name, "rb") as file:
            results["line_count"] = sum(1 for line in file)
    except FileNotFoundError:
        print(f"{file_name} does not exist at run location.")
    except PermissionError:
        print(f"You don't have permission to access {file_name}.")
    except OSError as e:
        print(f"OS error occured: {e}")

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                for keyword in KEYWORDS:
                    if line.lower().find(keyword) != -1:
                        results["keywords"][keyword]["entries"].append(line)
                        results["keywords"][keyword]["entry_count"] += 1
    except FileNotFoundError:
        print(f"{file_name} does not exist at run location.")
    except PermissionError:
        print(f"You don't have permission to access {file_name}.")
    except OSError as e:
        print(f"OS error occured: {e}")
    except UnicodeDecodeError:
        print("Failed to decode the file with UTF-8 encoding.")

    return results

def generate_report(results):
    '''
    generate_report will take a very specific input and will save append it's content to a text file in a human readable format.
    the input file structure is:
    results = {"file_name": <file_name (string)>,
            "line_count": <number of lines in file (int)>,
            "keywords": {<keyword_1 (string)>: {"entry_count": <number of entries with <keyword_1> (int)>,
                                                "entries": [<line_1 (string)>, <line_2 (string)>, ...]},
                        <keyword_2 (string)>: {...} ...}}
    '''
    try:
        with open(REPORT_FILE_PATH, "a", encoding="utf-8") as report_file:
            report_file.writelines(f"\n{results["line_count"]} lines of {results["file_name"]} scanned\n--- report ---\n")
            for keyword in results["keywords"]:
                report_file.writelines(f"{results["keywords"][keyword]["entry_count"]} {keyword} entries found\n")
                for entry in results["keywords"][keyword]["entries"]:
                    report_file.writelines(entry)
    except FileNotFoundError:
        print(f"{REPORT_FILE_PATH} does not exist at run location.")
    except PermissionError:
        print(f"You don't have permission to access {REPORT_FILE_PATH}.")
    except OSError as e:
        print(f"OS error occured while saving file {REPORT_FILE_PATH}: {e}")
    except UnicodeDecodeError:
        print("Failed to decode the file with UTF-8 encoding.")
    else:
        print(f"File {results["file_name"]} successfully processed and results saved to {REPORT_FILE_PATH}")

os.chdir("./01_Beginner/module_2/excercise")
create_new_file(REPORT_FILE_PATH)
for file in glob.glob("*.txt"):
    generate_report(process_log_file(file))
