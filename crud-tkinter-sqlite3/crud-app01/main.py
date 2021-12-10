# EJECURA PARA PANTALLAS HD, COMPATIBLE CON WINDOWS
try:
    from ctypes import windll
    windll.shcore.SetProcesDpiAwareness(1)
    print(windll.shcore)
except:
    pass

# importar los módulos sqlite3 y tkinter
import sqlite3
from tkinter import *
# importamos la clase para mostrar ventanas
from tkinter import messagebox
# importamos los nuevos widgets de tkinter
from tkinter import ttk 
# importamos la clase para disponer del explorador de archivos
from tkinter import filedialog
# importamos os para acceder a funciones del S.0
import os

# ================ BASE DE DATOS ==============
def conexionBBDD():
	'''función para crear la base de datos'''
	con = sqlite3.connect('empleados.db')
	cursor = con.cursor()
	try:
		cursor.execute('''
			CREATE TABLE IF NOT EXISTS empleados(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(50) NOT NULL,
				cargo VARCHAR(30) NOT NULL,
				salario REAL NOT NULL)''')
		messagebox.showinfo('INFO', 'BASE DE DATOS CREADA')

	except sqlite3.Error as e:
		print(e)
		messagebox.showinfo('INFO', 'ERROR EN LA CONEXIÓN')
	
	con.close()

def eliminarBBDD():
	'''Función que elimina la base de datos si existe'''
	con = sqlite3.connect('empleados.db')
	cursor = con.cursor()
	if messagebox.askyesno('ADVERTENCIA', '¿Estás seguro de eliminar la base de datos?'):
		try:
			cursor.execute('DROP TABLE empleados')
			messagebox.showinfo('INFO', '¡LA BASE DE DATOS FUE ELIMINADA!')
		except sqlite3.OperationalError as e:
			messagebox.showinfo('INFO', '¡BASE DE DATOS NO EXISTE!')
		finally:
			con.close()

		if os.path.isfile('empleados.db'):
			os.remove('empleados.db')

# ================= CRUD ======================
def crear():
	con = sqlite3.connect('empleados.db')
	cursor = con.cursor()
	datos = nombre.get(), cargo.get(), salario.get()
	#prueba = ('marcelo', 'supervisor', 150000)

	try:
		cursor.execute('''
			INSERT INTO empleados VALUES(NULL, ?,?,?)''', (datos))
		con.commit()
		messagebox.showinfo('INFO', '¡REGISTRO INSERTADO EXITOSAMENTE!')
		mostrar()
	except sqlite3.OperationalError as e:
		print(e)
		messagebox.showinfo('INFO', 'ERROR INTERNO AL INGRESAR LOS DATOS')
	finally:
		con.close()

def mostrar():
	con = sqlite3.connect('empleados.db')
	cursor = con.cursor()
	registros = tree.get_children()
	
	for fila in registros:
		tree.delete(fila)
	
	try:
		cursor.execute('SELECT * FROM empleados;')
		resultados = cursor.fetchall()
		for registro in resultados:
			tree.insert('', 'end', text=registro[0], values=(registro[1], registro[2], registro[3]))
	except:
		pass
	finally:
		con.close()

def actualizar():
	con = sqlite3.connect('empleados.db')
	cursor = con.cursor()
	datos = nombre.get(), cargo.get(), salario.get(), id.get()
	try:
		cursor.execute('''UPDATE empleados SET nombre=?, cargo=?, salario=?
						WHERE id=?''', (datos))
		con.commit()
	except sqlite3.OperationalError as e:
		print(e)
		messagebox.showinfo('INFO', '¡ERROR INTERNO AL ACTUALIZAR LOS DATOS!')

def borrar():
	con = sqlite3.connect('empleados.db')
	cursor = con.cursor()
	
	if messagebox.askyesno('ADVERTENCIA', '¿Estás seguro que desea eliminar?'):
		try:
			cursor.execute('DELETE FROM empleados WHERE id=?', id.get())
		except sqlite3.OperationalError as e:
			print(e)
			messagebox.showinfo('INFO', '¡ERROR INTERNO AL ELIMINAR EL REGISTRO!')
