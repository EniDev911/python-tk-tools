import tkinter as tk 


class Calculator:

	def __init__(self):
		self.window = tk.Tk()
		self.window.geometry('375x637')
		self.window.resizable(0,0)
		self.window.title('Calculadora')

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	calc = Calculator()
	calc.run()