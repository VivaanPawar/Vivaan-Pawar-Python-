from tkinter import *

root = Tk()
root.title("Vivaan MAT")
root.resizable(0,0)
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="Images/Vivaan MAT.gif"))
myLabel0 = Label(text="Welcome To VIvaan MAT Oficial Aplication",font = ("Verdana",20))
myLabel1 = Label(text="So,Here You Are Going Find My YouTube Videos Before Youtube",font = "Verdana")

myLabel1.grid(row = 1,column = 0)
myLabel0.grid(row = 0 ,columnspan = 10)
root.mainloop()
