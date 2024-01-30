import customtkinter as ct
from customtkinter import *
from PIL import Image
from tkinter import messagebox as mg
import tkinter as tk
from datetime import datetime, timedelta
import csv,os
import random as r

def add_mem ():
    with open ('data.csv','a',newline='') as f :
        sturec=csv.writer(f)
        d={}
        start_date = start.get()
        try:
                start1 = datetime.strptime(start_date, '%d-%m-%Y')
               
        except ValueError:
                                mg.showinfo('Date Info', 'Invalid Date')
        expiration_date = start1 + timedelta(days=6*30)
        expiration_date = expiration_date.strftime('%d-%m-%Y') 
        memnam=un.get()
        phno=ph.get()
        ema=em.get()
        with open('mem_id.txt','r') as f:
                n=f.read().split()
        n=[int(i)for i in n]
        memid=r.choice(n)
        if len(phno)!=10:
                mg.showerror("Error","Invalid Phone Number")
        l=[memnam,phno,ema,start_date,expiration_date,memid]
        sturec.writerow(l)
        mg.showinfo("Information","Added succesfully")
def Clear():
   un.delete(0,END)
   ph.delete(0,END)
   em.delete(0,END)
   start.delete(0,END)
def exit():
    wi.destroy()
    import mem
ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk()
wi.geometry('1400x800')
wi.title('Membership Page')
wi.resizable(width='True',height='True')
wi.configure(fg_color='#F5F5F5')

bgimg=CTkImage(light_image=Image.open('bg2.jpg'),size=(800,800))
bg=CTkLabel(master=wi,text='',image=bgimg)
bg.pack(fill='y',side='left')

f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

l0=CTkLabel(master=f1,text='Add Membership',font=('century gothic',50),text_color='#333')
l0.place(relx=0.13,rely=0.1)

un=CTkEntry(master=f1,width=350,placeholder_text='UserName...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
un.place(relx=0.17,rely=0.3)
ph=CTkEntry(master=f1,width=350,placeholder_text='Phone Number...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
ph.place(relx=0.17,rely=0.4)
em=CTkEntry(master=f1,width=350,placeholder_text='Email Address...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
em.place(relx=0.17,rely=0.5)
start=CTkEntry(master=f1,width=350,placeholder_text='Date [dd-mm-yy]...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
start.place(relx=0.17,rely=0.6)

ad=CTkButton(master=wi,text='Add',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
             fg_color='#747574',border_width=2,border_color='#333',text_color='white',command=lambda:[add_mem(),Clear()])
ad.place(relx=0.74,rely=0.75,anchor='center')
ex=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
             fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=exit)
ex.place(relx=0.84,rely=0.75,anchor='center')

wi.mainloop()