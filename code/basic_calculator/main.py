#----------------------------------------------------------------------------------
#          Name: Basic_calculator - main.py
#        
#         Autor: Marco Contreras
#
# Código fuente: https://github.com/EniDev911/PythonTk/tree/master/basic_calculator
#       Support: https://www.buymeacoffee.com/9111592
#       Licence: <MIT>
#----------------------------------------------------------------------------------


# Execute for HD windows, compatible with S.O windows
try:
    from ctypes import windll
    windll.shcore.SetProcesDpiAwareness(1)
    print(windll.shcore)
except:
    pass

from tkinter import *
from tkinter import ttk
import tkinter.font as font
import os
import sys


root = Tk()
root.title("Calculator")
path_logo = './icon.png'
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=path_logo))
root.resizable(0, 0)
root.config(padx=5)
root.config(pady=5)


# text input
input_ = StringVar(value="0")
myFont = font.Font(size=17)

# display
screen = Entry(root, text=input_,width=25,
                justify='right', font=myFont, bd=4)
screen.grid(row=0, columnspan=4,pady= (5, 15),ipady=5,sticky="w"+"e")

# calculator keyboard settings
key_matrix = [["C", u"\u221A", "/", u"\u25C4"],
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "+"],
              ["!", "0", ".", "="]]

#  define a dictionary to add the widgets
btn_dict = {}

# Variable to store the result
ans_to_print = 0

# Defining the function for calculation
def calculate(event=None):
    button = event.widget.cget("text")


    # Referencia a los valores
    global key_matrix, input_, ans_to_print

    try:

        if button == u"\u221A": # Para la raíz cuadrada
            answer = float(input_.get())**(0.5)
            ans_to_print = str(answer)
            input_.set(str(answer)[:11])

        elif button.upper() == "C":  # Limpiar pantalla
            input_.set("0")

        elif button == "!":  # Factorial
            def fact(n): return 1 if n == 0 else n*fact(n-1)
            input_.set(str(fact(int(input_.get()))))

        elif button == u"\u25C4":  # Backspace
            input_.set(input_.get()[:len(input_.get())-1])

        elif button == "=":  # Mostrando resultado
            ans_to_print = str(eval(input_.get()))
            input_.set(ans_to_print)


        else:
            # Mostrando el digito presionado
            if button:
                if input_.get() == "0":
                    input_.set("")                
                input_.set(input_.get()+str(button))                

            #input_.set(input_.get()+str(event))

    except:
        # In case the expression is invalid
        input_.set("Wrong operation")


# Style to buttons
style = ttk.Style()
style.configure("TButton",font = myFont, width=5)
style.map("TButton", background = [('active', 'gray70')],
                     foreground = [('pressed', 'green')])


# Creando los botones
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
        btn_dict["btn_"+str(key_matrix[i][j])].bind('<Button-1>', calculate)

root.mainloop()
