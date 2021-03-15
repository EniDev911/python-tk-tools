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





root.mainloop()