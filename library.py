from tkinter import*
from tkinter import messagebox,ttk
from datetime import datetime,date
import sqlite3
db=sqlite3.connect("DB1.db")
cr=db.cursor()
try:
    cr.execute("create table Admin(User_id text primary key,Pass text not null)")
    db.commit()
    print("Admin table created")
except:
    print("Admin table already exist")
try:
    cr.execute("create table Students(F_name text not null,L_name text not null,M_name text,DOB text not null,Address text not null,City text not null,State text not null,Gender text not null,Phn_no text not null,S_Userid text primary key,S_Pass text not null)")
    db.commit()
    print("Students table created")
except:
    print("Students table already exist")
try:
    cr.execute("create table Add_Book(Book_Id text not null primary key,Book_Name text not null,Author_Name text not null,Quantity text not null)")
    db.commit()
    print("Add_Book table created")
except:
    print("Add_Book table already exist")
try:
    cr.execute("create table Issue_Book(F_name text not null,M_name text,L_name text not null,S_Userid text not null,Book_Id text not null,Book_Name text not null,Issue_Date text not null,Return_Date text not null)")
    db.commit()
    print("Issue_Book table created")
except:
    print("Issue_Book table already exist")
try:
    cr.execute("create table Fine(S_Userid text not null,Book_Id text not null,Book_Name text not null,Issue_Date text not null,Return_Date text not null,Late_Days text not null,Total_Fine text not null)")   
    db.commit()
    print("Fine table created")
except:
    print("Fine table already exist") 
