from tkinter import*
import tkinter as tk
import pyttsx3
 
engine = pyttsx3.init()


root = Tk()
root.title("Text To Speach")
root.geometry("350x100")
root.resizable(0, 0)
root.tk.call("wm","iconphoto",root._w, PhotoImage(file="Viv.png"))

def speaknow():
    engine.say(txtv.get())
    engine.runAndWait()
    engine.stop()


txtv = StringVar()


wraper = LabelFrame(root, text="Text To Speach")
wraper.pack(fill="both",expand="yes",padx= 10,pady=10)

lbl = Label(wraper,text="Text")
lbl.pack(side=tk.LEFT,padx=10)

txt = Entry(wraper, textvariable=txtv)
txt.pack(side=tk.LEFT,padx=10)

btn = Button(wraper, text="Speak",command = speaknow)
btn.pack(side=tk.LEFT,padx=10)






root.mainloop()
