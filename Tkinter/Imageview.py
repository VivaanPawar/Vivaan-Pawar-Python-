from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title ("Image Viewer")
root.tk.call("wm","iconphoto",root._w, PhotoImage(file="/home/vivaan/Documents/Programming/Python/Images/download.png"))
#==================Defs==========================
def back(image_number):
    global my_label0 
    global my_btnf
    global my_btnb 

    my_label0.grid_forget()
    my_label0 = Label(image=imagelist[image_number-1])
    my_btnf = Button(root,text=">>",command=lambda: front(image_number+1))
    my_btnb = Button(root,text="<<",command=lambda: back(image_number-1))

    if image_number == 1:
         my_btnb = Button(root,text="<<",state=DISABLED)

    my_label0.grid(row = 0, column = 0,columnspan = 3) 
    my_btnb.grid(row=1,column=0) 
    my_btnf.grid(row=1,column=2)
def front(image_number):
    global my_label0 
    global my_btnf
    global my_btnb 

    my_label0.grid_forget()
    my_label0 = Label(image=imagelist[image_number-1])
    my_btnf = Button(root,text=">>",command=lambda: front(image_number+1))
    my_btnb = Button(root,text="<<",command=lambda: back(image_number-1))

    if image_number == 5:
        my_btnf = Button(root,text=">>",state=DISABLED)

    my_label0.grid(row = 0, column = 0,columnspan = 3) 
    my_btnb.grid(row=1,column=0) 
    my_btnf.grid(row=1,column=2)
#=================Images And Packing=================
my_img0 = ImageTk.PhotoImage(Image.open("/home/vivaan/Documents/Programming/Python/Images/Calc.gif"))
my_img1 = ImageTk.PhotoImage(Image.open("/home/vivaan/Documents/Programming/Python/Images/download.png"))
my_img2 = ImageTk.PhotoImage(Image.open("/home/vivaan/Documents/Programming/Python/Images/Image.gif"))
my_img3 = ImageTk.PhotoImage(Image.open("/home/vivaan/Documents/Programming/Python/Images/Only Ben.png"))
my_img4 = ImageTk.PhotoImage(Image.open("/home/vivaan/Documents/Programming/Python/Images/Vivaan MAT.gif"))

imagelist = [my_img0,my_img1,my_img2,my_img3,my_img4]

my_label0 = Label(image = my_img0)
# my_label1 = Label(image = my_img1)
# my_label2 = Label(image = my_img2)
# my_label3 = Label(image = my_img3)
# my_label4 = Label(image = my_img4)
my_label0.grid(row = 0, column = 0,columnspan = 3)
# my_label1.grid(row = 0, column = 0,columnspan = 3)
# my_label2.grid(row = 0, column = 0,columnspan = 3)
# my_label3.grid(row = 0, column = 0,columnspan = 3)
# my_label4.grid(row = 0, column = 0,columnspan = 3)
#====================Buttons===============
my_btnb = Button(root,text="<<",command=back,state = DISABLED)
my_btn2 = Button(root,text="Quit",command = root.quit)
my_btnf = Button(root,text=">>",command=lambda: front(2))
my_btnb.grid(row=1,column=0)
my_btn2.grid(row=1,column=1)
my_btnf.grid(row=1,column=2)

root.mainloop()