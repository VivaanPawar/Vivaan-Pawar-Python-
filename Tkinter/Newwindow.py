from tkinter import *
from PIL import Image, ImageTk
#========================Define======================
def open():
    global my_img
    top = Toplevel()
    top.title("Second Window")
    myl0 = Label(top,text="Hi Vivaan").pack()
    my_img = ImageTk.PhotoImage(Image.open("Viv.png"))
    my_Label = Label(root, image= my_img).pack()
    btn = Button(top,text="Exit Top",command = top.destroy).pack()
#=======================+Windows=====================
root = Tk()
root.title("New Window")
root.tk.call("wm","iconphoto",root._w, PhotoImage(file="/home/vivaan/Documents/Programming/Python/Images/download.png"))

# top = Toplevel()
# top.title("Second Window")

#=================================+Buttons===============
my_btn = Button(root,text="Second Window",command = open).pack()
#=========================Labels=======================
# myl0 = Label(top,text="Hi Vivaan").pack()
myl1 = Label(root,text="Main Widow").pack()
# my_img = ImageTk.PhotoImage(Image.open("Viv.png"))
# my_Label = Label(root, image= my_img).pack()

root.mainloop()
# top.mainloop()