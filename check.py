import tkinter as tk 
from tkinter import *

import math

win = tk.Tk()
win.title("Binary/Decimal Converter")
win.geometry("600x200")

state = IntVar()
state.set(0)
state2 = IntVar()
state2.set(0)
state3 = IntVar()
state3.set(0)
state4 = IntVar()
state4.set(0)
state5 = IntVar()
state5.set(0)
state6 = IntVar()
state6.set(0)
state7 = IntVar()
state7.set(0)
state8 = IntVar()
state8.set(0)

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    bi=binary
    a=int(bi[0])*128
    b=int(bi[1])*64
    c=int(bi[2])*32
    d=int(bi[3])*16
    e=int(bi[4])*8
    f=int(bi[5])*4
    g=int(bi[6])*2
    h=int(bi[7])*1

    decimal=a+b+c+d+e+f+g+h

    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    decimal=int(decimal)
   
    dc=decimal
    a1=dc%2
    a2=int((dc/2)%2)
    a3=int((dc/4)%2)
    a4=int((dc/8)%2)
    a5=int((dc/16)%2)
    a6=int((dc/32)%2)
    a7=int((dc/64)%2)
    a8=int((dc/128)%2)

    if a1 == 1:
        state8.set(1)
    else:
        state8.set(0)
    if a2 == 1:
        state7.set(1)
    else:
        state7.set(0)
    if a3 == 1:
        state6.set(1)
    else:
        state6.set(0)
    if a4 == 1:
        state5.set(1)
    else:
        state5.set(0)
    if a5 == 1:
        state4.set(1)
    else:
        state4.set(0)
    if a6 == 1:
        state3.set(1)
    else:
        state3.set(0)
    if a7 == 1:
        state2.set(1)
    else:
        state2.set(0)
    if a8 == 1:
        state.set(1)
    else:
        state.set(0)

    binary=[a8,a7,a6,a5,a4,a3,a2,a1]

    return binary

def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = e1.get()
    binary = decimal_to_binary(decimal)

def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    a=state.get()
    b=state2.get()
    c=state3.get()
    d=state4.get()
    e=state5.get()
    f=state6.get()
    g=state7.get()
    h=state8.get()

    binary.append(a)
    binary.append(b)
    binary.append(c)
    binary.append(d)
    binary.append(e)
    binary.append(f)
    binary.append(g)
    binary.append(h)

    decimal = binary_to_decimal(binary)
    e1.delete(0,END)
    e1.insert(0,decimal)

e1=tk.Entry(win,width=60)

b1 = tk.Button(win, text="Convert to Binary", command=get_binary)
b2 = tk.Button(win, text="Convert to Decimal", command=get_decimal)

cb1 = Checkbutton(win, variable = state)
cb2 = Checkbutton(win, variable = state2)
cb3 = Checkbutton(win, variable = state3)
cb4 = Checkbutton(win, variable = state4)
cb5 = Checkbutton(win, variable = state5)
cb6 = Checkbutton(win, variable = state6)
cb7 = Checkbutton(win, variable = state7)
cb8 = Checkbutton(win, variable = state8)

cb1.grid(row=1,column=1)
cb2.grid(row=1,column=2)
cb3.grid(row=1,column=3)
cb4.grid(row=1,column=4)
cb5.grid(row=1,column=5)
cb6.grid(row=1,column=6)
cb7.grid(row=1,column=7)
cb8.grid(row=1,column=8)

e1.grid(row=3,column=1,columnspan=8)
b1.grid(row=4,column=1)
b2.grid(row=4,column=2)


win.mainloop()