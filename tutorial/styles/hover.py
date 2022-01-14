
# ==== Imports

from tkinter import *
from tkinter import messagebox

# === Funcionts

def showmessage():
	messagebox.showinfo('Info','Pasaste por encima del elemento')


def hover(event=None):
	showmessage()

def leave(event=None):
	my_btn['bg'] = 'red'

# == Settings windows
root = Tk()
root.title('App with hover event')
# == config open in the center of screen 
width_window = 600
height_window = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_window/2)
y_coordinate = (screen_height/2)-(height_window/2)
root.geometry("%dx%d+%d+%d"%(width_window, height_window, x_coordinate, y_coordinate))

# == Buttons 
my_btn = Button(root, text='Active hover', bg='lightgreen')
my_btn.pack()
my_btn.bind('<Enter>', hover)
my_btn.bind('<Leave>', leave)


# == Labels

# 
root.mainloop()