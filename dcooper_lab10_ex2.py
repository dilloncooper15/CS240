# Dillon J. Cooper
# Lab 10

# Chapter 16, Exercise 2: Write a GUI application with a single button.
# Initially the button is labeled 0, but each time it is clicked, the value
# on the button increases by 1.

import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

text = tkinter.IntVar()
text.set('0')

button = tkinter.Button(frame, textvariable=text,
                        command=lambda: increase(text))
button.pack()

quit = tkinter.Button(frame, text='Quit', command=lambda: window.destroy())
quit.pack()


def increase(text):
    """Starts at 0 and increases by one everytime the user clicks on the\
    number. Click quit to exit."""

    count = int(text.get())
    text.set(str(count + 1))

window.mainloop()
