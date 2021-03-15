from tkinter import * 

root = Tk()
root.title('Tkinter-Meme')


# Define the images
bg = PhotoImage(file="images/01.png")

# Get the image size
w = bg.width()
h = bg.height()


# make the root window the size of the image
root.geometry("%dx%d" % (w,h))


# Create to label for background 
lbl_img = Label(root, image=bg)
lbl_img.place(x=0, y=0, relheight=1, relwidth=1)

# Add text for funny with canvas 
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas  
my_canvas.create_image(0, 0, image=bg, anchor="nw")
my_canvas.create_text(250, 250, text="Porque yo lo valgo", font=("consolas", 20),
                        fill="white")


## Add some buttons 
btn_01 = Button(root, text = "Start")
btn_02 = Button(root, text = "Reset")
btn_03 = Button(root, text = "Exit")


btn01_window = my_canvas.create_window(10, 10, anchor="nw", window=btn_01)
btn02_window = my_canvas.create_window(70, 10, anchor="nw", window=btn_02)
btn03_window = my_canvas.create_window(140, 10, anchor="nw", window=btn_03)


root.mainloop()