from tkinter import *
from tkinter import messagebox
import requests
from io import BytesIO
import pokebase as pb
from PIL import Image, ImageTk

w = Tk()
w.title('P O K E D E X')
width_window = 490
height_window = 600
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_window/2)
y_coordinate = (screen_height/2)-(height_window/2)
w.geometry("%dx%d+%d+%d"%(width_window, height_window, x_coordinate, y_coordinate))
w.resizable(0,0)
w.config(bd = 10, relief = 'raised', bg='gray30')

def search():
    pokemon = pb.pokemon(pokemon_input.get().lower())
    try:
        details.delete('1.0', END)
        response = requests.get(pokemon.sprites.front_default)
        image = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
        pokemon_image.config(image=image)
        pokemon_image.image = image
        abilities = ''
        types = ''
        for ability in pokemon.abilities:
            abilities += ability.ability.name + ','
        for poketype in pokemon.types:
            types += poketype.type.name + ','

            data = f"""{pokemon_input.get().capitalize()}
            \nAltura: {pokemon.height}
            \nPeso: {pokemon.weight}
            \nHabilidades: {abilities}
            \nTipos: {types}
            """
            details.insert(END, data)

    except AttributeError:
        pokemon_image.configure(image='')
        details.insert(END, 'Pokemon no válido')


canvas = Canvas(width=470, height=580, bg='#FF0000', highlightbackground='yellow')
canvas.place(x=0,y=0)


frame = Frame(w, width=370, height=250, bg='white', bd=5, relief='sunken')
frame.place(x=50, y=100)

pokemon_image = Label(frame)
pokemon_image.place(x=10,y=10)

bordehoval = canvas.create_oval(10, 7,105, 85, width=2, fill='white')
ligthoval = canvas.create_oval(20, 10, 100, 80, width=2, fill='blue')
ligthoval_small2 = canvas.create_oval(110, 10, 140, 40, width=2, fill='#941005')
ligthoval_small3 = canvas.create_oval(150, 10, 180, 40, width=2, fill='blue')

borderhoval_small3 = canvas.create_oval(43, 367, 103, 424, width=2, fill='gray30')
ligthoval_small3 = canvas.create_oval(50, 370, 100, 420, width=2, fill='gray15', activefill='black')

canvas.create_rectangle(380, 490, 410, 400, width=3, fill='gray30')
canvas.create_rectangle(350, 460, 440, 430, width=3, fill='gray30')
canvas.create_line(382, 430, 409, 430, width=4, fill='gray30')
canvas.create_line(382, 460, 409, 460, width=4, fill='gray30')


def cambiarcolor(color):
    if color == 'blue':
        canvas.itemconfigure(ligthoval, fill = '#00FF00')
        w.after(500, lambda:cambiarcolor('yellow'))
    elif color == 'yellow':
        canvas.itemconfigure(ligthoval, fill = 'blue')
        w.after(500, lambda:cambiarcolor('blue'))

cambiarcolor('blue')

font1 = ('consolas', 13)


l2 = Label(w, text='Pokemón', bg='white')
l2.config(font = font1)
l2.place(x=80, y=280)


pokemon_input = Entry(w,width=28, border=0)
pokemon_input.config(font = font1)
pokemon_input.focus()
pokemon_input.place(x=80, y=310)

details = Text(frame, height=10, width=32, bg='gray80')
details.place(x=100, y=10)

Frame(w, width=320, height=2, bg="gray15").place(x=80,y=335)
Frame(w, width=370, height=6, bg="gray25").place(x=50,y=350)


Button(w, width=25, height=2, 
        text='S E A R C H',fg="white",bg='#139511',
        font=('Helvetica', 11, 'bold'),border=3, relief="raised", 
        activebackground='darkgreen',activeforeground='yellow',
        cursor='hand2',command=search).place(x=80, y=475)

w.mainloop()