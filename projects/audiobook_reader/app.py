import tkinter as tk
import tkinter.ttk as ttk 
from infotips import CreateToolTip
from miner import PDFMiner
from tkinter import PhotoImage
from tkinter import filedialog
from tkinter import messagebox
import os


# Execute for HD windows, compatible with S.O windows
try:
    from ctypes import windll
    windll.shcore.SetProcesDpiAwareness(1)
    print(windll.shcore)
except:
    pass

BG_COLOR = '#042948'

class Application(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master=master)
		self.master = master
		self.grid()

		self.is_open=False
		self.speaker_on = False
		self.path = None
		self.author = None 
		self.name = None 
		self.current_page = 0 
		self.numPages = None

		self.draw_frames()
		self.draw_display_frame()
		self.draw_controls_frame()
		
		# Binding
		self.master.bind('<Left>', self.prev_page)
		self.master.bind('<Return>', self.search_page)
		self.master.bind('<Right>', self.next_page)

	def draw_frames(self, event=None):
		self.display_frame = tk.Frame(self, width=400, height=400,
										bg='gray18')
		self.display_frame.grid(row=0, column=0)
		self.display_frame.grid_propagate(0)


		self.controls_frame = tk.Frame(self, width=400, height=50,
										bg=BG_COLOR)

		self.controls_frame.grid(row=1, column=0)
		self.controls_frame.grid_propagate(0)


	def draw_display_frame(self):
		self.scrolly = tk.Scrollbar(self.display_frame, orient=tk.VERTICAL)
		self.scrolly.grid(row=0, column=1, sticky='ns')

		self.scrollx = tk.Scrollbar(self.display_frame, orient=tk.HORIZONTAL)
		self.scrollx.grid(row=1, column=0, sticky='we')

		self.output = tk.Canvas(self.display_frame, bg='gray18')
		self.output.configure(width=380, height=380, yscrollcommand=self.scrolly.set,
								xscrollcommand=self.scrollx.set)
		self.output.grid(row=0, column=0)

		self.scrolly.configure(command=self.output.yview)
		self.scrollx.configure(command=self.output.xview)

	def draw_controls_frame(self):

		self.open_file_btn = tk.Button(self.controls_frame, image=open_img,
											background=BG_COLOR, bd=0,
											activebackground=BG_COLOR,
											command=self.open_file)

		self.open_file_btn.grid(row=0, column=0, padx=10, pady=(4,0))
		self.open_file_btn = CreateToolTip(self.open_file_btn, 'Open a file')

		self.up_btn = tk.Button(self.controls_frame, image=up_img, 
									background=BG_COLOR, bd=0,
									activebackground=BG_COLOR,
									command=self.prev_page)
		self.up_btn.grid(row=0, column=1, padx=(70, 2))


		self.pagevar = tk.StringVar()
		self.entry = ttk.Entry(self.controls_frame, textvariable=self.pagevar, width=4)
		self.entry.grid(row=0, column=2)


		self.down_btn = tk.Button(self.controls_frame, image=down_img, 
									background=BG_COLOR, bd=0,
									activebackground=BG_COLOR,
									command=self.next_page)
		self.down_btn.grid(row=0, column=3, padx=(2, 5), pady=(4, 0))

		self.speaker_btn = tk.Button(self.controls_frame, image=speakoff_img, 
										background=BG_COLOR, bd=0,
										activebackground=BG_COLOR)
		self.speaker_btn.grid(row=0, column=4, pady=(4, 0))
		self.speaker_btn = CreateToolTip(self.speaker_btn, 'Press to play')

		self.page_label = tk.Label(self.controls_frame, text='',
										background=BG_COLOR, foreground='white',
										font=('Papyrus', 12, 'bold'))
		self.page_label.grid(row=0, column=5, pady=(4, 0))


	def open_file(self):

		files = [('PDF files', '*.pdf'),
				 ('All files', '*.*')]

		tmppath = filedialog.askopenfilename(
						title = "Select a PDF file",
						initialdir='./', 
						filetypes=files,
						parent=self.master) 
		if tmppath:
			self.path = tmppath
			filename = os.path.basename(self.path)
			self.miner = PDFMiner(self.path)
			data, numPages = self.miner.get_metadata()
			self.current_page = 0 

			if numPages:
				self.name = data.get('title', filename[:-4])
				self.author = data.get('author', None)
				self.numPages = numPages
				self.is_open = True
				self.display_page()
				print(self.name, self.author)

			else:
				self.is_open = False
				messagebox.showinfo('PDF AudioBook', 'Cannot read file')

	def display_page(self):
		if 0 <= self.current_page < self.numPages:
			self.img_file = self.miner.get_page(self.current_page)
			self.output.create_image(0, 0, anchor='nw', image=self.img_file)

			self.page_label['text'] = self.current_page + 1


			region = self.output.bbox(tk.ALL)
			self.output.configure(scrollregion=region)

	def prev_page(self, event=None):
		if self.is_open and self.current_page >= 0:
			self.current_page -= 1
			self.display_page()

	def next_page(self, event=None):
		if self.is_open and self.current_page <= self.numPages - 1:
			self.current_page += 1
			self.display_page()


	def search_page(self, event=None):
		if self.is_open:
			page = self.pagevar.get()
			if page != ' ':
				page = int(self.pagevar.get())

				if 0 < page < self.numPages + 1:
					if page == 0:
						page = 1
					else:
						page -= 1

					self.current_page = page 
					self.display_page()
					self.pagevar.set(' ')

def search_page(self, event=None):
	if not self.speaker_on:
		self.speaker_on = True 
		self.speak_btn





if __name__ == '__main__':
	root = tk.Tk()
	root.geometry("400x450")
	root.title("PDF Audiobook")
	# charge images
	open_img = PhotoImage(file='assets/png/bisel/open.png')
	up_img = PhotoImage(file='assets/png/bisel/up.png')
	down_img = PhotoImage(file='assets/png/bisel/down.png')
	speakon_img = PhotoImage(file='assets/png/bisel/speaker.png')
	speakoff_img = PhotoImage(file='assets/png/bisel/mute.png')
	


	root.resizable(0,0)
	app = Application(master=root)
	app.mainloop()


