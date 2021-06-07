from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.geometry("400x240")
root.resizable(0,0)
root.title("Login")

def login():
    w = Frame(root, width=400, height=240, bg='#EFAD29')
    w.place(x=0, y=0)

    # Entry box for username
    def on_enter(e):
        e1.delete(0, 'end')

    def on_leave(e):
        if e1.get() == '':
            e1.insert(0, 'username')

    e1 = Entry(w, width=28, fg = 'grey')
    e1.configure(font=('Consolas', 13, 'bold'))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0, 'username')
    e1.place(x=70, y=42)

    # Clean box
    def clean_box():
        e1.delete(0,'end')
        e2.delete(0,'end')

    # Entry box for password
    def on_enter(e):
        e2.delete(0, 'end')

    def on_leave(e):
        if e2.get() == '':
            e2.insert(0, 'password')

    e2 = Entry(w, width=28, fg = 'grey')
    e2.configure(font=('Consolas', 13, 'bold'))
    e2.place(x=70, y=92)
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0, 'password')

    # Command when login button pressed
    def login_command():
        file=open('username.txt', 'r')
        r = file.readline()
        print(r)

        f = open('password.txt', 'r')
        rd = f.readline()
        f.close()
        print(rd)

        if e1.get() == r and e2.get() == rd:
            messagebox.showinfo('Info','Succesfully Logged In')
            clean_box()

        else:
           messagebox.showwarning('try again', 'Incorrect username or password')

    btn = Button(w, width=18, height=0, text='Login', command=login_command, bd=0,
            bg='dark red', fg='white')
    btn.place(x=130, y=146)

login()


def sigup():
    pass

root.mainloop()