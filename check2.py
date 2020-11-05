import tkinter as tk 
from tkinter import *

win = tk.Tk()

# A variable to track the state of the checkbutton
# Note that it uses an IntVar() here instead of StringVar() as we are going to
# use 1 as checked and 0 as unchecked.  We then set the value of the variable
# to be 1 so that the checkbox will start Checked
state = IntVar()
state.set(0)
state2 = IntVar()
state2.set(0)

def updateCheck():
    # Function bound to the checkbutton being clicked
    # updates the value of the Entry widget with the current value
    # of the checkbox variable state
    e1.delete(0,END)
    d=state.get()
    a=state2.get()
    b=d*4
    c=a*3
    s=c+b

    e1.insert(0,s)


# Creates a Checkbutton in the "win" window.  There is text as well as a variable
# that will match the current variable state as well as a command to be run every
# time that the checkbutton is clicked
cb = Checkbutton(win, text="This is a checkbutton", variable = state, command=updateCheck)
cb2 = Checkbutton(win, text="2", variable = state2, command=updateCheck)

# creates an entry widget and then sets the initial value
e1 = Entry(win)
d=state.get()
a=state2.get()
b=d*4
c=a*3
s=c+b

e1.insert(0,s)

cb.pack()
cb2.pack()
e1.pack()

win.mainloop()