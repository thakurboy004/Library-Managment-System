from tkinter import*
from tkinter import messagebox
import os
import pymysql
import pymysql.cursors
from PIL import Image,ImageTk
from tkinter import ttk

win=Tk()
win.title("Login page")
win.geometry("2000x900")
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo 

image = Image.open('circular.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(win, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

user=StringVar()
passw=StringVar()
nam=StringVar()
phn_no=StringVar()
em=StringVar()

def clicked1():
    u=user.get()
    p=passw.get()
    n=nam.get()
    ph=phn_no.get()
    e=em.get()

    conn=pymysql.connect(host="localhost", user="root", password="", db="library")

    d=conn.cursor()
    d.execute("insert into users(username,name,phone_no,password,email)values('"+u+"','"+n+"','"+ph+"','"+p+"','"+e+"')")
    conn.commit()
    conn.rollback()
    conn.close()

f1=Frame(label, bd=10, relief="groove", bg="blue")
f1.pack(pady=10)
l1=Label(f1, bg="yellow", text="Stark Public Library", font=("italic", 20, "bold"), justify=CENTER, width=60)
l1.grid(row=0, column=0)

f2=Frame(label, bd=10, relief="groove", bg="grey")
f2.pack(pady=50)

l2=Label(f2, bg="yellow", text="Create Your Account", font=("italic", 20, "bold"), width=40)
l2.grid(row=2, column=0, columnspan=2, padx=20, pady=10)

l3=Label(f2, bg="grey", fg="black", text="Username:", font=("italic", 20, "bold") )
l3.grid(row=3, column=0, pady=20)
tb1=Entry(f2, textvariable=user, font=("italic", 20, "bold"))
tb1.grid(row=3, column=1, pady=20)

l4=Label(f2, bg="grey", fg="black", text="Password:", font=("italic", 20, "bold") )
l4.grid(row=4, column=0, pady=20)
tb2=Entry(f2, textvariable=passw, font=("italic", 20, "bold"))
tb2.grid(row=4, column=1, pady=20)

l5=Label(f2, bg="grey", fg="black", text="Name:", font=("italic", 20, "bold") )
l5.grid(row=5, column=0, pady=20)
tb3=Entry(f2, textvariable=nam, font=("italic", 20, "bold"))
tb3.grid(row=5, column=1, pady=20)

l6=Label(f2, bg="grey", fg="black", text="Phone No.:", font=("italic", 20, "bold") )
l6.grid(row=6, column=0, pady=20)
tb4=Entry(f2, textvariable=phn_no, font=("italic", 20, "bold"))
tb4.grid(row=6, column=1, pady=20)

l7=Label(f2, bg="grey", fg="black", text="E-mail:", font=("italic", 20, "bold") )
l7.grid(row=7, column=0, pady=20)
tb5=Entry(f2, textvariable=em, font=("italic", 20, "bold"))
tb5.grid(row=7, column=1, pady=20)

btn1=Button(f2, text="Sign Up", bg="yellow", font=("italic", 15, "bold"), command=clicked1, bd=0, width=10)
btn1.grid(row=8, column=0, pady=20)

btn2=Button(f2, text="Exit", bg="yellow", font=("italic", 15, "bold"), command=win.destroy, bd=0, width=10)
btn2.grid(row=8, column=1, pady=20)

win.mainloop()
