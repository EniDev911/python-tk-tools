from tkinter import *
from tkinter import ttk
import tkinter.font as font
import os

root = Tk()
#root.geometry("500x420")
root.title("Calculator")
path_logo = r'assets\logo\logo.png'
# Comenta la siguiente línea si no tienes la ruta del logo
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path_logo))
root.resizable(0, 0)
root.config(padx=5)
root.config(pady=5)

# maneja el texto en la pantalla
input_ = StringVar()
myFont = font.Font(size=17)

# display
screen = Entry(root, text=input_,width=25,
                justify='right', font=myFont, bd=4)
screen.grid(row=0, columnspan=4,pady= (5, 15),ipady=5,sticky="w"+"e")

# Key matrix contiene todos los valores para el teclado
key_matrix = [["C", u"\u221A", "/", u"\u25C4"],
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "+"],
              ["!", 0, ".", "="]]

# Definimos un dictionary para manejar los botones que creemos
btn_dict = {}

# Variable para almacenar el resultado
ans_to_print = 0

# Defining the function for calculation
def Calculate(event):

    # invocamos al texto que tiene el boton
    button = event.widget.cget("text")

    # Referencia a los valores
    global key_matrix, input_, ans_to_print

    try:

        if button == u"\u221A": # Para la raíz cuadrada
            answer = float(input_.get())**(0.5)
            ans_to_print = str(answer)
            input_.set(str(answer))

        elif button.upper() == "C":  # Limpiar pantalla
            input_.set("")

        elif button == "!":  # Factorial
            def fact(n): return 1 if n == 0 else n*fact(n-1)
            input_.set(str(fact(int(input_.get()))))

        elif button == u"\u25C4":  # Backspace
            input_.set(input_.get()[:len(input_.get())-1])

        elif button == "=":  # Mostrando resultado
            # Usamos eval para calcular la expresión de la pantalla
            ans_to_print = str(eval(input_.get()))
            input_.set(ans_to_print)


        else:
            # Mostrando el digito presionado
            input_.set(input_.get()+str(button))

    except:
        # En caso de que la expresión sea invalidad
        input_.set("Wrong operation")


# Declarando un estilo para los botones
style = ttk.Style()
style.configure("TButton",font = myFont, width=3)
style.map("TButton", background = [('active', 'gray70')],
                     foreground = [('pressed', 'green')])

# Creando los botones con un loops

# Numero de fila que contiene los botones
for i in range(len(key_matrix)):
    # Numeros de columnas
    for j in range(len(key_matrix[i])):

        # Creando y añadiendo los botones al dictionary
        btn_dict["btn_"+str(key_matrix[i][j])] = ttk.Button(
          root, text=str(key_matrix[i][j]))

        # Posicionando los botones con grid()
        btn_dict["btn_"+str(key_matrix[i][j])].grid(
          row=i+1, column=j, ipady=5,sticky="w"+"e")

        # Asignando la acción a los botones al presionas el clic izquierdo
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', Calculate)

root.mainloop()
