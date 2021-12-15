import tkinter
from tkinter import simpledialog

root = tkinter.Tk()
#root.iconbitmap(default="C:\\Users\\username\\random.ico")

dialog = simpledialog.askstring("INFO", "Nombre para el mp3?")
ext = ".mp3"

print(dialog+ext)

root.mainloop()