# Dillon J. Cooper
# Lab 10

# Chapter 16, Exercise 5: Write a GUI application that when a value is entered
# in the text field and the Convert button is clicked, the value should be
# converted from Fahrenheit to Celsius and displayed in the window.

import tkinter

window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

title = tkinter.Label(frame, text='Temperature in Fahrenheit')
title.pack()

tem = tkinter.IntVar()
a = tkinter.Entry(frame, textvar=tem)
a.pack()

c = tkinter.IntVar()
label = tkinter.Label(frame, textvar=c)
label.pack()

button = tkinter.Button(frame, text='Convert', command=lambda: convert(c, tem))
button.pack()

quit = tkinter.Button(frame, text='Quit', command=lambda: window.destroy())
quit.pack()


def convert(output, tem):
    """Converts user input in Fahrenheit to Celsius. Click quit to exit."""
    f = tem.get()
    output.set((f - 32) * 5 / 9)
    label.config(textvar=c)

window.mainloop()
