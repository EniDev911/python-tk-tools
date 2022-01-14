from tkinter import *

root = Tk()

for r in range(0, 9):
    for c in range(0, 5):
        cell = Entry(root, width=10)
        cell.grid(row=r, column=c)
        cell.insert(0, '({}, {})'.format(r, c))

root.mainloop()