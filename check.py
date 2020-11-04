#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""

"""
import tkinter as tk 
from tkinter import *

import math

win = tk.Tk()
win.title("Binary/Decimal Converter")
win.geometry("600x200")



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
    binary=[a8,a7,a6,a5,a4,a3,a2,a1]

    return binary

def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = e1.get()
    binary = decimal_to_binary(decimal)
    e1.delete(0,END)
    e1.insert(0,binary)

def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    binary = e1.get()
    decimal = binary_to_decimal(binary)
    e1.delete(0,END)
    e1.insert(0,decimal)


e1=tk.Entry(win,width=40)

b1 = tk.Button(win, text="Convert to Binary", command=get_binary)
b2 = tk.Button(win, text="Convert to Decimal", command=get_decimal)

'''
cb1 = Checkbutton(win, variable = state, command=updateCheck)
cb2 = Checkbutton(win, variable = state, command=updateCheck)
cb3 = Checkbutton(win, variable = state, command=updateCheck)
cb4 = Checkbutton(win, variable = state, command=updateCheck)
cb5 = Checkbutton(win, variable = state, command=updateCheck)
cb6 = Checkbutton(win, variable = state, command=updateCheck)
cb7 = Checkbutton(win, variable = state, command=updateCheck)
cb8 = Checkbutton(win, variable = state, command=updateCheck)
'''

e1.grid(row=1,column=1)
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)


win.mainloop()
"""