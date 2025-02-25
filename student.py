from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
import mysql.connector as ms
from datetime import date,timedelta

def return_book(name):
    cur=ms.connect(host='localhost',user='root',passwd='*****',database='^^^^^')
    cursor=cur.cursor()

    Return= Tk()
    Return.geometry('1500x1600')
    fr1=Frame(Return)
    fr1.pack(fill=BOTH,expand=True)

    columns = ('user_name','book_borrowed','borrowed_date','return_date')  # define columns
    tree = Treeview(fr1, columns=columns, show='headings')  #create the treeview

    tree.heading('user_name', text='User Name') # define headings
    tree.heading('book_borrowed', text='Book Borrowed')
    tree.heading('borrowed_date', text='Borrowed Date')
    tree.heading('return_date', text='Expected Return Date')

    cursor.execute('''select u.user_name,b.bookName,t.borrowed_date,t.expected_return_date
                   from user_details u, book_master b, transaction t where u.user_id=t.user_id and b.bookID=t.book_id and actual_return_date is null;''') 
    data=cursor.fetchall()
    cursor.execute("Select user_name from user_details where user_id='{}'".format(name))
    username=cursor.fetchone()[0]
    data1=[]
    for i in data:
        if username in i:
            data1.append(i) #data

    for i in data1:  
        tree.insert('', END, values=i)  # add data to the treeview


    def item_selected(event):   #function to be executed when a row is selected
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record=item['values']
            cursor.execute('''select bookid from book_master where bookname="{}" '''.format(record[1]))
            bkid=cursor.fetchone()[0]
            query="update transaction set actual_return_date = '{}' where user_id='{}' and book_id='{}'".format(date.today(),name,bkid)
            cursor.execute(query)
            cursor.execute("update book_master set availability = 'y' where bookid={}".format(bkid))
            cursor.execute("commit;")
            # show a message
            x=showinfo(title='Notification', message='Book Successfully Returned!')
            if bool(x):
                Return.destroy()
    tree.bind('<<TreeviewSelect>>', item_selected)  #binds the tree selection with the item_selected function
    tree.pack(fill="both", expand=1)    #fill the treeview in the entire window
    Return.mainloop()
    

def borrowbook(name):
    borrow_date=str(date.today())
    return_date=str(date.today()+timedelta(7))
    cur=ms.connect(host='localhost',user='root',passwd='*****',database='^^^^^')
    cursor=cur.cursor()

    borrow= Tk()
    borrow.geometry('1500x1600')
    fr1=Frame(borrow)
    fr1.pack(fill=BOTH,expand=True)

    columns = ('book_id', 'book_name', 'author_id','availability')  # define columns
    tree = Treeview(fr1, columns=columns, show='headings')  #create Treeview

    tree.heading('book_id', text='Book ID') # define headings
    tree.heading('book_name', text='Book Name')
    tree.heading('author_id', text='Author ID')
    tree.heading('availability', text='Availability')

    cursor.execute("Select * from book_master where availability='y';") #data
    data=cursor.fetchall()

    for i in data:  
        tree.insert('', END, values=i)  # add data to the treeview


    def item_selected(event):   #function to be executed when a row is selected
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record= item['values']
            query="insert into transaction(user_id, book_id, borrowed_date, expected_return_date) values {}".format((name,record[0],borrow_date,return_date))
            cursor.execute(query)
            cursor.execute("update book_master set availability = 'n' where bookid={}".format(record[0]))
            cursor.execute("commit;")
            # show a message
            x=showinfo(title='Notification', message='Book Successfully Borrowed!')
            if bool(x):
                borrow.destroy()


    tree.bind('<<TreeviewSelect>>', item_selected)  #binds the tree selection with the item_selected function
    tree.pack(fill="both", expand=1)    #fill the treeview in the entire window
    borrow.mainloop()



