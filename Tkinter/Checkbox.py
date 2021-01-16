from tkinter import*
from PIL import Image, ImageTk

root=Tk()
root.title("Checkbox")
root.tk.call("wm","iconphoto",root._w, PhotoImage(file="Viv.png"))

var = IntVar()

c = Checkbutton(root, text="This IS A Checkbox",variable = var)
c.pack()



root.mainloop()