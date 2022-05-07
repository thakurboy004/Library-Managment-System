
from tkinter import*
import pymysql
import os
import pymysql.cursors
from tkinter import messagebox
import random
import datetime
from PIL import Image,ImageTk
from tkinter import ttk

wi=Tk()
wi.title("Strak Public Library")
wi.geometry("2000x900")

def clicked1():
   path='List.rtf'
   os.system(path)

def clicked2():
    win2=Tk()
    win2.title("Request a book")
    win2.config(bg="grey")
    win2.geometry('700x200')
    bk=StringVar()
    us=StringVar()
    print(us)
    print(bk)
    
    def select():
       li=["The Divine Comedy","Leaves of Grass","The Complete Poetry Of Edgar Allan Poe","Robert Frost’s Poems","100 Selected Poems",
        "The Complete Poetry ","Selected Poems","Ariel","The Waste Land and Other Poems","The Essential Neruda: Selected Poems",
        "The Penguin Anthology of Twentieth-Century","The Essential Rumi","The Complete Sonnets and Poems","On Love and Barley: Haiku of Basho",
        "Songs of Innocence and Experience","The Complete Poems of Emily Dickinson","Selected Poetry","Lyrical Ballads","The Collected Poems",
        "If Not, Winter: Fragments of Sappho","Then She Was Gone: A Novel","Before We Were Yours","Where the Crawdads Sing","The Silent Wife",
        "Small Great Things: A Novel","Another Love","Click","Twelve Patients: Life and Death at Bellevue Hospital",
        "My Brother's Bad Best Friend","That Christmas Eve: A Brother's Bestfriend Baby Romance","Killer by Nature: An Audible Original Drama",
        "Neverwhere","The X-Files: Cold Cases","Alien: Out of the Shadows","Secrets of Our House","The Secret Love Letters of Olivia Moretti",
        "The Winter Rose","Her Darling Mr. Day","Apples Never Fall","These Tangled Vines","Come to the Edge","The Book Thief","Pride and Prejudice",
        "The Name of the Wind","Call Me by Your Name","Atonement","The Short Life of Sparrows","The Highwayman","Great Tales and Poems","Lonesome Dove",
        "A Midsummer Night's Dream","Dictionary of the Khazars","The Last Unicorn","The Art of Racing in the Rain","The Adventures of Huckleberry Finn",
        "Blood Meridian, or the Evening Redness in the West","The Sky Is Everywhere","The Road","Silk","The Awakening","Between the World and Me",
        "The Emperor of All Maladies: A Biography of Cancer","The Sixth Extinction: An Unnatural History","How to Survive a Plague",
        "The Art of Cruelty: A Reckoning","How to Do Nothing","100 Essays I Don’t Have Time to Write","An Indigenous Peoples’ History of the United States",
        "The New Jim Crow","The Year of Magical Thinking","Sapiens: A Brief History of Humankind","Thinking, Fast and Slow","A Short History of Nearly Everything",
        "When Breath Becomes Air","Moneyball: The Art of Winning an Unfair Game","Evicted: Poverty and Profit in the American City","Alexander Hamilton",
        "Dreamland","The Warmth of Other Suns"]

    
       now=datetime.datetime.now()
       print(us)
       print(bk)
       b=now.strftime("%d-%m-%y")
       c=us.get()
       a2=bk.get()
       print(c)
       print(b)
       print(a2)
       conn=pymysql.connect(host="localhost", user="root", password="", db="library")
       a=conn.cursor()
       a.execute("select*from users where username='"+c+"'")
       result=a.fetchall()
       count=a.rowcount
       if(count>0):
          for i in li:
             if(a2==i):
                d=conn.cursor()
                d.execute("insert into books(username,book_name,sanction_date,submission_date)values('"+c+"','"+a+"','"+b+"')")
                conn.commit()
                conn.rollback()
                conn.close()
             if(a2!=i):
                messagebox.showinfo("Message","Book is Unavailable")
                
                
             
             
       else:
          messagebox.showerror("Error","Username is Incorrect")

    
    lb1=Label(win2, text="Enter Username:", font=("italic", 20, "bold"), bg="grey")
    lb1.grid(row=0,column=0,pady=10)
    tb1=Entry(win2, textvariable=us, font=("italic", 20, 'bold'))
    tb1.grid(row=0, column=1,pady=10)

    lb2=Label(win2, text="Enter the name of book:", font=("italic", 20, "bold"), bg="grey")
    lb2.grid(row=1,column=0,pady=10)
    tb2=Entry(win2, textvariable=bk, font=("italic", 20, 'bold'))
    tb2.grid(row=1, column=1,pady=10)

    btn=Button(win2, text="Borrow", font=("italic", 20, "bold"), bd=0, bg="yellow", command=select)
    btn.grid(row=2, column=0,pady=10)


    
    win2.mainloop()
