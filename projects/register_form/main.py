from tkinter import *


root = Tk()
width = 370
height = 380
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width/2) - (width/2)
y_coordinate = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d'%(width, height, round(x_coordinate), round(y_coordinate)))


def send():
    data = [entrys['entry_Name'].get(),
            entrys['entry_Phone'].get(),
            entrys['entry_Gender'].get(),
            entrys['entry_Address'].get(),
            entrys['entry_Email'].get(),
            entrys['entry_Country'].get()]
    print(data)

def clean():
    entrys['entry_Name'].delete(0,'end')
    entrys['entry_Phone'].delete(0,'end')
    entrys['entry_Gender'].delete(0,'end')
    entrys['entry_Address'].delete(0,'end')
    entrys['entry_Email'].delete(0,'end')
    entrys['entry_Country'].delete(0,'end')


# Fonts
font_s = ('Century gothic', 15)
font_m = ('Century gothic', 18)
font_xl = ('Segoe UI', 21)

# form
form = ['Name', 'Phone', 'Gender', 'Address', 'Email', 'Country']

frame = LabelFrame(root, text='Register', labelanchor='n', font=font_s)
frame.grid(row = 0, column = 0, pady=10, padx=15, columnspan = 2, sticky='w'+'e')

# Labels form
for i, row in enumerate(form):
    for y, t in enumerate(row.split(',')):
        lbls = Label(frame, text = row, font = font_s)
        lbls.grid(row = i, column=y, sticky='e', padx=(10,0))


# Entrys form
entrys = {}

for i, row in enumerate(form):
    for y, t in enumerate(row.split(','), start=1):
        entrys['entry_'+str(t)] = Entry(frame, font = font_s)
        entrys['entry_'+str(t)].grid(row = i, column=y, padx=(0, 20))

print(entrys.keys())


# Buttons
btn_send = Button(frame, text='S E N D', bg='green', fg='white', font=font_m, command=send)
btn_send.grid(row = 6, columnspan=2, column=0, sticky='w'+'e', pady=(15,0))

btn_clean = Button(frame, text='C L E A N', bg='cyan', fg='black', font=font_m, command=clean)
btn_clean.grid(row = 7, columnspan=2, column=0, sticky='w'+'e', pady=(0,0))

root.mainloop()