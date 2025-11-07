import os
import subprocess

PROJECTS = {"1": ["Weather Report", "intermediate/module_1/excercise/global_weather_tracker/main.py"],
            "2": ["Coffee Machine", "intermediate/module_1/practice_tasks/coffee_machine/coffee_machine.py"],
            "3": ["Log Detective", "beginner/module_2/log_detective/log_detective.py"]
            }

def run_project(choice):
    project_path = PROJECTS[choice][1]
    print(f"Running Project {PROJECTS[choice][0]}...\n")
    subprocess.run(["python", project_path], check=False)
    print(f"Project {PROJECTS[choice][0]} finished.\n")

def main():
    user_prompt = ""
    for i in PROJECTS:
        user_prompt += f"   {i}) {PROJECTS[i][0]}\n"
    user_prompt += "   Type 1, 2 or 3: "

    while True:
        print("\n\n\n***   Super Spy Toolkit   ***")
        print("menu:")
        user_input = input(user_prompt)
        if user_input == "Q":
            print("Goodbye!")
            break
        elif user_input in PROJECTS:
            run_project(user_input)
        else:
            print("Invalid choice.\n")

        
if __name__ == "__main__":
    main()
