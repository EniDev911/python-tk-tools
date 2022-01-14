from tkinter import Label, Tk 
from time import strftime


w = Tk()

w.title("Digital Clock")
w.config(bg='#fff')
w.geometry("350x250+10+10")
w.minsize(width=250, height=200)

w.columnconfigure(0, weight=15)
w.rowconfigure(0, weight=15)

w.columnconfigure(0, weight=1)
w.rowconfigure(2, weight=1)


def get_time():
	hour = strftime("%H:%M:%S")
	day = strftime("%A")
	

w.mainloop()