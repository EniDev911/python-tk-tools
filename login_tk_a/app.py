from tkinter import *
from tkinter import messagebox

w = Tk()
w.geometry('350x500+600+150')
w.title('L O G I N')
w.resizable(0,0)

j = 0
r = 0

for i in range(100):
    c=str(139313+r) 
    background = Frame(w, width=10, height=500, bg=f'#{c}')
    background.place(x=j,y=0)
    j += 10
    r += 2
    
    
Frame(w, width=250, height=400, bg='white').place(x=50, y=50)



# fonts
font1 = ('consolas', 13)
# label 1
l1 = Label(w, text='Username', bg='white')
l1.config(font = font1)
l1.place(x=80, y=200)

e1 = Entry(w, width=20, border=0)
e1.config(font=font1)
e1.place(x=80, y=230)
e1.focus()

# label 2
l2 = Label(w, text='Password', bg='white')
l2.config(font = font1)
l2.place(x=80, y=280)

e2 = Entry(w,width=20, border=0, show=u'\u25CF')
e2.config(font = font1)
e2.place(x=80, y=310)

Frame(w, width=180, height=2, bg="#139313").place(x=80,y=250)
Frame(w, width=180, height=2, bg="#139313").place(x=80,y=330)

# Include image
from PIL import Image, ImageTk

image1 = Image.open('assets/img/user.png')
timage = ImageTk.PhotoImage(image1)

limage = Label(image=timage, border = 0, bg="white",justify="center")
limage.place(x=115, y=60)

def cmd(e=None):
    if e1.get() == 'Enidev911' and e2.get() == '12345':
        messagebox.showinfo('LOGIN SUCCESFULLY', '\tWELCOME\t')
        q = Tk()
        q.mainloop
    else:
        messagebox.showwarning('LOGIN FAILED', '\tPLEASE TRY AGAIN\t')

btn_login = Button(w, width=20, height=2, 
        text='L O G I N',fg="white",bg='#139511',
        font=('Helvetica', 11, 'bold'),border=0, 
        activebackground='darkorange',activeforeground='yellow',
        cursor='hand2',command=cmd)

btn_login.place(x=80, y=375)

w.bind('<Return>', cmd)

w.mainloop()