from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World!").grid(row=1, column=1)

myButton = Button(root, text="Terminate", padx=50, pady=50).grid(row=0, column=0)

root.mainloop()
