import tkinter as tk
from tkinter import messagebox

def add():
    task = entry.get()
    if task :
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)

    else:
        messagebox.showwarning("Warning !", "Please add task")

def delete():
    try:
        select_index = listbox.curselection()
        listbox.delete(select_index)

    except:
        messagebox.showwarning("Warning !", "Please select task")    

window = tk.Tk()
window.title("TO DO LIST")

entry = tk.Entry(window,width=30)
entry.pack()

Button_add = tk.Button(window,text="Add Task",command=add)
Button_add.pack()
Button_del = tk.Button(window,text="Delete Task",command=delete)
Button_del.pack()
listbox = tk.Listbox(window,selectmode=tk.SINGLE,width=40,height=10)
listbox.pack()


window.mainloop()
