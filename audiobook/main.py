#-------------------------------------------------------------------------------
#          Name: main
#
#         Autor: Marco Contreras
#
# Código fuente: https://github.com/EniDev911/PythonTk/blob/master/audiobook/main.py
#     Copyright: (c) Marco Contreras
#       Licence: GPL 3.0
#-------------------------------------------------------------------------------


# Execute for HD windows, compatible with S.O windows
try:
    from ctypes import windll
    windll.shcore.SetProcesDpiAwareness(1)
    print(windll.shcore)
except:
    pass

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pyttsx3
import PyPDF2
from PIL import Image, ImageTk

# COLORS
BG = '#293442'
FG = '#E8EBEF'
## GUI
app = Tk()
app.geometry('350x400')
app.title('Audiobook')
app.configure(bg=BG)

## Functions
path = None
def clic():
	global path
	path = filedialog.askopenfilename()
	print(path)
	lbl_openfile.pack()

def talk():
	page_n = page_number_box.get()
	if path and page_n:
		## init the speaker
		speaker = pyttsx3.init()
		## open the pdf
		book = open(path, 'rb')
		## read the pdf200...
		read_file = PyPDF2.PdfFileReader(book)
		try:
			#choosing the page that we want to read
			page = read_file.getPage(int(page_n))
			## extract the text from the page
			text = page.extractText()

			speaker.say(text)
			speaker.runAndWait()
		except IndexError as e:
			print(e)
			messagebox.showinfo('information', 'The page is not in the range')
	else:
		messagebox.showinfo('information', 'you must choose a PDF file from the directory')

image = Image.open('assets/image/audiobook_01.png')
image_resized = image.resize((85, 85), Image.ANTIALIAS)
my_image = ImageTk.PhotoImage(image_resized)


logo = Label(app, image=my_image, bg=BG)
logo.pack(pady=(15,0))

title = Label(app, text='Let listen to the book', 
			bg=BG, font='none 20', fg=FG)
title.pack()

lbl_openfile = Label(app, text=path)

page_number = Label(app, text='Please enter the page number', 
			bg=BG, font='none 14', fg=FG)
page_number.pack(pady=(40,0))

page_number_box = Entry(app, font='none 15', bg=BG, fg=FG)
page_number_box.pack()



open_PDF = Button(app, text='Open', width=20, 
					bd=2, relief='raised', 
					bg='#21956F', fg='white',
					cursor='hand2', font=('Century gothic', 12, 'bold'),
					command=clic)
open_PDF.pack(pady=(20,0))

say_PDF = Button(app, text='Talk', width=20,
					bg='#21956F', fg='white',
					bd=2, relief='raised',
					activebackground='gray60',
					cursor='hand2', font=('Century gothic', 12, 'bold'),
					command=talk)
say_PDF.pack(pady=(20, 0))

app.mainloop()