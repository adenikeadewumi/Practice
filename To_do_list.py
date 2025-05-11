#This is a simple To-do list app program using tkinter

#Importations
import json
import os
import tkinter as tk
from tkinter import messagebox


#Create file to save tasks made
my_file= "tasks.json"



#Define functions for basic operations like add task, delete task, mark task as done and so on
def load_tasks():
    #Check if file exists and load content
    if os.path.exists(my_file):
        with open(my_file, "r") as f:
            return json.load(f)
    # Return empty list if file doesn't exist
    return []

def save_tasks():
    with open(my_file, "w") as f:
        json.dump(tasks, f, indent=4)

# Function to update status of visual of list of tasks
def refresh_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status= "[✔]" if task["done"] else "[]"
        listbox.insert(tk.END, status + " "+ task["task_name"])

#Function to add tasks        
def add_task():
    task_name= entry.get()
    if task_name:
        tasks.append({"task_name": task_name, "done": False})
        entry.delete(0, tk.END)
        #refresh the listbox to show addition
        refresh_listbox()
        #save the new tasks added
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task can't be empty!! \n Add task to continue")


#Function to mark task as done
def mark_done():
    selected= listbox.curselection() #To keep track of selected task in the list box
    if selected:
        #Get index of seleted
        idx= selected[0]
        tasks[idx]["done"]= True # Update status
        #Update visuals as well
        refresh_listbox()
        #save changes mad
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task in order to mark it as done!!")

#Funtion to delete a task
def delete_task():
    selected= listbox.curselection()
    if selected:
        idx= selected[0]
        del tasks[idx]#Delete task from json file
        #Visualize changes
        refresh_listbox()
        #save changes
        save_tasks()






#Create tkinter instance
root= tk.Tk()

#Give it a name
root.title("To-do List")
root.configure(bg="#1e1e1e")  # match background of window
label = tk.Label(root, text="My To-Do List", bg="#1e1e1e", fg="white")


tasks= load_tasks()

#Create a box to visualize the tasks added
listbox= tk.Listbox(root, width= 50,
    height= 20,
    bg="#1e1e1e",# background color
    fg="white", # text color
    selectbackground="#3e8ef7",
    selectforeground="white",
    font=("Segoe UI", 12))
listbox.pack()

#Create box to type in new tasks
entry= tk.Entry(root, width=25)
entry.pack()


#Create buttons for each task
#for adding new tasks
add_button= tk.Button(root, text= "Add Task", bg= "green", fg= "white", command= add_task)
add_button.pack(pady= 10)

#Create markdone button
mark_done_button= tk.Button(root, text="Mark as Done", bg= "skyblue", fg= "black", command= mark_done)
mark_done_button.pack(pady= 5)

#Create delete task button
delete_button= tk.Button(root, text= "Delete Task", bg= "red", fg= "white", command= delete_task)
delete_button.pack(pady= 10)

refresh_listbox()

root.mainloop()

