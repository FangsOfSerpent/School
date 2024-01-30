import customtkinter as ct
from customtkinter import *
from PIL import Image
import tkinter as tk
import pickle
from tkinter import messagebox as mg

L=[]
def save():
    with  open ('password.bin','ab')  as  f:
        pas=str(pa.get())
        us=str(un.get())
        unique=ui.get()
        re=rp.get()
        if pas==re:
            if pas==''or us==''or unique=='' or re=='':
                mg.showerror('Error','All fields are required')
            else:
                l=[pas,us,unique]
                L.append(l)  
                pickle.dump(L,f)
                mg.showinfo("Information","Saved succesfully")
        else:
            mg.showerror('Error','Password does match')
        
def lp():
    wi.update()
    wi.destroy()
    import login



ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk()
wi.geometry('1400x800')
wi.title('SignUp Page')
wi.resizable(width='True',height='True')
wi.configure(fg_color='#DEDFDF')

bgimg=CTkImage(light_image=Image.open('bg1.jpg'),size=(800,800))
bg=CTkLabel(master=wi,text='',image=bgimg)
bg.pack(fill='y',side='left')

f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

l0=CTkLabel(master=f1,text='Admin Sign Up',font=('century gothic',50),text_color='#333')
l0.place(relx=0.18,rely=0.1)

un=CTkEntry(master=f1,width=350,placeholder_text='UserName...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
un.place(relx=0.17,rely=0.3)
pa=CTkEntry(master=f1,width=350,placeholder_text='Password...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
pa.place(relx=0.17,rely=0.4)
rp=CTkEntry(master=f1,width=350,show='*',placeholder_text='Confirm Password...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
rp.place(relx=0.17,rely=0.5)
ui=CTkEntry(master=f1,width=350,placeholder_text='ID Number...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
ui.place(relx=0.17,rely=0.6)

sg=CTkButton(master=f1,text='Sign Up',corner_radius=32,text_color=('#333'),fg_color='transparent',hover_color='#C1C0C0',
             border_color='#333',border_width=2,height=50,font=('centurygothic',20),command=lambda:[save(),lp()])
sg.place(relx=0.3,rely=0.8,anchor='center')
lg=CTkButton(master=f1,text='Login',corner_radius=32,hover_color='#A8A9A8',height=50,font=('century gothic',20),
             command=lp,fg_color='#747574',border_width=2)
lg.place(relx=0.68,rely=0.8,anchor='center')

wi.mainloop()