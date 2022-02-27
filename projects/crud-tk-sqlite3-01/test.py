#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk 

# Calcula los coste de viaje y cálculo posterior

class Application():
	"""docstring for Application"""
	def __init__(self):
		self.root = Tk()
		self.root.title('Validar reserva')

		# Variables de control
		self.num_via = IntVar(value=1)
		self.ida_vue = BooleanVar()
		self.clase = StringVar(value='t')
		self.km = IntVar(value=1)
		self.precio = DoubleVar(value=2000)
		self.total = DoubleVar(value=0.0)

		# Carga imagen para asociar al widget Label()
		#logo = PhotoImage(file='logo.png')

		#self.imagen = ttk.Label(self.root, image=logo, anchor="center")
		self.etiq1 = ttk.Label(self.root, text='Viajeros: ')
		