m=Tk()
A_Userid=StringVar()
A_Pass=StringVar()
A_Userid1=StringVar()
A_Pass1=StringVar()
A_new_pass=StringVar()
F_name=StringVar()
L_name=StringVar()
M_name=StringVar()
DOB=StringVar()
Addr=StringVar()
City=StringVar()
State=StringVar()
Gender=StringVar()
Phn_no=StringVar()
S_Userid=StringVar()
S_Pass=StringVar()
S_Userid1=StringVar()
S_Pass1=StringVar()
S_new_pass=StringVar()
Book_Id=StringVar()
Book_Name=StringVar()
Author_Name=StringVar()
Quantity=StringVar()
Issue_Date=StringVar()
Return_Date=StringVar()
m.title("LIBRARY MANAGEMENT SYSTEM")
canvas=Canvas(m,width=1900,height=1900)
canvas.pack()
my_photo=PhotoImage(file='Library background.png')
canvas.create_image(0,0,anchor=NW,image=my_photo)
L1=Label(m,text='Welcome to Library manager',font=('Algerian',50),fg='blue',relief='solid').place(x=200,y=200)
L1=Label(m,text='Select option As',font=('Arial',25),fg='red',relief='solid').place(x=550,y=300)
my_photo1=PhotoImage(file='images.png')
admin_Frame=Frame(m,bg='white')
admin_Frame.place(x=300,y=400)
logo=Label(admin_Frame,image=my_photo1).grid(row=0,column=0,padx=1,pady=1)
my_photo2=PhotoImage(file='download.png')
students_Frame=Frame(m,bg='white')
students_Frame.place(x=800,y=400)
logo=Label(students_Frame,image=my_photo2).grid(row=0,column=0,padx=0,pady=30)
def admin():
    w1=Toplevel()
    w1.title("Admin Page")
    canvas=Canvas(w1,width=1700,height=2000)
    canvas.pack()
    image=PhotoImage(file='Library background.png')
    image_1=PhotoImage(file='Admin.png')
    image_2=PhotoImage(file='password.png')
    canvas.create_image(0,0, image=image,anchor=NW)
    L1=Label(w1,image=image_1).place(x=640,y=310)
    L2=Label(w1,image=image_2).place(x=640,y=400)
    L1=Label(w1,text='Welcome To Admin Page',font=('Algerian 38'),fg='blue',relief='solid').place(x=430,y=80)
    canvas.create_rectangle(1000,600, 500, 150, fill="lightyellow")
    canvas.create_text(750,230,fill="orange",font=("ariel 25 bold"),text="LOGIN WINDOW")
    canvas.create_text(560,340,fill="blue",font=("ariel 16"),text="USER ID")
    E1=Entry(w1,font=('ariel 16'),textvar=A_Userid)
    E1.place(x=720,y=325)
    canvas.create_text(570,425,fill="blue",font=("ariel 16"),text="PASSWORD")
    E2=Entry(w1,font=('ariel 16'),textvar=A_Pass,show="*")
    E2.place(x=720,y=410)
    def Login():
        x=A_Userid.get()
        y=A_Pass.get()
        cr.execute("select User_id,Pass from Admin")
        data=cr.fetchall()
        check=0
        for i in data:
            a=i[0]
            b=i[1]
            if x==a and y==b:
                check=1
                break
            else:
                check=0
        if check==1:
            E1.delete(0,END)
            E2.delete(0,END)
            w1.destroy()
            w=Toplevel()
            w.title("Admin Menu")
            canvas=Canvas(w,width=2000,height=2000)
            canvas.pack()
            image=PhotoImage(file='Library background.png')
            canvas.create_image(0,0, image = image,anchor=NW)
            my_photo3=PhotoImage(file='add-book.png')
            add_book_Frame=Frame(w,bg='white')
            add_book_Frame.place(x=50,y=50)
            logo1=Label(add_book_Frame,image=my_photo3).grid(row=0,column=0,padx=1,pady=1)
            my_photo4=PhotoImage(file='search-book.png')
            Search_book_Frame=Frame(w,bg='white')
            Search_book_Frame.place(x=300,y=50)
            logo2=Label(Search_book_Frame,image=my_photo4).grid(row=0,column=0,padx=1,pady=1)
            my_photo5=PhotoImage(file='update-book.png')
            Update_book_Frame=Frame(w,bg='white')
            Update_book_Frame.place(x=550,y=50)
            logo3=Label(Update_book_Frame,image=my_photo5).grid(row=0,column=0,padx=1,pady=1)
            my_photo6=PhotoImage(file='view-book.png')
            View_book_Frame=Frame(w,bg='white')
            View_book_Frame.place(x=800,y=50)
            logo4=Label(View_book_Frame,image=my_photo6).grid(row=0,column=0,padx=1,pady=1)
            my_photo7=PhotoImage(file='delete-book.png')
            Delete_book_Frame=Frame(w,bg='white')
            Delete_book_Frame.place(x=1050,y=50)
            logo5=Label(Delete_book_Frame,image=my_photo7).grid(row=0,column=0,padx=1,pady=1)
            my_photo8=PhotoImage(file='issue-book.png')
            Delete_book_Frame=Frame(w,bg='white')
            Delete_book_Frame.place(x=1300,y=50)
            logo8=Label(Delete_book_Frame,image=my_photo8).grid(row=0,column=0,padx=1,pady=1)
            my_photo9=PhotoImage(file='view-issue-book.png')
            view_issue_book_Frame=Frame(w,bg='white')
            view_issue_book_Frame.place(x=50,y=300)
            logo9=Label(view_issue_book_Frame,image=my_photo9).grid(row=0,column=0,padx=1,pady=1)
            my_photo10=PhotoImage(file='add-student.png')
            view_issue_book_Frame=Frame(w,bg='steelblue')
            view_issue_book_Frame.place(x=335,y=300)
            logo10=Label(view_issue_book_Frame,image=my_photo10).grid(row=0,column=0,padx=1,pady=1)
            my_photo11=PhotoImage(file='delete-student.png')
            view_issue_book_Frame=Frame(w,bg='steelblue')
            view_issue_book_Frame.place(x=620,y=300)
            my_photo11=PhotoImage(file='delete-student.png')
            view_issue_book_Frame=Frame(w,bg='steelblue')
            view_issue_book_Frame.place(x=620,y=300)
            logo11=Label(view_issue_book_Frame,image=my_photo11).grid(row=0,column=0,padx=1,pady=1)
            my_photo12=PhotoImage(file='changepass.png')
            view_issue_book_Frame=Frame(w,bg='steelblue')
            view_issue_book_Frame.place(x=890,y=315) 
            logo12=Label(view_issue_book_Frame,image=my_photo12).grid(row=0,column=0,padx=1,pady=1) 
            my_photo13=PhotoImage(file='return-book-2.png')
            return_book_Frame=Frame(w,bg='white')
            return_book_Frame.place(x=1120,y=315)
            logo13=Label(return_book_Frame,image=my_photo13).grid(row=0,column=0,padx=1,pady=1)
            my_photo14=PhotoImage(file='exit-book.png')
            view_issue_book_Frame=Frame(w,bg='steelblue')
            view_issue_book_Frame.place(x=700,y=600) 
            logo14=Label(view_issue_book_Frame,image=my_photo14).grid(row=0,column=0,padx=1,pady=1)
            my_photo15=PhotoImage(file='update-student.png')
            exit_book_Frame=Frame(w,bg='white')
            exit_book_Frame.place(x=1350,y=315)
            logo15=Label(exit_book_Frame,image=my_photo15).grid(row=0,column=0,padx=1,pady=1)
            def Add_book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Book Addition Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1100,760, 450, 80, fill="systembuttonface")
                L=Label(w,text='ADD BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=680,y=20)
                L1=Label(w,text='BOOK ID:',font=('ariel 18'),fg='blue').place(x=470,y=200)
                E1=Entry(w,font=('ariel 18'),textvar=Book_Id)
                E1.place(x=670,y=200)
                L2=Label(w,text='BOOK NAME:',font=('ariel 18'),fg='blue').place(x=470,y=300)
                E2=Entry(w,font=('ariel 18'),textvar=Book_Name)
                E2.place(x=670,y=300)
                L3=Label(w,text='AUTHOR NAME:',font=('ariel 18'),fg='blue').place(x=470,y=400)
                E3=Entry(w,font=('ariel 18'),textvar=Author_Name)
                E3.place(x=670,y=400)
                L4=Label(w,text='QUANTITY:',font=('ariel 18'),fg='blue').place(x=470,y=500)
                E4=Entry(w,font=('ariel 18'),textvar=Quantity)
                E4.place(x=670,y=500)
                def Book_Add():
                    a=Book_Id.get()
                    b=Book_Name.get()
                    c=Author_Name.get()
                    d=Quantity.get()
                    if len(a)==0:
                        messagebox.showwarning("Warning", "book id should not be empty!") 
                    elif len(a)>0 and len(b)>0 and len(c)>0  and len(d)>0:
                        try:
                            cr.execute("insert into Add_Book(Book_Id,Book_Name,Author_Name,Quantity)values(?,?,?,?)",(a,b,c,d))
                            db.commit()
                            flag=1
                        except:
                            flag=0
                        if flag==1:
                            E1.delete(0,END)
                            E2.delete(0,END)
                            E3.delete(0,END)
                            E4.delete(0,END)
                            messagebox.showinfo("Info", "Addition of book has beeen entered succesfully!")
                        else:
                            messagebox.showerror("Error", "Book_Id already exist!")
                    else:
                        messagebox.showwarning("Warning", "One or more filed is empty!")
                B1=Button(w,text='ADD',font=('ariel 18'),fg='blue',padx=2,pady=1,command=Book_Add).place(x=730,y=600) 
                w.mainloop()
            def Search_book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Search Book Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1300,760, 200, 80, fill="systembuttonface")
                L=Label(w,text='SERACH BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=600,y=20)
                L1=Label(w,text='SEARCH BOOK BY',font=('ariel 18'),fg='blue').place(x=600,y=220)
                L2=Label(w,text='BOOK ID:',font=('ariel 18'),fg='blue').place(x=230,y=400)
                E2=Entry(w,font=('ariel 18'),textvar=Book_Id)
                E2.place(x=350,y=400)
                L3=Label(w,text='OR',font=('ariel 18'),fg='blue').place(x=700,y=400)
                L4=Label(w,text='BOOK NAME:',font=('ariel 18'),fg='blue').place(x=830,y=400)
                E4=Entry(w,font=('ariel 18'),textvar=Book_Name)
                E4.place(x=1000,y=400) 
                def View_Book1():
                    a=Book_Id.get()
                    b=Book_Name.get()
                    if len(a)==0 and len(b)==0:
                        messagebox.showwarning("Warning", "Please enter book id or book name")
                    elif len(a)!=0 and len(b)==0:
                        data=cr.execute("select Book_Id from Add_Book")
                        flag=0
                        for i in data:
                            x=i[0]
                            if x==a:
                                flag=1
                                break
                            else:
                                flag=0
                        if flag==1:
                            w=Toplevel()
                            w.geometry('2000x2000')
                            w.title("Specific Book Page")
                            canvas=Canvas(w,width=2000,height=2000)
                            canvas.pack()
                            image=PhotoImage(file='Library background.png')
                            canvas.create_image(0,0, image = image,anchor=NW)
                            L=Label(w,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                            style = ttk.Style()
                            style.configure("Treeview.Heading", font=("ariel 18 bold"))
                            style.configure("Treeview", rowheight=50)
                            tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4"), show='headings',selectmode='browse')
                            tree.heading("#1", text="Book Id")
                            tree.heading("#2", text="Book Name")
                            tree.heading("#3", text="Author Name")
                            tree.heading("#4", text="Quantity")
                            tree.tag_configure('monospace', font='ariel 18')
                            vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                            vsb.place(x=1143, y=100, height=529)
                            tree.place(x=340,y=100)
                            tree.configure(style="Treeview",yscrollcommand=vsb.set)
                            data=cr.execute("select * from Add_Book where Book_Id=?",(a,))
                            flag=0
                            for i in data:
                                tree.insert("",END,values=i,tag='monospace')
                                flag=1
                        else:
                            messagebox.showerror("Error", "Invalid Book Id")
                        if flag==1:
                            E2.delete(0,END)
                            w.mainloop()
                    elif len(b)!=0 and len(a)==0:
                        flag=1
                        if flag==1:
                            w=Toplevel()
                            w.geometry('2000x2000')
                            w.title("Specific Book Page")
                            canvas=Canvas(w,width=2000,height=2000)
                            canvas.pack()
                            image=PhotoImage(file='Library background.png')
                            canvas.create_image(0,0, image = image,anchor=NW)
                            L=Label(w,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                            style = ttk.Style()
                            style.configure("Treeview.Heading", font=("ariel 18 bold"))
                            style.configure("Treeview", rowheight=50)
                            tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4"), show='headings',selectmode='browse')
                            tree.heading("#1", text="Book Id")
                            tree.heading("#2", text="Book Name")
                            tree.heading("#3", text="Author Name")
                            tree.heading("#4", text="Quantity")
                            tree.tag_configure('monospace', font='ariel 18')
                            vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                            vsb.place(x=1143, y=100, height=529)
                            tree.place(x=340,y=100)
                            tree.configure(style="Treeview",yscrollcommand=vsb.set)
                            data=cr.execute("select * from Add_Book where Book_Name like ?",(b+'%',))
                            flag=0
                        for i in data:
                            tree.insert("",END,values=i,tag='monospace')
                            flag=1
                        if flag==1:
                            E4.delete(0,END)
                            w.mainloop() 
                        else:
                            w.destroy()
                            messagebox.showerror("Error", "No book with this name was found!")
                    else:
                        messagebox.showwarning("Warning", "Please enter either Book Id or Book name")
                B1=Button(w,text='SEARCH',font=('ariel 18'),fg='blue',padx=2,pady=1,command=View_Book1).place(x=670,y=600)  
                w.mainloop()
            def Update_book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Book Addition Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1100,760, 450, 80, fill="systembuttonface")
                L=Label(w,text='UPDATE BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=680,y=20)
                L1=Label(w,text='BOOK ID:',font=('ariel 18'),fg='blue').place(x=470,y=200)
                E1=Entry(w,font=('ariel 18'),textvar=Book_Id)
                E1.place(x=670,y=200)
                L2=Label(w,text='BOOK NAME:',font=('ariel 18'),fg='blue').place(x=470,y=300)
                E2=Entry(w,font=('ariel 18'),textvar=Book_Name)
                E2.place(x=670,y=300)
                L3=Label(w,text='AUTHOR NAME:',font=('ariel 18'),fg='blue').place(x=470,y=400)
                E3=Entry(w,font=('ariel 18'),textvar=Author_Name)
                E3.place(x=670,y=400)
                L4=Label(w,text='QUANTITY:',font=('ariel 18'),fg='blue').place(x=470,y=500)
                E4=Entry(w,font=('ariel 18'),textvar=Quantity)
                E4.place(x=670,y=500)
                def Book_update():
                    a=Book_Id.get()
                    b=Book_Name.get()
                    c=Author_Name.get()
                    d=Quantity.get()
                    if len(a)>0 and len(b)>0 and len(c)>0 and len(d)>0:
                            data=cr.execute("select Book_Id from Add_Book")
                            flag=0
                            for l in data:
                                x=l[0]
                                if x==a:
                                    flag=1
                                    break
                                else:
                                    flag=0
                            if flag==1:
                                cr.execute("update Add_Book Set Book_Name=?,Author_Name=?,Quantity=? where Book_Id=?",(b,c,d,a))
                                db.commit()
                                E1.delete(0,END)
                                E2.delete(0,END)
                                E3.delete(0,END)
                                E4.delete(0,END)
                                messagebox.showinfo("Info", "Book information has beeen updated succesfully!")
                            else:
                                messagebox.showerror("Error", "No book with this book id was found!")
                    else:
                        messagebox.showwarning("Warning", "One or more filed is empty!")
                B1=Button(w,text='UPDATE',font=('ariel 18'),fg='blue',padx=2,pady=1,command=Book_update).place(x=670,y=600) 
                w.mainloop()
            def View_book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("View Book Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                L=Label(w,text='VIEW BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=600,y=20)
                style = ttk.Style()
                style.configure("Treeview.Heading", font=("ariel 18 bold"))
                style.configure("Treeview", rowheight=50)
                tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4"), show='headings',selectmode='browse')
                tree.heading("#1", text="Book Id")
                tree.heading("#2", text="Book Name")
                tree.heading("#3", text="Author Name")
                tree.heading("#4", text="Quantity")
                tree.tag_configure('monospace', font='ariel 18')
                vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                vsb.place(x=1103, y=100, height=529)
                tree.place(x=300,y=100)
                tree.configure(style="Treeview",yscrollcommand=vsb.set)
                def Book_View():
                    data=cr.execute("select * from Add_Book")
                    for i in data:
                        tree.insert("",END,values=i,tag='monospace')
                data=cr.execute("select * from Add_Book")
                flag=0
                for i in data:
                        if len(i)>0:
                            flag=1
                            break
                        else:
                            flag=0
                            break
                if flag==1:
                    B=Button(w,text='View',font=('ariel 18'),fg='blue',padx=2,pady=1,command=Book_View).place(x=687,y=635)
                    w.mainloop()
                else:
                    w.destroy()
                    messagebox.showwarning("Warning", "No book in the database!")
            def Delete_book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Delete Book Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1000,760, 500, 80, fill="systembuttonface")
                L=Label(w,text='DELETE BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=600,y=20)
                L1=Label(w,text='DELETE BOOK BY',font=('ariel 18'),fg='blue').place(x=600,y=220)
                L2=Label(w,text='BOOK ID:',font=('ariel 18'),fg='blue').place(x=530,y=400)
                E2=Entry(w,font=('ariel 18'),textvar=Book_Id)
                E2.place(x=670,y=400)
                def book_delete():
                    x=Book_Id.get()
                    cr.execute("select Book_Id  from Add_Book")
                    data=cr.fetchall()
                    flag=0
                    for i in data:
                        a=i[0]
                        if x==a:
                            cr.execute("delete from Add_Book where Book_Id=?",(x,))
                            db.commit()
                            flag=1
                            break
                    if flag==1:
                        E2.delete(0,END)
                        messagebox.showinfo("Info", "Book data deleted!")
                    else:
                        messagebox.showerror("Error", "Book Id  not found")
                B1=Button(w,text='DELETE',font=('ariel 18'),fg='blue',padx=2,pady=1,command=book_delete).place(x=670,y=600)
                w.mainloop()
            def Issue_book():
                w=Toplevel()
                w.geometry('1900x1900')
                w.title("Issue Book Page")
                canvas=Canvas(w,width=1900,height=1900)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1100,780, 450, 80, fill="systembuttonface")
                L=Label(w,text='ISSUE BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=670,y=20)
                L1=Label(w,text='FIRST NAME:',font=('ariel 18'),fg='blue').place(x=470,y=100)
                E1=Entry(w,font=('ariel 18'),textvar=F_name)
                E1.place(x=670,y=100)
                L2=Label(w,text='MIDDLE NAME:',font=('ariel 18'),fg='blue').place(x=470,y=180)
                E2=Entry(w,font=('ariel 18'),textvar=M_name)
                E2.place(x=670,y=180)
                L3=Label(w,text='LAST NAME:',font=('ariel 18'),fg='blue').place(x=470,y=260)
                E3=Entry(w,font=('ariel 18'),textvar=L_name)
                E3.place(x=670,y=260)
                L4=Label(w,text='USER ID:',font=('ariel 18'),fg='blue').place(x=470,y=340)
                E4=Entry(w,font=('ariel 18'),textvar=S_Userid)
                E4.place(x=670,y=340)
                L5=Label(w,text='BOOK ID:',font=('ariel 18'),fg='blue').place(x=470,y=420)
                E5=Entry(w,font=('ariel 18'),textvar=Book_Id)
                E5.place(x=670,y=420)
                L6=Label(w,text='BOOK NAME:',font=('ariel 18'),fg='blue').place(x=470,y=500)
                E6=Entry(w,font=('ariel 18'),textvar=Book_Name)
                E6.place(x=670,y=500)
                L7=Label(w,text='ISSUE DATE:\n (DD/MM/YYYY)',font=('ariel 18'),fg='blue').place(x=470,y=580)
                E7=Entry(w,font=('ariel 18'),textvar=Issue_Date)
                E7.place(x=670,y=580)
                L8=Label(w,text='RETURN DATE:\n (DD/MM/YYYY)',font=('ariel 18'),fg='blue').place(x=470,y=660)
                E8=Entry(w,font=('ariel 18'),textvar=Return_Date)
                E8.place(x=670,y=660)
                def book_Issue():
                    a=F_name.get()
                    b=M_name.get()
                    c=L_name.get()
                    d=Book_Id.get()
                    e=S_Userid.get()
                    f=Book_Name.get()
                    g=Issue_Date.get()
                    h=Return_Date.get()
                    if len(d)==0 or len(e)==0:
                        messagebox.showwarning("Warning", "book id or User id should not be empty!") 
                    elif len(a)>0 and len(c)>0  and len(d)>0 and len(e)>0 and len(f)>0 and len(g)>0 and len(h)>0:
                        data1=cr.execute("select F_name,M_name,L_name,S_Userid from Students")
                        flag=0
                        flag1=0
                        flag2=0
                        flag3=0
                        check=0
                        x7=0
                        for i in data1:
                            x1=i[0]
                            x2=i[1]
                            x3=i[2]
                            x4=i[3]
                            if x4==e:
                                data2=cr.execute("select Book_Id,Book_Name,Quantity from Add_Book")
                                for j in data2:
                                    x5=j[0]
                                    x6=j[1]
                                    x7=j[2]
                                    check=1
                                    if x5==d:
                                        flag=1
                                        break
                                    else:
                                        flag=0
                            if flag==1:
                                flag1=1
                                break
                        if flag==0:
                            messagebox.showerror("Error", "Userid or Book id does not match")
                        if flag1==1:
                            data3=cr.execute("select S_Userid,Book_Id from Issue_Book")
                            flag2=1
                            for k in data2:
                                x8=k[0]
                                x9=k[1]
                                if x8==e and x9==d:
                                    flag2=0
                                    messagebox.showwarning("Warning", "One of this book copy has already been issued to this Student")
                                    break
                                else:
                                    flag2=1
                        if int(x7)==1 and check==1 and flag!=0:
                            messagebox.showwarning("Warning", "This Book is out of stock")
                        if flag2==1 and int(x7)>1:
                            if x1==a and x2==b and x3==c and x6==f:
                                cr.execute("insert into Issue_Book(F_name,M_name,L_name,Book_Id,S_Userid,Book_Name,Issue_Date,Return_Date)values(?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h))
                                db.commit()
                                flag3=1        
                            else:
                                messagebox.showwarning("Warning", "Book info or Student info does not match")
                        if flag3==1:
                            x7=int(x7)-1
                            cr.execute("update Add_Book set Quantity=? where Book_Id=?",(x7,x5))
                            db.commit()
                            E1.delete(0,END)
                            E2.delete(0,END)
                            E3.delete(0,END)
                            E4.delete(0,END)
                            E5.delete(0,END)
                            E6.delete(0,END)
                            E7.delete(0,END)
                            E8.delete(0,END)
                            messagebox.showinfo("Info", "Book has beeen issued succesfully!")
                            
                    else:
                        messagebox.showwarning("Warning", "One or more filed is empty!")
                B1=Button(w,text='ISSUE',font=('ariel 18'),fg='blue',padx=2,pady=1,command=book_Issue).place(x=700,y=720)
                w.mainloop()
            def View_issued_book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("View Issued Book Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1300,760, 200, 80, fill="systembuttonface")
                L=Label(w,text='VIEW ISSUED BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=600,y=20)
                L1=Label(w,text=' VIEW ISSUED BOOK BY',font=('ariel 18'),fg='blue').place(x=600,y=220)
                L2=Label(w,text='BOOK ID:',font=('ariel 18'),fg='blue').place(x=230,y=400)
                E2=Entry(w,font=('ariel 18'),textvar=Book_Id)
                E2.place(x=350,y=400)
                L3=Label(w,text='OR',font=('ariel 18'),fg='blue').place(x=700,y=400)
                L4=Label(w,text='BOOK NAME:',font=('ariel 18'),fg='blue').place(x=830,y=400)
                E4=Entry(w,font=('ariel 18'),textvar=Book_Name)
                E4.place(x=1000,y=400)
                L5=Label(w,text='User Id:',font=('ariel 18'),fg='blue').place(x=510,y=500)
                E5=Entry(w,font=('ariel 18'),textvar=S_Userid)
                E5.place(x=610,y=500)
                def View_Book2():
                    a=Book_Id.get()
                    b=Book_Name.get()
                    c=S_Userid.get()
                    if len(a)==0 and len(b)==0 and len(c)==0:
                        messagebox.showwarning("Warning", "Please enter book id or book name or Student Id")
                    elif len(a)!=0 and len(b)==0 and len(c)==0:
                        data=cr.execute("select Book_Id from Issue_Book")
                        flag=0
                        for i in data:
                            x=i[0]
                            if x==a:
                                flag=1
                                break
                            else:
                                flag=0
                        if flag==1:
                            w=Toplevel()
                            w.geometry('2000x2000')
                            w.title("Specific Book Page")
                            canvas=Canvas(w,width=2000,height=2000)
                            canvas.pack()
                            image=PhotoImage(file='Library background.png')
                            canvas.create_image(0,0, image = image,anchor=NW)
                            L=Label(w,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                            style = ttk.Style()
                            style.configure("Treeview.Heading", font=("ariel 18 bold"))
                            style.configure("Treeview", rowheight=50)
                            tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4", "Column5", "column6", "column7"), show='headings',selectmode='browse')
                            tree.heading("#1", text="First Name")
                            tree.heading("#2", text="Last Name")
                            tree.heading("#3", text="Userid")
                            tree.heading("#4", text="Bookid")
                            tree.heading("#5", text="Book Name")
                            tree.heading("#6", text="Issue Date")
                            tree.heading("#7", text="Return Date")
                            tree.tag_configure('monospace', font='ariel 18')
                            vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                            vsb.place(x=1453, y=100, height=529)
                            tree.place(x=50,y=100)
                            tree.configure(style="Treeview",yscrollcommand=vsb.set)
                            data=cr.execute("select F_name,L_name,S_Userid,Book_Id,Book_Name,Issue_Date,Return_Date from Issue_Book where Book_Id=?",(a,))
                            flag=0
                            for i in data:
                                tree.insert("",END,values=i,tag='monospace')
                                flag=1
                        else:
                            messagebox.showerror("Error", "Invalid Book Id or No book with this id was issued")
                        if flag==1:
                            E2.delete(0,END)
                            w.mainloop()
                    elif len(b)!=0 and len(a)==0 and len(c)==0:
                        flag=1
                        if flag==1:
                            w=Toplevel()
                            w.geometry('2000x2000')
                            w.title("Specific Book Page")
                            canvas=Canvas(w,width=2000,height=2000)
                            canvas.pack()
                            image=PhotoImage(file='Library background.png')
                            canvas.create_image(0,0, image = image,anchor=NW)
                            L=Label(w,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                            style = ttk.Style()
                            style.configure("Treeview.Heading", font=("ariel 18 bold"))
                            style.configure("Treeview", rowheight=50)
                            tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4", "Column5", "column6", "column7"), show='headings',selectmode='browse')
                            tree.heading("#1", text="First Name")
                            tree.heading("#2", text="Last Name")
                            tree.heading("#3", text="Userid")
                            tree.heading("#4", text="Bookid")
                            tree.heading("#5", text="Book Name")
                            tree.heading("#6", text="Issue Date")
                            tree.heading("#7", text="Return Date")
                            tree.tag_configure('monospace', font='ariel 18')
                            vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                            vsb.place(x=1453, y=100, height=529)
                            tree.place(x=50,y=100)
                            tree.configure(style="Treeview",yscrollcommand=vsb.set)
                            data=cr.execute("select F_name,L_name,S_Userid,Book_Id,Book_Name,Issue_Date,Return_Date from Issue_Book where Book_Name like ?",(b+"%",))
                            flag=0
                        for i in data:
                            tree.insert("",END,values=i,tag='monospace')
                            flag=1
                        if flag==1:
                            E4.delete(0,END)
                            w.mainloop() 
                        else:
                            w.destroy()
                            messagebox.showerror("Error", "No book with this name was issued or invalid book name!")
                    elif len(c)!=0 and len(a)==0 and len(b)==0:
                        data=cr.execute("select S_Userid from Issue_Book")
                        flag=0
                        for i in data:
                            x=i[0]
                            if x==c:
                                flag=1
                                break
                            else:
                                flag=0
                        if flag==1:
                            w=Toplevel()
                            w.geometry('2000x2000')
                            w.title("Specific Book Page")
                            canvas=Canvas(w,width=2000,height=2000)
                            canvas.pack()
                            image=PhotoImage(file='Library background.png')
                            canvas.create_image(0,0, image = image,anchor=NW)
                            L=Label(w,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                            style = ttk.Style()
                            style.configure("Treeview.Heading", font=("ariel 18 bold"))
                            style.configure("Treeview", rowheight=50)
                            tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4", "Column5", "column6", "column7"), show='headings',selectmode='browse')
                            tree.heading("#1", text="First Name")
                            tree.heading("#2", text="Last Name")
                            tree.heading("#3", text="Userid")
                            tree.heading("#4", text="Bookid")
                            tree.heading("#5", text="Book Name")
                            tree.heading("#6", text="Issue Date")
                            tree.heading("#7", text="Return Date")
                            tree.tag_configure('monospace', font='ariel 18')
                            vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                            vsb.place(x=1453, y=100, height=529)
                            tree.place(x=50,y=100)
                            tree.configure(style="Treeview",yscrollcommand=vsb.set)
                            data=cr.execute("select F_name,L_name,S_Userid,Book_Id,Book_Name,Issue_Date,Return_Date from Issue_Book where S_Userid=?",(x,))
                            flag=0
                            for i in data:
                                tree.insert("",END,values=i,tag='monospace')
                                flag=1
                        else:
                            messagebox.showerror("Error", "No book was issud to this student or invalid Student Id! ")
                        if flag==1:
                            E5.delete(0,END)
                            w.mainloop()
                    else:
                        messagebox.showwarning("Warning", "Please enter either Book Id or Book name or Student Id")       
                B1=Button(w,text='VIEW',font=('ariel 18'),fg='blue',padx=2,pady=1,command=View_Book2).place(x=670,y=600) 
                w.mainloop()
            def Add_students():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Students Registration")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1100,760, 450, 80, fill="systembuttonface")
                L=Label(w,text='Students Registration',font=('Algerian 28'),fg='blue',relief='solid').place(x=570,y=20)
                L1=Label(w,text='FIRST NAME:',font=('ariel 18'),fg='blue').place(x=470,y=100)
                E1=Entry(w,font=('ariel 18'),textvar=F_name)
                E1.place(x=700,y=100)
                L2=Label(w,text='LAST NAME:',font=('ariel 18'),fg='blue').place(x=470,y=160)
                E2=Entry(w,font=('ariel 18'),textvar=L_name)
                E2.place(x=700,y=160)
                L3=Label(w,text='MIDDLE NAME:',font=('ariel 18'),fg='blue').place(x=470,y=220)
                E3=Entry(w,font=('ariel 18'),textvar=M_name)
                E3.place(x=700,y=220)
                L4=Label(w,text='DATE OF BIRTH :\n(DD/MM/YYYY)',font=('ariel 18'),fg='blue').place(x=470,y=280)
                E4=Entry(w,font=('ariel 18'),textvar=DOB)
                E4.place(x=700,y=280)
                L5=Label(w,text='ADDRESS:',font=('ariel 18'),fg='blue').place(x=470,y=350)
                E5=Entry(w,font=('ariel 18'),textvar=Addr)
                E5.place(x=700,y=350)
                L6=Label(w,text='CITY:',font=('ariel 18'),fg='blue').place(x=470,y=410)
                E6=Entry(w,font=('ariel 18'),textvar=City)
                E6.place(x=700,y=410)
                L7=Label(w,text='STATE:',font=('ariel 18'),fg='blue').place(x=470,y=470)
                choices = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarg','Goa','Gujrat','Haryana','Himachak Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharastra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajastjan','Sikkim','Tamil Nadu','Teleangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
                popupMenu = OptionMenu(w,State,*choices).place(x=560,y=470)
                State.set('Select State')
                L7_1=Label(w,text='Phone No: +91-',font=('ariel 16'),fg='blue').place(x=670,y=470)
                E7_1=Entry(w,font=('ariel 18'),textvar=Phn_no)
                E7_1.place(x=825,y=470)
                L8=Label(w,text='GENDER:',font=('ariel 18'),fg='blue').place(x=470,y=530)
                R1=Radiobutton(w,text='Male',variable=Gender,value='Male',font=('ariel 16')).place(x=590,y=530)
                R2=Radiobutton(w,text='Female',variable=Gender,value='Female',font=('ariel 16')).place(x=680,y=530)
                R3=Radiobutton(w,text='Other',variable=Gender,value='Other',font=('ariel 16')).place(x=790,y=530)
                Gender.set('Male')
                L8=Label(w,text='USER ID:',font=('ariel 18'),fg='blue').place(x=470,y=590)
                E8=Entry(w,font=('ariel 18'),textvar=S_Userid)
                E8.place(x=700,y=590)
                L9=Label(w,text='PASSWORD:',font=('ariel 18'),fg='blue').place(x=470,y=650)
                E9=Entry(w,font=('ariel 18'),textvar=S_Pass,show='*')
                E9.place(x=700,y=650)
                def Submit():
                    a=F_name.get()
                    b=L_name.get()
                    c=M_name.get()
                    d=DOB.get()
                    e=Addr.get()
                    f=City.get()
                    g=State.get()
                    h=Gender.get()
                    i=Phn_no.get()
                    j=S_Userid.get()
                    k=S_Pass.get()
                    if len(a)>0 and len(b)>0 and len(d)>0 and len(e)>0 and len(f)>0 and len(g)>0 and len(h)>0 and len(i)>0 and len(j)>0 and len(k)>0:
                        if len(k)<6:
                            messagebox.showwarning("Warning", "Password need to be atleast 6 characters!")
                        else:
                            try:
                                cr.execute("insert into Students(F_name,L_name,M_name,DOB,Addr,City,State,Gender,Phn_no,S_Userid,S_Pass)values(?,?,?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,i,j,k))
                                db.commit()
                                flag=1
                            except:
                                flag=0
                            if flag==1:
                                E1.delete(0,END)
                                E2.delete(0,END)
                                E3.delete(0,END)
                                E4.delete(0,END)
                                E5.delete(0,END)
                                E6.delete(0,END)
                                E7_1.delete(0,END)
                                E8.delete(0,END)
                                E9.delete(0,END)
                                messagebox.showinfo("Info", "Students information has beeen entered succesfully!")
                            else:
                                messagebox.showerror("Error", "Userid already exist!")
                    else:
                        messagebox.showwarning("Warning", "One or more filed is empty!")
                B1=Button(w,text='Submit',font=('ariel 18'),fg='blue',padx=2,pady=1,command=Submit).place(x=620,y=700)
                def exit():
                    E1.delete(0,END)
                    E2.delete(0,END)
                    E3.delete(0,END)
                    E4.delete(0,END)
                    E5.delete(0,END)
                    E6.delete(0,END)
                    E7_1.delete(0,END)
                    E8.delete(0,END)
                    E9.delete(0,END)
                    w.destroy()
                B2=Button(w,text='Exit',font=('ariel 18'),fg='blue',padx=2,pady=1,command=exit).place(x=820,y=700)
                w.mainloop()
            def Delete_students():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Delete Students Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                L=Label(w,text='DELETE STUDENT',font=('Algerian 28'),fg='blue',relief='solid').place(x=600,y=20)
                canvas.create_rectangle(1000,500,500,80, fill="systembuttonface")
                L1=Label(w,text='USER ID:',font=('ariel 18'),fg='blue').place(x=520,y=200)
                E1=Entry(w,font=('ariel 18'),textvar=S_Userid1)
                E1.place(x=650,y=200)
                def student_delete():
                    x=S_Userid1.get()
                    cr.execute("select S_Userid from Students")
                    data=cr.fetchall()
                    flag=0
                    for i in data:
                        a=i[0]
                        if x==a:
                            cr.execute("delete from Students where S_Userid=?",(x,))
                            db.commit()
                            flag=1
                            break
                    if flag==1:
                        E1.delete(0,END)
                        messagebox.showinfo("Info", "Student data deleted!")
                    else:
                        messagebox.showerror("Error", "Student Userid not found")
                B1=Button(w,text='DELETE',font=('ariel 18'),fg='blue',padx=2,pady=1,command=student_delete).place(x=680,y=400)
                w.mainloop()
            def Change_pass():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Change Password Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                L=Label(w,text='CHANGE ADMIN PASSWORD',font=('Algerian 28'),fg='blue',relief='solid').place(x=500,y=20)
                canvas.create_rectangle(1200,700,300,80, fill="systembuttonface")
                L1=Label(w,text='USER ID:',font=('ariel 18'),fg='blue').place(x=520,y=200)
                E1=Entry(w,font=('ariel 18'),textvar=A_Userid1)
                E1.place(x=650,y=200)
                L2=Label(w,text='OLD PASSWORD:',font=('ariel 18'),fg='blue').place(x=520,y=300)
                E2=Entry(w,font=('ariel 18'),textvar=A_Pass1,show='*')
                E2.place(x=750,y=300)
                L3=Label(w,text='NEW PASSWORD:',font=('ariel 18'),fg='blue').place(x=520,y=400)
                E3=Entry(w,font=('ariel 18'),textvar=A_new_pass,show='*')
                E3.place(x=750,y=400)
                def A_pass_change():
                    x=A_Userid1.get()
                    y=A_Pass1.get()
                    z=A_new_pass.get()
                    cr.execute("select User_id,Pass from Admin")
                    data=cr.fetchall()
                    for i in data:
                        a=i[0]
                        b=i[1]
                        if x==a and y==b:
                            check=1
                            break
                        else:
                            check=0
                    if check==1:
                        if len(z)>0 and z!=y:
                            if len(z)<6:
                                messagebox.showwarning("Warning","New password need to be atleast 6 characters!")
                            else:
                                cr.execute("update Admin set Pass=? where User_id=?",(z,x))
                                db.commit()
                                E1.delete(0,END)
                                E2.delete(0,END)
                                E3.delete(0,END)
                                messagebox.showinfo("info", "Password has been changed succesfully!")
                        elif z==y:
                            messagebox.showwarning("Warning", "Old and new password cant be same")
                        else:
                            messagebox.showwarning("Warning", "One or more filled is empty")
                    else:
                        messagebox.showerror("Error", "Wrong Userid or Old password")
                B1=Button(w,text='CHANGE PASSWORD',font=('ariel 18'),fg='blue',padx=2,pady=1,command=A_pass_change).place(x=600,y=600)
                w.mainloop()
            def Return_Book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Return Book Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                L=Label(w,text='RETURN BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=600,y=20)
                canvas.create_rectangle(1000,500,500,80, fill="systembuttonface")
                L1=Label(w,text='USER ID:',font=('ariel 18'),fg='blue').place(x=520,y=200)
                E1=Entry(w,font=('ariel 18'),textvar=S_Userid)
                E1.place(x=650,y=200)
                def Fine_Book():
                    a=S_Userid.get()
                    if len(a)>0:
                        data=cr.execute("select S_Userid from Students")
                        flag1=0
                        for i in data:
                            x=i[0]
                            if x==a:
                                flag1=1
                                break
                            else:
                                flag1=0
                        if flag1==1:
                            data=cr.execute("select S_Userid from Issue_Book")
                            flag=0
                            for i in data:
                                x=i[0]
                                if x==a:
                                    flag=1
                                    break
                                else:
                                    flag=0
                            if flag==1:
                                w=Toplevel()
                                w.geometry('2000x2000')
                                w.title("Specific Book Page")
                                canvas=Canvas(w,width=2000,height=2000)
                                canvas.pack()
                                image=PhotoImage(file='Library background.png')
                                canvas.create_image(0,0, image = image,anchor=NW)
                                L=Label(w,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                                style = ttk.Style()
                                style.configure("Treeview.Heading", font=("ariel 18 bold"))
                                style.configure("Treeview", rowheight=50)
                                tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4", "Column5", "column6", "column7"), show='headings',selectmode='browse')
                                tree.heading("#1", text="First Name")
                                tree.heading("#2", text="Last Name")
                                tree.heading("#3", text="Userid")
                                tree.heading("#4", text="Bookid")
                                tree.heading("#5", text="Book Name")
                                tree.heading("#6", text="Issue Date")
                                tree.heading("#7", text="Return Date")
                                def selectItem():
                                    curItem = tree.focus()
                                    x=tree.item(curItem)
                                    y1=x['values'][2]
                                    y2=x['values'][3]
                                    y3=x['values'][4]
                                    y4=x['values'][5]
                                    y5=x['values'][6]
                                    return y1,y2,y3,y4,y5
                                tree.tag_configure('monospace', font='ariel 18')
                                vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                                vsb.place(x=1453, y=100, height=529)
                                tree.place(x=50,y=100)
                                tree.bind(selectItem)
                                tree.configure(style="Treeview",yscrollcommand=vsb.set)
                                data=cr.execute("select F_name,L_name,S_Userid,Book_Id,Book_Name,Issue_Date,Return_Date from Issue_Book where S_Userid=?",(x,))
                                flag=0
                                for i in data:
                                    tree.insert("",END,values=i,tag='monospace')
                                    flag=1
                            else:
                                messagebox.showwarning("Warning", "No book has been issued to this student")
                            if flag==1:
                                E1.delete(0,END)
                                def Return():
                                    y1,y21,y3,y4,y5=selectItem()
                                    y2=str(y21)
                                    cr.execute("SELECT Return_Date FROM Issue_Book where Book_Id=?",(y2,))
                                    data=cr.fetchall()
                                    for i in data:
                                        a=i[0]
                                    today=date.today()
                                    date_time_str =a
                                    date_time_obj =datetime.strptime(date_time_str, '%d/%m/%Y')
                                    c=date_time_obj.date()
                                    d=(today-c).days
                                    y6=str(d*2)
                                    data=cr.execute("select S_Userid,Book_Id from Fine where S_Userid=? and Book_Id=?",(y1,y2))
                                    check=1
                                    for i in data:
                                        u=i[0]
                                        v=i[1]
                                        if u!=y1 and v!=y2:
                                            check=1
                                        else:
                                            check=0
                                            break
                                    if check==1:
                                        cr.execute("insert into Fine(S_Userid,Book_Id,Book_Name,Issue_Date,Return_Date,Late_Days,Total_Fine)values(?,?,?,?,?,?,?)",(y1,y2,y3,y4,y5,str(d),y6))
                                        db.commit()
                                    w1=Toplevel()
                                    w1.geometry('2000x2000')
                                    w1.title("Specific Book Page")
                                    canvas=Canvas(w1,width=2000,height=2000)
                                    canvas.pack()
                                    image=PhotoImage(file='Library background.png')
                                    canvas.create_image(0,0, image = image,anchor=NW)
                                    L=Label(w1,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                                    style = ttk.Style()
                                    style.configure("Treeview.Heading", font=("ariel 18 bold"))
                                    style.configure("Treeview", rowheight=50)
                                    tree= ttk.Treeview(w1, column=("column1", "column2", "column3", "column4", "Column5", "column6", "column7"), show='headings',selectmode='browse')
                                    tree.heading("#1", text="Userid")
                                    tree.heading("#2", text="Book Id")
                                    tree.heading("#3", text="Book Name")
                                    tree.heading("#4", text="Issue Date")
                                    tree.heading("#5", text="Return Date")
                                    tree.heading("#6", text="Late Days")
                                    tree.heading("#7", text="Total Fine(₹)")
                                    tree.tag_configure('monospace', font='ariel 18')
                                    vsb = ttk.Scrollbar(w1, orient="vertical",command=tree.yview)
                                    vsb.place(x=1453, y=100, height=529)
                                    tree.place(x=50,y=100)
                                    tree.configure(style="Treeview",yscrollcommand=vsb.set)
                                    check4=0
                                    def Confirm_Return():
                                        cr.execute("delete from Fine where S_Userid=? and Book_Id=?",(y1,y2,))
                                        cr.execute("delete from Issue_Book where S_Userid=? and Book_Id=?",(y1,y2,))
                                        db.commit()
                                        try:
                                            data=cr.execute("select Quantity from Add_Book")
                                            for i in data:
                                                z=i[0]
                                            z1=int(z)+1
                                            cr.execute("update Add_Book set Quantity=? where Book_Id=?",(z1,y2))
                                            db.commit()
                                            w1.destroy()
                                            w.destroy()
                                            messagebox.showinfo("Info", "Book has been returned succesfully!")
                                        except:
                                            cr.execute("insert into Add_Book(Book_Id,Book_Name,Author_Name,Quantity)values(?,?,'','1')",(y2,y3,))
                                            db.commit()
                                            w1.destroy()
                                            w.destroy()
                                            messagebox.showinfo("Info", "Book has been returned succesfully!")
                                    data=cr.execute("select * from Fine where S_Userid=? and Book_Id=?",(y1,y2))
                                    flag=0
                                    for i in data:
                                        tree.insert("",END,values=i,tag='monospace')
                                        flag=1
                                    if flag==1:
                                        B=Button(w1,text='Confirm Return',font=('ariel 18'),fg='blue',padx=2,pady=1,command=Confirm_Return).place(x=687,y=635)
                                        w1.mainloop()
                                B=Button(w,text='Return',font=('ariel 18'),fg='blue',padx=2,pady=1,command=Return).place(x=687,y=635)
                                w.mainloop()
                        else:
                            messagebox.showerror("Error", "Invalid Students Id")
                    else:
                        messagebox.showwarning("Warning", "Userid cant be empty")
                B1=Button(w,text='View',font=('ariel 18'),fg='blue',padx=2,pady=1,command=Fine_Book).place(x=720,y=350)
                w.mainloop()
            
            def Update_details():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Update Details Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1100,760, 450, 80, fill="systembuttonface")
                L=Label(w,text='UPDATE OF STUDENT DETAILS',font=('Algerian 28'),fg='blue',relief='solid').place(x=520,y=20)
                L1=Label(w,text='FIRST NAME:',font=('ariel 18'),fg='blue').place(x=470,y=100)
                E1=Entry(w,font=('ariel 18'),textvar=F_name)
                E1.place(x=700,y=100)
                L2=Label(w,text='LAST NAME:',font=('ariel 18'),fg='blue').place(x=470,y=160)
                E2=Entry(w,font=('ariel 18'),textvar=L_name)
                E2.place(x=700,y=160)
                L3=Label(w,text='MIDDLE NAME:',font=('ariel 18'),fg='blue').place(x=470,y=220)
                E3=Entry(w,font=('ariel 18'),textvar=M_name)
                E3.place(x=700,y=220)
                L4=Label(w,text='DATE OF BIRTH :\n(DD/MM/YYYY)',font=('ariel 18'),fg='blue').place(x=470,y=280)
                E4=Entry(w,font=('ariel 18'),textvar=DOB)
                E4.place(x=700,y=280)
                L5=Label(w,text='ADDRESS:',font=('ariel 18'),fg='blue').place(x=470,y=350)
                E5=Entry(w,font=('ariel 18'),textvar=Addr)
                E5.place(x=700,y=350)
                L6=Label(w,text='CITY:',font=('ariel 18'),fg='blue').place(x=470,y=410)
                E6=Entry(w,font=('ariel 18'),textvar=City)
                E6.place(x=700,y=410)
                L7=Label(w,text='STATE:',font=('ariel 18'),fg='blue').place(x=470,y=470)
                choices = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarg','Goa','Gujrat','Haryana','Himachak Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharastra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajastjan','Sikkim','Tamil Nadu','Teleangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
                popupMenu = OptionMenu(w,State,*choices).place(x=560,y=470)
                State.set('Select State')
                L7_1=Label(w,text='Phone No: +91-',font=('ariel 16'),fg='blue').place(x=670,y=470)
                E7_1=Entry(w,font=('ariel 18'),textvar=Phn_no)
                E7_1.place(x=825,y=470)
                L8=Label(w,text='GENDER:',font=('ariel 18'),fg='blue').place(x=470,y=530)
                R1=Radiobutton(w,text='Male',variable=Gender,value='Male',font=('ariel 16')).place(x=590,y=530)
                R2=Radiobutton(w,text='Female',variable=Gender,value='Female',font=('ariel 16')).place(x=680,y=530)
                R3=Radiobutton(w,text='Other',variable=Gender,value='Other',font=('ariel 16')).place(x=790,y=530)
                Gender.set('Male')
                L8=Label(w,text='USER ID:',font=('ariel 18'),fg='blue').place(x=470,y=590)
                E8=Entry(w,font=('ariel 18'),textvar=S_Userid)
                E8.place(x=700,y=590)
                L9=Label(w,text='PASSWORD:',font=('ariel 18'),fg='blue').place(x=470,y=650)
                E9=Entry(w,font=('ariel 18'),textvar=S_Pass,show='*')
                E9.place(x=700,y=650)
                def update_student():
                    a=F_name.get()
                    b=L_name.get()
                    c=M_name.get()
                    d=DOB.get()
                    e=Addr.get()
                    f=City.get()
                    g=State.get()
                    h=Gender.get()
                    i=Phn_no.get()
                    j=S_Userid.get()
                    k=S_Pass.get()
                    if len(a)>0 and len(b)>0 and len(d)>0 and len(e)>0 and len(f)>0 and len(g)>0 and len(h)>0 and len(i)>0 and len(j)>0 and len(k)>0:
                        if len(k)<6:
                            messagebox.showwarning("Warning", "Password need to be atleast 6 characters!")
                        else:
                            data=cr.execute("select S_Userid from Students")
                            for l in data:
                                x=l[0]
                                if x==j:
                                    flag=1
                                    break
                                else:
                                    flag=0
                            if flag==1:
                                cr.execute("update Students Set F_name=?, L_name=?, M_name=?, DOB=?, Addr=?, City=?, State=?, Gender=?, Phn_no=?, S_Pass=? where S_Userid=?",(a,b,c,d,e,f,g,h,i,k,j))
                                db.commit()
                                E1.delete(0,END)
                                E2.delete(0,END)
                                E3.delete(0,END)
                                E4.delete(0,END)
                                E5.delete(0,END)
                                E6.delete(0,END)
                                E7_1.delete(0,END)
                                E8.delete(0,END)
                                E9.delete(0,END)
                                messagebox.showinfo("Info", "Students information has beeen updated succesfully!")
                            else:
                                messagebox.showerror("Error", "No students with this Userid was found!")
                    else:
                        messagebox.showwarning("Warning", "One or more filed is empty!")
                B1=Button(w,text='UPDATE',font=('ariel 18'),fg='blue',padx=2,pady=1,command=update_student).place(x=720,y=700)
                w.mainloop()
            B3=Button(w,padx=10,pady=10,text='ADD BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Add_book).place(x=38,y=170)
            B4=Button(w,padx=10,pady=10,text='SEARCH BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Search_book).place(x=270,y=170)
            B5=Button(w,padx=10,pady=10,text='UPDATE BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Update_book).place(x=520,y=170)
            B6=Button(w,padx=10,pady=10,text='VIEW BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=View_book).place(x=785,y=170)
            B7=Button(w,padx=10,pady=10,text='DELETE BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Delete_book).place(x=1025,y=170)
            B8=Button(w,padx=10,pady=10,text='ISSUE BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Issue_book).place(x=1280,y=170)
            B9=Button(w,padx=10,pady=10,text=' VIEW ISSUED BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=View_issued_book).place(x=10,y=440)
            B10=Button(w,padx=10,pady=10,text='ADD Students',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Add_students).place(x=315,y=440)
            B11=Button(w,padx=10,pady=10,text='DELETE Students',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Delete_students).place(x=580,y=440)
            B12=Button(w,padx=10,pady=10,text='CHANGE PASSWORD',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Change_pass).place(x=845,y=440)
            B13=Button(w,padx=10,pady=10,text='RETURN BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Return_Book).place(x=1100,y=440)
            B14=Button(w,padx=10,pady=10,text='EXIT',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=w.destroy).place(x=710,y=720)
            B15=Button(w,padx=10,pady=10,text='UPDATE DETAILS',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Update_details).place(x=1300,y=440)
            w.mainloop()
        else:
            messagebox.showerror("Error", "Wrong Userid or Password") 
    B1=Button(w1,text='Login',font=('ariel 18 bold'),bg='orange',command=Login).place(x=720,y=500)
    w1.mainloop()
def students():
    w1=Toplevel()
    w1.title("Students Login")
    canvas=Canvas(w1,width=2000,height=2000)
    canvas.pack()
    image=PhotoImage(file='Library background.png')
    image_1=PhotoImage(file='student.png')
    image_2=PhotoImage(file='password.png')
    canvas.create_image(0,0, image=image,anchor=NW)
    L1=Label(w1,image=image_1).place(x=640,y=310)
    L2=Label(w1,image=image_2).place(x=640,y=400)
    L1=Label(w1,text='Welcome To Student Page',font=('Algerian 38'),fg='blue',relief='solid').place(x=395,y=80)
    canvas.create_rectangle(1000,600, 500, 150, fill="lightyellow")
    canvas.create_text(750,230,fill="orange",font=("ariel 25 bold"),text="LOGIN WINDOW")
    canvas.create_text(560,340,fill="blue",font=("ariel 16"),text="USER ID")
    E1=Entry(w1,font=('ariel 16'),textvar=S_Userid)
    E1.place(x=720,y=325)
    canvas.create_text(570,425,fill="blue",font=("ariel 16"),text="PASSWORD")
    E2=Entry(w1,font=('ariel 16'),textvar=S_Pass,show='*')
    E2.place(x=720,y=410)

    def Login():
        x=v=S_Userid.get()
        y=S_Pass.get()
        cr.execute("select S_Userid,S_Pass from Students")
        data=cr.fetchall()
        check=0
        for i in data:
            a=i[0]
            b=i[1]
            if x==a and y==b:
                check=1
                break
            else:
                check=0
        if check==1:
            E1.delete(0,END)
            E2.delete(0,END)
            w1.destroy()
            w=Toplevel()
            w.title("students Menu")
            canvas=Canvas(w,width=2000,height=2000)
            canvas.pack()
            image=PhotoImage(file='Library background.png')
            canvas.create_image(0,0, image = image,anchor=NW)
            my_photo1=PhotoImage(file='search-book.png')
            Search_book_Frame=Frame(w,bg='white')
            Search_book_Frame.place(x=300,y=50)
            logo1=Label(Search_book_Frame,image=my_photo1).grid(row=0,column=0,padx=1,pady=1)
            my_photo2=PhotoImage(file='view-book.png')
            view_book_Frame=Frame(w,bg='white')
            view_book_Frame.place(x=550,y=50)
            logo2=Label(view_book_Frame,image=my_photo2).grid(row=0,column=0,padx=1,pady=1)
            my_photo3=PhotoImage(file='changepass.png')
            exit_book_Frame=Frame(w,bg='white')
            exit_book_Frame.place(x=860,y=50)
            logo3=Label(exit_book_Frame,image=my_photo3).grid(row=0,column=0,padx=1,pady=1)
            my_photo4=PhotoImage(file='exit-book.png')
            exit_book_Frame=Frame(w,bg='white')
            exit_book_Frame.place(x=1135,y=50)
            logo4=Label(exit_book_Frame,image=my_photo4).grid(row=0,column=0,padx=1,pady=1)
            def Search_book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Search Book Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                canvas.create_rectangle(1300,760, 200, 80, fill="systembuttonface")
                L=Label(w,text='SERACH BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=600,y=20)
                L1=Label(w,text='SEARCH BOOK BY',font=('ariel 18'),fg='blue').place(x=600,y=220)
                L2=Label(w,text='BOOK ID:',font=('ariel 18'),fg='blue').place(x=230,y=400)
                E2=Entry(w,font=('ariel 18'),textvar=Book_Id)
                E2.place(x=350,y=400)
                L3=Label(w,text='OR',font=('ariel 18'),fg='blue').place(x=700,y=400)
                L4=Label(w,text='BOOK NAME:',font=('ariel 18'),fg='blue').place(x=830,y=400)
                E4=Entry(w,font=('ariel 18'),textvar=Book_Name)
                E4.place(x=1000,y=400) 
                def View_Book1():
                    a=Book_Id.get()
                    b=Book_Name.get()
                    if len(a)==0 and len(b)==0:
                        messagebox.showwarning("Warning", "Please enter book id or book name")
                    elif len(a)!=0 and len(b)==0:
                        data=cr.execute("select Book_Id from Add_Book")
                        flag=0
                        for i in data:
                            x=i[0]
                            if x==a:
                                flag=1
                                break
                            else:
                                flag=0
                        if flag==1:
                            w=Toplevel()
                            w.geometry('2000x2000')
                            w.title("Specific Book Page")
                            canvas=Canvas(w,width=2000,height=2000)
                            canvas.pack()
                            image=PhotoImage(file='Library background.png')
                            canvas.create_image(0,0, image = image,anchor=NW)
                            L=Label(w,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                            style = ttk.Style()
                            style.configure("Treeview.Heading", font=("ariel 18 bold"))
                            style.configure("Treeview", rowheight=50)
                            tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4"), show='headings',selectmode='browse')
                            tree.heading("#1", text="Book Id")
                            tree.heading("#2", text="Book Name")
                            tree.heading("#3", text="Author Name")
                            tree.heading("#4", text="Quantity")
                            tree.tag_configure('monospace', font='ariel 18')
                            vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                            vsb.place(x=1143, y=100, height=529)
                            tree.place(x=340,y=100)
                            tree.configure(style="Treeview",yscrollcommand=vsb.set)
                            data=cr.execute("select * from Add_Book where Book_Id=?",(a,))
                            flag=0
                            for i in data:
                                tree.insert("",END,values=i,tag='monospace')
                                flag=1
                        else:
                            messagebox.showerror("Error", "Invalid Book Id")
                        if flag==1:
                            E2.delete(0,END)
                            w.mainloop()
                    elif len(b)!=0 and len(a)==0:
                        flag=1
                        if flag==1:
                            w=Toplevel()
                            w.geometry('2000x2000')
                            w.title("Specific Book Page")
                            canvas=Canvas(w,width=2000,height=2000)
                            canvas.pack()
                            image=PhotoImage(file='Library background.png')
                            canvas.create_image(0,0, image = image,anchor=NW)
                            L=Label(w,text='BOOK LIST',font=('Algerian 28'),fg='blue',relief='solid').place(x=650,y=20)
                            style = ttk.Style()
                            style.configure("Treeview.Heading", font=("ariel 18 bold"))
                            style.configure("Treeview", rowheight=50)
                            tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4"), show='headings',selectmode='browse')
                            tree.heading("#1", text="Book Id")
                            tree.heading("#2", text="Book Name")
                            tree.heading("#3", text="Author Name")
                            tree.heading("#4", text="Quantity")
                            tree.tag_configure('monospace', font='ariel 18')
                            vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                            vsb.place(x=1143, y=100, height=529)
                            tree.place(x=340,y=100)
                            tree.configure(style="Treeview",yscrollcommand=vsb.set)
                            data=cr.execute("select * from Add_Book where Book_Name like ?",(b+'%',))
                            flag=0
                        for i in data:
                            tree.insert("",END,values=i,tag='monospace')
                            flag=1
                        if flag==1:
                            E4.delete(0,END)
                            w.mainloop() 
                        else:
                            w.destroy()
                            messagebox.showerror("Error", "No book with this name was found!")
                    else:
                        messagebox.showwarning("Warning", "Please enter either Book Id or Book name")
                B1=Button(w,text='SEARCH',font=('ariel 18'),fg='blue',padx=2,pady=1,command=View_Book1).place(x=670,y=600)
                w.mainloop()
            def View_book():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("View Book Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                L=Label(w,text='VIEW BOOK',font=('Algerian 28'),fg='blue',relief='solid').place(x=600,y=20)
                style = ttk.Style()
                style.configure("Treeview.Heading", font=("ariel 18 bold"))
                style.configure("Treeview", rowheight=50)
                tree= ttk.Treeview(w, column=("column1", "column2", "column3", "column4", "Column5", "column6", "column7"), show='headings',selectmode='browse')
                tree.heading("#1", text="First Name")
                tree.heading("#2", text="Last Name")
                tree.heading("#3", text="Userid")
                tree.heading("#4", text="Bookid")
                tree.heading("#5", text="Book Name")
                tree.heading("#6", text="Issue Date")
                tree.heading("#7", text="Return Date")
                tree.tag_configure('monospace', font='ariel 18')
                vsb = ttk.Scrollbar(w, orient="vertical",command=tree.yview)
                vsb.place(x=1453, y=100, height=529)
                tree.place(x=50,y=100)
                tree.configure(style="Treeview",yscrollcommand=vsb.set)
                data=cr.execute("select S_Userid from Issue_Book")
                check=0
                for i in data:
                    a=i[0]
                    if a==v:
                        check=1
                        break
                    else:
                        check=0
                if check==1:
                    def Book_View():
                        data=cr.execute("select F_name,L_name,S_Userid,Book_Id,Book_Name,Issue_Date,Return_Date from Issue_Book where S_Userid=?",(a,))
                        for i in data:
                            tree.insert("",END,values=i,tag='monospace')
                    B=Button(w,text='View',font=('ariel 18'),fg='blue',padx=2,pady=1,command=Book_View).place(x=687,y=635)
                    w.mainloop()
                else:
                    w.destroy()
                    messagebox.showwarning("Warning", "No book has been issued to you!")
            def Change_pass():
                w=Toplevel()
                w.geometry('2000x2000')
                w.title("Change Password Page")
                canvas=Canvas(w,width=2000,height=2000)
                canvas.pack()
                image=PhotoImage(file='Library background.png')
                canvas.create_image(0,0, image = image,anchor=NW)
                L=Label(w,text='CHANGE STUDENT PASSWORD',font=('Algerian 28'),fg='blue',relief='solid').place(x=500,y=20)
                canvas.create_rectangle(1200,700,300,80, fill="systembuttonface")
                L1=Label(w,text='USER ID:',font=('ariel 18'),fg='blue').place(x=520,y=200)
                E1=Entry(w,font=('ariel 18'),textvar=S_Userid1)
                E1.place(x=650,y=200)
                L2=Label(w,text='OLD PASSWORD:',font=('ariel 18'),fg='blue').place(x=520,y=300)
                E2=Entry(w,font=('ariel 18'),textvar=S_Pass1,show='*')
                E2.place(x=750,y=300)
                L3=Label(w,text='NEW PASSWORD:',font=('ariel 18'),fg='blue').place(x=520,y=400)
                E3=Entry(w,font=('ariel 18'),textvar=S_new_pass,show='*')
                E3.place(x=750,y=400)
                def S_pass_change():
                    x=S_Userid1.get()
                    y=S_Pass1.get()
                    z=S_new_pass.get()
                    cr.execute("select S_Userid,S_Pass from Students")
                    data=cr.fetchall()
                    for i in data:
                        a=i[0]
                        b=i[1]
                        if x==a and y==b:
                            check=1
                            break
                        else:
                            check=0
                    if check==1:
                        if len(z)>0 and z!=y:
                            if len(z)<6:
                                messagebox.showwarning("Warning", "Password need to be atleast 6 characters")
                            else:
                                cr.execute("update Students set S_Pass=? where S_Userid=?",(z,x))
                                db.commit()
                                E1.delete(0,END)
                                E2.delete(0,END)
                                E3.delete(0,END)
                                messagebox.showinfo("info", "Password has been changed succesfully!")
                        elif z==y:
                            messagebox.showwarning("Warning","Old and new password Cant be same")
                        else:
                            messagebox.showwarning("Warning","One or more filled is emepty")
                    else:
                        messagebox.showerror("Error", "Wrong Userid or Old password")
                B1=Button(w,text='CHANGE PASSWORD',font=('ariel 18'),fg='blue',padx=2,pady=1,command=S_pass_change).place(x=600,y=600)
                w.mainloop()
            B1=Button(w,padx=10,pady=10,text='SEARCH BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Search_book).place(x=270,y=170)
            B2=Button(w,padx=10,pady=10,text='VIEW BOOK',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=View_book).place(x=535,y=170)
            B3=Button(w,padx=10,pady=10,text='CHANGE PASSWORD',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=Change_pass).place(x=800,y=170)
            B4=Button(w,padx=10,pady=10,text='EXIT',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=w.destroy).place(x=1150,y=170)
            w.mainloop()
        else:
            messagebox.showerror("Error", "Wrong Userid or Password")
    B1=Button(w1,text='Login',font=('ariel 18 bold'),bg='orange',command=Login).place(x=720,y=500)
    w1.mainloop()                                
B1=Button(m,padx=10,pady=10,text='ADMIN',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=admin).place(x=370,y=650)
B2=Button(m,padx=10,pady=10,text='STUDENTS',font=('Algerian',15),bg='orange',fg='red',relief='solid',command=students).place(x=890,y=650)
m.mainloop()
