from tkinter import *

root = Tk()
root.wm_title('My First GUI')
w1 = Label(root, text='tkinter learning', background='red')
w2 = Label(root, text='tkinter learning2', background='green')
w3 = Label(root, text='tkinter learning3', background='yellow')
w1.pack()
w2.pack()
w3.pack()
root.mainloop()
