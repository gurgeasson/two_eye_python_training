'''
Log Detective
this script takes all text files from a directory and produces a report that summarises the 'critical' and 'error' entries from the files and saves the report in 'summary_report.txt'
'''

'''
read and process line by line
use loops
use functions: eg read_logs(), generate_report()
upload to Git
'''

'''
output template:
<no of lines> lines of <file name> scanned

--- report ---

<no of finds> critical entries found
<line/s>

<no of finds> errors found
<line/s>

report saved to <save name>

'''


import glob, os

keywords = ["error", "critical"]

def find_in_file(file_name, search_term):
    return_data = {"count": 0,
                    "lines": []}
    with open(file_name, "r") as file:
        for line in file:
            return_data["count"] += 1
            search_for_error = line.find(search_term)
            if search_for_error != -1:
                return_data["lines"].append("Line{}: {}".format(return_data["count"], line.strip()))
    return return_data

os.chdir("./01_Beginner/module_2/excercise")
for file in glob.glob("*.txt"):
    print(file)
    for keyword in keywords:
        for item in find_in_file(file, keyword)["lines"]:
            print(item)