# ================ FUNCIONES ==================
def salirAplicacion():
	'''función para salir de la aplicación'''
	respuesta = messagebox.askquestion('SALIR', '¿Estás seguro de salir de la aplicación?')
	if respuesta == 'yes':
		root.destroy()


def limpiarCampos():
	'''función que limpia las cajas de texto'''
	id.set('')
	nombre.set('')
	cargo.set('') 
	salario.set('') 

def mostrarDerechos():
	'''función para mostrar los derechos de autor en el menú Ayuda'''
	msg = 'APLICACIÓN CRUD\n'+\
		'VERSION 1.0\n'+\
		'HECHO CON PYTHON-TKINTER.8.X\n'+\
		'2022'
	messagebox.showinfo('ACERCA DE', msg)


# =============== INTERFAZ GRÁFICA ============
root = Tk()
root.title('App CRUD con sqlite3')
root.geometry('600x350')
# VARIABLES DE CONTROL
id = StringVar()
nombre = StringVar()
cargo = StringVar() 
salario = StringVar() 
# TABLA PARA MOSTRAR LOS REGISTRO
tree = ttk.Treeview(height=10, columns=('#0', '#1', '#2'))
tree.place(x=0, y=130)
# Ajustar el ancho de las columnas
tree.column('#0', width=100)
tree.column('#1', width=150)
tree.column('#2', width=150)
# Configurar los encabezados de las columnas
tree.heading('#0', text='ID', anchor='center')
tree.heading('#1', text='NOMBRE', anchor='w')
tree.heading('#2', text='CARGO', anchor='w')
tree.heading('#3', text='SALARIO', anchor='w')
# MENU
menubar = Menu(root)
menuInicio = Menu(menubar, tearoff=0)
menuInicio.add_command(label='Abrir', command=None)
menuInicio.add_command(label='Salir', command=salirAplicacion)
menuAyuda = Menu(menubar)
menuAyuda.add_command(label='Acerca de', command=mostrarDerechos)
menubar.add_cascade(label='Inicio', menu=menuInicio)
menubar.add_cascade(label='Ayuda', menu=menuAyuda)
root.config(menu=menubar)
# CAMPOS DE TEXTOS
eId = Entry(root, textvariable=id)

cajatextoNombre = Entry(root, textvariable=nombre, width=30)
cajatextoNombre.place(x=100, y=10)
cajatextoCargo = Entry(root, textvariable=cargo, width=30)
cajatextoCargo.place(x=100, y=40)
cajatextoSalario = Entry(root, textvariable=salario, width=30)
cajatextoSalario.place(x=100, y=70)
# ETIQUETAS PARA LOS CAMPOS
etiquetaId = Label(root, text='ID:')
etiquetaNombre = Label(root, text='Nombre:')
etiquetaNombre.place(x=40, y=10)
etiquetaCargo = Label(root, text='Cargo:')
etiquetaCargo.place(x=40, y=40)
etiquetaSalario = Label(root, text='Salario:')
etiquetaSalario.place(x=40, y=70)
# BOTONES PARA LAS OPERACIONES CRUD
frame = LabelFrame(root, text='Operaciones', labelanchor='', width=170, height=90)
frame.place(x=330, y=10)
botonMostrar = ttk.Button(frame, text='MOSTRAR', command=mostrar)
botonMostrar.place(x=5, y=5)
botonCrear = ttk.Button(frame, text='CREAR', command=crear)
botonCrear.place(x=85, y=5)
botonEditar = ttk.Button(frame, text='EDITAR')
botonEditar.place(x=5, y=40)
botonEliminar = ttk.Button(frame, text='ELIMINAR', command=None)
botonEliminar.place(x=85, y=40)

# INICIAMOS EL BUCLE INFINITO PARA MOSTRAR LA INTERFAZ GRÁFICA
root.mainloop()

