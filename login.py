from tkinter import *
from signup import *
from tkinter import messagebox as m
from PIL import Image,ImageTk
import mysql.connector
r=Tk()
r.title("Login Portal")
# myico=PhotoImage(file="images/icon.png")
# r.iconphoto(False,myico)
r.geometry("700x420")
r.maxsize(700,420)
r.minsize(700,420)
r.configure(bg="White")

#Database Connection
db=mysql.connector.connect(host="localhost",user="root",password="W7301@jqir#",database="login")
c=db.cursor()

#Image Resize

im=Image.open("images/images (4).jpeg")
ima=im.resize((350,230))
image=ImageTk.PhotoImage(ima)

#All Functions For The Form

def minimize():
    r.iconify()

def signin():
    opensignup()

try:    
    def login():
        aa=1
        u=i.get()   #Username
        p=j.get()   #Password
        i.set("")
        j.set("")
        if u=="" or p=="": m.askretrycancel("Error","Not enough information")
        else:
            c.execute("select * from details")
            r=c.fetchall()
            for list_t in range(0,len(r)):
                point=r[list_t]
                if point[7]==p: 
                    aa=0
                    p1=point[0]
                    p2=point[1]
                    p3=point[2]
                    p4=point[3]
                    p5=point[4]
                    p6=point[5]
                    p7=point[6]
            if aa == 0:
                minimize()
                open_win(p1,p2,p3,p4,p5,p6,p7)
            else: m.showerror("INPUT ERROR","Access Denied")
except: m.showerror("Something wrong","Try Again later!")

def open_win(p1,p2,p3,p4,p5,p6,p7):

    r2=Toplevel()
    r2.geometry("1000x700")
    r2.configure(bg="White")

    Frame_h=LabelFrame(r2,borderwidth=0,bg="yellow")
    Frame_h.pack(fill=X)

    Frame_h1=LabelFrame(r2,borderwidth=0,bg="White")
    Frame_h1.pack(fill=X,pady=3)

    heading=Label(Frame_h,text=u"\u25CF "+f"Wellcome {p7}",font=("Arial",12,"bold"),bg="yellow")
    heading.pack(fill=X)

    fc_1=Label(Frame_h1,text=f"Name: {p1+p2}",font=("Arial",12,"bold"),bg="White")
    fc_2=Label(Frame_h1,text=f"Phone Number: {p3}",font=("Arial",12,"bold"),bg="White")
    fc_3=Label(Frame_h1,text=f"Alternet Number: {p4}",font=("Arial",12,"bold"),bg="White")
    fc_4=Label(Frame_h1,text=f"Age: {p5}",font=("Arial",12,"bold"),bg="White")
    fc_5=Label(Frame_h1,text=f"Address: {p6}",font=("Arial",12,"bold"),bg="White")

    fc_1.grid(row=0,column=0,padx=5)
    fc_2.grid(row=0,column=1,padx=5)
    fc_3.grid(row=0,column=2,padx=5)
    fc_4.grid(row=0,column=3,padx=5)
    fc_5.grid(row=1,column=0,columnspan=2) 


#All Labels and LabelFrams

f=LabelFrame(r,font=("Arial",15,"bold"),bg="White",borderwidth=0)                

l0=Label(image=image,borderwidth=0)
l_0=Label(f,text="User Login",fg="#02d9b1",bg="White",font=("Arial",16,"bold"))
l=Label(f,text="Username:",font=("Arial",12),bg="White")
l1=Label(f,text="Password:",font=("Arial",12),bg="White")
l2=Label(r,text="Don't have any account ?",font=("Helvetica",10),bg="White")

#All Entry Wegets

i=StringVar()
j=StringVar()

e=Entry(f,textvariable=i,borderwidth=0.5,width=27,relief="raised",bg="White")
e1=Entry(f,textvariable=j,borderwidth=0.5,width=27,relief="raised",bg="White",show="*")

#All Buttons

b=Button(f,text="login",font=("Arial",11,"bold"),bg="#45edce",borderwidth=1,width=10,relief="ridge",command=login)
b1=Button(r,text="sign up",font=("Helvetica",10,"bold"),bg="White",fg="#039e82",borderwidth=0,width=8,relief="flat",command=signin)

#All gridings


""" l0.grid(row=0,column=0,padx=20,pady=65)
f.grid(row=0,column=1,padx=10,columnspan=3)
l.grid(row=0,column=0,padx=5)
l1.grid(row=1,column=0,padx=5)
l2.grid(row=1,column=1)
e.grid(row=0,column=1,padx=4,pady=15,columnspan=2)
e1.grid(row=1,column=1,padx=3,pady=15)
b.grid(row=2,column=0,padx=5,pady=20,columnspan=2)
b1.grid(row=1,column=2) """


l0.grid(row=0,column=0,padx=20,pady=65)
f.grid(row=0,column=1,padx=10,columnspan=3)
l_0.grid(row=0,column=0,columnspan=2,pady=5)
l.grid(row=1,column=0,padx=5)
l1.grid(row=2,column=0,padx=5)
l2.grid(row=1,column=1)
e.grid(row=1,column=1,padx=4,pady=15,columnspan=2)
e1.grid(row=2,column=1,padx=3,pady=15)
b.grid(row=3,column=0,padx=5,pady=20,columnspan=2)
b1.grid(row=1,column=2)

r.mainloop()