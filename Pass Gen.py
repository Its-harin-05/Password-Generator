import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

def generate_password():
    entry.delete(0, END)
    length = var1.get()
    if var.get() == 1:
        chars = "abcdefghijklmnopqrstuvwxyz"
    elif var.get() == 2:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elif var.get() == 3:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    else:
        return
    password = ''.join(random.choice(chars) for _ in range(length))
    entry.insert(1,password)

def copy_to_clipboard():
    pyperclip.copy(entry.get())

root = Tk()
var, var1 = IntVar(), IntVar()
root.title("Password Generator")

Label(root, text="Password:").grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
Label(root, text="Length:").grid(row=1)

copy_button = Button(root, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=0, column=2)
copy_button1 = Button(root, text="Generate", command=generate_password)
copy_button1.grid(row=0, column=3)

Radiobutton(root, text="Low", variable=var, value=1).grid(row=1, column=2)
Radiobutton(root, text="Medium", variable=var, value=2).grid(row=1, column=3)
Radiobutton(root, text="Strong", variable=var, value=3).grid(row=1, column=4)

combo = Combobox(root, textvariable=var1, values=(8,14,16,20,24,26,30))
combo.current(0)
combo.grid(column=1, row=1)
root.configure(bg="lightgray")

root.mainloop()
