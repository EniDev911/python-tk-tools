try:
    from ctypes import windll
    windll.shcore.SetProcesDpiAwareness(1)
    print(windll.shcore)
except:
    pass

import tkinter as tk 
import os
import sys 


# Constant Fonts and size
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

# Constant Colors
OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:

	def __init__(self):
		# Window initital setting 
		self.window = tk.Tk()													    
		self.window.geometry('375x637')											    
		self.window.resizable(0,0)												    
		self.window.title('Calculator')
		self.icon_png = resource_path("./icon.png")
		self.window.tk.call('wm', 'iconphoto', self.window._w, tk.PhotoImage(file=self.icon_png))
		# ==============================
		self.total_expression = ""
		self.current_expression = "0"
		self.display_frame = self.create_display_frame()
		self.total_label, self.label = self.create_display_labels()
		self.digits = {
			7:(1,1), 8:(1,2), 9:(1,3),
			4:(2,1), 5:(2,2), 6:(2,3),
			1:(3,1), 2:(3,2), 3:(3,3),
			0:(4,2), '.': (4,1)
		}

		self.operations = {
			"/": "\u00F7", "*": "\u00D7", "-": "-",
			"+": "+"}
		self.buttons_frame = self.create_buttons_frame()
		for x in range(1, 5):
			self.buttons_frame.rowconfigure(x, weight=1)
			self.buttons_frame.columnconfigure(x, weight=1)

		# methods call
		self.create_digit_buttons()
		self.create_operator_buttons()
		self.create_special_buttons()
		self.create_square_button()
		self.create_sqrt_button()
		self.bind_keys()


	def create_special_buttons(self):
		self.create_clear_button()
		self.create_equals_button()

	def create_display_frame(self):
		frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
		frame.pack(expand=True, fill='both')
		return frame


	def create_digit_buttons(self):
		for digit, grid_value in self.digits.items():
			button = tk.Button(self.buttons_frame, text=str(digit),
								bg=WHITE, fg=LABEL_COLOR,
								font=DIGITS_FONT_STYLE, bd=0,
								command= lambda x=digit: self.add_to_expression(x))
			button.grid(row=grid_value[0], column=grid_value[1],
						sticky=tk.NSEW)


	def append_operator(self, operator):
		self.current_expression += operator
		self.total_expression += self.current_expression
		self.current_expression = ""
		self.update_label()
		self.update_total_label()

	def create_operator_buttons(self):
		i = 0
		for operator, symbol in self.operations.items():

			button = tk.Button(self.buttons_frame, text=symbol,
								bg=OFF_WHITE, fg=LABEL_COLOR,
								font=DEFAULT_FONT_STYLE, bd=0,
								command= lambda x = operator: self.append_operator(x))
			button.grid(row=i, column=4, sticky=tk.NSEW)
			i += 1

	def bind_keys(self):
		self.window.bind("<Return>", lambda e : self.evaluate())
		for key in self.digits:
			self.window.bind(str(key), lambda e, digit=key: self.add_to_expression(digit))

		for key in self.operations:
			self.window.bind(str(key), lambda e, operator=key: self.add_to_expression(operator))
			

	def evaluate(self, e=None):
		self.total_expression += self.current_expression
		self.update_total_label()
		try:
			self.current_expression = str(eval(self.total_expression))
			self.total_expression = ""

		except Exception as e:
			self.current_expression = "Error"
		
		finally:
			self.update_label()

	def clear(self):
		self.current_expression = "0"
		self.total_expression = ""
		self.update_label()
		self.update_total_label()

	
	def create_clear_button(self):
		button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE,
								fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
								borderwidth=0, command=self.clear)
		button.grid(row=0, column=1, sticky=tk.NSEW)


	def square(self):
		self.current_expression = str(eval(f"{self.current_expression}**2"))
		self.update_label()

	def sqrt(self):
		self.current_expression = str(eval(f"{self.current_expression}**0.5"))
		self.update_label()


	def create_square_button(self):
		button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE,
								fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
								borderwidth=0, command=self.square)
		button.grid(row=0, column=2, sticky=tk.NSEW)


	def create_sqrt_button(self):
		button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE,
								fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
								borderwidth=0, command=self.sqrt)
		button.grid(row=0, column=3, sticky=tk.NSEW)


	def create_equals_button(self):
		button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE,
								fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
								borderwidth=0, command=self.evaluate)
		button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

	def create_display_labels(self):

		total_label = tk.Label(self.display_frame, 
								text=self.total_expression,
								anchor=tk.E, bg=LIGHT_GRAY,
								fg=LABEL_COLOR, padx=24,
								font=SMALL_FONT_STYLE)
		total_label.pack(expand=True, fill='both')

		label = tk.Label(self.display_frame, 
								text=self.current_expression,
								anchor=tk.E, bg=LIGHT_GRAY,
								fg=LABEL_COLOR, padx=24,
								font=LARGE_FONT_STYLE)
		label.pack(expand=True, fill='both')

		return total_label, label


	def add_to_expression(self, value):

		if self.current_expression == "0":
			self.current_expression ="" 
			
		self.current_expression += str(value)
		self.update_label()


	def create_buttons_frame(self):
		frame = tk.Frame(self.window)
		frame.pack(expand=True, fill='both')
		return frame


	def update_total_label(self):
		expression = self.total_expression

		for operator, symbol in self.operations.items():
			expression = expression.replace(operator, f' {symbol} ')

		self.total_label.config(text=expression)

	def update_label(self):
		self.label.config(text=self.current_expression[:11])

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':

	def resource_path(relative_path):
	    """ Get absolute path to resource, works for dev and for PyInstaller """
	    try:
	        # PyInstaller creates a temp folder and stores path in _MEIPASS
	        base_path = sys._MEIPASS
	    except Exception:
	        base_path = os.path.abspath(".")

	    return os.path.join(base_path, relative_path)
	    
	# Run App.
	calc = Calculator()
	calc.run()

	#sentence = "+++++"
	#print(sentence.count("+"))