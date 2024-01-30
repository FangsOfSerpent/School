#Update adding
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

l0=CTkLabel(master=wi,text='Updating book details',font=('century gothic',40),text_color='#333')
l0.place(relx=0.13,rely=0.02)


label2=CTkEntry(master=wi,width=360,placeholder_text='Book Name:',height=40,fg_color='#A8A9A8',
               placeholder_text_color='white',text_color='white')
label2.place(relx=0.15 ,rely=0.25)
   
label31=CTkLabel(master=wi,text='Genre:',font=('centurygothic',20),text_color='#333')
label31.place(relx=0.15 ,rely=0.155)
label3=CTkComboBox(master=wi,width=150,values=['Action','Mythology','Fiction','Romance','Crime','Horror','Biography','Mystery'],
                      height=40,fg_color='#A8A9A8',dropdown_fg_color='#EEEEEE',dropdown_text_color='#333',
                      dropdown_hover_color='#BDBDBD',text_color='white')
label3.place(relx=0.2 ,rely=0.15)

label4=CTkEntry(master=wi,width=150,placeholder_text='Stock:',height=40,fg_color='#A8A9A8',
               placeholder_text_color='white',text_color='white')
label4.place(relx=0.15 ,rely=0.35)

label5=CTkEntry(master=wi,width=360,placeholder_text='Author:',height=40,fg_color='#A8A9A8',
               placeholder_text_color='white',text_color='white')
label5.place(relx=0.15 ,rely=0.45)

label6=CTkEntry(master=wi,width=150,placeholder_text='Price:',height=40,fg_color='#A8A9A8',
               placeholder_text_color='white',text_color='white')
label6.place(relx=0.3,rely=0.35)
   
label71=CTkLabel(master=wi,text='Row Number:',font=('centurygothic',20),text_color='#333')
label71.place(relx=0.15 ,rely=0.655) 
label7=CTkComboBox(master=wi,width=100,values=['1','2','3','4','5','6'],
                      height=40,fg_color='#A8A9A8',dropdown_fg_color='#EEEEEE',dropdown_text_color='#333',
                      dropdown_hover_color='#BDBDBD',text_color='white')
label7.place(relx=0.35 ,rely=0.65)

label81=CTkLabel(master=wi,text='Shelf Number:',font=('centurygothic',20),text_color='#333') 
label81.place(relx=0.15,rely=0.555)
label8=CTkComboBox(master=wi,width=100,values=['1','2','3','4','5','6','7','8'],
                      height=40,fg_color='#A8A9A8',dropdown_fg_color='#EEEEEE',dropdown_text_color='#333',
                      dropdown_hover_color='#BDBDBD',text_color='white')
label8.place(relx=0.35 ,rely=0.55)

out = CTkTextbox(wi, height=500, width=400,corner_radius=20,border_color='#333',border_width=2,fg_color='transparent',text_color='#333')
out.place(relx=0.7 ,rely=0.4,anchor=tk.CENTER)

def Clear():
        label2.delete(0,END)
        label4.delete(0,END)
        label5.delete(0,END)
        label6.delete(0,END)
def searchbook():
     with open ('deleted_books.csv','r',newline='')as f6:
            rr=csv.reader(f6)
            l5=[]
            for i in rr:
                l5+=[i]
            for j in l5:
                    out.insert('end',f'Old book details:{j}\n')
                    out.insert('end','----'*22+'\n')
                    


def write_to_csv():
        with open ('deleted_books.csv','r+',newline='')as f5:
            rr=csv.reader(f5)
            l4=[]
            for i in rr:
                 if len(i)==0:
                     pass
                 else: l4+=[i]
            print(l4)

        lst = [l4[0][0], label2.get(), label3.get(), label4.get(), label5.get(), label6.get(), label7.get(), label8.get()]
        with open('temp.csv','a+',newline='') as f:
            wr = csv.writer(f) 
            wr.writerow(lst)
        with open ('temp.csv','r+', newline='') as f:
              reader = csv.reader(f)
              l=[]
              for i in reader:
                l.append(i)
              for i in l:
                   if str(i[0])==str(lst[0]):
                        messagebox.showinfo('Sucess','Added sucessfully')
                        f.close()                  
                        
                        

def exite():
    wi.destroy()

addingstock = CTkButton(master=wi,text='Add',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
               fg_color='#747574',border_width=2,border_color='#333',text_color='white', command=lambda:[write_to_csv(),Clear()])
addingstock.place(relx=0.24,rely=0.8,anchor='center')
exitb=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
               fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=exite)
exitb.place(relx=0.34,rely=0.8,anchor='center')

sb=CTkButton(master=wi,text='Check',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
               fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=searchbook)
sb.place(relx=0.29,rely=0.9,anchor='center')

wi.mainloop()