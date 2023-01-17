import tkinter as tk


text = 'Hello world my name is Paul'
words = text.split(' ')
def speed_of_text():
    global words
    if words:
        word = words.pop(0)
        label.config(text=word)
        root.after(150, speed_of_text)
    else:
        print('All words typed')
        root.after_cancel(speed_of_text)

root = tk.Tk()
label = tk.Label(root, text="")
label.pack()
root.after(150, speed_of_text)
root.mainloop()
