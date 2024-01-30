import customtkinter as ct
from customtkinter import *
from PIL import Image
from tkinter import messagebox as mg
import tkinter as tk
from datetime import datetime, timedelta
import csv,os

def addmem():
    wi.destroy()
    import add_mem
def check():
   import check_mem 

ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk() 
wi.geometry('500x500')
wi.title('Membership Page')
wi.resizable(width='False',height='False')
wi.configure(fg_color='#F5F5F5')

memimg=CTkImage(light_image=Image.open('mem.png'),size=(60,60))
mem=CTkLabel(master=wi,text='',image=memimg)
mem.place(relx=0.17,rely=0.095)

l0=CTkLabel(master=wi,text='Membership',font=('century gothic',50),text_color='#333')
l0.place(relx=0.3,rely=0.1)

ad=CTkButton(master=wi,text='  Add Memeber  ',corner_radius=32,text_color=('#333'),fg_color='transparent',hover_color='#C1C0C0',
             border_color='#333',border_width=2,height=80,width=80,font=('centurygothic',20),command=addmem)
ad.place(relx=0.5,rely=0.4,anchor='center')
ch=CTkButton(master=wi,text=' Check Member ',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
             fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=check)
ch.place(relx=0.5,rely=0.6,anchor='center')

wi.mainloop()
