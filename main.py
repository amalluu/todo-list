import json
import os

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
        print("4. EXIT")
        choice = input("enter your choice:")

        if choice=="1":
            taskno=int(input("How many tasks you want to add:"))
            for task in range(taskno):
                task = input(" enter task:")
                tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print("task/s added!")
        elif choice == "2":
            if not tasks:
                print("no tasks in here")
            else:
                print("\nTasks:")
                for i, task in enumerate (tasks,start= 1):
                    print(i, task["task"]["done"])

        elif choice == "3":
            index =int(input("which task to delete:")) - 1
            left = tasks.pop(index)
            print(f"after deletion:{left}")
            save_tasks(tasks)
        elif choice =="4":
            print("exiting..")
            break   
        else:
            print("choice is invalid")   
main()