def clicked3():
    win3=Tk()
    win3.title("Return a book")
    win3.config(bg="grey")
    win3.geometry("900x300")

    def data():
       now2=datetime.datetime.now()
       b3=now2.strftime("%d-%m-%y")
       r2=bk2.get()
       conn=pymysql.connect(host="localhost", user="root", password="", db="library")
       g=conn.cursor()
       g.execute("insert into books (submission_date) values('"+b3+"') where book_name='"+r2+"' and username='"+c+"'")
       conn.commit()
       conn.rollback()
       conn.close()
       

    
    bk2=StringVar()
    lb1=Label(win3, text="Enter the name of book:", font=("italic", 20, "bold"), bg="grey")
    lb1.grid(row=0, column=0, pady=10)
    tb1=Entry(win3, textvariable=bk2 , font=("italic", 20, 'bold'))
    tb1.grid(row=0, column=1, pady=10)

    btn1=Button(win3, text="Return", font=("italic", 20, "bold"), bd=0, bg="yellow", command=data)
    btn1.grid(row=2, column=0, pady=20)

    win3.mainloop()
    
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo 

image = Image.open('the-library-wallpaper.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(wi, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

s=StringVar()
br=StringVar()
li3=["The Divine Comedy","Leaves of Grass","The Complete Poetry Of Edgar Allan Poe","Robert Frost’s Poems","100 Selected Poems",
      "The Complete Poetry ","Selected Poems","Ariel","The Waste Land and Other Poems","The Essential Neruda: Selected Poems",
      "The Penguin Anthology of Twentieth-Century","The Essential Rumi","The Complete Sonnets and Poems","On Love and Barley: Haiku of Basho",
      "Songs of Innocence and Experience","The Complete Poems of Emily Dickinson","Selected Poetry","Lyrical Ballads","The Collected Poems",
      "If Not, Winter: Fragments of Sappho","Then She Was Gone: A Novel","Before We Were Yours","Where the Crawdads Sing","The Silent Wife",
      "Small Great Things: A Novel","Another Love","Click","Twelve Patients: Life and Death at Bellevue Hospital",
      "My Brother's Bad Best Friend","That Christmas Eve: A Brother's Bestfriend Baby Romance","Killer by Nature: An Audible Original Drama",
      "Neverwhere","The X-Files: Cold Cases","Alien: Out of the Shadows","Secrets of Our House","The Secret Love Letters of Olivia Moretti",
      "The Winter Rose","Her Darling Mr. Day","Apples Never Fall","These Tangled Vines","Come to the Edge","The Book Thief","Pride and Prejudice",
      "The Name of the Wind","Call Me by Your Name","Atonement","The Short Life of Sparrows","The Highwayman","Great Tales and Poems","Lonesome Dove",
      "A Midsummer Night's Dream","Dictionary of the Khazars","The Last Unicorn","The Art of Racing in the Rain","The Adventures of Huckleberry Finn",
      "Blood Meridian, or the Evening Redness in the West","The Sky Is Everywhere","The Road","Silk","The Awakening","Between the World and Me",
      "The Emperor of All Maladies: A Biography of Cancer","The Sixth Extinction: An Unnatural History","How to Survive a Plague",
      "The Art of Cruelty: A Reckoning","How to Do Nothing","100 Essays I Don’t Have Time to Write","An Indigenous Peoples’ History of the United States",
      "The New Jim Crow","The Year of Magical Thinking","Sapiens: A Brief History of Humankind","Thinking, Fast and Slow","A Short History of Nearly Everything",
      "When Breath Becomes Air","Moneyball: The Art of Winning an Unfair Game","Evicted: Poverty and Profit in the American City","Alexander Hamilton",
      "Dreamland","The Warmth of Other Suns"]
    

a=random.choices(li3)
print(a)
    

br=a[0]

f1=Frame(label, relief="groove", bd=10, bg="blue")
f1.pack(pady=20)
l1=Label(f1, text="Welcome To Stark Public Library", font=("italic", 20, "bold"), width=60, bg="yellow")
l1.grid(row=0, column=0)

f2=Frame(label, bd=0)
f2.pack(pady=30)
l2=Label(f2, text="Choose an option:", font=('italic', 20, 'bold'), width=40, fg="blue")
l2.grid(row=1, column=0, columnspan=2)

btn1=Button(f2, text="List all the books", bg="yellow", bd=0, font=('italic', 15, 'bold'), width=15, command=clicked1)
btn1.grid(row=2, column=0, pady=10)

btn1=Button(f2, text="Borrow a book", bg="yellow", bd=0, font=('italic', 15, 'bold'), width=15, command=clicked2)
btn1.grid(row=2, column=1, pady=10)

btn1=Button(f2, text="Return a book", bg="yellow", bd=0, font=('italic', 15, 'bold'), width=15, command=clicked3)
btn1.grid(row=3, column=0, pady=10)

btn1=Button(f2, text="Exit the Library", bg="yellow", bd=0, font=('italic', 15, 'bold'), width=15, command=wi.destroy)
btn1.grid(row=3, column=1, pady=10)

f3=Frame(label, bd=0)
f3.pack(pady=40)

l3=Label(f3, text="Best Seller Of The Day:" ,font=('italic', 20, 'bold'), width=40, fg="blue")
l3.grid(row=4, column=0, pady=10)

l3=Label(f3, text=br ,font=('italic', 20, 'bold'), fg="Red")
l3.grid(row=5, column=0, pady=10)

wi.mainloop()


