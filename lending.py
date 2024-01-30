import customtkinter as ct
from customtkinter import *
from PIL import Image
from tkinter import messagebox as mg
import tkinter as tk
from datetime import datetime, timedelta
import csv,os

def buy ():
    with open ('lend.csv','a',newline='') as f:
        lend=csv.writer(f)
        l1=[]
        mid=mi.get()
        l=[]
        L=[]
        bookid=bi.get()
        duw=int(nd.get())
        c_date=datetime.now()
        Rdate = c_date + timedelta(days=duw)
        Rdate = Rdate.strftime('%d-%m-%Y')
        if duw==3:
            am=20
        elif duw==5:
            am=30
        elif duw==7:
            am=40
        with open ('data.csv','r') as f:
            r=csv.reader(f)
            for i in r:
                l+=[i]
            for i in range(len(l)):
                L.append(l[i][5])
            if mid in L:
                l1=[mid,bookid,c_date,duw,Rdate,am]
                lend.writerow(l1)
            else:
                mg.showerror('Error','Membership does not exist!!')
        
ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk()
wi.geometry('1400x800')
wi.title('Check Membership Page')
wi.resizable(width='True',height='True')
wi.configure(fg_color='#F5F5F5')

bgimg=CTkImage(light_image=Image.open('bg4.jpg'),size=(800,800))
bg=CTkLabel(master=wi,text='',image=bgimg)
bg.pack(fill='y',side='left')

f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

l0=CTkLabel(master=f1,text='Lending Book',font=('century gothic',50),text_color='#333')
l0.place(relx=0.2,rely=0.1)
l1=CTkLabel(master=f1,text='Number of Days:',font=('centurygothic',20),text_color='#333')
l1.place(relx=0.17,rely=0.45)

bi=CTkEntry(master=f1,width=350,placeholder_text='Book-Id...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
bi.place(relx=0.17,rely=0.3)
nd=CTkComboBox(master=f1,width=100,values=['3','5','7'],height=30,fg_color='#A8A9A8',dropdown_fg_color='#EEEEEE',
               dropdown_text_color='#333',dropdown_hover_color='#BDBDBD',border_color='#333',)
nd.place(relx=0.49,rely=0.45)
mi=CTkEntry(master=f1,width=350,placeholder_text='Membership-Id...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
mi.place(relx=0.17,rely=0.56)

le=CTkButton(master=wi,text='Lend',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
             fg_color='#747574',border_width=2,border_color='#333',text_color='white',command=buy)
le.place(relx=0.74,rely=0.75,anchor='center')
ex=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
             fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'))
ex.place(relx=0.84,rely=0.75,anchor='center')

wi.mainloop()