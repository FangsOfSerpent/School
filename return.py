import customtkinter as ct
from customtkinter import *
from PIL import Image
from tkinter import messagebox as mg
import tkinter as tk
from datetime import datetime, timedelta
import csv,os
def Return():
        f=open('lend.csv','r')
        reader=csv.reader(f)
        l=list(reader)
        f.close()
        t=bi.get()
        f3=open('lend.csv','a+',newline='')
        f4=open('temp1.csv','w',newline='')
        for i in l:
                if i[1]==str(t):
                        f1=open('stock.csv','r+',newline='')
                        r=csv.reader(f1)
                        l2=[]
                        for i in r:
                                l2+=[i]
                        f1.close()
                
                        f1=open('stock.csv','a+',newline='')
                        f2=open('temp.csv','w+',newline='')
                        for i in l2:
                                if i[0]==str(t):
                                        s=int(i[3])+1
                                        i[3]=s        
                                        twr=csv.writer(f2)
                                        twr.writerow(i) 
                                else:
                                        twr=csv.writer(f2)
                                        twr.writerow(i)
                        f1.close()
                        f2.close()
                        os.remove('stock.csv')
                        os.rename('temp.csv','stock.csv')
                else:
                        mg.showerror('Error',"Book ID does not exist!!")
                        tw=csv.writer(f4)
                        tw.writerow(i)
        f3.close()
        f4.close()
        os.remove('lend.csv')
        os.rename('temp1.csv','lend.csv')
def clear():
        mid.delete(0,END)
        bi.delete(0,END)

wi=ct.CTk()
wi.geometry('1400x800')
wi.title('Check Membership Page')
wi.resizable(width='True',height='True')
wi.configure(fg_color='#F5F5F5')

bgimg=CTkImage(light_image=Image.open('bg8.jpg'),size=(800,800))
bg=CTkLabel(master=wi,text='',image=bgimg)
bg.pack(fill='y',side='left')

f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

l0=CTkLabel(master=f1,text='Returning Book',font=('century gothic',50),text_color='#333')
l0.place(relx=0.2,rely=0.1)

bi=CTkEntry(master=f1,width=350,placeholder_text='Book-Id...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
bi.place(relx=0.17,rely=0.3)
mid=CTkEntry(master=f1,width=350,placeholder_text='Membership-Id...',height=50,fg_color='#A8A9A8',
            placeholder_text_color='white',text_color='white')
mid.place(relx=0.17,rely=0.45)

le=CTkButton(master=wi,text='Return',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
             fg_color='#747574',border_width=2,border_color='#333',text_color='white',command=lambda:[Return(),clear()])
le.place(relx=0.74,rely=0.75,anchor='center')
ex=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
             fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'))
ex.place(relx=0.84,rely=0.75,anchor='center')


    

