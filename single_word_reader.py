from tkinter import *
import os
from time import sleep
root = Tk()
root.title("Show")


def take_input():
    input_txt = inputtxt.get("1.0", "end-1c")
    print(input_txt)
    if os.path.isfile(str(input_txt)) and input_txt.endswith('.txt'):
        f = open(input_txt, 'r')
        Output.insert(END, f.read())
    else:
        Output.insert(END, "Wrong directory")


def speed_of_words():
    words = Output.get("1.0", "end-1c").replace('/n', ' ').split(' ')
    while words:
        word = words.pop(0)
        label_txt.set(word)
        root.update_idletasks()
        label.config(text=word)
        sleep(0.3)
        print(word)
    print('All words typed')


h = Scrollbar(root, orient='horizontal')
h.pack(
    side=BOTTOM,
    fill=X,
)
v = Scrollbar(root)
v.pack(side=RIGHT, fill=Y)


lab = Label(text="set the directory for the text file")
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
                 command=lambda: take_input())

label_txt = StringVar()

label = Label(root,
              height=4,
              width=20,
              textvariable=label_txt,
              font=('Helvetica bold', 26),
              bg="pink"
              )

Start = Button(root, height=2,
               width=20,
               text='Start',
               command=lambda: speed_of_words(),
               )


lab.pack()
inputtxt.pack()
Display.pack()
Output.pack()
label.pack()
Start.pack()
mainloop()
