from tkinter import *
from tkinter import filedialog,messagebox
import os
import tkinter as tk
import vlc


root = Tk()
root.title("Music Player")
root.geometry("450x150")
root.resizable(0, 0)
root.tk.call("wm","iconphoto",root._w, PhotoImage(file="Viv.png"))

filetoplay=""
vlc_obj = vlc.Instance()
player = vlc_obj.media_player_new()

def selffile():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Music",filetypes = (("Music File","*.mp3"),("Webm File","*.webm"),("All Files","*.*")))
    txt.set(os.path.basename(fln))
    filetoplay = fln

def playmusic():
    if filetoplay == "":
        messagebox.showerror(title="Please Select A Music",message="Please Select A Music")
        return False
    track = vlc_obj.media_new(filetoplay)
    player.set_media(track)
    player.play()    
def stopmusic():
    player.stop()    
txt =StringVar()
txt.set("No Music Selected")


wraper = LabelFrame(root, text="Music Player")
wraper.pack(fill="both",expand="yes",padx=10,pady=10)

lbl = Label(wraper,textvariable=txt)
lbl.pack()

btn2 = Button(wraper,text="Select Music",command = selffile)
btn2.pack(side=tk.LEFT,padx=10)

btn3 = Button(wraper,text="Play Music",command = playmusic)
btn3.pack(side=tk.LEFT,padx=10)

btn4 = Button(wraper,text="Stop Music",command = stopmusic)
btn4.pack(side=tk.LEFT,padx=10)

btn1 = Button(wraper,text="Quit",command =root.quit)
btn1.pack(side=tk.LEFT,padx=10)

root.mainloop()