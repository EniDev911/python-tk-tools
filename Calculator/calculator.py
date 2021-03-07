from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(0, 0)
# root.iconbitmap('calculate.ico')
root.iconphoto(False, PhotoImage(file='calculate.png'))

# Display
screen = Entry(root, text = "0", font = ("Calibri 20"), justify = "right")
screen.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 5)
screen.configure(state = 'disabled')



# Functions 
i = 0
def clic_button(value):
	global i
	screen['state'] = 'normal'
	screen.insert(i, value)
	screen['state'] = 'disabled'
	i += 1

def clean_screen(btn):
	global i
	if btn == btn_clear['text']:
		screen.delete(0, END)
		i = 0
	elif btn == 'back':
		i -= 1
		screen.delete(i, END)
		

def operations():
	global i
	equation = screen.get()
	result = eval(equation)
	screen.delete(0, END)
	screen.insert(0, result)
	i = 0

# number buttons
btn_1 = Button(root, text = "1", bd = 3, width = 5, height = 2, command = lambda: clic_button(1))
btn_2 = Button(root, text = "2", bd = 3, width = 5, height = 2, command = lambda: clic_button(2))
btn_3 = Button(root, text = "3", bd = 3, width = 5, height = 2, command = lambda: clic_button(3))
btn_4 = Button(root, text = "4", bd = 3, width = 5, height = 2, command = lambda: clic_button(4))
btn_5 = Button(root, text = "5", bd = 3, width = 5, height = 2, command = lambda: clic_button(5))
btn_6 = Button(root, text = "6", bd = 3, width = 5, height = 2, command = lambda: clic_button(6))
btn_7 = Button(root, text = "7", bd = 3, width = 5, height = 2, command = lambda: clic_button(7))
btn_8 = Button(root, text = "8", bd = 3, width = 5, height = 2, command = lambda: clic_button(8))
btn_9 = Button(root, text = "9", bd = 3, width = 5, height = 2, command = lambda: clic_button(9))
btn_0 = Button(root, text = "0", bd = 3, width = 5, height = 2, command = lambda: clic_button(0))

# operation buttons 0
btn_clear = Button(root, text = "AC", bd= 3, width = 5, height = 2, command = lambda: clean_screen('AC')) # btn_clear['activebacgrnd'] = "#F50743" # Active when to press
btn_back = Button(root, text = "", width = 5, height = 2, command = lambda: clean_screen('back'))
btn_parenthesis_left = Button(root, text = "(", bd= 3, width = 5, height = 2)
btn_parenthesis_right = Button(root, text = ")", bd= 3, width = 5, height = 2)
btn_point = Button(root, text = ".", bd = 3, width = 5, height = 2) 

# math buttons
btn_div = Button(root, text = "÷", bd = 3, width = 5, height = 2)
btn_multi = Button(root, text = "*", bd = 3, width = 5, height = 2) 
btn_sum = Button(root, text = "÷", bd = 3, width = 5, height = 2)
btn_rest = Button(root, text = "-", bd = 3, width = 5, height = 2)
btn_result = Button(root, text = "=", bd = 3, width = 5, height = 2) 


# show widgets 
btn_clear.grid(row = 1, column = 0, padx = 5, pady = 5)
btn_back.grid(row = 5, column = 2, padx = 5, pady = 5)
btn_parenthesis_left.grid(row = 1, column = 1, padx = 5, pady = 5)
btn_parenthesis_right.grid(row = 1, column = 2, padx = 5, pady = 5)




# show widgets numeric buttons
btn_1.grid(row = 2, column = 0, padx = 4, pady = 5)
btn_2.grid(row = 2, column = 1, padx = 4, pady = 5)
btn_3.grid(row = 2, column = 2, padx = 4, pady = 5)
btn_4.grid(row = 3, column = 0, padx = 4, pady = 5)
btn_5.grid(row = 3, column = 1, padx = 4, pady = 5)
btn_6.grid(row = 3, column = 2, padx = 4, pady = 5)
btn_7.grid(row = 4, column = 0, padx = 4, pady = 5)
btn_8.grid(row = 4, column = 1, padx = 4, pady = 5)
btn_9.grid(row = 4, column = 2, padx = 4, pady = 5)
btn_0.grid(row = 5, column = 0, padx = 4, pady = 5, columnspan = 2, sticky = W + E)


# Show operations widget
btn_div.grid(row = 1, column = 3, padx = 5, pady = 5)
btn_multi.grid(row = 2, column = 3, padx = 5, pady = 5)
btn_sum.grid(row = 3, column = 3, padx = 5, pady = 5)
btn_rest.grid(row = 4, column = 3, padx = 5, pady = 5)
btn_result.grid(row = 5, column = 3, padx = 5, pady = 5)


# bind key with btn
# btn_1.bind('<Button-1>', clic_button(btn_1['text'].get()))


root.mainloop()