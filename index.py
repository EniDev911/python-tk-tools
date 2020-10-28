from tkinter import ttk, messagebox as msg, font
from tkinter import *
#module for connect to sqlite
import sqlite3

class Product:


    def __init__(self, root):
        self.master = root
        self.master.title('Products Application')
        
    
        #Creating a frame Container
        frame = LabelFrame(self.master, text = 'Nuevo Producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #Cod Input Product
        Label(frame, text = 'Código: ', ).grid(row = 1, column = 0)
        self.cod = Entry(frame)
        self.cod.focus()
        self.cod.grid(row = 1, column = 1, pady = 10)

        #Name Input Product
        
        Label(frame, text = 'Nombre: ').grid(row = 2, column = 0)
        self.name = Entry(frame)
        self.name.grid(row = 2, column = 1, pady = 10)

        #Price Input
        Label(frame, text = 'Precio: ').grid(row = 3, column = 0)
        self.price = Entry(frame)        
        self.price.grid(row = 3, column = 1, pady = 10)

        #Button Add Product
        ttk.Button(frame, text = 'Guardar Producto').grid(row = 4, columnspan = 2, sticky =  W + E)

        #Table Show Product
        self.three = ttk.Treeview(height = 10, columns = 3)
        self.three.grid(row = 4, column = 0, columnspan = 3)
        self.three.heading('#0', text = 'Código', anchor = CENTER)
        self.three.heading('#1', text = 'Nombre', anchor = CENTER)
     
if __name__== '__main__':
    root = Tk()
    app = Product(root)
    root.mainloop()

#msg.showinfo(title=None, message='Nuevo Producto')

