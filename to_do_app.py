import argparse
parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("task", nargs="?")
args = parser.parse_args()
if args.action == "add":
   file = open("tasks1.txt", "a")
   file.write(args.task + "\n")
   file.close()
   print("Task added")

elif args.action == "view":
    file = open("tasks1.txt", "r")
    print(file.read())
    file.close()

elif args.action == "delete":
    file = open("tasks1.txt", "r")
    tasks = file.readlines()
    file.close()
    tasks.pop(int(args.task) - 1)
    file = open("tasks1.txt", "w")
    file.writelines(tasks)
    file.close()
    print("Task deleted")
    

