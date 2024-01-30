import customtkinter as ct
from customtkinter import *
from PIL import Image
from tkinter import messagebox as mg
import tkinter as tk
from datetime import datetime, timedelta
import csv,os
from Google import Create_Service 
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def check():
    with open('data.csv','r') as f:
        st=csv.reader(f)
        current_date = datetime.now()
        l=[]
        for mem in st:
            l+=[mem]
        for i in range(len(l)):
            exp=datetime.strptime(l[i][4], '%d-%m-%Y')
            if exp<current_date:  
                na=f'Name:{l[i][0]}'
                ph=f'Phone Number:{l[i][1]}'
                em=f'Email Address:{l[i][2]}'
                out.insert('end',na+'\n'+ph+'\n'+em+'\n')
                out.insert('end','----'*28+'\n')
                
            elif exp>current_date:
                p=exp-current_date
                p1=str(p)
                l1=p1.split()
                days=int(l1[0])
                if days<=7:
                        mail=l[i][2]
                        CLIENT_SECRET_FILE = 'client_secret.json'
                        API_NAME = 'gmail'
                        API_VERSION = 'v1'
                        SCOPES = ['https://mail.google.com/']

                        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
                        emailMsg = f'''Greeting from ridm libraary
    You're membership is going to expire in {days} days'''
                        mimeMessage = MIMEMultipart()
                        mimeMessage['to'] = mail
                        mimeMessage['subject'] = 'Membership about to get expired'
                        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
                        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

                        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
                        print(message)
ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

wi=ct.CTk()
wi.geometry('700x700')
wi.title('Check Membership Page')
wi.resizable(width='False',height='False')
wi.configure(fg_color='#F5F5F5')

l0=CTkLabel(master=wi,text='Membership Details',font=('century gothic',40),text_color='#333')
l0.place(relx=0.23,rely=0.05)

out = CTkTextbox(wi, height=500, width=500,corner_radius=20,border_color='#333',border_width=2,fg_color='transparent',text_color='#333')
out.place(relx=0.5 ,rely=0.5,anchor=tk.CENTER)

ch=CTkButton(master=wi,text=' Check Member ',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
             fg_color='#747574',border_width=3,border_color='#333',text_color=('white'),command=check)
ch.place(relx=0.5,rely=0.85,anchor='center')


wi.mainloop()