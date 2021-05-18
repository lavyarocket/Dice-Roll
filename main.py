import random
from tkinter import *

root = Tk()
root.title('Dice Roll')

root.geometry("500x300")

l1 = Label(root, font=("times", 200))


def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()


b1 = Button(root, text="Roll the Die", command=roll)
b1.place(x=200, y=20)

root.mainloop()
