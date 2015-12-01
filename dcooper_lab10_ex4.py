# Dillon J. Cooper
# Lab 10

# Chapter 16, Exercise 4: A DNA sequence is a sting made up of As, Ts, Cs, and
# Gs. Write a GUI application in which a DNA sequence is entered, and when the
# Count button is clicked, the number of As, Ts, Cs, and Gs are counted and
# displayed in the window.

import tkinter
window = tkinter.Tk()
i = tkinter.Text(window, height=10, width=40)
i.pack()

frame = tkinter.Frame(window)
frame.pack()

sequence = tkinter.IntVar()

button = tkinter.Button(window, text='Count', command=lambda: count(i,
                        sequence))
button.pack()

label = tkinter.Label(window, textvar=sequence)
label.pack()

quit = tkinter.Button(frame, text='Quit', command=lambda: window.destroy())
quit.pack()


def count(i, sequence):
    """Counts the total number of occurences of A, T, C and G. Click quit to\
    exit."""
    data = i.get('0.0', tkinter.END)
    a = {}
    for char in 'ATCG':
        a[char] = data.count(char)
    sequence.set('Number of As: {0}, Number of Ts: {1}, Number of Cs: {2}, \
Number of Gs: {3}'.format(a['A'], a['T'], a['C'], a['G']))

window.mainloop()
