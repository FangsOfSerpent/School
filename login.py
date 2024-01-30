import customtkinter as ct
from customtkinter import *
from PIL import Image
import tkinter as tk
import pickle
from tkinter import messagebox as mg


ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk()
wi.geometry('1400x800')
wi.title('Login Page')
wi.resizable(width='True',height='True')
wi.configure(fg_color='#F5F5F5')

def sp():
    wi.destroy()
    import signup
def show():
    if pa.cget('show')=='*':
        pa.configure(show='')
    else:
        pa.configure(show='*')
def login():
    with open ('password.dat','rb')  as  f:
        pas=str(pa.get())
        us=str(un.get())
        id=Id.get()
        l=pickle.load(f)
        for i in range(len(l)):
            if pas==l[i][0]and us==l[i][1] and id==l[i][2]:
              wi.destroy()
              import main_page

            elif pas!=l[i][0]and us==l[i][1] and id==l[i][2]:
                mg.showerror('Error','Password Incorrect')
            elif pas==l[i][0]and us!=l[i][1] and id==l[i][2]:
                mg.showerror('Error','Username Incorrect')
            elif pas==l[i][0]and us==l[i][1] and id!=l[i][2]:
                mg.showerror('Error','ID Incorrect')
            elif pas!=l[i][0]and us!=l[i][1] and id!=l[i][2]:
                mg.showerror('Error','All fiels are Incorrect')
                
bgimg=CTkImage(light_image=Image.open('bg.jpg'),size=(800,800))
bg=CTkLabel(master=wi,text='',image=bgimg)
bg.pack(fill='y',side='left')

f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)


l0=CTkLabel(master=f1,text='Admin Login',font=('century gothic',40),text_color='#333')
l0.place(relx=0.3,rely=0.1)
l1=CTkLabel(master=f1,width=50,text='')
l1.place(relx=0.05,rely=0.45)
l2=CTkLabel(master=f1,text='',width=50)
l2.place(relx=0.04,rely=0.6)
l3=CTkLabel(master=f1,text='',width=50)
l3.place(relx=0.04,rely=0.3)

un=CTkEntry(master=f1,width=350,placeholder_text='UserName...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
un.place(relx=0.17,rely=0.45)
pa=CTkEntry(master=f1,width=350,show='*',placeholder_text='Password...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
pa.place(relx=0.17,rely=0.6)
Id=CTkEntry(master=f1,width=350,placeholder_text='ID Number...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
Id.place(relx=0.17,rely=0.3)

lg=CTkButton(master=f1,text='Login',corner_radius=32,hover_color='#A8A9A8',height=50,font=('century gothic',20),
             command=login,fg_color='#747574',border_width=2,border_color='#333',text_color='white')
lg.place(relx=0.3,rely=0.85,anchor='center')
sg=CTkButton(master=f1,text='Sign Up',corner_radius=32,text_color=('#333'),fg_color='transparent',hover_color='#C1C0C0',
             border_color='#333',border_width=2,height=50,font=('centurygothic',20),command=sp)
sg.place(relx=0.68,rely=0.85,anchor='center')
sp=CTkSwitch(master=f1,text='Show Password',command=show,text_color='#333',progress_color='#909190',fg_color='#E0E0E0',
             button_color='#535353',button_hover_color='#707170',switch_height=20)
sp.place(relx=0.6,rely=0.7)


wi.mainloop()