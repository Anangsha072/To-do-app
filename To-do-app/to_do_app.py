import argparse


# TASK OBJECT
class Task:
    # this creates task blueprint
    def __init__(self, name):

        self.name = name

        self.completed = False

        self.priority = "Normal"

    def __str__(self):

        return self.name
parser = argparse.ArgumentParser()
parser.add_argument("action")
parser.add_argument("task", nargs="?")
args = parser.parse_args()


TASK_FILE = "list.txt"

UNDO_FILE = "undo.txt"


# Create files automatically if not present
open(TASK_FILE, "a").close()

open(UNDO_FILE, "a").close()


# SAVE UNDO HISTORY
def save_undo(tasks):

    LIMIT = 5

    undo = open(UNDO_FILE, "r")

    history = undo.read().split("===\n")

    undo.close()

    # remove empty states
    history = [state for state in history if state.strip() != ""]

    # convert current tasks into string
    current_state = ""

    for task in tasks:

        current_state += task.name + "\n"

    # STACK PUSH
    history.append(current_state)

    # QUEUE REMOVE
    if len(history) > LIMIT:

        history.pop(0)

    # rewrite undo history
    undo = open(UNDO_FILE, "w")

    for state in history:

        undo.write(state)

        undo.write("===\n")

    undo.close()


def read_tasks():

    file = open(TASK_FILE, "r")

    lines = file.readlines()

    file.close()

    tasks = []

    for line in lines:

        parts = line.strip().split("|") # splitting the data into parts while reading
        # parts[0]=name, parts[1]=priority, parts[2]=completed
        if len(parts) == 1:

            task_obj = Task(parts[0])

        else:
            # object creation
            task_obj = Task(parts[0]) # task=Task(parts[0])

            task_obj.priority = parts[1]

            task_obj.completed = parts[2] == "True"

        tasks.append(task_obj)

    return tasks


def save_tasks(tasks):

    file = open(TASK_FILE, "w")

    for task in tasks:

        line = task.name + "|" + task.priority + "|" + str(task.completed)

        file.write(line + "\n") # if file.write(tasks.name,"w") only task name gets saved, not priority, completed, these features gets reset

    file.close()


# ADD TASK
if args.action == "add":

    tasks = read_tasks()

    save_undo(tasks)

    new_task = Task(args.task) # here object is created, add "study"-> Task("Study")
    tasks.append(new_task) # this stores object inside list
    save_tasks(tasks)

    print("Task added")


# VIEW TASKS
elif args.action == "view":

    tasks = read_tasks()

    if len(tasks) == 0:

        print("No tasks available")

    else:

        for i, task in enumerate(tasks, 1):

            print(i, task.name)

            print("Priority:", task.priority)

            print("Completed:", task.completed)

            print()


# DELETE TASK
elif args.action == "delete":

    tasks = read_tasks()

    save_undo(tasks)

    tasks.pop(int(args.task) - 1)

    save_tasks(tasks)

    print("Task deleted")


# PRIORITY TASK
elif args.action == "priority":

    tasks = read_tasks()

    save_undo(tasks)

    num = int(args.task) - 1

    important = tasks.pop(num)
    # reset all priorities
    for task in tasks:

        task.priority = "Normal"
    important.priority = "High" # makes selected task high priority
    # now modify

    tasks.insert(0, important)

    save_tasks(tasks)

    print("Priority updated")


# UPDATE TASK POSITION
elif args.action == "update":

    tasks = read_tasks()

    save_undo(tasks)

    old = int(input("Current position: ")) - 1

    new = int(input("New position: ")) - 1

    task = tasks.pop(old)

    tasks.insert(new, task)

    save_tasks(tasks)

    print("Position updated")


# COMPLETE TASK
elif args.action == "complete":

    tasks = read_tasks()

    save_undo(tasks)

    num = int(args.task) - 1
    completed_task=tasks.pop(num)
    completed_task.completed = True
    tasks.append(completed_task) # moves completed task to the end
    save_tasks(tasks)

    print("Task completed and moved to the end")


# UNDO
elif args.action == "undo":

    undo = open(UNDO_FILE, "r")

    history = undo.read().split("===\n")

    undo.close()

    # remove empty states
    history = [state for state in history if state.strip() != ""]

    if len(history) == 0:

        print("Nothing to undo")

    else:

        # STACK POP
        last_state = history.pop()

        file = open(TASK_FILE, "w")

        file.write(last_state)

        file.close()

        # rewrite remaining history
        undo = open(UNDO_FILE, "w")

        for state in history:

            undo.write(state)

            undo.write("===\n")

        undo.close()

        print("Undo completed")


else:

    print("Invalid action")




