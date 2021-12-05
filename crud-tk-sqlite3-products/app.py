try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    print(windll.shcore)
except:
    pass

from tkinter import *
from tkinter import ttk 
import sqlite3

class Product:

	def __init__(self, window):
		self.win = window
		self.win.title('Products Stock')
		self.win.geometry("500x500")

		frame = LabelFrame(self.win, text="Register a new Product",
							labelanchor='n')
		frame.grid(row=0, column=0, columnspan=3, pady=20, ipady=5)

		# Name input
		Label(frame, text='Name: ').grid(row=1, column=0)
		self.name = Entry(frame)
		self.name.grid(row = 1, column=1)

		# Price input
		


if __name__ == '__main__':
	window = Tk()
	app = Product(window)
	window.mainloop()
