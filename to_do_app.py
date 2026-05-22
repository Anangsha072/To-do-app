import argparse
parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("task", nargs="?")
args = parser.parse_args()
if args.action == "add":
    file = open("list.txt", "a")
    file.write(args.task + "\n")
    file.close()
    print("Task added")
elif args.action == "view":
    file = open("list.txt", "r")
    print(file.read())
    file.close()
elif args.action == "delete":
    file = open("list.txt", "r")
    tasks = file.readlines()
    file.close()
    tasks.pop(int(args.task) - 1)
    file = open("list.txt", "w")
    file.writelines(tasks)
    file.close()
    print("Task deleted")
elif args.action == "priority":
    file = open("list.txt", "r")
    tasks = file.readlines()
    file.close()
    num = int(args.task) - 1 # as python starts from 0 but user sees it from 1 so (-1)
    important = tasks.pop(num)
    tasks.insert(0, important)
    file = open("list.txt", "w")
    file.writelines(tasks)
    file.close()
    print("Priority to do that task is updated")
elif args.action=="update":
    file=open("list.txt","r")
    tasks=file.readlines()
    file.close()
    old=int(input("current position: "))-1
    new=int(input("new position: "))-1
    task=tasks.pop(old)
    tasks.insert(new,task)
    file=open("list.txt","w")
    file.writelines(tasks)
    file.close()
    print("Position updated")
    

