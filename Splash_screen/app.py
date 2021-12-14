from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import *

w = Tk()
width_window = 427
height_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_window/2)
y_coordinate = (screen_height/2)-(height_window/2)
w.geometry("%dx%d+%d+%d"%(width_window, height_window, x_coordinate, y_coordinate))
w.overrideredirect(1)

s = ttk.Style()
s.theme_use('clam')
print(s.theme_names())
s.configure('red.Horizontal.TProgressbar', foreground='red', background='#4fCf4f')

progress = Progressbar(w, style='red.Horizontal.TProgressbar',
                        orient=HORIZONTAL, length=500, mode='determinate')

def main_window():
    q = Tk()
    q.geometry('450x250')
    l1 = Label(q, text= "Progress", fg="dark grey", bg=None)
    l = ('Calibri (Body)', 24, 'bold')
    l1.config(font=l)

    l1.place(x=80, y=100)
    q.mainloop()

def bar():
    l4 = Label(w, text="Loading...", fg='white',bg='#1F618D')
    lst4 = ('Terminal', 14)
    l4.configure(font = lst4)
    l4.place(x=0, y=190)

    import time
    r=0
    for i in range(100):
        progress['value'] = r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    w.destroy()
    main_window()

progress.place(x=-15, y=235)

Frame(w, width=427, height=234, bg='#1F618D').place(x=0, y=0)
b1 = Button(w, width=10, height=1, text='JUGAR', bg='#73C6B6',
        border=3, relief='raised', command=bar,fg="#212F3D", font=('Terminal', 13))
b1.place(x=170, y=180)

l1 = Label(w, text= "SPLASH", fg="white", bg='#1F618D')
lst1 = ('Calibri (Body)', 18, 'bold')
l1.configure(font=lst1)
l1.place(x=50, y=80)




l2 = Label(w, text= "LOGO", fg="white", bg='#1F618D')
lst2 = ('Calibri (Body)', 18)
l2.configure(font=lst1)
l2.place(x=155, y=80)

l3 = Label(w, text= "ENIDEV911", fg="white", bg='#1F618D')
lst3 = ('Terminal', 18, 'bold')
l3.configure(font=lst3)
l3.place(x=50, y=110)


w.mainloop()