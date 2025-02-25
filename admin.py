from tkinter import *
from tkinter.ttk import *
import mysql.connector as ms
from tkinter.messagebox import showinfo
from datetime import date

def add_student_rec():  #adding student record to the database
    def Submit():
        con=ms.connect(host='localhost',user='root',passwd='*****',database='^^^^^')
        cursor=con.cursor()
        user_name=name_var.get()
        init=init_var.get()
        roll_no=roll_var.get()
        user_id=(init+user_name)[0:5]   
        user_pwd=user_name[0:3]+'@2023'
        record=(user_id,user_name,'student',user_pwd,roll_no)
        cursor.execute("insert into user_details values {};".format(record))
        cursor.execute("commit;")
        showinfo(title='Notification', message='New Student Added!')
        
    root=Toplevel()
    root.geometry("1500x1600")
    fr1=Frame(root)
    name_var=StringVar()
    init_var=StringVar()
    roll_var=IntVar()
    lb=Label(fr1,text="Name of the student")
    lb1=Label(fr1,text="Initials of Student")
    lb2=Label(fr1,text="Roll Number of Student")
    sty=Style() #create a style_class variable
    sty.configure("TLabel",font=("Papyrus",20,'bold'))  #set a customised style for label class
    ent1=Entry(fr1,textvariable=name_var,font=('Papyrus',20))
    ent2=Entry(fr1,textvariable=init_var,font=('Papyrus',20))
    ent3=Entry(fr1,textvariable=roll_var,font=('Papyrus',20))
    sub=Button(fr1,text="Submit",command=Submit)
    bstyle=Style()
    bstyle.configure("TButton",font=('Papyrus',18),foreground='purple') #set a customised style for button class
    lb.grid(row=0,column=0)
    lb1.grid(row=1,column=0)
    lb2.grid(row=2,column=0)
    ent1.grid(row=0,column=1)
    ent2.grid(row=1,column=1)
    ent3.grid(row=2,column=1)
    sub.grid(row=3,column=1)
    fr1.place(relx=0.5,rely=0.5,anchor='c')
    root.mainloop()

def add_books():
    def go():
        db=ms.connect(host='localhost',user='root',passwd='*****',database='^^^^^')
        co=db.cursor()
        bname=book_var.get()
        aname=auth_var.get()
        q="select * from book_master where bookName ='{}';".format(bname)#search for book
        co.execute(q)
        rows=co.fetchall()
        found=0
        for i in rows:
            if i[1]==bname:                  #search if book exists
                showinfo(title='Notification', message='Book already exists!')
                found=1
        if found==0:            
            co.execute("select max(bookid) from book_master;")
            bid=(co.fetchone()[0])+1
            q1="select * from author_master where AuthorName='{}';".format(aname)
            co.execute(q1)
            r=co.fetchall()
            if len(r)>0:
                r=r[0]
                q3="insert into book_master values({},'{}',{},'y')".format(bid,bname,r[0])
                co.execute(q3)
                co.execute("commit")
                showinfo(title='Notification', message='Book added!')
            elif r==[]:
                co.execute("select MAX(authorid) from author_master")
                authid=(co.fetchone()[0])+1
                q3="insert into author_master values ({},'{}')".format(authid,aname)
                q4="insert into book_master values({},'{}',{},'y')".format(bid,bname,authid)
                co.execute(q3)
                co.execute(q4)
                co.execute("commit")
                showinfo(title='Notification', message='Book added!')
    root=Toplevel()
    root.geometry("1500x1600")
    book_var=StringVar()
    auth_var=StringVar()
    fr1=Frame(root)
    blabel=Label(fr1,text='Book Name:')
    alabel=Label(fr1,text='Author Name:')
    lstyle=Style()
    lstyle.configure('TLabel',font=('Papyrus',20,'bold'))
    bent=Entry(fr1,textvariable=book_var,font=('Papyrus',20))
    aent=Entry(fr1,textvariable=auth_var,font=('Papyrus',20))
    go=Button(fr1,text='Go',command=go)
    bstyle=Style()
    bstyle.configure('TButton',font=('Papyrus',18,'bold'),foreground='purple')
    blabel.grid(row=0,column=0)
    alabel.grid(row=1,column=0)
    bent.grid(row=0,column=1)
    aent.grid(row=1,column=1)
    go.grid(row=3,column=1)
    fr1.place(relx=0.5,rely=0.5,anchor='c')
    root.mainloop()

def view_overdue():
    root=Toplevel()
    root.geometry("1500x1600")
    title_frame=Frame(root)
    content_frame=Frame(root)
    lstyle=Style()
    lstyle.configure("TLabel",font=("Papyrus",20,'bold'))
    con = ms.connect(host='localhost',user='root',passwd='*****',database='^^^^^')
    cur = con.cursor()
    cur.execute("select u.user_name,b.bookName from user_details u, book_master b,transaction t where u.user_id=t.user_id and b.bookID=t.book_id and '{}'>t.expected_return_date and actual_return_date is null;".format(str(date.today())))
    data=cur.fetchall()
    title_lb=Label(title_frame,text="List of Overdue Books")
    name_frame=Frame(root)
    book_frame=Frame(root)
    for i in data:
        lbn=Label(name_frame,text=str(i[0]))
        lbb=Label(book_frame,text=str(i[1]))
        lbn.pack()
        lbb.pack()
    title_frame.pack()
    title_lb.pack()
    name_frame.place(relx=0.3,rely=0.1)
    book_frame.place(relx=0.5,rely=0.1)
    root.mainloop()









