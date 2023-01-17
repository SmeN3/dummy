from tkinter import *
import os
root = Tk()

root.title("Show")


def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if os.path.isfile(str(INPUT)) and INPUT.endswith('.txt'):
        f = open(INPUT, 'r')
        Output.insert(END, f.read())
    else:
        Output.insert(END, "Wrong directory")


l = Label(text="set the directory for the text file")
inputtxt = Text(root, height=1,
                width=200,
                bg="light yellow")

Output = Text(root, height=40,
              width=200,
              bg="light cyan")

Display = Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: Take_input())

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()