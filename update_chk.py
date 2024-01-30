import csv, os
import customtkinter as ct
from customtkinter import *
from PIL import Image
from tkinter import messagebox as mg
import tkinter as tk
from datetime import datetime, timedelta
import csv,os
import random as r
from tkinter import messagebox
ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk()
wi.geometry('1400x800')
wi.title('Stock')
wi.resizable(width='True',height='True')
wi.configure(fg_color='#F5F5F5')
bgimg=CTkImage(light_image=Image.open('bg5.jpg'),size=(800,800))
bg=CTkLabel(master=wi,text='',image=bgimg)
bg.pack(fill='y',side='left')

bkid=CTkEntry(master=wi,width=400,placeholder_text='Enter the Book ID:',height=40,placeholder_text_color='white',text_color='white')
bkid.place(relx=0.65 ,rely=0.25)

l1=[]


def check():
    f=open('stock.csv','r+',newline='')
    q=str(bkid.get())
    r=csv.reader(f)
    l=[]
    for i in r:
       l+=[i]
    f1=open('temp.csv','w+',newline='')
    tr=csv.writer(f1)
    tr.writerow(['Book ID','Book Name','Genre','Stock','Author','Price','Shelf number','Row number'])
    f1.close()

    f12=open('temp.csv','a+',newline='')
    twr=csv.writer(f12)
    tlid=[]
    for i in l:
        tlid.append(i[0])
    print (tlid)
    if q not in tlid:
        messagebox.showerror('Error','Given Book ID is not found')
        for i in l:
            if i[0]==q:
                pass
            elif i[0]=='Book ID':
                pass
            else:
                twr.writerow(i) 
    
    elif q in tlid:
        messagebox.showinfo('Proceed?','Are you sure to proceed with updating details?')
        for i in l:
            if i[0]==q:
                f2=open ('deleted_books.csv','w',newline='')
                ob=csv.writer(f2)
                ob.writerow(i)
                f2.close()
                f12.close()
                import Update_adding
            elif i[0]=='Book ID':
                pass
            else:
                f12=open('temp.csv','a+',newline='')
                twr=csv.writer(f12)
                twr.writerow(i)
    f12.close()
    f.close()
    os.remove('stock.csv')
    os.rename('temp.csv','stock.csv')

ch=CTkButton(master=wi,text='Continue',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
             fg_color='#747574',border_width=3,border_color='#333',text_color=('white'),command=check)
ch.place(relx=0.8,rely=0.45,anchor='center')
wi.mainloop()