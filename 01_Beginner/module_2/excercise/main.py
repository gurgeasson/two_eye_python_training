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

import glob, os

os.chdir("./01_Beginner/module_2/excercise")
for file in glob.glob("*.txt"):
    print(file)
    with open(file, "r") as file:
        count = 0
        for line in file:
            count += 1
            # print("Line{}: {}".format(count, line.strip()))
            search_for_error = line.find("error")
            if search_for_error != -1:
                print(count)
