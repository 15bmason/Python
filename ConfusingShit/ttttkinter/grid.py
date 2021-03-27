from tkinter import *

root = Tk()
root.geometry("500x500") 

myLabel = Label(root, text="Hello world")
myLabel1 = Label(root, text="Yoinks")

myLabel.grid(row=2, column=1)
myLabel1.grid(row=3, column=2)

root.mainloop()