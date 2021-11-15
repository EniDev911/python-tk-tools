#-------------------------------------------------------------------------------
#          Name: main
#
#         Autor: Marco Contreras
#
# Código fuente: https://github.com/EniDev911/desktop-app-aiep.git
#     Copyright: (c) Marco Contreras
#       Licence: GPL 3.0
#-------------------------------------------------------------------------------


# Execute for HD windows, compatible with S.O windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    print(windll.shcore)
except:
    pass


from tkinter import *
import pyttsx3
import PyPDF2
from PIL import Image, ImageTk

# COLORS
BG = '#1E3C62'
FG = '#C6CED7'
## GUI
app = Tk()
app.geometry('350x400')
app.title('Audiobook')
app.configure(bg=BG)

image = Image.open('assets/image/audiobook_01.png')
image_resized = image.resize((85, 85), Image.ANTIALIAS)
my_image = ImageTk.PhotoImage(image_resized)


logo = Label(app, image=my_image, bg=BG)
logo.pack(pady=(15,0))

title = Label(app, text='Let listen to the book', 
			bg=BG, font='none 20', fg=FG)
title.pack()

page_number = Label(app, text='Please enter the page number', 
			bg=BG, font='none 14', fg=FG)
page_number.pack(pady=(40,0))

page_number_box = Entry(app, font='none 15', bg=BG)
page_number_box.pack()

open_PDF = Button(app, text='Open', width=20, 
					bd=2, relief='raised', 
					bg='#21956F', fg='white',
					cursor='hand2', font=('Century gothic', 12, 'bold'))
open_PDF.pack(pady=(20,0))

say_PDF = Button(app, text='Talk', width=20,
					bg='#21956F', fg='white',
					bd=2, relief='raised',
					cursor='hand2', font=('Century gothic', 12, 'bold'))
say_PDF.pack(pady=(20, 0))

## text = 'Hola me llamo Marcos Alonso Contreras Villalobos'
## init the speaker
#speaker = pyttsx3.init()
## open the pdf
#book = open('jugar_dota1.pdf', 'rb')

## read the pdf
#read_file = PyPDF2.PdfFileReader(book)

## choosing the page that we want to read

## extract the text from the page
#text = page.extractText()

## print the text from the page
#print(text)

#speaker.say(text)
#speaker.runAndWait()

app.mainloop()