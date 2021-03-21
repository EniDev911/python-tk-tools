import tkinter as tk
import time


root = tk.Tk()
root.geometry("400x150+450+300")
root.resizable(0, 0)
root.title('Digital Clock')


# Time Label
lbl_current_time = tk.Label(root, text = '', font=('Consolas', 60))
lbl_current_time['fg'] = '#ffffff'
lbl_current_time['bg'] = '#443355'
lbl_current_time.pack(fill='both', expand=True)

# Update time
def update_clock():
	time_now = time.strftime('%H:%M:%S')

	if lbl_current_time['text'] != time_now:
		lbl_current_time['text'] = time_now
	root.after(1000, update_clock)

update_clock()
root.mainloop()
