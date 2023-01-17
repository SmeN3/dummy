from tkinter import *
import os
root = Tk()

root.title("Show")


def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    if os.path.isfile(str(INPUT)) and INPUT.endswith('.txt'):
        f = open(INPUT, 'r')
        answer = f.read().split()
        Output.insert(END, f.read())
    else:
        Output.insert(END, "Wrong directory")
    return answer


def speed_of_text(words):

    if words:
        word = list(words).pop(0)
        label.config(text=word)
        root.after(150, speed_of_text(words))
    else:
        print('All words typed')
        root.after_cancel(speed_of_text)

h = Scrollbar(root, orient='horizontal')
h.pack(
    side=BOTTOM,
    fill=X,
)
v = Scrollbar(root)
v.pack(side=RIGHT, fill=Y)


l = Label(text="set the directory for the text file")
inputtxt = Text(root, height=1,
                width=200,
                bg="light yellow")

Output = Text(root, height=40,
              width=200,
              bg="light cyan",
              xscrollcommand=h.set,
              yscrollcommand=v.set)

Display = Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: Take_input())

label = Label(root, text="", height=10, width= 10,
              font=('Helvetica bold', 26))

Start = Button(root, height=2,
               width=20,
               text='Start',
               command=lambda: speed_of_text(Take_input),

               )


l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
Start.pack()
label.pack()
mainloop()