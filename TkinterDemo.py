from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_5_30"
        )


def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_mobile.get()=="" or e_email.get()=="":
        msg.showinfo("Insert Status","All fields are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into student(fname,lname,mobile,email) values(%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_mobile.get(),e_email.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_mobile.delete(0,'end') 
        e_email.delete(0,'end')
        msg.showinfo("Insert Status","Data inserted successfully")
        
def search_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_mobile.delete(0,'end') 
    e_email.delete(0,'end')
    if e_id.get()=="":
        msg.showinfo("Search Status","Id is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_mobile.insert(0,row[0][3])
            e_email.insert(0,row[0][4])
        else:
            msg.showinfo("Search Status","Id not found")
        conn.close()
        
def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_mobile.get()=="" or e_email.get()=="" or e_id.get()=="":
        msg.showinfo("Update Status","All Fields are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update student set fname=%s,lname=%s,mobile=%s,email=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_mobile.get(),e_email.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_mobile.delete(0,'end') 
        e_email.delete(0,'end')
        e_id.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfuly")
        conn.close()

        
def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","ID is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from student where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_mobile.delete(0,'end') 
        e_email.delete(0,'end')
        e_id.delete(0,'end')
        msg.showinfo("Delete Status","Data deleted Successfuly")
        conn.close()

def clear_data():
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_mobile.delete(0,'end') 
    e_email.delete(0,'end')
    e_id.delete(0,'end')
    

root=Tk()
root.geometry("320x380")
root.title("My Tkinter Example")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="First Name")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="Last Name")
l_lname.place(x=50,y=150)

l_mobile=Label(root,text="Mobile No")
l_mobile.place(x=50,y=200)

l_email=Label(root,text="Email")
l_email.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_mobile=Entry(root)
e_mobile.place(x=150,y=200)

e_email=Entry(root)
e_email.place(x=150,y=250)

insert=Button(root,text="Insert",bg="red",fg="black",font=("Arial",12),command=insert_data)
insert.place(x=20,y=300)

search=Button(root,text="Search",bg="red",fg="black",font=("Arial",12),command=search_data)
search.place(x=75,y=300)

update=Button(root,text="Update",bg="red",fg="black",font=("Arial",12),command=update_data)
update.place(x=143,y=300)

delete=Button(root,text="Delete",bg="red",fg="black",font=("Arial",12),command=delete_data)
delete.place(x=213,y=300)

clear=Button(root,text="Clear",bg="red",fg="black",font=("Arial",12),command=clear_data)
clear.place(x=120,y=340)

root.mainloop()

