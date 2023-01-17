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

    words = f.read().split()
    if words:
        word = words.pop(0)
        label.config(text=word)
        root.after(150, Take_input())
    else:
        print('All words typed')
        root.after_cancel(Take_input())




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
                 command=lambda: Take_input()
                 )

label = Label(root, text="")

root.after(150, speed_of_text)


label.pack()
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()

