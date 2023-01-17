import tkinter as tk
from tkinter import *
root = Tk()

# specify size of window.
root.geometry("250x170")

# Create text widget and specify size.
T = Text(root, height=5, width=52)

# Create label

directory = """set directory"""

# Create button for next text.
b1 = Button(root, text="Import", )

# Create an Exit button.
b2 = Button(root, text="Exit",
            command=root.destroy)


T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(tk.END,directory)

tk.mainloop()