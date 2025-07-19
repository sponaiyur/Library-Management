from tkinter import *
from tkinter.ttk import *
import student
import admin
import mysql.connector as ms

root = Tk()     #root window
root.title("Library") 
root.geometry("1500x1600")  #pixel size
frame1=Frame(root)
title= Label(frame1, text = "Welcome to the Library!")
lbstyle=Style()
lbstyle.configure('TLabel',font=("Papyrus",30,"bold"))

def welcome_page(name,password,cur_inst):   #second toplevel,welcome page of the library system customised for student and admin
    welcome=Toplevel(root)
    welcome.geometry('1550x1650')
    frm=Frame(welcome)
    frm.place(relx=0.5,rely=0.5,anchor='c') 
    cur_inst.execute("select user_name from user_details where user_id='{}' and user_pwd='{}';".format(name,password))
    data=cur_inst.fetchone()[0]
    text=("Welcome,{}!".format(data))
    title=Label(frm, text = text, font =('Algerian', 25))
    title_1=Label(frm,text="What would you like to do today?",font=('Papyrus',20))

    cur_inst.execute("select user_type from user_details where user_id='{}' and user_pwd='{}';".format(name,password))
    typ=cur_inst.fetchone()[0]
    if "student" in typ:
        ph_borrow=PhotoImage(file=r"images\borrow_book.png")
        borrow = Button(frm, text = 'Borrow A Book',image=ph_borrow,compound= 'top',command = lambda: student.borrowbook(name))
        ph_return=PhotoImage(file=r'images\return_book.png')
        returnBook = Button(frm, text = 'Return A Book',image=ph_return,compound= 'top',command = lambda: student.return_book(name))
        title.pack()
        title_1.pack()
        borrow.pack(side='left',padx=5,pady=5)
        returnBook.pack(side='right',padx=5,pady=5)
    elif "admin" in typ:
        ph_addstud=PhotoImage(file=r"images\add_stud.png")
        add_stud = Button(frm, text = 'Add A Student',image=ph_addstud,compound= 'top',command = admin.add_student_rec)
        ph_addbook=PhotoImage(file=r"images\add_book.png")
        add_book=Button(frm,text="Add a book",image=ph_addbook,compound='top',command =admin.add_books)
        ph_overdue=PhotoImage(file=r'images\over_due.png')
        overdue=Button(frm,text="View Overdue Books",image=ph_overdue,compound='top',command =admin.view_overdue)
        title.pack()
        title_1.pack()
        add_stud.pack(side='left',padx=5,pady=5)
        add_book.pack(side='left',padx=5,pady=5)
        overdue.pack(side='left',padx=5,pady=5)
    welcome.mainloop()
        

def login_page():   #login page, first toplevel
    def submit():
        login.destroy()
        cur=ms.connect(host='localhost',user='root',passwd='*****',database='^^^^^')
        cursor=cur.cursor()
        name=name_var.get()
        password=passw_var.get()
        welcome_page(name,password,cursor)
        
    login = Toplevel(root)
    login.title("Login")
    login.geometry("1500x1600")
    frame1=Frame(login)
    frame2=Frame(login)
    frame1.place(relx=0.5,rely=0.3,anchor='c')
    frame2.place(relx=0.5,rely=0.5,anchor='c')
    name_var=StringVar() 
    passw_var=StringVar()
    label = Label(frame1,text = "Login To proceed")
    name_label =Label(frame2, text = 'UserID:', font=('Papyrus',16, 'bold'))
    name_entry =Entry(frame2,textvariable = name_var, font=('Papyrus',16))
    passw_label =Label(frame2, text = 'Password:', font = ('Papyrus',16,'bold'))
    passw_entry=Entry(frame2, textvariable = passw_var, font = ('Papyrus',16), show = '*')
    sub_btn=Button(frame2,text = 'Submit', command = submit)
    label.pack()
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
    login.mainloop()

button = Button(frame1, text = "LOGIN!",command = login_page)
btstyle=Style()
btstyle.configure("TButton",font=("Papyrus",20,"bold"),foreground="purple")
frame1.place(relx=0.5,rely=0.5,anchor='c')
title.pack()
button.pack()
root.mainloop()
