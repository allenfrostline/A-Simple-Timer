from os import system
from time import sleep
from tkinter import *


N = 90


def start():
    n = N
    while n:
        label.configure(text='{:02d}{}{:02d}{}{:02d}'.format(n // 3600, ' ' if (n % 2) else ':', n // 60, ' ' if (n % 2) else ':', n % 60))
        root.update()
        n -= 1
        sleep(1)
    label.configure(text='Time is up')
    root.update()
    system('afplay /System/Library/Sounds/Glass.aiff')


root = Tk()
root.resizable(0, 0)
root.geometry('200x25+0+0')
root.pack_propagate(0)
root.title('A Simple Timer')
label = Label(root, text='{:02d}:{:02d}:{:02d}'.format(N // 3600, N // 60, N % 60))
label.pack(side=LEFT)
Button(root, text='Start', command=start).pack(side=RIGHT)
root.mainloop()
