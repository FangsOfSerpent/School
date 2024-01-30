import customtkinter as ct
from customtkinter import *
from PIL import Image
from tkinter import messagebox as mg
import tkinter as tk
from datetime import datetime, timedelta
import csv,os
import random as r
from tkinter import messagebox

def find():
    n=label1.get()
    f=open('stock.csv','r+',newline='')
    r=csv.reader(f)
    l=[]
    for i in r:
        l+=[i]
    f.close()
    for i in l:
        if i[0]==n:
            out.insert('end',f'The Shelf number is:{i[6]}\n'+
                       f'The Column number is:{i[7]}\n')
            out.insert('end','----'*22+'\n')
        else:
            pass

ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk()
wi.geometry('1400x800')
wi.title('Membership Page')
wi.resizable(width='True',height='True')
wi.configure(fg_color='#F5F5F5')
bgimg=CTkImage(light_image=Image.open('bg7.jpg'),size=(800,800))
bg=CTkLabel(master=wi,text='',image=bgimg)
bg.pack(fill='y',side='left')

f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

l0=CTkLabel(master=f1,text='Find a Book',font=('century gothic',50),text_color='#333')
l0.place(relx=0.2,rely=0.1)

label1=CTkEntry(master=f1,width=350,placeholder_text='Enter Book ID:',height=40,fg_color='#A8A9A8',
               placeholder_text_color='white',text_color='white')
label1.place(relx=0.15 ,rely=0.25)

find=CTkButton(master=f1,text='Find',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
               fg_color='#747574',border_width=2,border_color='#333',text_color='white',command=find)
find.place(relx=0.5,rely=0.4,anchor='center')
Exit=CTkButton(master=f1,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
               fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=wi.destroy)

out = CTkTextbox(f1, height=250, width=400,corner_radius=20,border_color='#333',border_width=2,fg_color='transparent',text_color='#333')
out.place(relx=0.5 ,rely=0.7,anchor=tk.CENTER)
wi.mainloop()
