import tkinter as tk
tasks =[]

root= tk.Tk() # mainwindow created
root.title("MY FIRST To-Do APP")
root.geometry("400x300")

task_entry =tk.Entry(root)#text input inside the main window
task_entry.pack()

task_display =tk.Listbox(root)#to display tasks from the list tasks
task_display.pack(fill=tk.BOTH , expand= True)# "Fill" the space in both directions: horizontally (X) and vertically (Y) and also let it 'expand' if the window grows.

def add_tasks():
    input=task_entry.get()# we get the input text
    if input.strip() !="":#Is the input not empty after removing spaces? .strip() removes any leading or trailing whitespace
        tasks.append({"task": input, "done":False})# made a dictionary
        task_display.insert(tk.END,input)#task_display is the area that visually shows the tasks-->insert(tk.END, input) means: “Add this item at the end of the Listbox.”-->tk.END refers to the bottom of the list.
        task_entry.delete(0,tk.END)#clear the text box


add_button=tk.Button(root, text= "Add task",command= add_tasks)#button inside the main window- When the button is clicked, call the function add_tasks
add_button.pack()



root.mainloop() #Start the GUI event loop
