import argparse
import os

FILE_NAME = "tasks.txt"
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [task.strip() for task in file.readlines()]
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

parser = argparse.ArgumentParser()
parser.add_argument(
    "action",
    choices=["add", "view", "delete"]
)
parser.add_argument(
    "task",
    nargs="?"
)
args = parser.parse_args()
tasks = load_tasks()
if args.action == "add":
    tasks.append(args.task)
    save_tasks(tasks)
    print("Task added")

elif args.action == "view":
    if (len(tasks) == 0):
        print("No tasks found")
    else:
        print("To-Do List:")

        for i, task in enumerate(tasks, 1):
            print(i,".",task)

elif args.action == "delete":
    num = int(args.task) - 1
    if 0 <= num < len(tasks):
        removed = tasks.pop(num)
        save_tasks(tasks)
        print("Deleted:", removed)
    else:
        print("Invalid task number")
    

