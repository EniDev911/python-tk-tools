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
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
import pyttsx3
import PyPDF2
import os
from PIL import Image, ImageTk
import os 

# COLORS
BG = '#0F082A'
FG = '#E8EBEF'
## GUI
app = Tk()
width_window = 350
height_window = 450
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_window/2)
y_coordinate = (screen_height/2)-(height_window/2)

app.geometry("%dx%d+%d+%d"%(width_window, height_window, x_coordinate, y_coordinate))
app.title('Audiobook')
app.resizable(0,0)
app.configure(bg=BG)


## Functions


## Open file
path = None
def clic():
	global path
	path = filedialog.askopenfilename(initialdir='./')
	print(path)
	lbl_openfile.config(text=path)
	filename = os.path.basename(path)
	lbl_openfile.config(text=filename)
	lbl_openfile.pack()
	save_OUTPUT.place(x=148, y=210)

## play talk
def talk():
	page_n = page_number_box.get()
	say_PDF.config(image=my_stopimg)
	if path:
		## init the speaker
		speaker = pyttsx3.init("sapi5")
		## open the pdf
		book = open(path, 'rb')
		## read the pdf200...
		reader = PyPDF2.PdfFileReader(book)
		
		if page_n != '':
			read = reader.getPage(int(page_n))
			r = read.extractText()

			speaker.say(r)
			speaker.runAndWait()


		elif page_n == '':
			try:

				for page in range(reader.numPages):
					#choosing the page that we want to read
					next_page = reader.getPage(page)
					## extract the text from the page
					text = next_page.extractText()

					speaker.say(text)
					print(text)
					speaker.runAndWait()


			except IndexError as e:
				print(e)
				messagebox.showinfo('information', 'The page is not in the range')

		speaker.stop()
	else:
		messagebox.showinfo('information', 'you must choose a PDF file from the directory')


## save talk
def save_MP3(content):

	files = [('All files', '*.*'),
			 ('MP3 files', '*.mp3')]
	file = 	asksaveasfile(filetypes = files, defaultextension = files)

	engine.save_to_file(content, file)



image = Image.open('assets/image/book_01.png')
image_resized = image.resize((95, 145), Image.ANTIALIAS)
my_image = ImageTk.PhotoImage(image_resized)

play_img = Image.open('assets/image/play.png')
play_resized = play_img.resize((43, 43), Image.ANTIALIAS)
my_playimg = ImageTk.PhotoImage(play_resized)

stop_img = Image.open('assets/image/stop.png')
stop_resized = stop_img.resize((43, 43), Image.ANTIALIAS)
my_stopimg = ImageTk.PhotoImage(stop_resized)


save_img = Image.open('assets/image/save.png')
save_resized = save_img.resize((28, 28), Image.ANTIALIAS)
my_saveimg = ImageTk.PhotoImage(save_resized)


logo = Label(app, image=my_image, bg=BG)
logo.pack(pady=(15,0))



title = Label(app, text='Let listen to the book', 
			bg=BG, font='none 20', fg=FG)
title.pack()

lbl_openfile = Label(app, text='', bg=BG, fg=FG, font=('Century gothic', 12, 'italic'))

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

say_PDF = Button(app, image=my_playimg, width=40,
					bg='#F3413B', fg='white',
					bd=0, relief='raised',
					activebackground='gray60',
					cursor='hand2', font=('Century gothic', 12, 'bold'),
					command=talk)
say_PDF.place(x=155, y=105)


save_OUTPUT = Button(app, image=my_saveimg, width=50,
						bg=BG, fg='white',
						bd=0, relief='raised',
						activebackground='gray20',
						cursor='hand2',
						command=save_MP3)



app.mainloop()