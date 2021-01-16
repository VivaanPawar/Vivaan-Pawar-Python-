from tkinter import*
import datetime
from tkinter.messagebox import *
from tkinter.ttk import*
# import winsound
# ==============================+++++Window============================
root = Tk()
root.geometry("400x200")
root.title("Alarm Clock")
root.tk.call("wm", "iconphoto", root._w, PhotoImage(file="Viv.png"))
# ===============================================Define============================


def alarm():
    x = int(l1.get())
    y = int(l2.get())
    showinfo("Message", "Alarm has Been Set")
    while True:
        if x == datetime.datetime.now().hour and y == datetime.datetime.now().minute:
            showinfo("Alarm","The Alarm Is Ringing")
            break


# $=========================Contents========================$
Label1 = Label(root, text="Hours")
Label2 = Label(root, text="Minutes")
# Label3 = Label(root, text="Seconds")
Label1.grid(row=0, column=0)
Label2.grid(row=1, column=0)
l1 = Entry(root)
l2 = Entry(root)
l1.grid(row=0, column=1)
l2.grid(row=1, column=1)
btn = Button(root, text="Set Alarm", command=alarm)
btn.grid(row=3, column=1)
v = Combobox(root,values=["AM","PM"])
v.grid(row=0,column=2)




root.mainloop()
