from tkinter import *
 
rot = Tk()
rot.title("Chat Bot")
rot.geometry("400x500")

menu = Menu(rot)

fmenu = Menu(rot)
fmenu.add_command(label="New..")
fmenu.add_command(label="Save As..")
fmenu.add_command(label="Exit")

    
menu.add_command(label="File")
menu.add_command(label="Edit")
menu.add_command(label="Quit")
rot.config(menu=menu)

chatwindow=Text(rot, bd=1 , bg="grey",width=50,height=8)
chatwindow.place(x=6,y=6,height=385,width=370)

messagebox = Text(rot,bg="grey", width=30,height=4)
messagebox.place(x=128,y=400,height=88,width=260)

btn = Button(rot,text="Send",bg="blue",activebackground="lightblue",width=12,height=5,font=("Arial", 20))
btn.place(x=6,y=400,height=88,width=120)

bar = Scrollbar(rot, command=chatwindow.yview())
bar.place(x=375,y=5,height=385)

rot.mainloop()