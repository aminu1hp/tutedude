# tkinter load
from tkinter import *

# interface
interface = Tk()
interface.geometry("300x500")
interface.title("Calculator")
interface.config(bg="white")

# input
# entry
entry1 = Entry(interface, width=45, borderwidth=2)
entry1.place(x=12, y=5)

# messagebox
from tkinter import messagebox
def show_about():
    messagebox.showinfo("About", "This is a Calculator app.\nCreated with Tkinter.")

def confirm_exit():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        interface.quit()

# menu
menu = Menu(interface)
file_menu = Menu(menu, tearoff=0 )
file_menu.add_command(label="Exit", command=confirm_exit)
menu.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu.add_cascade(label="Help", menu=help_menu)
interface.config(menu=menu)

# stores entries
def click(num):
    current = entry1.get()
    entry1.delete(0,END)
    entry1.insert(0, current + str(num))

# button
button = Button(interface, text="1", width=11, command=lambda: click(1))
button.place(x=12, y=50)

button = Button(interface, text="2", width=11, command=lambda: click(2))
button.place(x=104, y=50)

button = Button(interface, text="3", width=11, command=lambda: click(3))
button.place(x=196, y=50)

button = Button(interface, text="4", width=11, command=lambda: click(4))
button.place(x=12, y=100)

button = Button(interface, text="5", width=11, command=lambda: click(5))
button.place(x=104, y=100)

button = Button(interface, text="6", width=11, command=lambda: click(6))
button.place(x=196, y=100)

button = Button(interface, text="7", width=11, command=lambda: click(7))
button.place(x=12, y=150)

button = Button(interface, text="8", width=11, command=lambda: click(8))
button.place(x=104, y=150)

button = Button(interface, text="9", width=11, command=lambda: click(9))
button.place(x=196, y=150)

button = Button(interface, text="0", width=11, command=lambda: click(0))
button.place(x=104, y=200)

def add():
    n1 = entry1.get()
    global math
    math = "ADDITION"
    global i
    i = int(n1)
    entry1.delete(0, END)

button = Button(interface, text="+", width=11, command=add)
button.place(x=12, y=200)

def sub():
    n1 = entry1.get()
    global math
    math = "SUBTRACTION"
    global i
    i = int(n1)
    entry1.delete(0, END)

button = Button(interface, text="-", width=11, command=sub)
button.place(x=196, y=200)

def mult():
    n1 = entry1.get()
    global math
    math = "MULTIPLICATION"
    global i
    i = int(n1)
    entry1.delete(0, END)

button = Button(interface, text="*", width=11, command=mult)
button.place(x=12, y=250)

def div():
    n1 = entry1.get()
    global math
    math = "DIVISION"
    global i
    i = int(n1)
    entry1.delete(0, END)

button = Button(interface, text="/", width=11, command=div)
button.place(x=104, y=250)

def equal():
    n2 = entry1.get()
    entry1.delete(0, END)
    if math == "ADDITION":
        entry1.insert(0, i + int(n2))
    elif math == "SUBTRACTION":
        entry1.insert(0, i - int(n2))
    elif math == "MULTIPLICATION":
        entry1.insert(0, i * int(n2))
    elif math == "DIVISION":
        if int(n2) == 0:
            messagebox.showerror("Error", "Infinite Loop..:)")
        else:
            entry1.insert(0, i / int(n2))

button = Button(interface, text="=", width=11, command=equal)
button.place(x=196, y=250)

def clear():
    entry1.delete(0, END)

button = Button(interface, text="Clear", width=11, command=clear)
button.place(x=12, y=300)

# mainloop
interface.mainloop()
