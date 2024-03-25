import tkinter as tk
from tkinter import messagebox 


def add_task():
    task = E1.get()
    t1=E2.get()
    t2=task,t1
    if  task:
        listbox.insert(tk.END,task)
        listbox2.insert(tk.END,t1)
        E1.delete(0, tk.END)
        E2.delete(0,tk.END)
            
    else:
        messagebox.showwarning("Warning","please enter Name ! .") 

def delete_task():
    try:
        selected_index = listbox.curselection()
        listbox.delete(selected_index)
        listbox2.curselection()
        listbox2.delete(selected_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create a main window
window = tk.Tk()
window.title("TO-DO LIST Application")
window.geometry("800x600")


l1 = tk.Label(window, text= "Student Name :")
l1.place(x=20,y=20)
E1 = tk.Entry(window)
E1.place(x=150,y=20)

l2 = tk.Label(window, text= "Mark :")
l2.place(x=450,y=20)
E2 = tk.Entry(window)
E2.place(x=500,y=20)




add_button = tk.Button(window, text="Add Task", command= add_task)
add_button.place(x=300,y=100)

add_button = tk.Button(window, text="Add Task", command= add_task)
add_button.place(x=300,y=100)

delete_button = tk.Button(window, text= "delete Task", command= delete_task)
delete_button.place(x=250,y=550)

l2 = tk.Label(window, text= "Student Name :")
l2.place(x=100,y=130)
l2 = tk.Label(window, text= "Mark :")
l2.place(x=420,y=130)

listbox = tk.Listbox(window, selectmode=tk.SINGLE, height=20, width=30)
listbox.place(x=100, y=150)

listbox2 = tk.Listbox(window, selectmode=tk.SINGLE, height=20, width=30)
listbox2.place(x=400, y=150)

# Start the main event loop
window.mainloop()
