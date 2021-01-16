from tkinter import*
from PIL import Image, ImageTk

root = Tk()
root.title("Sliders")
root.tk.call("wm","iconphoto",root._w, PhotoImage(file="Viv.png"))

vertical = Scale(root,from_=0,to = 200)
vertical.pack()
horizontal = Scale(root,from_=0,to = 200,orient = HORIZONTAL)
horizontal.pack()


root.mainloop()
