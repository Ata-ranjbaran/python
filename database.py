import tkinter as TK
from tkinter import *
from tkinter import messagebox
import sqlite3
# 
connection=sqlite3.connect("library1.db")
curser=connection.cursor()
curser.execute("""CREATE TABLE IF NOT EXISTS book(name TEXT PRIMARY KEY,author TEXT,year INT,isbn INT );""") 
connection.commit()
# 
def show():

    curser.execute("""SELECT * FROM book ;""")
    result=curser.fetchall()
    if text.get("1.0","end-1c")=="":
        for i in result:
            text.insert("end",i)
            text.insert("end","\n")
    else:
        text.delete("1.0","end")
        for i in result:
            text.insert("end",i)
            text.insert("end","\n")
def search():
    if ename.get()=="" and eauthor.get()=="" and eyear.get()=="" and eisbn.get()=="" :
        messagebox.showerror("خطا","کادر را پر کنید")
    else:
        curser.execute("""SELECT * FROM book WHERE name=? or author=? or year=? or isbn=? ;""",
        [ename.get(),eauthor.get(),eyear.get(),eisbn.get()])
        result=curser.fetchall()
        if not result:
            messagebox.showerror("خطا","کتابی پیدا نشد")
        else:
            text.delete("1.0","end")
            text.insert("end",result)
            # show()


def insert():
    if ename.get()=="" or eauthor.get()=="" or eyear.get()=="" or eisbn.get()=="" :
        messagebox.showerror("خطا","کادر ها را پیر کنید")
    else:
        curser.execute("""INSERT INTO book VALUES(?,?,?,?) ;""",
        [ename.get(),eauthor.get(),eyear.get(),eisbn.get()])
        connection.commit()
        ename.delete(0,"end")
        eauthor.delete(0,"end")
        eyear.delete(0,"end")
        eisbn.delete(0,"end")
        show()

    


def delete():
    if ename.get()=="":
        messagebox.showerror("خطا","عنوان کتاب را وراد کنید")
    else:
        curser.execute("""SELECT * FROM book WHERE name=? ;""",[ename.get()])
        result=curser.fetchone()
        if not result:
            messagebox.showerror("خطا","کتابی پیدا نشد")
        else:
            eauthor.delete(0,"end")
            eyear.delete(0,"end")
            eisbn.delete(0,"end")
            eauthor.insert("end",result[1])
            eyear.insert("end",result[2])
            eisbn.insert("end",result[3])
        ob=messagebox.askyesno("خطا","ایا اطمینان دارید")
        if ob:
            curser.execute("""DELETE FROM book WHERE name=? ;""",[ename.get()])
            connection.commit()
            show()


    

# tk
root=Tk()
root.geometry("500x400")
root.title("مدیریت کتابخانه")
# label
lnane=Label(root,text="عنوان").grid(row=0,column=0)
lauthor=Label(root,text="نویسنده").grid(row=0,column=2)
lyear=Label(root,text="سال انتشار").grid(row=1,column=0)
lisbn=Label(root,text="ISBN").grid(row=1,column=2)
ok=Label(root).grid(row=3,column=0)
# ٍEntry
ename=Entry(root,bd=2,width=20)
ename.grid(row=0,column=1,padx=15)
eauthor=Entry(root,bd=2,width=20)
eauthor.grid(row=0,column=3,padx=15)
eyear=Entry(root,bd=2,width=20)
eyear.grid(row=1,column=1,padx=15)
eisbn=Entry(root,bd=2,width=20)
eisbn.grid(row=1,column=3,padx=15)
# button
bshow=Button(root,text="مشاهده همه",bd=2,width=10,command=show)
bshow.grid(row=4,column=3)
bsearch=Button(root,text="جستوجو",bd=2,width=10,command=search)
bsearch.grid(row=5,column=3)
binsert=Button(root,text="اضافه",bd=2,width=10,command=insert)
binsert.grid(row=6,column=3)
bdelete=Button(root,text="حذف",bd=2,width=10,command=delete)
bdelete.grid(row=7,column=3)
bclose=Button(root,text="بستن",bd=2,width=10,command=quit)
bclose.grid(row=8,column=3)
# text and scrool
scrool=Scrollbar(root)
scrool.grid(row=4,column=2,rowspan=3)
text=Text(root,width=30,height=8,yscrollcommand=scrool.set)
text.grid(row=4,column=0,rowspan=5,columnspan=2)







root.mainloop()