from tkinter import *

root = Tk()

frame = Frame(root)
frame.grid()

btn = Button(frame, text="Ver")
btn.grid()

#print(dir(btn))
#print(set(btn.configure().keys()) - set(frame.configure().keys()))


root.mainloop()