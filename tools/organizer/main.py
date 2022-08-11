import tkinter as tk
from tkinter.simpledialog import askstring
import tkinter.ttk as ttk
import os
from organizer import organizer
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.simpledialog import askstring
from makeproject import makeVoidProject

# Execute for HD windows, compatible with S.O windows
try:
    from ctypes import windll
    windll.shcore.SetProcesDpiAwareness(1)
    print(windll.shcore)
except:
    pass
  
app = tk.Tk()
app.title('My tool')
width_window = 400
height_window = 400
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_window/2)
y_coordinate = (screen_height/2) - (height_window/2)
app.geometry('%dx%d+%d+%d'%(width_window,height_window, x_coordinate, y_coordinate))
app.minsize(400,400)

assets_dir = '../../assets/'

#app.tk.call('lappend', 'auto_path', 'awthemes-10.3.0')
#app.tk.call('package', 'require', 'awdark')

app.tk.eval("""
# base_theme_dir = path/download/theme/
set base_theme_dir [pwd]/awthemes-10.3.0/


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

s.theme_use('awdark')
# Setting font
s.configure('TButton', font=('Century gothic', 25, 'italic'))
s.configure('Tools.TButton', font=('Century gothic', 35, 'italic'))


s.map('TButton', font=[('active', ('consolas', 28, 'bold'))],
				 foreground=[('active', '#f1f1c1')],
				 background=[('active', '#464656')]
				 )


def chageOnHover(button, imageHover, imageLeave):
  button.bind('<Enter>', func=lambda e: button.configure(
        image=imageHover))
  button.bind("<Leave>", func=lambda e: button.configure(
        image=imageLeave))


# images assets
folder_img = tk.PhotoImage(file = 'assets/kawaii_folder.png')
folder_img = folder_img.subsample(1)

folders_img = tk.PhotoImage(file = 'assets/folders.png')
folders_img = folders_img.subsample(1)

card_index_img = tk.PhotoImage(file= 'assets/card_index.png')
card_index_img = card_index_img.subsample(1)

close_red_img = tk.PhotoImage(file= 'assets/cancel_red.png')
close_red_img = close_red_img.subsample(1)

close_gray_img = tk.PhotoImage(file= 'assets/cancel_gray.png')
close_gray_img = close_gray_img.subsample(1)

web_project_void_img = tk.PhotoImage(file='assets/tree-web-void.png')
web_project_void_img = web_project_void_img.subsample(1)

web_project_void_hover_img = tk.PhotoImage(file='assets/tree-web-void-hover.png')
web_project_void_hover_img = web_project_void_hover_img.subsample(1)

def getDirectory():
  return askdirectory()

def newProject():
  new_window = tk.Toplevel(app)
  new_window.overrideredirect(1)
  app.tk.eval(f'tk::PlaceWindow {str(new_window)} center')
  btn_web = ttk.Button(new_window, image=web_project_void_img, command=lambda: new_window.destroy())
  btn_web.grid(row=1, column=0)
  name_project = lambda: askstring(new_window, "Nombre para el proyecto nuevo")
  btn_project_web = ttk.Button(new_window, 
    image=web_project_void_img,
    text="Proyecto web vacio",
    command=lambda: makeVoidProject(getDirectory(), name_project()))
  btn_project_web.grid(row=1, column=1) 
  chageOnHover(btn_project_web, web_project_void_hover_img, web_project_void_img)
  return new_window


btn_organizer = ttk.Button(text='Organizar', image=folders_img, 
            cursor='hand2', compound = 'left', 
            command= lambda: organizer(getDirectory()))
btn_organizer.pack(fill = 'both', expand=True)

chageOnHover(btn_organizer, folder_img, folders_img)


btn_project = ttk.Button(text = 'Nuevo Proyecto', image = card_index_img,
	      compound='left', cursor='hand2',
	      command = newProject)
btn_project.pack(fill = 'both', expand = True,ipady=20)

btn_close = ttk.Button(image=close_gray_img,
		  cursor='hand2' , 
		  command= lambda:app.destroy())
      
btn_close.pack(fill = 'both', expand = True,ipady=20)
chageOnHover(btn_close, close_red_img, close_gray_img)



app.mainloop()