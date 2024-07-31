from tkinter import *
import mysql.connector
from tkinter import messagebox as m
from PIL import Image,ImageTk
from tkinter import ttk

db=mysql.connector.connect(host="localhost",user="root",password="W7301@jqir#",database="login")
c=db.cursor()

def opensignup():
    top1=Toplevel()
    top1.geometry("400x680")
    top1.minsize(695,400)
    top1.maxsize(695,400)
    top1.title("Sign Up")
    top1.configure(bg="White")
        
    # open_1() :  total database insersion

    def minimize():
        top1.iconify()

    def open_1():
        check_1=e10.get()
        if check_1==1:
            pasw=e8.get()
            pasw_c=e9.get()
            if pasw != pasw_c:
                entry_9.config(highlightbackground = "red",highlightcolor="Red")
                #m.askretrycancel("Error","Password dosn't match")
            else:
                entry_9.config(highlightbackground = "green",highlightcolor="green")
                fn=e1.get()
                ln=e2.get()
                ph=e3.get()
                al=e4.get()
                age=e5.get()
                add=e6.get()
                user=e7.get()
                t=(fn,ln,ph,al,age,add,user,pasw)
                e7.set("")
                e8.set("")
                e9.set("")
                if fn=="" or ln=="" or ph=="" or al=="" or age=="" or add=="" or user=="" or pasw=="" or pasw_c=="" or check_1=="": m.askretrycancel("Failed","Enter The Data....")
                else:
                    a=1
                    c.execute("select * from details") 
                    r=c.fetchall()
                    # password check: it dose exist or not
                    for k in range(0,len(r)):
                        x=r[k]
                        if x[7]==pasw: a=0
                    if a==0: m.showerror("Error","Password Already Exist...")
                    else:
                        b=e=d=1
                        # Password check: It correct or not
                        for k1 in range(0,len(pasw)):
                            if pasw[k1].isalnum()==True: b=0
                            if pasw[k1].isdigit()==True: e=0
                            if pasw[k1].isupper()==True: d=0
                        if b==e==d==0:
                            s="INSERT INTO details values(%s,%s,%s,%s,%s,%s,%s,%s)"
                            c.execute(s,t)
                            db.commit()
                            m.showinfo("Info","Sign in Successfull")
                            minimize()
                        else: m.showwarning("Error","Make a strong Password....")

        else: m.askretrycancel("Error","Fill the check box...")


    book=ttk.Notebook(top1)
    book.pack(fill=BOTH)

    #la=Label(top1,text="",font=("Helvetica",13,"bold"),bg="#00F2DE")
    #la.pack(fill=X,pady=5)

    #first label frame

    f1=LabelFrame(book,bg="White",borderwidth=0,height=600,width=700)
    
    # all label

    la_1=Label(f1,text="First Name:",font=("Arial",12,"bold"),bg="White")
    la_2=Label(f1,text="Last Name:",font=("Arial",12,"bold"),bg="White")
    la_3=Label(f1,text="Phone Number:",font=("Arial",12,"bold"),bg="White")
    la_4=Label(f1,text="Alternet Number:",font=("Arial",12,"bold"),bg="White")
    la_5=Label(f1,text="Age:",font=("Arial",12,"bold"),bg="White")
    la_6=Label(f1,text="Address:",font=("Arial",12,"bold"),bg="White")
    
    # All Value Variables

    e1=StringVar()
    e2=StringVar()
    e3=StringVar()
    e4=StringVar()
    e5=IntVar()
    e6=StringVar()

    e7=StringVar()
    e8=StringVar()
    e9=StringVar()

    e10=IntVar()


    # all Entry Wedgits

    entry_1=Entry(f1,textvariable=e1,borderwidth=1,width=30,relief="sunken",bg="White")
    entry_2=Entry(f1,textvariable=e2,borderwidth=1,width=30,relief="sunken",bg="White")
    entry_3=Entry(f1,textvariable=e3,borderwidth=1,width=30,relief="sunken",bg="White")
    entry_4=Entry(f1,textvariable=e4,borderwidth=1,width=30,relief="sunken",bg="White")
    entry_5=Entry(f1,textvariable=e5,borderwidth=1,width=30,relief="sunken",bg="White")
    entry_6=Entry(f1,textvariable=e6,borderwidth=1,width=55,relief="sunken",bg="White")
    
    f1.pack(fill=BOTH,padx=10,pady=20,anchor="center",expand=1)

    # all Gridings

    la_1.grid(row=0,column=0,padx=5,pady=10)
    la_2.grid(row=0,column=2,padx=5,pady=10)
    la_3.grid(row=1,column=0,padx=5,pady=10)
    la_4.grid(row=1,column=2,padx=5,pady=10)
    la_5.grid(row=2,column=0,padx=5,pady=10)
    la_6.grid(row=3,column=0,pady=10)

    entry_1.grid(row=0,column=1,padx=5,pady=10)
    entry_2.grid(row=0,column=3,padx=5,pady=10)
    entry_3.grid(row=1,column=1,padx=5,pady=10)
    entry_4.grid(row=1,column=3,padx=5,pady=10)
    entry_5.grid(row=2,column=1,padx=5,pady=10)
    entry_6.grid(row=3,column=1,pady=10,columnspan=2)

    #la1=Label(top1,text="",font=("Helvetica",13,"bold"),bg="#00F2DE")
    #la1.pack(fill=X,pady=30)

    #Second label frame

    f2=LabelFrame(book,borderwidth=0,bg="White",height=600,width=700)
    f2.pack(fill=BOTH,padx=10,pady=5,anchor="center",expand=1)

    la_7=Label(f2,text="Set Username:",font=("Arial",12,"bold"),bg="White")
    la_8=Label(f2,text="Set Password:",font=("Arial",12,"bold"),bg="White")
    la_9=Label(f2,text="Conform Password:",font=("Arial",12,"bold"),bg="White")
    
    entry_7=Entry(f2,textvariable=e7,borderwidth=1,width=30,relief="sunken",bg="White")
    entry_8=Entry(f2,textvariable=e8,borderwidth=1,width=30,relief="sunken",bg="White")
    entry_9=Entry(f2,textvariable=e9,borderwidth=1,width=30,relief="sunken",highlightthickness=2,bg="White",show=u"\u00b0")

    la_7.grid(row=0,column=0,padx=5,pady=10)
    la_8.grid(row=0,column=2,padx=5,pady=10)
    la_9.grid(row=1,column=0,padx=5,pady=10)

    entry_7.grid(row=0,column=1,padx=5,pady=10)
    entry_8.grid(row=0,column=3,padx=5,pady=10)
    entry_9.grid(row=1,column=1,padx=5,pady=10)

    check=Checkbutton(f2,text="I fill up this sign up form for myself to the best of my knowledge.",font=("Helvetica",9,"bold"),bg="White",variable=e10)

    #check.pack(fill=X,padx=30,pady=5,anchor="center")
    check.grid(row=2,column=0,padx=5,pady=10,columnspan=6)

    b2=Button(f2,text="Submit",font=("Arial",10,"bold"),bg="White",borderwidth=1,width=10,relief="ridge",command=open_1)

    #b2.pack(padx=30,pady=20,anchor="center")
    b2.grid(row=3,column=0,padx=5,pady=10,columnspan=6)

    book.add(f1,text="Personal Information")
    book.add(f2,text="Log-in Details")

    


