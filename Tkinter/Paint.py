import tkinter as tk
from tkinter import *
from tkinter import ttk,colorchooser


root = Tk()

class vn:
    def init(self, master):
        self.master = master 
        self.color_fg = "black"
        self.color_bg = "white"
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.creatWidgets()
        self.c.bind("<B1-Motion>",self.Paint)
        self.c.bind("<ButtonRelease-1>",self.reset)
    

    def Paint(self, event):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, self.penwidth, fill=self.color_bg, capstyle=ROUND, smooth=True)

            self.old_x = event.x
            self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def chageW(self, event):
        self.penwidth = event 

    def Clear(self):
        self.c.delete(All)

    def change_bg(self):
        self.color_bg = colorchooser.askcolor(color= self.color_bg)[1]
        self.c["bg"] = self.color_bg

    def  change_fg(self):
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]          

    def creatWidgets():
        self.control = Frame(self.master, padx =5, pady =5)
        Label(self.control, text="Pen Width:", font=("arial 18")).grid(rows=0, column=0)

        self.slider = ttk.Scale(self.control, from_=5, to=100, command="self.changeW", orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=30)
        self.slider.pack(slide=LEFT)

        self.c = Canvas(self.master, width=500, height=500, bg=self.color_bg)
        self.c.pack(fill=BOTH, expand=True)

        menu=Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label="Colors", menu=colormenu)
        colormenu.add_command(Label="Brush Colour", command=self.change_fg)
        colormenu.add_command(Label="Brush Colour", command=self.change_bg)
        optionMenu = Menu(menu)
        menu.add_cascade(label="Options", menu=colormenu)
        optionMenu.add_command(Label="Clear Canvas", command=self.Clear)
        optionMenu.add_command(Label="Background Colour", command=self.change_bg)
        optionMenu.add_command(Label="Exit", command=self.master.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    vn()
    root.title("Paint")
    root.mainloop()