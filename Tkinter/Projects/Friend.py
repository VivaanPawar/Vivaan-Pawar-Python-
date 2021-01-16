import wolframalpha
import wikipedia
from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import time

while True:
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak Something.....")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            if text == "stop":
                break
            else:
                window = Tk()
                window.geometry("700x600")
                try:
                    app_id="W6JKA3-VK4VUXLQ6A"
                    client=wolframalpha.Client(app_id)
                    answer=next(res.results).text

                    Label1 = Label(window,justify=LEFT,compound=CENTER,padx=10,text=answer,font="time 15 bold")
                    Label1.pack()
                    window.after(500,lambda:window.destroy())
                    mainloop()
                except:
                    answer=wikipedia,summary()
                    Label1 = Label(window,justify=LEFT,compound=CENTER,padx=10,text=answer,font="time 15 bold")
                    Label1.pack()
                    window.after(500,lambda:window.destroy())
                    mainloop()        
        except:
            answer="Sorry! You Were Not Audible"
            print(answer)                 