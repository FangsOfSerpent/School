

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
                      messagebox.showerror(title='Error', message='Book IDs are not unique' )
                      break
              else:  
               wr = csv.writer(f) 
               wr.writerow(lst)
               messagebox.showinfo(title='Success', message='Added sucessfully')
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
               fg_color='#747574',border_width=2,border_color='#333',text_color='white', command=write_to_csv)
addingstock.place(relx=0.74,rely=0.8,anchor='center')
exitb=CTkButton(master=wi,text='Exit',corner_radius=32,hover_color='#C1C0C0',height=80,width=50,font=('centurygothic',20),
               fg_color='transparent',border_width=2,border_color='#333',text_color=('#333'),command=exite)
exitb.place(relx=0.84,rely=0.8,anchor='center')
    

# Call the new function to create a new file


# Start the Tkinter event loop
wi.mainloop()
