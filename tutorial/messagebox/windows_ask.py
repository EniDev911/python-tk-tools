from tkinter import messagebox

ventana_askquestion = messagebox.askquestion("Salir", "¿Estás seguro que quieres salir de la aplicación")
print(ventana_askquestion)

ventana_askyesno = messagebox.askyesno("Abrir", "¿Estás seguro de abrir esta página")
print(ventana_askyesno)

ventana_askokcancel = messagebox.askokcancel("Licencia", "¿Estás de acuerdo con los terminos de licencia?")
print(ventana_askokcancel)


ventana_askretrycancel = messagebox.askretrycancel("Conexión", "Tiempo de espera agotado, ¿Reintentar conexión?")
print(ventana_askretrycancel)

ventana_askyesnocancel = messagebox.askyesnocancel("Publicidad", "¿Quieres segui viendo esta publicidad?")
print(ventana_askyesnocancel)
