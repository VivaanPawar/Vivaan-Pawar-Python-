from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image, ImageTk


def showimg():
		fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(
			("PNG file", "*.png"), ("JPG file", " *.jpg"), ("All File", "*.*")))
		img = Image.open(fln)
		img.thumbnail((350,350))
		img = ImageTk.PhotoImage(img)
		lbl.configure(image=img)
		lbl.image = img 

root = Tk()

frm = Frame(root)
frm.pack(side = BOTTOM,padx=15,pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frm, text="Browse Image",command=showimg)
btn.pack(side=tk.LEFT)

btn2 = Button(frm, text="Quit",command=lambda: exit())
btn2.pack(side = tk.LEFT, padx = 10)

root.tk.call("wm","iconphoto",root._w, PhotoImage(file="Viv.png"))
root.title("Image Browser")
root.geometry("300x300")
root.mainloop()
