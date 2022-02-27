# -*- coding utf-8 -*-

from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
from pyzbar.pyzbar import decode, ZBarSymbol
import cv2
import pyautogui
import numpy as np 
import threading
from PIL import Image, ImageTk, ImageDraw
import os

class App:

	def __init__(self, font_video=0):
		self.active_camera = False
		self.info = []
		self.codelist = []
		self.appName = 'QR Code Reader'
		self.window = Tk()
		self.window.title(self.appName)
		self.window['bg'] = 'darkorange'
		self.font_video = font_video
		Label(self.window, text=self.appName, font=15,
				bg='blue', fg='white').pack(side=TOP, fill=BOTH)
		Button(self.window, text='S A V E', bg='light blue', command=self.save).pack(side=BOTTOM)

		self.display = scrolledtext.ScrollText(self.window, width=86,
												background='snow3', height=4,
												padx=10, pady=10, font=('Arial', 10))

		self.display.pack(side=BOTTOM)

		self.canvas = Canvas(self.window, bg='black', width=640, height=0)
		self.canvas.pack()

		Button(self.window, text='LOAD  FILE', bg='goldenrod2',
				activebackground='red', command=self.open_file).pack(side=LEFT)

		self.btnCamera=Button(self.window, text='INIT READ WITH CAM', width=30, bg='goldenrod2',
								activebackground='red', command=self.active_cam)
		self.btnCamera.pack(side=LEFT)
		Button(self.window, text='DETECTE IN SCREEN', width=29, bg='goldenrod2')

		self.window.mainloop()


	def save(self):
		if len(self.display.get('1.0', END))>1:
			document = filedialog.asksaveasfilename(initialdir='/',
								title='Save as', defaultextension='.txt')

			if document != '':
				save_file = open(document, 'w', encoding='utf-8')
				line = ''
				for c in str(self.display.get('1.0', END)):
					line = line+c 

				save_file.write(line)
				save_file.close()
				messagebox.showinfo("SAVED", "INFORMATION SAVE IN \'{}\'".format(document))


	def open_file(self):
		path = filedialog.askopenfilename(initialdir='/', title='SELECT FILE',
										filetypes=(("png files","*.png"), ("jpg files", "*.jpg")))

		if path != "":
			file = cv2.imread(path)
			self.info = decode(file)
			if self.info != []:
				self.display.delete('1.0', END)
				for i in self.info:
					self.display.insert(END, (i[0].decode('utf-8'))+'\n')

			else:
				messagebox.showwarning("FILE IS NOT VALID", "NO QR DETECTED")

	def screen_shot(self):
		pyautogui.screenshot("QRsearch_screenshot.jpg")
		file = cv2.imread("QRsearch_screenshot.jpg")

		self.info = decode(file)

		if self.info != []:
			self.display.delete('1.0', END)
			for i in self.info:
				self.display.insert(END, (i[0].decode('utf-8'))+'\n')
		else:
			messagebox.showwarning("QR NOT FOUND", "QR IS NOT DETECTED")
		os.remove('QRsearch_screenshot.jpg')

	def visor(self):
		ret, frame=self.get_frame()
		if ret:
			self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
			self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
			self.window.after(15, self.visor)

	def active_cam(self):
		if self.active_camera == False:
			self.active_camera = True
			self.VideoCapture()
			self.visor()

		else:
			self.active_camera = False
			self.codelist = []
			self.btnCamera.configure(text="START READ WITH CAM")
			self.vid.release()
			self.canvas.delete('all')
			self.canvas.configure(height=0)

	def capta(self, frm):
		self.info = decode(frm)
		cv2.putText(frm, "SHOW THE CODE INSIDE OF THE CAM", (84, 37), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 50, 255), 2)
		if self.info != []:
			self.display.delete('')

	def 



