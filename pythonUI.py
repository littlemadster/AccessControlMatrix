from tkinter import *
from tkinter import ttk

def close():
    window.destroy()

window = Tk()
window.title("Window")
window.geometry('500x500')

rule = "own"

Button(window, text = "Quit", command = close).grid(row = 5, column = 5)

Label(window, text="").grid(row=0,column=0)
Label(window, text="Sub1").grid(row=1,column=0)
Label(window, text="Obj1").grid(row=0,column=1)
Label(window, text=rule).grid(row=1,column=1)

rule = rule + ", control"
Label(window, text=rule).grid(row=1,column=1)


window.mainloop()
