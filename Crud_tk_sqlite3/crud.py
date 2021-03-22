from tkinter import *
from tkinter import messagebox
import sqlite3



def connectionDB(): 
    # Create the database
    conn=sqlite3.connect("ContactDB.db")
    cursor=conn.cursor()
    try:

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Contacts (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME VARCHAR(50) NOT NULL,
            LAST_NAME VARCHAR(50) NOT NULL,
            PHONE VARCHAR(12) NOT NULL,
            EMAIL VARCHAR(50),
            ADDRESS VARCHAR(50))
            ''')
        messagebox.showinfo(title="DATABASE", message='Database created successfully')
    
    except sqlite3.OperationalError:
        messagebox.showwarning(title="Attention!",message="Database already exists")

    finally:
        return conn.closet()


def quitApplication():
    # Exit application    
    value=messagebox.askquestion(title="Exit",message="Do you want to exit the application?")
    if value=="yes":
        root.destroy()

def cleanBox():
    # Clean boxes
    myId.set("")
    myName.set("")
    myLast.set("")
    myPhone.set("")
    myEmail.set("")
    myAddress.set("")
    txt_fname.focus_set()

def validation():
    return len(txt_fname.get()) != 0 and len(txt_lname.get()) !=0  and len(txt_phone.get()) != 0

def help():
    # About
    message = """
    Developed by Enidev911
    enidev911@gmail.com
                """
    messagebox.showinfo(title='Contact', message=message)

def blockedbox():
    # block the boxes
    txt_fname['state'] = 'disabled'
    txt_lname['state'] = 'disabled'
    txt_phone['state'] = 'disabled'
    txt_address['state'] = 'disabled'
    txt_email['state'] = 'disabled'

def unblockedbox():
    #boxes unblocked
    txt_fname['state'] = 'normal'
    txt_lname['state'] = 'normal'
    txt_phone['state'] = 'normal'
    txt_address['state'] = 'normal'
    txt_email['state'] = 'normal'



def create():
    # Create new row
    with sqlite3.connect('ContactDB.db') as conn:
        cursor=conn.cursor()
        try:
            data=(myName.get(),myLast.get(),myPhone.get(),myEmail.get(),myAddress.get())
            if validation():
                cursor.execute("INSERT INTO Contacts VALUES(NULL,?,?,?,?,?)", data)
                conn.commit()
                messagebox.showinfo(title="Database",message="Record inserted successfuly")
                cleanBox()
            else:
                message='All fields are required'
                messagebox.showwarning(title="Database", message=message)

        except sqlite3.OperationalError as e:        
            messagebox.showwarning(title="Database", message='You have not created the database')    

def get_contact():

    with sqlite3.connect('ContactDB.db') as conn:
        cursor=conn.cursor()
        try:
            cursor.execute("SELECT * FROM Contacts")
            print(cursor.fetchall())
      

        except sqlite3.OperationalError as e:
            print(e)


def read(): 
    # recover a row 
    with sqlite3.connect('ContactDB.db') as conn:
        cursor=conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM Contacts WHERE ID={ myId.get() }")
    
            for contact in cursor.fetchall():
                myName.set(contact[1])
                myLast.set(contact[2])
                myPhone.set(contact[3])
                myEmail.set(contact[4])
                myAddress.set(contact[5])

        except sqlite3.OperationalError as e:
            messagebox.showwarning(title="Database", message='You have not created the database')


def update():
    # Update one row
    lbl_msg.grid(row=6, column=0)
    txt_id.grid(row=6, column=1, sticky='w')
    btn_cancel.grid(row=6, column=1, sticky='w', padx=45, ipadx=8)
    btn_watch.grid(row=6, column=1, sticky='e', ipadx=15)


    with sqlite3.connect('ContactDB.db') as conn:
        cursor=conn.cursor()
        data=(myName.get(),myLast.get(),myPhone.get(),myAddress.get())

        
        if validation():
            try:
                cursor.execute("""UPDATE Contacts SET 
                                    NAME=:name,
                                    LAST_NAME=:last_name,
                                    PHONE=:phone,
                                    EMAIL=:email,
                                    ADDRESS=:address 
                                    WHERE ID=:id""",
                                    {
                                    'name' : myName.get(),
                                    'last_name':myLast.get(),
                                    'phone': myPhone.get(),
                                    'email': myEmail.get(),
                                    'address': myAddress.get(),
                                    'id': myId.get()
                                    })
                conn.commit()
                messagebox.showinfo("Database","Record successfully updated")
                cleanBox()


            except sqlite3.OperationalError as e:
                messagebox.showwarning(title="Database", message=e)
            finally:
                lbl_msg.grid_forget()
                btn_watch.grid_forget()
                txt_id.grid_forget()
                btn_cancel.grid_forget()

        unblockedbox()


    
def delete():
    # Delete one row
    lbl_msg.grid(row=6, column=0)
    txt_id.grid(row=6, column=1, sticky='w')
    btn_watch.grid(row=6, column=1, sticky='e', ipadx=20)
    blockedbox()    
  

    if myId.get() != '':
        confirm = messagebox.askyesno(title='Confimation', message='Are you sure to delete this record?')

        try:
            if confirm:
                with sqlite3.connect("ContactDB.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute(f"DELETE FROM Contacts WHERE ID={ int(myId.get()) }")       
                    conn.commit()
                    messagebox.showinfo(title="Database",message="Record successfuly deleted")
                cleanBox()
            else:
                unblockedbox()
                cleanBox()

        except sqlite3.OperationalError as e:
            messagebox.showinfo(title="Database",message=e)

        finally:
            lbl_msg.grid_forget()
            btn_watch.grid_forget()
            txt_id.grid_forget()



# Create GUI
root=Tk()
root.title("Contact book")
root.iconbitmap('iconapp.ico')
root.geometry('450x300+550+250')
root.resizable(0,0)
root.config(padx=75)
root.config(pady=20)


## Variables 
myId=StringVar()
myName=StringVar()
myLast=StringVar()
myPhone=StringVar()
myEmail=StringVar()
myAddress=StringVar()


# Create the menu 
menubar=Menu(root)

# Database
database_menu=Menu(menubar, tearoff=0)
database_menu.add_command(label="Connect", command=connectionDB)
database_menu.add_command(label="Exit", command=quitApplication)
menubar.add_cascade(label="Database", menu=database_menu)

# Clean
clean_menu=Menu(menubar, tearoff=0)
clean_menu.add_command(label="Clean boxes", command=cleanBox)
menubar.add_cascade(label="Erase",menu=clean_menu)


# Operations
crud=Menu(menubar, tearoff=0)
crud.add_command(label="add", command=create)
crud.add_command(label="read", command=read)
crud.add_command(label="update", command=update)
crud.add_command(label="delete", command=delete)
menubar.add_cascade(label="Operations", menu=crud)

# Help
help_menu=Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=help)
menubar.add_cascade(label="Help", menu=help_menu)

# Assign the menu to main window
root.config(menu=menubar)

# Creating labels and entrys inside to frame
frame = LabelFrame(root, text='Contacts', labelanchor='n', padx=10, pady=5)
frame.grid(row=0, column=0, columnspan=2)

lbl_msg = Label(frame, text='Enter an ID: ', fg='red')
txt_id = Entry(frame, width=6, textvariable=myId)


lbl_fname = Label(frame, text='First Name: ')
lbl_fname.grid(row=1, column=0)

txt_fname = Entry(frame, width=30, textvariable=myName)
txt_fname.grid(row=1, column=1)
txt_fname.focus_set()

lbl_lname = Label(frame, text='Last Name: ')
lbl_lname.grid(row=2, column=0)

txt_lname = Entry(frame, width=30, textvariable=myLast)
txt_lname.grid(row=2, column=1)

# Phone
lbl_phone = Label(frame, text='Phone: ')
lbl_phone.grid(row=3, column=0, sticky='e')
txt_phone = Entry(frame, width=30, textvariable=myPhone)
txt_phone.grid(row=3, column=1)

# Email
lbl_email = Label(frame, text='Email: ')
lbl_email.grid(row=4, column=0, sticky='e')
txt_email = Entry(frame, width=30, textvariable=myEmail)
txt_email.grid(row=4, column=1)

# Adress
lbl_address = Label(frame, text='Address: ')
lbl_address.grid(row=5, column=0, sticky='e')
txt_address = Entry(frame, width=30, textvariable=myAddress)
txt_address.grid(row=5, column=1)



# Group Buttons

frame2 = LabelFrame(root, text='Operations', labelanchor='n', padx=10, pady=5)
frame2.grid(row=1, column=0, columnspan=2, sticky='w'+'e')

btn_create=Button(frame2, text="Create", cursor='hand2',command=create)
btn_create.grid(row=0, column=0, sticky='w'+'e', ipadx=40)

btn_read=Button(frame2, text="Read", padx=10, cursor='hand2',command=get_contact)
btn_read.grid(row=0, column=1, sticky='w'+'e', ipadx=35)

btn_update=Button(frame2, text="Update", cursor='hand2',command=update)
btn_update.grid(row=1, column=0, sticky='w'+'e')

btn_delete=Button(frame2, text="Delete", cursor='pirate',command=delete)
btn_delete.grid(row=1, column=1, sticky='w'+'e')

btn_watch = Button(frame, text='watch', command=read)
btn_cancel = Button(frame, text='cancel', command=cleanBox)


# List Contact 


 
root.mainloop()

