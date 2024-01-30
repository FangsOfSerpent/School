import customtkinter as ct
from customtkinter import *
from PIL import Image
from tkinter import messagebox as mg
import tkinter as tk
from datetime import datetime, timedelta
import csv,os

def addlend():
    wi.destroy()
    import lending
def check():
   import check_lend 

ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk()
wi.geometry('500x500')
wi.title('Lend Page')
wi.resizable(width='False',height='False')
wi.configure(fg_color='#F5F5F5')

memimg=CTkImage(light_image=Image.open('lend_logo.png'),size=(100,100))
mem=CTkLabel(master=wi,text='',image=memimg)
mem.place(relx=0.2,rely=0.05)

l0=CTkLabel(master=wi,text=' Lend ',font=('century gothic',50),text_color='#333')
l0.place(relx=0.4,rely=0.1)

ad=CTkButton(master=wi,text='  Lend Book  ',corner_radius=32,text_color=('#333'),fg_color='transparent',hover_color='#C1C0C0',
             border_color='#333',border_width=2,height=80,width=80,font=('centurygothic',20),command=addlend)
ad.place(relx=0.5,rely=0.4,anchor='center')
ch=CTkButton(master=wi,text=' Check Status ',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
             fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=check)
ch.place(relx=0.5,rely=0.6,anchor='center')
wi.mainloop()
