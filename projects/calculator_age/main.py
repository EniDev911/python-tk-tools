from tkinter import *
import datetime
from tkinter import messagebox


root = Tk()
root.title("Age Calculator")
root.geometry("350x295")
root.resizable(0,0)
root.eval('tk::PlaceWindow . center')

# frame background
j = 0
r = 0
for i in range(100):
    c = str(10439+r)
    Frame(root, width=10, height=500, bg=f"#1{c}").place(x=j, y=0)
    j += 10
    r += 1

def calculate_age(event=None):
    try: 
        b_day = birth_day_entry.get()
        b_month = birth_month_entry.get()
        b_year = birth_year_entry.get()

        if b_year == '':
            messagebox.showinfo(master=root, title="Required", message="The year is required")

        elif b_month == '':
            messagebox.showinfo(master=root, title="Required", message="The month is required")

        elif b_day == '':
            messagebox.showinfo(master=root, title="Required", message="The day is required")
  
        else:
            today = datetime.date.today()
            b=str(today)
            year = b[0]+b[1]+b[2]+b[3]
            age = int(year)-int(b_year)
            month = b[5]+b[6]

     
            if int(month)>int(b_month):
                age2 = int(month)-int(b_month)
            elif int(month)<int(b_month):
                age = int(year)-(int(b_year)+1)
                age2 = 12-((int(month)-int(b_month))*-1)
            else:
                age2 = 0
            total_months=age*12+age2

            txt1 = Text(height=3, width=40, border=0)
            txt1.place(x=30, y=220)
            txt1.configure(font=("Helvetica", 10))
            txt1.insert(END,"A G E :  {} Y E A R S  {} M O N T H S !".format((age),(age2)))

            txt2 = Text(height=1, width=40, border=0)
            txt2.place(x=30, y=250)
            txt2.configure(font=("Helvetica", 10, "bold"), foreground="gray10")
            txt2.insert(END,"I N  M O N T H S :  {} M O N T H S !".format(total_months))

    except:
        messagebox.showerror(master=root, title="Error", message="ERROR")


Frame(root, width =320,height=180, bg='white').place(x=15, y=15)
Frame(root, width =320,height=35, bg='#e8e8e8').place(x=15, y=15)
Frame(root, width =320,height=70, bg='white').place(x=15, y=210)
Label(root, text= 'E N T E R  D A T E  O F  B I R T H', bg= '#e8e8e8').place(x=80, y=22)

button1 = Button(root, width=15, bg='#004392', text='C A L C U L A T E',
                    fg='white', font=('Helvetica', 11, 'bold'),
                    cursor='hand2',  command=calculate_age, border=0)
button1.place(x=100, y=145)


# Label YEAR
Label(root, text="Y E A R", bg ="white").place(x=65, y=67)
birth_year_entry = Entry(root, border =0, bg="#e8e8e8", width = 5, justify="center")
birth_year_entry.configure(font = ('Helvetica', 17, 'bold'))
birth_year_entry.focus()
birth_year_entry.place(x=50, y=125-35)

# Label MONTH
Label(root, text="M O N T H", bg ="white").place(x=150, y=67)
birth_month_entry = Entry(root, border =0, bg="#e8e8e8", width = 5, justify="center")
birth_month_entry.configure(font = ('Helvetica', 15, 'bold'))
birth_month_entry.place(x=150, y=90)

# Label DAY
Label(root, text="D A Y", bg ="white").place(x=257, y=67)
birth_day_entry = Entry(root, border =0, bg="#e8e8e8", width = 5, justify="center")
birth_day_entry.configure(font = ('Helvetica', 15, 'bold'))
birth_day_entry.place(x=250, y=90)


# Events BIND
root.bind('<Return>', calculate_age)
root.mainloop()
