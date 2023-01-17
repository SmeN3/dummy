import tkinter as tk


text = 'Hello world my name is Paul'
words = text.split(' ')
def speed_of_text():
    global words
    if words:
        word = words.pop(0)
        print(word)
        root.after(1000, speed_of_text)
    else:
        print('All words typed')
        root.after_cancel(speed_of_text)

root = tk.Tk()
root.after(1000, speed_of_text)
root.mainloop()
