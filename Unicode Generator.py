from tkinter import *
from tkinter import messagebox
import pandas as pd
import smtplib
from email.message import EmailMessage
def login():
    nx.withdraw()


    def save():
        ############################ Collecting Inputs ##########################
        email = textfieldemail.get()
        p = textfieldpass.get()
        name=(textfieldname.get()).title()
        gender=textfieldsex.get().upper()
        dob=textfielddob.get()
        year=textfielddob.get()
        year=(year[-4:])
        area=(textfieldarea.get())
        sender=textfieldadd.get()
        
        if gender=='M': 
            gender='Male'
        elif gender=='F': 
            gender='Female'
        else: 
            gender='Other'

        ############################ Pandas Dataframe ##########################
        
        Data={'Name':[],'Gender':[],'DOB':[],'Area':[],'Email':[]} 
        df=pd.DataFrame(Data) 
        try:
            df=pd.DataFrame(Data)
            pd.read_csv('Project_CTS.csv',index_col="Name")

        except:
            df.to_csv('Project_CTS.csv',index=False)

        finally:
            Data['Name'].append(name)
            Data['Gender'].append(gender)
            Data['DOB'].append(dob)
            Data['Area'].append(area)
            Data['Email'].append(sender)
            df=pd.DataFrame(Data)
            df.to_csv('Project_CTS.csv',mode='a',header=False,index=False)
        
        ############################ Unicode Generating and Messagebox ##########################
        
        try:
            unicode=name[:2].upper()+area[::-1]+year[2:]
            messagebox.showinfo(title='notification',message='Your Unicode is '+str(unicode)+'  \n Please remember it \n Check your email')
            
                    
        except:
            messagebox.showinfo(title='notification',message='Unable to generate unicode')
     

        ############################ Sending Mail ##########################
        
        try:
            firstname=name.split()
            msg=EmailMessage()
            msg['Subject']='Unicode For Passport Application'
            msg['From']='Passport Seva Kendra'
            msg['To']=sender
            body = 'Dear '+firstname[0]+',\n\nYour initial application process has been completed.\nYour Unicode is: '+unicode+'\nYou are requested to check your credentials\rName: '+name+'\rGender:'+gender+'\rDate of Birth:'+dob+'\rArea Code:'+area+'\rThankyou for your patience.\r\rRegards,\rPassport office\n'
            
            msg.set_content(body)
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
                server=smtplib.SMTP_SSL('smtp.gmail.com',465)
                server.login(email, password=p)
                server.send_message(msg)

            messagebox.showinfo(title='notification',message='Mail has been sent successfully')
        except Exception as e:
            messagebox.showinfo(title='notification',message='Unable to send mail')
        finally:
            server.quit()


    def clear():
        textfieldadd.delete(0,END)
        textfieldname.delete(0,END)
        textfieldsex.delete(0,END)
        textfieldarea.delete(0,END)
        textfielddob.delete(0,END)
        

    def end():
        window.withdraw()

    ############################ Main Window ##########################
    window=Tk()
    window.geometry('500x500+400+30')
    window.config(bg='grey')
    window.title('Passport Application')

    ############################ Labels ##########################
    
    labelheadig=Label(window,text='Passport Application Form',font=('',18,''),bg='grey',fg='black')
    labelheadig.place(x=110,y=30)
    labelname=Label(window,text='Name',font=('',14,''),bg='black',fg='pink')
    labelname.place(x=30,y=90)
    labelsex=Label(window,text='Gender(F/M)',font=('',14,''),bg='black',fg='pink')
    labelsex.place(x=30,y=130)
    labeladdress=Label(window,text='Email Address',font=('',14,''),bg='black',fg='pink')
    labeladdress.place(x=30,y=170)
    labeldob=Label(window,text='Date Of Birth(dd/mm/yyyy)',font=('',14,''),bg='black',fg='pink')
    labeldob.place(x=30,y=210)
    labelarea=Label(window,text='Area Code(eg. 700039)',font=('',14,''),bg='black',fg='pink')
    labelarea.place(x=30,y=250)

    ############################ Textfields ##########################
    
    textfieldname=Entry(window,font=('',12),justify=CENTER)
    textfieldname.place(x=270,y=90)
    textfieldsex=Entry(window,font=('',12),justify=CENTER)
    textfieldsex.place(x=270,y=130)
    textfieldadd=Entry(window,font=('',12),justify=CENTER)
    textfieldadd.place(x=270,y=170)
    textfielddob=Entry(window,font=('',12),justify=CENTER)
    textfielddob.place(x=270,y=210)
    textfieldarea=Entry(window,font=('',12),justify=CENTER)
    textfieldarea.place(x=270,y=250)

    ############################ Buttons ##########################
    
    btnsave=Button(window,text='Save',cursor='hand2',font=('helvetica',12,''),width=9,height=2,relief='sunken',activebackground='orange',activeforeground='white',command=save)
    btnsave.place(x=50,y=350)
    btnclear=Button(window,text='Clear',cursor='hand2',font=('helvetica',12,''),width=9,height=2,relief='sunken',activebackground='orange',activeforeground='white',command=clear)
    btnclear.place(x=190,y=350)
    btnexit=Button(window,text='Exit',cursor='hand2',font=('helvetica',12,''),width=9,height=2,relief='sunken',activebackground='orange',activeforeground='white',command=end)
    btnexit.place(x=330,y=350)


############################ Admin Login Window ##########################

nx=Tk()
nx.geometry('500x390+400+30')
nx.title('Admin Login')

############################ Label of Admin Page ##########################

labelheadnx=Label(nx,text='Login Here',font=('Impact',35,'bold'),fg='#d77337')
labelheadnx.place(x=60,y=30)
labelmsg=Label(nx,text='Administration login area',font=('Goudy old style',15,'bold'),fg='#d25d17')
labelmsg.place(x=60,y=90)
labelemail=Label(nx,text='Email Id',font=('Goudy old style',15,'bold'),fg='grey')
labelemail.place(x=60,y=140)
labelpasswordnx=Label(nx,text='Password',font=('Goudy old style',15,'bold'),fg='grey')
labelpasswordnx.place(x=60,y=210)

############################ Textfield of Admin Page ##########################

textfieldemail=Entry(nx,font=('times new roman',15),justify=CENTER,bg='lightgrey')
textfieldemail.place(x=60,y=170,width=350,height=30)
textfieldpass=Entry(nx,show='*',font=('times new roman',15),justify=CENTER,bg='lightgrey')
textfieldpass.place(x=60,y=245,width=350,height=30)

def endnx():
    nx.withdraw()

############################ Buttons of Admin Page ##########################

btnenter=Button(nx,text='login',font=('times new roman',13),cursor='hand2',width=9,height=2,bg='orange',fg='white',activebackground='lightgrey',command=login)
btnenter.place(x=70,y=300)
btnexitnx=Button(nx,text='Exit',font=('times new roman',13),cursor='hand2',width=9,height=2,bg='orange',fg='white',activebackground='lightgrey',command=endnx)
btnexitnx.place(x=190,y=300)

nx.mainloop()