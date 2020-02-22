# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:34:01 2020

@author: balu
"""

from tkinter import *
import datetime
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import cv2 
import pyttsx3 as p
import time
import os
from PIL import Image
import facetrain
import faces

engine=p.init()        #initiailizing voice command package
date = datetime.datetime.now().date()
con=sqlite3.connect('officer.db')  #creating officer database for login empoyees
cur=con.cursor()
terrorists =sqlite3.connect('terrorist.db')
tcur=terrorists.cursor()
con.commit()
class Main(object):
    def __init__(self,master):
        
        #initializing all labels to self to master
        self.master= master #initializing to master


########################################   creatig Frames ###################################################################-----------
        
        self.top = Frame(self.master,width=1350,height=100,relief=SUNKEN,borderwidth=1)
        self.top.pack(fill=X)
        self.bottom = Frame(self.master,bg='#888',width=1350,height=569,relief=SUNKEN,borderwidth=1)
        #self.label1 = Label(self.bottom,text='balu').place(x=0,y=0)
        self.bottom.pack(fill=X)
        

        #creating top right subframe 
        self.subframe = Frame(self.top,bg='#006666',width=400,height=100,relief=SUNKEN,borderwidth=8)
        self.subframe.pack(fill=X,side=RIGHT)
        
                                               #creating date
        self.datelabel = Label(self.top,text='Date   :',font='Areal 13 bold',fg='#CCFFFF',bg='#006666')
        self.datelabel.place(x=1200,y=70)
        self.dateinput= Label(self.top,text=str(date),font ='Areal 13 bold',fg='#CCFFFF',bg='#006666')
        self.dateinput.place(x=1270,y=70)
        #creating  left frame in top frame
        self.subframe0 = Frame(self.top,bg='#009966',width=968,height=100,relief=SUNKEN,borderwidth=1)
        self.subframe0.pack(fill=X,side=LEFT)
        self.title = Label(self.subframe0,text = 'Intelligence Department of India',
                           font= 'Britannicbold 25 bold',bg='#009966',fg='#CCFFFF')
        self.title.place(x=190,y=20)
        self.ib = PhotoImage(file='bagrounds/bgtop.png')   #adding image to frame2 sub1
        self.label = Label(self.subframe0,image=self.ib).place(x=0,y=0)
        
        
        #creating  subframe1 in bottom frame
        self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN)
        self.subframe1.pack(fill=X,side=LEFT)
        self.images = PhotoImage(file='bagrounds/bgs.png')   #adding image to frame2 sub1
        self.label = Label(self.subframe1,image=self.images).place(x=0,y=0)
        #creating login page subframe2
        self.subframe2 = Frame(self.bottom,bg='white',width=400,height=600,relief=SUNKEN,bd=1)
        self.subframe2.pack(fill=X,side=RIGHT)
##########################################  Frames created   ###############################################################################        



########################################## Login window and acces to main page #########################################***************************#
        
            
        def log_page():
                chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
                U_entry = self.ientry.get()
                P_entry = self.pentry.get()
                con=sqlite3.connect('officer.db')
                cur=con.cursor()
                user_check=cur.execute('SELECT * FROM officers WHERE Officer_Id=(?)',(self.ientry.get(),))
                checkp=user_check.fetchall()
                usname = checkp[0][0]
                usid = checkp[0][1]
                usps = checkp[0][5]
                print(usid,usname,usps)
                  
                if (usid,usps) == (U_entry,P_entry) :
                                                               #Password Verified.....
                    print("Verified")
                    self.subframe1.destroy()
                    self.subframe2.destroy()
                    #creating  subframe1 in bottom frame
                    self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
                    self.subframe1.pack(fill=X,side=LEFT)
                    self.images = PhotoImage(file='bagrounds/bgs2.png')   #adding image to frame2 sub1
                    self.label = Label(self.subframe1,image=self.images).place(x=0,y=0)
                    self.subframe2 = Frame(self.bottom,bg='white',width=400,height=600,relief=SUNKEN,bd=1)
                    self.subframe2.pack(fill=X,side=RIGHT)
                    
                                                  #--------- ADD terrorist,Display,Delete,Analise buttons
                        
                    #creating bttons in right frame      #add button in main
                    self.log_add = Button(self.subframe2,text = 'Add Terrorist',width=15,bg='#99CCCC',fg='#000033',font = 'Areal 25 bold',bd=3,command=add_terrorist)
                    self.log_add.place(x=50,y=150)      #Display button in main
                    self.log_display= Button(self.subframe2,text = 'Display',width=15,bg='#99CCCC',fg='#000000',font = 'Areal 25 bold',bd=3,command=display_terrorist)
                    self.log_display.place(x=50,y=250)      #delete button in main
                    self.log_delete = Button(self.subframe2,text = 'Delete',width=15,bg='#99CCCC',fg='#000000',font = 'Areal 25 bold',bd=3,command=delete_terrorist)
                    self.log_delete.place(x=50,y=350)      #Analise button in main
                    self.log_analise = Button(self.subframe2,text = 'Analize',width=15,bg='#000033',fg='#CCFFFF',font = 'Areal 25 bold',bd=7,command=opencamera)
                    self.log_analise.place(x=50,y=450)   
                    self.log_out = Button(self.subframe2,text = 'Logout',width=7,bg='#330000',fg='white',font = 'Areal 11 bold',bd=5,command=Log_out)
                    self.log_out.place(x=310,y=0)    #creating logout button
                    self.useridlabel = Label(self.top,text='User Name:',font='Areal 13 bold',fg='#330000',bg='#006666')
                    self.useridlabel.place(x=1100,y=30)
                    
                    #creating User Name in logged page...........not completed ok
                    
                    self.idinput= Label(self.top,text=usname,font ='Areal 13 bold',fg='black',bg='#006666')
                    self.idinput.place(x=1200,y=30)
                    print(self.password_entry)
                
                        
                else:
                    messagebox.showinfo("","Employee ID or Password Incorrect")
        def Log_out():
            chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
            self.subframe1.destroy()
            self.subframe2.destroy()
            #creating  subframe1 in bottom frame
            self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
            self.subframe1.pack(fill=X,side=LEFT)
            self.images = PhotoImage(file='bagrounds/bgs.png')   #adding image to frame2 sub1
            self.label = Label(self.subframe1,image=self.images).place(x=0,y=0)
            #creating login page created in subFrame 2
            #creating login page subframe2
            self.subframe2 = Frame(self.bottom,bg='white',width=400,height=600,relief=SUNKEN,bd=1)
            self.subframe2.pack(fill=X,side=RIGHT)
            self.ientry=StringVar()
            self.pentry=StringVar()
            self.user_name = Label(self.subframe2,text='Employee ID',font='Areal 13 bold')
            self.user_name.place(x=60,y=200)
            self.user_entry= ttk.Entry(self.subframe2,textvariable=self.ientry,width=21,font='Areal 13 ')
            self.user_entry.place(x=180,y=200)
            self.user_password= Label(self.subframe2,text='Password',font='Areal 13 bold')
            self.user_password.place(x=60,y=240)
            self.password_entry= ttk.Entry(self.subframe2,textvariable=self.pentry,width=21,font='Areal 13')
            self.password_entry.config(show='*')
            self.password_entry.place(x=180,y=240)
            self.login_btn = Button(self.subframe2,text = 'Login',width=10,bg='black',fg='white',command=log_page)
            self.login_btn.place(x=230,y=280)
            self.register_btn = Button(self.subframe2,text = 'New Account',width=15,bg='green',fg='black',command=empreg,bd=5)
            self.register_btn.place(x=260,y=5)
                                
            self.subframe.destroy()
            self.subframe = Frame(self.top,bg='#006666',width=400,height=100,relief=SUNKEN,borderwidth=8)
            self.subframe.pack(fill=X,side=RIGHT)
        
                                               #creating date
            self.datelabel = Label(self.top,text='Date   :',font='Areal 13 bold',fg='#CCFFFF',bg='#006666')
            self.datelabel.place(x=1200,y=70)
            self.dateinput= Label(self.top,text=str(date),font ='Areal 13 bold',fg='#CCFFFF',bg='#006666')
            self.dateinput.place(x=1270,y=70)
            con.close()
            tcur.close()
        def login_home():
            chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
            #Top Frame labels adding in this field
        
            #creating login page created in subFrame 2
            self.ientry=StringVar()
            self.pentry=StringVar()
        
            self.user_name = Label(self.subframe2,text='Employee ID',font='Areal 13 bold')
            self.user_name.place(x=60,y=200)
            self.user_entry= ttk.Entry(self.subframe2,textvariable=self.ientry,width=21,font='Areal 13 ')
            self.user_entry.place(x=180,y=200)
            self.user_password= Label(self.subframe2,text='Password',font='Areal 13 bold')
            self.user_password.place(x=60,y=240)
            self.password_entry= ttk.Entry(self.subframe2,textvariable=self.pentry,width=21,font='Areal 13')
            self.password_entry.config(show='*')
            self.password_entry.place(x=180,y=240)
            self.login_btn = Button(self.subframe2,text = 'Login',width=10,bg='black',fg='white',command=log_page)
            self.login_btn.place(x=230,y=280)

        def opencamera():
            chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
            face=faces.faces()
        def display_terrorist():
            self.bottom.destroy()
#########################################  logs completed ##################################################################
          
            
########################################### Adding Terrorist form in after login ###################################################################
        '''def convertToBinaryData(filename):
            # Convert digital data to binary format
            with open(filename, 'rb') as file:
                binaryData = file.read()
            return binaryData
        
        def upload():
            file_name =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Image Files files","*.*"),("all files","*.*")))
            
            filename= convertToBinaryData(file_name)
            self.bio=filename'''
        
            
        
        def add_terrorist():
            
            chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
            TNE =StringVar()
            GE = StringVar()
            AE = StringVar()                    #storing image folder and get verified and trained
            CE = StringVar()
            AE =StringVar()
            NE = StringVar()
            aboutter=StringVar()
            def store_image():
                tname=TNE.get()
                print(tname)
                file_name =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Image Files files","*.*"),("all files","*.*")))
                #imagespath='D:\my python\6th sem\my project work\face recognition\images'
                #change_dir= os.chdir(imagespath)
                print(file_name)
                try:
                    
                    basedir=os.path.dirname(os.path.abspath(__file__))
                    chdir=os.chdir('images')
                    os.makedirs(tname)
                    if (os.path.exists(tname)):
                        print('created')
                        path=os.chdir(tname)
                        img = Image.open(file_name)
                        img.save('1.png')
                        print('image stored')
                        basedir=os.path.dirname(os.path.abspath(__file__))
                        self.subframe1.destroy()
                        self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
                        self.subframe1.pack(fill=X,side=LEFT)
                        Label(self.subframe1,text='Image  has been Uploaded',font='Areal 13 bold',fg='#3333CC').place(x=400,y=250)
                        tb=Button(self.subframe1,text='Click here to Train Image',width=35,font='Areal 16 bold',bg='#339933',fg='#FFFFFF',command=img_train).place(x=300,y=450)
                    
                    else:
                        basedir=os.path.dirname(os.path.abspath(__file__))
                        chdir=os.chdir('images')
                        os.makedirs(tname)
                        print('created')
                        path=os.chdir(tname)
                        img = Image.open(file_name)
                        img.save('1.png')
                        print('image stored')
                       
                        self.subframe1.destroy()
                        self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
                        self.subframe1.pack(fill=X,side=LEFT)
                        Label(self.subframe1,text='Image  has been Uploaded',font='Areal 13 bold',fg='#3333CC').place(x=320,y=200)
                        tb=Button(self.subframe1,text='Click here to Train Image',width=35,font='Areal 16 bold',bg='#339933',fg='#FFFFFF',command=img_train).place(x=350,y=450)
                    
                except:
                     messagebox.showinfo('Not seelcted an Image','Uploaded Image must be .png Extension with less than 1MB')
                    
                
            def img_train():
                self.subframe1.destroy()
                self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
                self.subframe1.pack(fill=X,side=LEFT)
                Label(self.subframe1,text='Image  Trained for future predictions',font='Areal 13 bold',fg='#3333CC').place(x=320,y=200)
                engine.say("Training   Image Please Wait")
                engine.runAndWait()
                chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
                train = facetrain.train()
                
                
            #------------------------------------------------------terrorist details adding to DATABASE ----------------------------
            
            def terrorist_database():
                
                #getting attribute values for stering in Database
                tname=TNE.get()
                tgender=GE.get()
                tage=AE.get()
                tcountry=CE.get()
                tatkcount=NE.get()
                tabout=aboutter.get()
                
                
                # Terrorists Database Created..............
                terrorists =sqlite3.connect('terrorist.db')
                tcur=terrorists.cursor()
                try:
                    tcur.execute('INSERT INTO terrorists(Terrorist_Name,Gender,Age,Country,Attacks_count,About) VALUES(?,?,?,?,?,?)',(tname,tgender,tage,tcountry,tatkcount,tabout,))
                    terrorists.commit()
                    self.subframe1.destroy()
                    #creating  subframe1 in bottom frame
                    self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
                    self.subframe1.pack(fill=X,side=LEFT)
                    self.thankyou=Label(self.subframe1,text='Terrorist Details  Added to Data base Sucessfully',font='Areal 13 bold',fg='#3333CC')
                    self.thankyou.place(x=320,y=200)
                    
                    engine.say("Please wait \n connecting to data base \n details accepted \nupload  an    image   of a terrorist  for   future   predictions \n thankyou")
                    engine.runAndWait()
                    #terrorists.close()
                    
                    ib=Button(self.subframe1,text='Upload Terrorist Photo',width=25,font='Areal 16 bold',bg='#339933',fg='#FFFFFF',command=store_image).place(x=350,y=450)
                    
                except sqlite3.IntegrityError:
                    message1 = messagebox.showinfo('Error','These Details already exist\n\n            or \n\n Unfilled Fields')
                                             
            #--<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<--- close database------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            self.subframe1.destroy()
            #creating  subframe1 in bottom frame
            self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
            self.subframe1.pack(fill=X,side=LEFT)
            #labels in terrorist from
            t_name = ttk.Label(self.subframe1,text='Terrorist Name',font='Areal 13 bold').place(x=250,y=140)
            t_gender= ttk.Label(self.subframe1,text='Gender',font='Areal 13 bold').place(x=250,y=190)
            t_age = ttk.Label(self.subframe1,text='Age ',font='Areal 13 bold').place(x=250,y=240)
            t_country = ttk.Label(self.subframe1,text='Country',font='Areal 13 bold').place(x=250,y=290)
            t_nattacks= ttk.Label(self.subframe1,text='No.of Attacks',font='Areal 13 bold').place(x=250,y=340)
            t_accused = ttk.Label(self.subframe1,text='About',font='Areal 13 bold').place(x=250,y=390)
            #t_Photo  = ttk.Label(self.subframe1,text='Photo',font='Areal 13 bold').place(x=250,y=480)
            
            # Entries in terrorist form
            tne=ttk.Entry(self.subframe1,width=40,font='Areal 13 ',textvar=TNE).place(x=430,y=140)
                            #Gender
            button1= ttk.Radiobutton(self.subframe1,text="Male",value="Male",var=GE).place(x=430,y=190)
            button2= ttk.Radiobutton(self.subframe1,text="Female",value="FeMale",var=GE).place(x=510,y=190)
            button3= ttk.Radiobutton(self.subframe1,text="Others",value="Others",var=GE).place(x=590,y=190)
                        #Terrorist Age spin box
            ae=ttk.Entry(self.subframe1,textvariable=AE,width=40,font='Areal 13 ').place(x=430,y=240)
                        #terrorist country
            ce = ttk.Combobox(self.subframe1,textvariable=CE,width=58,values=('Pakistan','China','India','Usa','Nigeria','Iraq','Syria','Others'))
            ce.place(x=430,y=290)
            ce.config(state='readonly')
            # Number of Attacks Entry
            ne=ttk.Entry(self.subframe1,width=40,font='Areal 13 ',textvar=NE).place(x=430,y=340)
                        #Accused entry using check boxes...
            
            getabout = ttk.Entry(self.subframe1,width=40,font='Areal13 ',textvar=aboutter).place(x=430,y=390)
                # Image upload button
            #ib=Button(self.subframe1,text='Upload',width=8,bg='#CCCCCC',command=store_image).place(x=430,y=480)
            Register=Button(self.subframe1,text=' Register',width=15,bg='#336600',fg='black',bd=3,font='Areal 10 bold',command=terrorist_database).place(x=460,y=480)
            Reset=Button(self.subframe1,text='Reset ',command=add_terrorist,width=15,bg='#9999CC',bd=3).place(x=620,y=480)
        
            
#############################################-----  CLOSE   ------########################################################################################




########################################   Display Terrorist Details by Search  ##############################################################################
        '''def converttophoto(Photo):
            # Convert digital data to binary format
            with open(Photo,'wb') as file:
                photodata = file.write(Photo)'''
            
        
        def tbsearch():
            #database part
            sget=self.SRE.get()
            terrorists =sqlite3.connect('terrorist.db') 
            tcur=terrorists.cursor()
            display_ter=tcur.execute('SELECT * FROM terrorists WHERE Terrorist_Name=?',(sget,))
            show=(display_ter.fetchall())
            
            
            try:
                trget1=show[0][0]
                trget2=show[0][1]
                trget3=show[0][2]
                trget4=show[0][3]
                trget5=show[0][4]
                tget6=show[0][5]
                #with open((trget1,'wb') as p:
                    #trget6=p.write(tget6)
                
                #details showing in Frame
                self.trname=Label(self.subframe1,text=("Terrorist Name   :"),font='Areal 13 bold').place(x=370,y=150)
                self.trgender=Label(self.subframe1,text=("Gender               :"),font='Areal 13 bold').place(x=370,y=200)
                self.trage=Label(self.subframe1,text=("Age                     :"),font='Areal 13 bold').place(x=370,y=250)  
                self.trcountry=Label(self.subframe1,text=("Country              :"),font='Areal 13 bold').place(x=370,y=300)
                self.trAttacks=Label(self.subframe1,text=("Attacks              :"),font='Areal 13 bold').place(x=370,y=350)
                self.trabout=Label(self.subframe1,text=("About                 :"),font='Areal 13 bold').place(x=370,y=400)
                #self.tphoto=Label(self.subframe1,height=150,width=100).place(x=150,y=10)
                            #printig terrorist data in  frame
                self.trnameentry=Label(self.subframe1,text=trget1,font='Areal 13 bold').place(x=570,y=150)
                self.trgenderentry=Label(self.subframe1,text=trget2,font='Areal 13 bold').place(x=570,y=200)
                self.trageentry=Label(self.subframe1,text=trget3,font='Areal 13 bold').place(x=570,y=250)
                self.trcountryentry=Label(self.subframe1,text=trget4,font='Areal 13 bold').place(x=570,y=300)
                self.trattacksentry=Label(self.subframe1,text=trget5,font='Areal 13 bold').place(x=570,y=350)
                self.traboutentry=Label(self.subframe1,text=tget6,font='Areal 13 bold').place(x=570,y=400)
                terrorists.close()
                
                '''getimage=os.chdir('images')
                getimage=os.chdir(sget)
                print(getimage)
                img=Image.open(getimage)
                print(img)
                Label(self.subframe1,image=img).place(x=500,y=0)'''
                
            except Exception:
                import traceback
                traceback.print_exc()
                messagebox.showinfo("Not Found","Doesn't Exist")
        
        def display_terrorist():                #after search creating new frames and label and search DB
            #frames created
            chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
            self.subframe1.destroy()
            self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
            self.subframe1.pack(fill=X,side=LEFT)
            self.images = PhotoImage(file='bagrounds/bgs2.png')   #adding image to frame2 sub1
            self.label = Label(self.subframe1,image=self.images).place(x=0,y=0)
            #----------------------------------------------------------------
            self.SRE=StringVar()
            self.searchtitle=Label(self.subframe1,text="  Enter Terrorist  Name ",font="Areal 16 bold",fg='#009999').place(x=50,y=230)
            self.searchentry=Entry(self.subframe1,width=28,font="Areal 11 ",bg='#CCCCCC',textvariable=self.SRE).place(x=60,y=265)
            self.searchbtn=Button(self.subframe1,text='Search',bg='#336699',font='Areal 10 bold',bd=5,command=tbsearch).place(x=125,y=305)
            
#################################################################################################################################
            
#***************************************** Delete Terrorist  ***************************************************************** '''
       
            
        def deleting_terrorist():
             #database part
            chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
            tget=self.dell.get()
            terrorists =sqlite3.connect('terrorist.db') 
            tcur=terrorists.cursor()
            del_ter=tcur.execute('SELECT * FROM terrorists WHERE Terrorist_Name=?',(tget,))
            dels=(del_ter.fetchall())
            print(del_ter)
            
            try:
                tdel1=dels[0][0]
                tdel2=dels[0][1]
                tdel3=dels[0][2]
                tdel4=dels[0][3]
                tdel5=dels[0][4]
                tdel6=dels[0][5]
                #details showing in Frame
                self.trname=Label(self.subframe1,text=("Terrorist Name   :"),font='Areal 13 bold').place(x=370,y=150)
                self.trgender=Label(self.subframe1,text=("Gender               :"),font='Areal 13 bold').place(x=370,y=200)
                self.trage=Label(self.subframe1,text=("Age                     :"),font='Areal 13 bold').place(x=370,y=250)  
                self.trcountry=Label(self.subframe1,text=("Country              :"),font='Areal 13 bold').place(x=370,y=300)
                self.trAttacks=Label(self.subframe1,text=("Attacks              :"),font='Areal 13 bold').place(x=370,y=350)
                self.trabout=Label(self.subframe1,text=("About                 :"),font='Areal 13 bold').place(x=370,y=400)
                            #printig terrorist data in  frame
                self.trnameentry=Label(self.subframe1,text=tdel1,font='Areal 13 bold').place(x=570,y=150)
                self.trgenderentry=Label(self.subframe1,text=tdel2,font='Areal 13 bold').place(x=570,y=200)
                self.trageentry=Label(self.subframe1,text=tdel3,font='Areal 13 bold').place(x=570,y=250)
                self.trcountryentry=Label(self.subframe1,text=tdel4,font='Areal 13 bold').place(x=570,y=300)
                self.trattacksentry=Label(self.subframe1,text=tdel5,font='Areal 13 bold').place(x=570,y=350)
                self.traboutentry=Label(self.subframe1,text=tdel6,font='Areal 13 bold').place(x=570,y=400)
                but=Button(self.subframe1,text='Delete',font='Areal 13 bold',bg="#339933",command=deletenow,bd=5).place(x=520,y=500)
                
            except :
                messagebox.showinfo("Not Found","Doesn't Existed")
                
                
        def delete_terrorist():
            #frames created
            chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
            self.subframe1.destroy()
            self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
            self.subframe1.pack(fill=X,side=LEFT)
            self.images = PhotoImage(file='bagrounds/bgs2.png')   #adding image to frame2 sub1
            self.label = Label(self.subframe1,image=self.images).place(x=0,y=0)
            #----------------------------------------------------------------
            self.dell=StringVar()
            self.searchtitle=Label(self.subframe1,text="  Enter Terrorist  Name ",font="Areal 16 bold",fg='#009999').place(x=50,y=230)
            self.searchentry=Entry(self.subframe1,width=28,font="Areal 11 ",bg='#CCCCCC',textvariable=self.dell).place(x=60,y=265)
            self.searchbtn=Button(self.subframe1,text='Search',bg='#336699',font='Areal 10 bold',bd=5,command=deleting_terrorist).place(x=125,y=305)
           
        def deletenow():
            #tname=TNE.get()
            self.tget=self.dell.get()
            print('deleted now')
            terrorists =sqlite3.connect('terrorist.db') 
            tcur=terrorists.cursor()
            g=tcur.execute('DELETE FROM terrorists WHERE Terrorist_Name=?',(self.tget,))
            terrorists.commit()
            print('deleted now')
            #deleted now frame with label created
            self.subframe1.destroy()
            self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
            self.subframe1.pack(fill=X,side=LEFT)
            Label(self.subframe1,text=(self.tget+'  Record Deleted successfully'),font='Areal 13 bold',fg='#003366').place(x=350,y=250)
            voice3()





#############################################  Officer Registration  ######################################################################################
        
        def empreg():
            chdir=os.chdir(os.path.dirname(os.path.abspath(__file__)))
            self.subframe1.destroy()
            #creating  subframe1 in bottom frame
            self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
            self.subframe1.pack(fill=X,side=LEFT)
            self.images = PhotoImage(file='bagrounds/bgs2.png')   #adding image to frame2 sub1
            self.label = Label(self.subframe1,image=self.images).place(x=0,y=0)
            #getting values to use further
            ONI =StringVar()
            OID =StringVar()
            dep =StringVar()
            question= StringVar()
            SAI = StringVar()
            NPI = StringVar()
            
            #heading for registration
            title =Label(self.subframe1,text="EMPLOYEE REGISTRATION DESK",fg="#3366FF",font='Areal 25 bold')
            title.place(x=260,y=30)
            #------------ #creating form --------------------------------------------------------------------
            officername= ttk.Label(self.subframe1,text="Name",font='Areal 12 bold').place(x=250,y=140)
            Employeeid= ttk.Label(self.subframe1,text="Employee ID",font='Areal 12 bold').place(x=250,y=190)   
            department= ttk.Label(self.subframe1,text="Department",font='Areal 12 bold').place(x=250,y=240)
            sq=ttk.Label(self.subframe1,text="Security Question",font='Areal 12 bold').place(x=250,y=290)
            sa=ttk.Label(self.subframe1,text="Security Answer",font='Areal 12 bold').place(x=250,y=330)
            np=ttk.Label(self.subframe1,text="new password",font='Areal 12 bold').place(x=250,y=380)
            
            #creating inputs to this from
            oni = ttk.Entry(self.subframe1,width=40,font='Areal 13 ',textvar=ONI).place(x=430,y=140)
            oid = ttk.Entry(self.subframe1,width=40,font='Areal 13 ',textvar=OID).place(x=430,y=190)
            sai = ttk.Entry(self.subframe1,width=40,font='Areal 13 ',textvar=SAI).place(x=430,y=330)
            npi = ttk.Entry(self.subframe1,width=40,font='Areal 13 ',textvar=NPI).place(x=430,y=380)
            
            #creating combo boxes for sequrity question
            
            cbox = ttk.Combobox(self.subframe1,textvariable=question,values=("What Is your favorite book?","Where did you meet your spouse?","Where is your favorite place to vacation?"))
            cbox.config(state="readonly",width=38,font='Areal 13 ')
            cbox.place(x=430,y=290)
            #department selection
            
            odp=ttk.Combobox(self.subframe1,textvariable=dep,font='Areal 13 ',values=("Directorate of Military Intelligence","Directorate of Naval Intelligence","Directorate of Air Intelligence","Intelligence Bureau","National Investigation Agency","Department of Criminal Intelligence"))
            odp.config(state="readonly",width=38)
            odp.place(x=430,y=240)
            #checkbox for the apply conformation
            confirm = IntVar()
            confirm.set(0)
            check = Checkbutton(self.subframe1,text="I hereby declare that the details furnished above are true and correct to the best of my knowledge and belief. " ,fg="#FF0000",bg='#CCCCFF',variable=confirm,font='Areal 10')
            check.place(x=250,y=450)
          
           
          
            
            def homefunc():
                self.subframe1.destroy()
                #creating  subframe1 in bottom frame
                self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
                self.subframe1.pack(fill=X,side=LEFT)
                self.images = PhotoImage(file='bagrounds/bgs.png')   #adding image to frame2 sub1
                self.label = Label(self.subframe1,image=self.images).place(x=0,y=0)

            # OFFICER REGISTRATION STORING IN DATABSE  ------------------------------------------------------
            def store_employee():
                value1 = confirm.get()
                ONI_G= ONI.get()
                OID_G=OID.get()
                dep_G=dep.get()
                question_G=question.get()
                SAI_G=SAI.get()
                NPI_G=NPI.get()
                v1=1
                
                
                if value1 == v1:
                    try:
                        con=sqlite3.connect('officer.db')  #creating officer database for login empoyees
                        cur=con.cursor()
                        id_check=cur.execute('SELECT Officer_id FROM officers')
                        cur.execute('INSERT INTO officers(Officer_Name,Officer_Id,Officer_Department,Security_Question,Security_Answer,New_Password) VALUES(?,?,?,?,?,?)',(ONI_G,OID_G,dep_G,question_G,SAI_G,NPI_G,))
                        con.commit()
                        self.subframe1.destroy()
                        #creating  subframe1 in bottom frame
                        self.subframe1 = Frame(self.bottom,bg='white',width=968,height=600,relief=SUNKEN,bd=2)
                        self.subframe1.pack(fill=X,side=LEFT)
                        self.thankyou=Label(self.subframe1,text='Application submited Successfully\n \nYour Account Will be Activated within 24 Hours!',font='Areal 13 bold',fg='#3333CC')
                        self.thankyou.place(x=250,y=250)
                        con.close()
                        home = Button(self.subframe1,text = "Home", bg='#993300',font='Helvetica 10 bold',bd=5,command=homefunc).place(x=5,y=5)
                        #ai voice initiated
                        voice1()
                        
                    except sqlite3.IntegrityError:
                        message1 = messagebox.showinfo('Error','This Employee ID already exist\n\n                     or \n \nDetails not Entered completly')
                            
                    
                else:
                    message1 = messagebox.showinfo('Oops','Pleas agree by clicking tick button')   
            #creating button to register
            apply=Button(self.subframe1,text="Apply",bg='green',width=11,font='Helvetica 10 bold',command=store_employee).place(x=500,y=500)
            reset = Button(self.subframe1,text = "Reset",width=11, bg='#33FFCC',command =empreg,font='Helvetica 10 bold').place(x=620,y=500)
            home = Button(self.subframe1,text = "Home", bg='#993300',font='Helvetica 10 bold',bd=5,command=homefunc).place(x=5,y=5)

################################################   close    ##############################################################################################
        
        #main buttons to start
        register_btn = Button(self.subframe2,text = 'New Account',width=15,bg='green',fg='black',command=empreg,bd=5)
        register_btn.place(x=260,y=5)
        login_home()
        def voice1():
            engine.say("Please Wait\n  \n submiting your  Application  \n \n application accepted \nYour Acoout Will be Activated within 24 Hours     When after vefied by our Team")
            engine.runAndWait()
            
        
            
            
        def voice3():
            engine.say("Record  Deleted")
            engine.runAndWait()
          
#------------------------------------------------------------------------------------------------------------------------------

def main():
    root=Tk()
    registration = Main(root)
    root.title('Facial Recognition To catch Terrorists in public Areas')
    root.geometry('1360x769')
    #root.iconbitmap('bgs3.png')
    root.mainloop()
if __name__== "__main__":
    main()
