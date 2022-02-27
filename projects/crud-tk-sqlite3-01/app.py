from tkinter import *
import sqlite3

root = Tk()
root.geometry('550x500')
root.title('Registration form')

# Variables
fullname = StringVar()
email = StringVar()
var = IntVar()
c = StringVar()
var1 = IntVar()
var2 = IntVar()

def database():
	name = fullname.get()
	mail = email.get()
	gender = var.get()
	country = c.get()
	prog = var1.get()
	conn = sqlite3.connect('form.db')

	with conn:
		cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS Student
					(fullname TEXT,
					 email TEXT,
					 gender TEXT,
					 country TEXT,
					 programming TEXT)''')
	cursor.execute('''INSERT INTO Student 
					(fullname, email, gender, country, programming)
					  VALUES(?,?,?,?,?)''', (name, mail, gender, country, prog,))
	conn.commit()

lbl_0 = Label(root, text='Registration form', width=20, font=('bold', 20))
lbl_0.place(x=90, y=53)

lbl_1 = Label(root, text='Fullname', width=20, font=('bold', 10))
lbl_1.place(x=80, y=130)

entry_1 = Entry(root, textvariable=fullname)
entry_1.place(x=240, y=130)

lbl_2 = Label(root, text='Email', width=20, font=('bold', 10))
lbl_2.place(x=68, y=180)

entry_2 = Entry(root, textvariable=email)
entry_2.place(x=240, y=180)

lbl_3 = Label(root, text='Gender', width=20, font=('bold', 10))
lbl_3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

lbl_4 = Label(root, text='Country', width=20, font=('bold', 10))
lbl_4.place(x=70, y=280)

country_list = ['Chile', 'Perú', 'Bolivia', 'Argentina']

droplist = OptionMenu(root, c, *country_list)
droplist.config(width=15)
c.set('Select your country')
droplist.place(x=240, y=280)

lbl_4 = Label(root, text='Programming', width=20, font=('bold', 10))
lbl_4.place(x=85, y=330)

Checkbutton(root, text='java', variable=var1).place(x=235, y=330)
Checkbutton(root, text='python', variable=var2).place(x=290, y=330)

Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)

root.mainloop()
