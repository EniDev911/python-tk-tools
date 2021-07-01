from tkinter import messagebox

ventana_info = messagebox.showinfo(title="Info", message="Esta es una ventana básica de información")
print(ventana_info)


ventana_error = messagebox.showerror(title="Error", message="Ha ocurrido un error en el sistema")
print(ventana_error)

ventana_advertencia = messagebox.showwarning(title="Advertencia", message="¡Haz desactivado el antivirus\ntu equipo está vulnerable!")
print(ventana_advertencia)
