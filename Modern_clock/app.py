from tkinter import *
from datetime import datetime
from time import strftime
from PIL import Image, ImageTk

w = Tk()
w.geometry('1400x600')
w.minsize(820,200)

# Background
img1 = Image.open('img.jpg')
new = img1.resize((w.winfo_screenwidth(), w.winfo_screenheight()))
img2 = ImageTk.PhotoImage(new)

Label(image=img2, width=w.winfo_screenwidth()).place(x=0,y=0)


f1 = Frame(w, width=820, height=200, bg='#0D0E0E')
#f1.place(x=0,y=0)
f1.pack(expand=True)

a = datetime.today().strftime("%A")
b = a.upper()
c = b[0:2]

def time():
    a = strftime('%H  :  %M  :  %S')
    l1.config(text = a)
    l1.after(1000, time)

l1 = Label(f1, font=('Century Gothic', 60), bg='#0D0E0E',
            fg="#d3d3d3")
l1.place(x=270, y=35)

l2 = Label(f1, font=('Century Gothic', 60), bg='#0D0E0E',
            fg="#d3d3d3")
l2.config(text=c+" |")
l2.place(x=80, y=35)

def labels():
    l3 = Label(f1, font=("Century Gothic", 8), bg="#0e1013", fg="#7f7f7f", text ="DAY")
    l3.place(x=122, y=130)

    l3 = Label(f1, font=("Century Gothic", 8), bg="#0e1013", fg="#7f7f7f", text ="HOURS")
    l3.place(x=300, y=130)

    l3 = Label(f1, font=("Century Gothic", 8), bg="#0e1013", fg="#7f7f7f", text ="MINUTES")
    l3.place(x=490, y=130)

    l3 = Label(f1, font=("Century Gothic", 8), bg="#0e1013", fg="#7f7f7f", text ="SECONDS")
    l3.place(x=680, y=130)

labels()
time()

# FullScreen
w.bind('<F11>', lambda event: w.attributes("-fullscreen",True))
w.bind('<Escape>', lambda event: w.attributes("-fullscreen",False))

w.mainloop()