# Dillon J. Cooper
# Lab 10

# Chapter 16, Exercise 2: Write a GUI application with a single button.
# Initially the button is labeled 0, but each time it is clicked, the value
# on the button increases by 1.

import tkinter


def increment(text):
    count = int(text.get())
    text.set(str(count + 1))

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

text = tkinter.StringVar()
text.set('0')

button = tkinter.Button(frame, textvariable=text,
                        command=lambda: increment(text))
button.pack()

window.mainloop()
