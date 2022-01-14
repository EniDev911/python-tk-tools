import tkinter as tk 
import tkinter.ttk as ttk
import os

app = tk.Tk()
app.title('My tool')
app.geometry('700x600+450+150')
app.minsize(600,500)

assets_dir = '../../assets/'

#app.tk.call('lappend', 'auto_path', 'awthemes-10.3.0')
#app.tk.call('package', 'require', 'awdark')

app.tk.eval("""
# base_theme_dir = path/download/theme/
set base_theme_dir ../../assets/themes_ttk/awthemes-10.3.0/


package ifneeded awthemes 10.3.0 \
	[list source [file join $base_theme_dir awthemes.tcl]]
package ifneeded colorutils 4.8 \
	[list source [file join $base_theme_dir colorutils.tcl]]
package ifneeded awdark 7.11 \
    [list source [file join $base_theme_dir awdark.tcl]]
package ifneeded awlight 7.9 \
    [list source [file join $base_theme_dir awlight.tcl]]
""")

app.tk.call('package', 'require', 'awdark')

s = ttk.Style()
#print(s.theme_names())

s.theme_use('awdark')
# Setting font
s.configure('TButton', font=('Century gothic', 25, 'italic'))
s.configure('Tools.TButton', font=('Century gothic', 35, 'italic'))


s.map('TButton', font=[('active', ('consolas', 35, 'bold'))],
				 foreground=[('active', '#2980B9')],
				 background=[('active', 'yellow')]
				 )

# print(s.layout('TButton'))

# Python
logo_python = tk.PhotoImage(file = assets_dir+'png/python(96px).png')
logo_python = logo_python.subsample(1)

btn_python = ttk.Button(text='Python Docs', image=logo_python, cursor='hand2')
btn_python.configure(compound = 'left')
btn_python.configure(command= lambda: os.system("start https://docs.python.org/3/"))
btn_python.pack(fill = 'both', expand=True)


ttk.Button(text = 'Open Python', image = logo_python, 
	      compound='left', cursor='hand2',
	      command = lambda: os.system('start cmd /k python')).pack(fill = 'both', expand = True,ipady=20)

ttk.Button(text = 'Online Practice', image = logo_python,
		  cursor='pencil' , compound='left',
		  command= lambda: os.system('start https://www.programiz.com/python-programming/online-compiler/')).pack(fill = 'both', expand = True,ipady=20)


app.mainloop() 