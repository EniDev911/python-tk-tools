#-------------------------------------------------------------------------------
# Name:        To-Do List App
# Purpose:
#
# Author:      Enidev
#-------------------------------------------------------------------------------
import tkinter
import tkinter.messagebox
import pickle
import os

root = tkinter.Tk()
width_window = 500
height_window = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_window/2)
y_coordinate = (screen_height/2) - (height_window/2)
root.geometry('%dx%d+%d+%d'%(width_window,height_window, x_coordinate, y_coordinate))
root.title("To-Do List by Enidev911")
#root.overrideredirect(1)


# Functions
def add_task(event=None):
    task = entry_task.get()
    if task != '':
        lst_task.insert('end', task)
        entry_task.delete(0, 'end')

    elif task == '':
        var_msg.set('You must enter a task')
        root.after(3000,lambda:var_msg.set(''))


def delete_task(event=None):
    task = lst_task.selection_get()
    option = tkinter.messagebox.askyesno('Warning!', f'Are you sure to delete a task {task}?')
    if option:
        lst_task.delete(tkinter.ACTIVE)
    entry_task.focus()



def save_task():
    tasks = lst_task.get(0, lst_task.size())
    pickle.dump(tasks, open('task.dat', 'wb'))

def load_task():
    tasks = pickle.load(open('task.dat', 'rb'))
    for task in tasks:
        lst_task.insert('end', task)


# Binding
root.bind('<Return>', add_task)
root.bind('<Delete>', delete_task)

# Fonts
font_s = ('Century gothic', 15)
font_m = ('Century gothic', 18)
font_xl = ('Segoe UI', 21)

# messages
var_msg = tkinter.StringVar()
message = tkinter.Label(textvariable=var_msg, font=font_s, fg='firebrick2')
message.pack()

# Create Gui
frame_task = tkinter.Frame(root, bd=2)
frame_task.pack(fill='both', expand=True)

scrollbar_tasks = tkinter.Scrollbar(frame_task)
scrollbar_tasks.pack(side='right', fill='y')


lst_task = tkinter.Listbox(frame_task, height=6, width=50, font=font_xl, justify='center',
                           selectbackground='steel blue', bg='snow')
lst_task.pack(fill='both', expand=True)

lst_task.config(yscrollcommand=scrollbar_tasks.set)

scrollbar_tasks.config(command=lst_task.yview)



entry_task = tkinter.Entry(font=font_s)
entry_task.pack(fill='x')
entry_task.focus()


# Buttons
btn_add_task = tkinter.Button(root, text='Add task', font=font_m,
                              bg = 'lime green', fg = 'white',
                              activebackground='green yellow',
                              command=add_task)
btn_add_task.pack(fill='x')


btn_delete_task = tkinter.Button(root, text='Delete task', font=font_m,
                              bg = 'firebrick2', fg = 'white',
                              activebackground='DarkOrange1',
                              command=delete_task)
btn_delete_task.pack(fill='x')



btn_save_task = tkinter.Button(root, text='Save task', font=font_m,
                              bg = 'gold', fg = 'white',
                              activebackground='DarkOrange1',
                              command=save_task)
btn_save_task.pack(fill='x')


btn_load_task = tkinter.Button(root, text='Load task', font=font_m,
                              bg = 'purple3', fg = 'white',
                              activebackground='purple4',
                              command=load_task)
btn_load_task.pack(fill='x')

btn_quit = tkinter.Button(root, text='Exit', font=font_m,
                              bg = 'darkred', fg = 'white',
                              activebackground='red',
                              command=root.destroy)
btn_quit.pack(fill='x')

root.mainloop()
