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
import random as r
def addm():
    def add_mem ():
        with open ('data.csv','a',newline='') as f :
            sturec=csv.writer(f)
            d={}
            start_date = start.get()
            try:
                    start1 = datetime.strptime(start_date, '%d-%m-%Y')
                
            except ValueError:
                                    mg.showinfo('Date Info', 'Invalid Date')
            expiration_date = start1 + timedelta(days=6*30)
            expiration_date = expiration_date.strftime('%d-%m-%Y') 
            memnam=un.get()
            phno=ph.get()
            ema=em.get()
            with open('mem_id.txt','r') as f:
                    n=f.read().split()
            n=[int(i)for i in n]
            memid=r.choice(n)
            if len(phno)!=10:
                    mg.showerror("Error","Invalid Phone Number")
            l=[memnam,phno,ema,start_date,expiration_date,memid]
            sturec.writerow(l)
            mg.showinfo("Information","Added succesfully")
    def Clear():
        un.delete(0,END)
        ph.delete(0,END)
        em.delete(0,END)
        start.delete(0,END)
        
        
    wi=ct.CTkToplevel(mi,fg_color='#F5F5F5')
    wi.geometry('1400x800')
    wi.title('Membership Page')
    wi.resizable(width='True',height='True')
        

    bgimg=CTkImage(light_image=Image.open('bg2.jpg'),size=(800,800))
    bg=CTkLabel(master=wi,text='',image=bgimg)
    bg.pack(fill='y',side='left')

    f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
    f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

    l0=CTkLabel(master=f1,text='Add Membership',font=('century gothic',50),text_color='#333')
    l0.place(relx=0.13,rely=0.1)

    un=CTkEntry(master=f1,width=350,placeholder_text='UserName...',height=50,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    un.place(relx=0.17,rely=0.3)
    ph=CTkEntry(master=f1,width=350,placeholder_text='Phone Number...',height=50,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    ph.place(relx=0.17,rely=0.4)
    em=CTkEntry(master=f1,width=350,placeholder_text='Email Address...',height=50,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    em.place(relx=0.17,rely=0.5)
    start=CTkEntry(master=f1,width=350,placeholder_text='Date [dd-mm-yy]...',height=50,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    start.place(relx=0.17,rely=0.6)

    ad=CTkButton(master=wi,text='Add',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
                fg_color='#747574',border_width=2,border_color='#333',text_color='white',command=lambda:[add_mem(),Clear()])
    ad.place(relx=0.74,rely=0.75,anchor='center')
    ex=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
                fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=wi.destroy())
    ex.place(relx=0.84,rely=0.75,anchor='center')     
def chm():
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
                            emailMsg = f'''Greetings from RIDM libraary
Your membership is going to expire in {days} days'''
                            mimeMessage = MIMEMultipart()
                            mimeMessage['to'] = mail
                            mimeMessage['subject'] = 'Membership about to get expired'
                            mimeMessage.attach(MIMEText(emailMsg, 'plain'))
                            raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

                            message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
                            print(message)
                    else:
                         out.insert('end','No Membership expired')
    

    wi=ct.CTkToplevel(mi)
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
def ret():
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

    wi=ct.CTkToplevel(mi)
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
                fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=wi.destroy())
    ex.place(relx=0.84,rely=0.75,anchor='center')
def lend():
    def buy ():
        with open ('lend.csv','a',newline='') as f:
            lend=csv.writer(f)
            l1=[]
            mid=Mid.get()
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
                    f1=open('stock.csv','r+',newline='')
                    r=csv.reader(f)
                    l2=[]
                    for i in r:
                        l2+=[i]
                    f1.close()
                    print('For',l[0][3],end='')
                    t=bookid
                    f1=open('stock.csv','a+',newline='')
                    f2=open('temp.csv','w+',newline='')
                    for i in l2:
                        if i[0]==str(t):
                            s=int(i[3])-1
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
                    mg.showerror('Error','Membership does not exist!!')
    def Clear():
        Mid.delete(0,END)
        bi.delete(0,END)
        
    wi=ct.CTkToplevel(mi)
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
    Mid=CTkEntry(master=f1,width=350,placeholder_text='Membership-Id...',height=50,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    Mid.place(relx=0.17,rely=0.56)

    le=CTkButton(master=wi,text='Lend',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
                fg_color='#747574',border_width=2,border_color='#333',text_color='white',command=lambda:[buy(),Clear()])
    le.place(relx=0.74,rely=0.75,anchor='center')
    ex=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
                fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=wi.destroy())
    ex.place(relx=0.84,rely=0.75,anchor='center')
def chl():
    def check():
        with open('Lend.csv', 'r') as lend_file, open('data.csv', 'r') as data_file:
            lend_reader = csv.reader(lend_file)
            data_reader = csv.reader(data_file)
            lend_data = list(lend_reader)
            data = list(data_reader)
            
            for data_row in data:
                membership_id = data_row[5]
                 
                
                for lend_row in lend_data:
                    if membership_id == lend_row[0]:
                         
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
                                            The alloted time for your lent book will get expired on {expiry_date}, kindly pay the following
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
                                        The alloted time for your lent book is expired on {expiry_date}, kindly pay the following
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
                        
                            

    wi=ct.CTkToplevel(mi)
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
def fi():
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

    wi=ct.CTkToplevel(mi)
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
    find.place(relx=0.35,rely=0.4,anchor='center')
    Exit=CTkButton(master=f1,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
                fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=wi.destroy)
    Exit.place(relx=0.6,rely=0.4,anchor='center')
    out = CTkTextbox(f1, height=250, width=400,corner_radius=20,border_color='#333',border_width=2,fg_color='transparent',text_color='#333')
    out.place(relx=0.5 ,rely=0.7,anchor=tk.CENTER)
def de():
    wi=ct.CTkToplevel(mi)
    wi.geometry('1400x800')
    wi.title('Membership Page')
    wi.resizable(width='True',height='True')
    wi.configure(fg_color='#F5F5F5')


    def deleteb():
        f=open('stock.csv','r+',newline='')
        q=label1.get()
        r=csv.reader(f)
        l=[]
        for i in r:
            l+=[i]
        f.close()
        f=open('stock.csv','a+',newline='')
        f1=open('temp.csv','w+',newline='')
        for i in l:
            if i[0]==str(q):
                    
                out.insert('end',f'Deleted Book is:{i[1]}\n'+
                            f'Genre:{i[2]}\n'+f'Author:{i[4]}\n')
                out.insert('end','----'*22+'\n')
                pass
            else:
            
                twr=csv.writer(f1)
                twr.writerow(i)
                
        f.close()
        f1.close()
        os.remove('stock.csv')
        os.rename('temp.csv','stock.csv')

    def Clear():
        label1.delete(0,END)

    bgimg=CTkImage(light_image=Image.open('bg6.jpg'),size=(800,800))
    bg=CTkLabel(master=wi,text='',image=bgimg)
    bg.pack(fill='y',side='left')

    f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
    f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

    l0=CTkLabel(master=f1,text='Delete a Book',font=('century gothic',50),text_color='#333')
    l0.place(relx=0.13,rely=0.1)

    label1=CTkEntry(master=f1,width=350,placeholder_text='Enter Book ID for deletion:',height=40,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    label1.place(relx=0.15 ,rely=0.25)

    out = CTkTextbox(f1, height=250, width=400,corner_radius=20,border_color='#333',border_width=2,fg_color='transparent',text_color='#333')
    out.place(relx=0.5 ,rely=0.7,anchor=tk.CENTER)

    delete=CTkButton(master=wi,text='Delete',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
                fg_color='#747574',border_width=2,border_color='#333',text_color='white',command=lambda:[deleteb(),Clear()])
    delete.place(relx=0.73,rely=0.4,anchor='center')
    Exit=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
                fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=wi.destroy)
    Exit.place(relx=0.83,rely=0.4,anchor='center')
def upd():
    wi=ct.CTkToplevel(mi)
    wi.geometry('1400x800')
    wi.title('Stock')
    wi.resizable(width='True',height='True')
    wi.configure(fg_color='#F5F5F5')
    bgimg=CTkImage(light_image=Image.open('bg5.jpg'),size=(800,800))
    bg=CTkLabel(master=wi,text='',image=bgimg)
    bg.pack(fill='y',side='left')

    bkid=CTkEntry(master=wi,width=400,placeholder_text='Enter the Book ID:',height=40,placeholder_text_color='white',text_color='white')
    bkid.place(relx=0.65 ,rely=0.25)

    l1=[]


    def check():
        f=open('stock.csv','r+',newline='')
        q=str(bkid.get())
        r=csv.reader(f)
        l=[]
        for i in r:
            l+=[i]
        f1=open('temp.csv','w+',newline='')
        tr=csv.writer(f1)
        tr.writerow(['Book ID','Book Name','Genre','Stock','Author','Price','Shelf number','Row number'])
        f1.close()

        f12=open('temp.csv','a+',newline='')
        twr=csv.writer(f12)
        tlid=[]
        for i in l:
            tlid.append(i[0])
        print (tlid)
        if q not in tlid:
            mg.showerror('Error','Given Book ID is not found')
            for i in l:
                if i[0]==q:
                    pass
                elif i[0]=='Book ID':
                    pass
                else:
                    twr.writerow(i) 
        
        elif q in tlid:
            mg.showinfo('Proceed?','Are you sure to proceed with updating details?')
            for i in l:
                if i[0]==q:
                    f2=open ('deleted_books.csv','w',newline='')
                    ob=csv.writer(f2)
                    ob.writerow(i)
                    f2.close()
                    f12.close()
                    import Update_adding
                elif i[0]=='Book ID':
                    pass
                else:
                    f12=open('temp.csv','a+',newline='')
                    twr=csv.writer(f12)
                    twr.writerow(i)
        f12.close()
        f.close()
        os.remove('stock.csv')
        os.rename('temp.csv','stock.csv')

    ch=CTkButton(master=wi,text='Continue',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
                fg_color='#747574',border_width=3,border_color='#333',text_color=('white'),command=check)
    ch.place(relx=0.8,rely=0.45,anchor='center')
def ads():


    def write_to_csv():
            lst = [label1.get(), label2.get(), label3.get(), label4.get(), label5.get(), label6.get(), label7.get(), label8.get()]
            print(lst)
            with open('stock.csv','r+',newline='') as f:
                reader = csv.reader(f)
                l=[]
                for i in reader:
                    l.append(i)
                for i in l:
                    if lst[0]==i[0]:
                        mg.showerror(title='Error', message='Book IDs are not unique' )
                        break
                else:  
                    wr = csv.writer(f) 
                    wr.writerow(lst)
                    mg.showinfo(title='Success', message='Added sucessfully')
    wi=ct.CTkToplevel(mi)
    wi.geometry('1400x800')
    wi.title('Stock')
    wi.resizable(width='True',height='True')
    wi.configure(fg_color='#F5F5F5')


    bgimg=CTkImage(light_image=Image.open('bg5.jpg'),size=(800,800))
    bg=CTkLabel(master=wi,text='',image=bgimg)
    bg.pack(fill='y',side='left')

    f1=CTkFrame(master=wi,height=700,width=500,corner_radius=30,fg_color='transparent')
    f1.place(relx=0.78 ,rely=0.5,anchor=tk.CENTER)

    l0=CTkLabel(master=f1,text='Add New Arrivals',font=('century gothic',50),text_color='#333')
    l0.place(relx=0.13,rely=0.02)
    
    def Clear():
        label1.delete(0,END)
        label2.delete(0,END)
        label4.delete(0,END)
        label5.delete(0,END)
        label5.delete(0,END)
        label6.delete(0,END)

    label1=CTkEntry(master=f1,width=100,placeholder_text='Book ID:',height=40,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    label1.place(relx=0.15 ,rely=0.15)

    label2=CTkEntry(master=f1,width=350,placeholder_text='Book Name:',height=40,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    label2.place(relx=0.15 ,rely=0.25)
    
    label31=CTkLabel(master=f1,text='Genre:',font=('centurygothic',20),text_color='#333')
    label31.place(relx=0.4 ,rely=0.155)
    label3=CTkComboBox(master=f1,width=150,values=['Action','Mythology','Fiction','Romance','Crime','Horror','Biography','Mystery'],
                        height=40,fg_color='#A8A9A8',dropdown_fg_color='#EEEEEE',dropdown_text_color='#333',
                        dropdown_hover_color='#BDBDBD',text_color='white')
    label3.place(relx=0.55 ,rely=0.15)

    label4=CTkEntry(master=f1,width=150,placeholder_text='Stock:',height=40,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    label4.place(relx=0.15 ,rely=0.35)

    label5=CTkEntry(master=f1,width=350,placeholder_text='Author:',height=40,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    label5.place(relx=0.15 ,rely=0.45)

    label6=CTkEntry(master=f1,width=150,placeholder_text='Price:',height=40,fg_color='#A8A9A8',
                placeholder_text_color='white',text_color='white')
    label6.place(relx=0.55,rely=0.35)
    
    label71=CTkLabel(master=f1,text='Row Number:',font=('centurygothic',20),text_color='#333')
    label71.place(relx=0.15 ,rely=0.655) 
    label7=CTkComboBox(master=f1,width=100,values=['1','2','3','4','5','6'],
                        height=40,fg_color='#A8A9A8',dropdown_fg_color='#EEEEEE',dropdown_text_color='#333',
                        dropdown_hover_color='#BDBDBD',text_color='white')
    label7.place(relx=0.45 ,rely=0.65)

    label81=CTkLabel(master=f1,text='Shelf Number:',font=('centurygothic',20),text_color='#333') 
    label81.place(relx=0.15,rely=0.555)
    label8=CTkComboBox(master=f1,width=100,values=['1','2','3','4','5','6','7','8'],
                        height=40,fg_color='#A8A9A8',dropdown_fg_color='#EEEEEE',dropdown_text_color='#333',
                        dropdown_hover_color='#BDBDBD',text_color='white')
    label8.place(relx=0.45 ,rely=0.55)

    addingstock= CTkButton(master=wi,text='Add',corner_radius=32,hover_color='#A8A9A8',height=80,width=50,font=('centurygothic',20),
                fg_color='#747574',border_width=2,border_color='#333',text_color='white', command=lambda:[write_to_csv(),Clear()])
    addingstock.place(relx=0.74,rely=0.8,anchor='center')
    exitb=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
                fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'))
    exitb.place(relx=0.84,rely=0.8,anchor='center')
   
ct.set_appearance_mode('dark')
ct.set_default_color_theme('blue')

mi=ct.CTk()
mi.geometry('1400x800')
mi.title('Home Page')
mi.resizable(width='True',height='True')
mi.configure(fg_color='#F5F5F5')

f1=CTkFrame(mi,height=750,width=300,fg_color='#333',corner_radius=22)
f1.place(relx=0.01,rely=0.03)
f2=CTkFrame(mi,height=300,width=1050,fg_color='#333',corner_radius=22)
f2.place(relx=0.24,rely=0.03)
f3=CTkFrame(mi,height=435,width=1050,fg_color='#333',corner_radius=22)
f3.place(relx=0.24,rely=0.425)

ad=CTkButton(master=f1,text='Add Stock',corner_radius=22,hover_color='#A8A9A8',height=50,width=200,font=('centurygothic',20),
             fg_color='#F5F5F5',border_width=2,border_color='#333',text_color='#333',command=ads)
ad.place(relx=0.5,rely=0.1,anchor='center')
ds=CTkButton(master=f1,text='Delete Stock',corner_radius=32,text_color=('#333'),fg_color='#F5F5F5',hover_color='#C1C0C0',
             border_color='#333',border_width=2,height=50,width=200,font=('centurygothic',20),command=de)
ds.place(relx=0.5,rely=0.2,anchor='center')
us=CTkButton(master=f1,text='Update Stock',corner_radius=22,hover_color='#A8A9A8',height=50,width=200,font=('centurygothic',20),
             fg_color='#F5F5F5',border_width=2,border_color='#333',text_color='#333',command=upd)
us.place(relx=0.5,rely=0.3,anchor='center')
fb=CTkButton(master=f1,text='Find Book',corner_radius=22,hover_color='#A8A9A8',height=50,width=200,font=('centurygothic',20),
             fg_color='#F5F5F5',border_width=2,border_color='#333',text_color='#333',command=fi)
fb.place(relx=0.5,rely=0.4,anchor='center')

mem=CTkButton(master=f3,text=' Add Membership ',corner_radius=22,hover_color='#A8A9A8',height=200,width=200,font=('centurygothic',20),
             fg_color='#F5F5F5',border_width=2,border_color='#333',text_color='#333',command=addm)
mem.place(relx=0.12,rely=0.27,anchor='center')
adm=CTkButton(master=f3,text='Check Membership',corner_radius=22,hover_color='#A8A9A8',height=200,width=200,font=('centurygothic',20),
             fg_color='#F5F5F5',border_width=2,border_color='#333',text_color='#333',command=chm)
adm.place(relx=0.12,rely=0.75,anchor='center')
lb=CTkButton(master=f3,text='  Lend Book  ',corner_radius=22,hover_color='#A8A9A8',height=200,width=200,font=('centurygothic',20),
             fg_color='#F5F5F5',border_width=2,border_color='#333',text_color='#333',command=lend)
lb.place(relx=0.352,rely=0.75,anchor='center')
rb=CTkButton(master=f3,text=' Return Book ',corner_radius=22,hover_color='#A8A9A8',height=200,width=200,font=('centurygothic',20),
             fg_color='#F5F5F5',border_width=2,border_color='#333',text_color='#333',command=ret)
rb.place(relx=0.352,rely=0.27,anchor='center')
sm=CTkButton(master=f3,text=" Check Status of Books Lended ",corner_radius=22,hover_color='#A8A9A8',height=200,width=200,font=('centurygothic',20),
             fg_color='#F5F5F5',border_width=2,border_color='#333',text_color='#333',command=chl)
sm.place(relx=0.632,rely=0.75,anchor='center')

mi.mainloop()