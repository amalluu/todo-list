import json
import os
from datetime import datetime

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json","r") as f:
            return json.load(f)
    return []
def save_tasks(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=2)




def main():
    tasks = load_tasks()
    while True:
        print("==To do list==")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete a Task")
        print("4. Mark Task as Completed")
        print("5. EXIT")
        choice = input("Enter your choice:")

        if choice=="1":
            taskno=int(input("How many tasks you want to add:"))
            for t in range(taskno):
                task = input(" enter task:")
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tasks.append({"task": task, "done": False,"created_at": current_time})
            save_tasks(tasks)
            print("task(s) added!")
        elif choice == "2":
            if not tasks:
                print("no tasks in here")
            else:
                print("\nTasks:")
                for i, task in enumerate (tasks,start= 1):
                    print(i, task['task'], "-", "✅" if task['done'] else "❌", "Added date and time:", task['created_at'])

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
            else:
                try:
                    index = int(input("Which task to delete, Give the number: ")) - 1
                    if 0 <= index < len(tasks):
                        left = tasks.pop(index)
                        print(f"Deleted: {left['task']}")
                        save_tasks(tasks)
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            if not tasks:
                print("No tasks to mark.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, start=1):
                    print(i, task['task'], "-", "✅" if task['done'] else "❌")
                try:
                    index = int(input("Enter the number of the task to mark as completed: ")) - 1
                    if 0 <= index < len(tasks):
                        tasks[index]['done'] = True
                        save_tasks(tasks)
                        print(f"Marked '{tasks[index]['task']}' as completed ✅")
                    else:
                        print ("Invalid task number.")
                except ValueError:
                        print(f"Please enter a valid number.")

        elif choice =="5":
            print("exiting..")
            break   
        else:
            print("choice is invalid")   
main()