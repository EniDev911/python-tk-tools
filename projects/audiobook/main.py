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
from tkinter import simpledialog
import pyttsx3
import PyPDF2
import os
from PIL import Image, ImageTk
import os 
import webbrowser

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
path_logo = 'assets/image/audiobook.png'
app.tk.call('wm', 'iconphoto', app._w, PhotoImage(file=path_logo))
app.resizable(0,0)
app.configure(bg=BG)

## init the speaker
engine = pyttsx3.init("sapi5")


## Open file
path = None
def clic():
	global path

	files = [('PDF files', '*.pdf'),
			 ('All files', '*.*')]

	path = filedialog.askopenfilename(
						title = "Select a PDF file",
						initialdir='./', 
						filetypes=files,
						parent=app)
	

	if path:

		filename = os.path.basename(path)
		lbl_openfile.config(text=filename)
		lbl_openfile.pack()
		save_OUTPUT.place(x=148, y=210)



## play talk
def talk():
	page_n = page_number_box.get()
	say_PDF.config(image=my_stopimg)
	if path:
		## open the pdf
		book = open(path, 'rb')
		## read the pdf200...
		reader = PyPDF2.PdfFileReader(book)
		
		if page_n != '':
			read = reader.getPage(int(page_n))
			r = read.extractText()

			engine.say(r)
			engine.runAndWait()

		elif page_n == '':
			try:
				contenido = ''

				for page in range(reader.numPages):
					#choosing the page that we want to read
					next_page = reader.getPage(page)
					## extract the text from the page
					text = next_page.extractText()
					contenido += text
					engine.say(text)
					print(contenido)
					engine.runAndWait()


			except IndexError as e:
				print(e)
				messagebox.showinfo('information', 'The page is not in the range')
		book.close()

	else:
		messagebox.showinfo('information', 'you must choose a PDF file from the directory')


## save talk
def save_as(document):

	book = open(document, 'rb')
	reader = PyPDF2.PdfFileReader(book)

	files = [('All files', '*.*'),
			 ('MP3 files', '*.mp3')]

	dialog = simpledialog.askstring("INFO", "Name to mp3?", parent=app)
	ext = '.mp3'
	print(dialog)
	
	if dialog != None:
		namesave = dialog+ext
	#namesave = 	asksaveasfile(mode='w', filetypes=files, defaultextension = files)
		contenido = ''
		for page in range(reader.numPages):
			next_page = reader.getPage(page)
			text = next_page.extractText()
			contenido += text

		print(contenido)
		print(namesave)
		engine.save_to_file(contenido, namesave)
		engine.runAndWait()



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

# File_explorer img
img_fs = Image.open('assets/image/file_explorer.png')
fs_resized = img_fs.resize((45, 40), Image.ANTIALIAS)
my_openimg = ImageTk.PhotoImage(fs_resized)

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



open_PDF = Button(app, image=my_openimg, width=40, 
					bd=0, relief='raised',
					bg=BG, fg='white',
					activebackground=BG, 
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
						command=lambda : save_as(path))

# Footer S.M
frame = LabelFrame(app, text='FOLLOW ME',
				   fg=FG, bg=BG, bd=0,
				   labelanchor='n',
				   font=('Century gothic', 8, 'italic bold'),
				   width=350, height=35)
frame.place(x=235, y=390)

img_github = Image.open('assets/image/social_media/github(96x96).png')
github_resized = img_github.resize((30, 30), Image.ANTIALIAS)
my_img_github = ImageTk.PhotoImage(github_resized)

btn_github = Button(frame, image=my_img_github,
					  bd=0,bg=BG,
					  activebackground=BG, 
					  cursor='hand2',
					  command=lambda: webbrowser.open('https://github.com/EniDev911'))
btn_github.pack(side='left', padx=10)

img_facebook = Image.open('assets/image/social_media/facebook(96x96).png')
facebook_resized = img_facebook.resize((30, 30), Image.ANTIALIAS)
my_img_facebook = ImageTk.PhotoImage(facebook_resized)

btn_facebook = Button(frame, image=my_img_facebook,
					  bd=0,bg=BG,
					  activebackground=BG, 
					  cursor='hand2',
					  command=lambda: webbrowser.open('https://www.facebook.com/profile.php?id=100009064421475'))
btn_facebook.pack(side='right')

app.mainloop()