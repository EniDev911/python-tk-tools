import tkinter as tk
from tkinter import ttk
import time
import os 
from tkinter.font import Font
from tkinter import font


root = tk.Tk()
root.resizable(0, 0)
root.title('Digital Clock')
root.configure(bg = '#443355')
root.configure(pady = 10)

# Functions
def changue_font(event):
	b.configure(family= combo.get())
    #lbl_current_time.configure(font = (combo.get(),60))

# Style
s = ttk.Style()
s.configure("TLabel", font=('consolas', 60))
s.configure("TCombobox", font=('consolas', 30))


b = Font(family='Arial', size=60, weight='bold', slant='italic', underline=1, overstrike=0)

# Time Label
lbl_current_time = ttk.Label(root, text = '', cursor='hand2')
lbl_current_time['foreground'] = '#ffffff'
lbl_current_time['background'] = '#443355'
lbl_current_time['font'] = b
lbl_current_time.pack(fill='both', expand=True, padx=20)

# Font system
#f = os.listdir(os.getenv('SystemRoot'))
#C:\Windows\Fonts
#font_root = os.getenv('SystemRoot')
#fonts_system = os.path.join(font_root, 'Fonts')
#list_font_system = os.listdir(fonts_system)
#for f in os.listdir(fonts_system):
#	print(f)

# 2da option
f = font.families()
#b = Font(family='Arial', size=20, weight='bold', slant='italic', underline=1, overstrike=0)
#print(f)
print(b.configure().keys())


# Combobox Select font
fonts = ['Helvetica', 'Consolas', 'Lucida Console', 'Segoe script',
          'Corbel', 'Gabriola', 'Ink Free', 'Segoe UI Emoji', 'Terminal',
           'Century Gothic']

combo = ttk.Combobox(root, values=f, state='readonly')
combo.current(1)
combo.bind("<<ComboboxSelected>>",changue_font)
combo.pack(ipadx=30)

# Update time
def update_clock():
	time_now = time.strftime('%H:%M:%S')

	if lbl_current_time['text'] != time_now:
		lbl_current_time['text'] = time_now
	root.after(1000, update_clock)

update_clock()
root.mainloop()