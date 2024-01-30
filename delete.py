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
wi.title('Membership Page')
wi.resizable(width='True',height='True')
wi.configure(fg_color='#F5F5F5')


def deleteb():
    f=open('stock.csv','r+',newline='')
    q=label1.get()
    r=csv.reader(f)
    l=[]
    for i in r:
        l+=[i]
    f.close()
    f=open('stock.csv','a+',newline='')
    f1=open('temp.csv','w+',newline='')
    for i in l:
        if i[0]==str(q):
            pass
        else:
            twr=csv.writer(f1)
            twr.writerow(i)
    f.close()
    f1.close()
    os.remove('stock.csv')
    os.rename('temp.csv','stock.csv')


bgimg=CTkImage(light_image=Image.open('bg6.jpg'),size=(800,800))
bg=CTkLabel(master=wi,text='',image=bgimg)
bg.pack(fill='y',side='left')

f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

l0=CTkLabel(master=f1,text='Delete a Book',font=('century gothic',50),text_color='#333')
l0.place(relx=0.13,rely=0.2)

label1=CTkEntry(master=f1,width=350,placeholder_text='Enter Book ID for deletion:',height=40,fg_color='#A8A9A8',
               placeholder_text_color='white',text_color='white')
label1.place(relx=0.15 ,rely=0.35)

delete=CTkButton(master=wi,text='Delete',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
               fg_color='#747574',border_width=2,border_color='#333',text_color='white',command=deleteb)
delete.place(relx=0.73,rely=0.55,anchor='center')
Exit=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
               fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=wi.destroy)
Exit.place(relx=0.83,rely=0.55,anchor='center')
wi.mainloop()
