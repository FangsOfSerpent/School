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
    with open('Lend.csv', 'r') as lend_file, open('data.csv', 'r') as data_file:
        lend_reader = csv.reader(lend_file)
        data_reader = csv.reader(data_file)
        lend_data = list(lend_reader)
        data = list(data_reader)
        
        for data_row in data:
            membership_id = data_row[5]
            found = False  
            
            for lend_row in lend_data:
                if membership_id == lend_row[0]:
                    found = True  
                    expiry_date = datetime.strptime(lend_row[4], '%d-%m-%Y')
                    current_date = datetime.now()
                    
                    if expiry_date >= current_date:
                        days_difference = (expiry_date-current_date)
                        t1=str(days_difference)
                        sl=t1.split()
                        days=int(sl[0])
                        print(days_difference)
                        if days==1:
                            CLIENT_SECRET_FILE = 'client_secret.json'
                            API_NAME = 'gmail'
                            API_VERSION = 'v1'
                            SCOPES = ['https://mail.google.com/']

                            service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
                            emailMsg = (f'''Dear Reader,
                                        The alloted time for your lent book is about to get over, kindly pay the following
                                        'Membership Id: {membership_id}\n
                                        'Email Address: {data_row[2]}\n
                                        'The price to be paid is {int(lend_row[5])}\n''')
                            mimeMessage = MIMEMultipart()
                            mimeMessage['to'] = data_row[2]
                            mimeMessage['subject'] = 'Fine amt'
                            mimeMessage.attach(MIMEText(emailMsg, 'plain'))
                            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

                            message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
                            print(message)
            

                    else:
                        days_difference = (expiry_date-current_date).days
                        additional_charge = days_difference * 5
                        total_price = int(lend_row[5]) + additional_charge
                        
                        out.insert('end', f'Membership Id: {membership_id}\n'
                                       f'Email Address: {data_row[2]}\n'
                                       f'The price to be paid is {total_price}\n')
                        out.insert('end', '----' * 28 + '\n')
                        CLIENT_SECRET_FILE = 'client_secret.json'
                        API_NAME = 'gmail'
                        API_VERSION = 'v1'
                        SCOPES = ['https://mail.google.com/']

                        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
                        emailMsg = (f'''Dear Reader,
                                    The alloted time for your lent book is over, kindly pay the following
                                    'Membership Id: {membership_id}\n
                                       'Email Address: {data_row[2]}\n
                                       'The price to be paid is {total_price}\n''')
                        mimeMessage = MIMEMultipart()
                        mimeMessage['to'] = data_row[2]
                        mimeMessage['subject'] = 'Fine amt'
                        mimeMessage.attach(MIMEText(emailMsg, 'plain'))
                        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

                        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
                        print(message)
            
                        

wi=ct.CTk()
wi.geometry('700x700')
wi.title('Check Membership Page')
wi.resizable(width='False',height='False')
wi.configure(fg_color='#F5F5F5')

l0=CTkLabel(master=wi,text='Lend Details',font=('century gothic',40),text_color='#333')
l0.place(relx=0.35,rely=0.05)

out = CTkTextbox(wi, height=500, width=500,corner_radius=20,border_color='#333',border_width=2,fg_color='transparent',text_color='#333')
out.place(relx=0.5 ,rely=0.5,anchor=tk.CENTER)

ch=CTkButton(master=wi,text=' Check ',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
             fg_color='#747574',border_width=3,border_color='#333',text_color=('white'),command=check)
ch.place(relx=0.5,rely=0.85,anchor='center')
wi.mainloop()
