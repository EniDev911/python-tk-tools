#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      enidev911
#
# Created:     10-08-2022
# Copyright:   (c) enidev911 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import Tk, Canvas, Frame, Label, Entry, Button, Listbox
from tkinter.messagebox import showinfo
import psycopg2


def connect_postgre():
    return psycopg2.connect(dbname="students", user="postgres", password="proPassword")

def save_new_student(name, age, address):
    conn = connect_postgre();
    if ((name and age and address != "") and (len(name)>5 and len(name) >1 and len(address)>5)):
        try:
            with conn as connect:
                cursor = connect.cursor()
                sql = "INSERT INTO student (name, age, address) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, age, address))
                conn.commit()
        except psycopg2.Error as err:
            print(err)
    else:
        showinfo("Info", "You must fill all fields")


def display_students():
    conn = connect_postgre();
    try:
        with conn as connect:
            cursor = connect.cursor()
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            result = cursor.fetchall()

            listbox = Listbox(frame, width=20, height=5)
            listbox.grid(row=10, columnspan=4, sticky="w"+"e")

            for row in result:
                listbox.insert(END, row)

    except psycopg2.Error as err:
            print(err)

display_students()

def main():

    root = Tk()
    root.title("Crud")
    canvas = Canvas(root, height=380, width=400)
    canvas.pack()

    frame = Frame()
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    label = Label(frame, text="Add A Student")
    label.grid(row=0, column=1)

    # name input
    label = Label(frame, text="Name")
    label.grid(row=1, column=0)
    e_name = Entry(frame)
    e_name.grid(row=1, column=1)

    # age
    label = Label(frame, text="Age")
    label.grid(row=2, column=0)
    e_age = Entry(frame)
    e_age.grid(row=2, column=1)

    # address
    label = Label(frame, text="Address")
    label.grid(row=3, column=0)
    e_address = Entry(frame)
    e_address.grid(row=3, column=1)


    button = Button(frame, text="Save",
                    command=lambda: save_new_student(
                                e_name.get(),
                                e_age.get(),
                                e_address.get()
                    ))
    button.grid(row=4, column=0, columnspan=3, sticky="w"+"e")
    root.mainloop()

# Canvas

if __name__ == '__main__':
    main()
