import numpy as np
import cv2
import os
import pickle
import pyttsx3 as p
import sqlite3
import time
import facetrain

#facetrains= facetrain.train()
engine=p.init() #voice information module initilalised.....
def faces():
    engine.say("Analiser initiated  \n please wait     connectiong to database \n if you want to    exit analizer  press   q    in keyboard  ")
    engine.runAndWait()
    face_cascade=cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
    eye_cascade=cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
    smile_cascade=cv2.CascadeClassifier('cascades/haarcascade_smile.xml')
    recogniser = cv2.face.LBPHFaceRecognizer_create()
    
    recogniser.read('trainer.yml')
    #loading label names...
    labels={'id':'1'}
    with open('labels.pickle','rb') as file:
        org_labels=pickle.load(file)
        labels={v:k for k,v in org_labels.items()}

    capture=cv2.VideoCapture(2)
    
    while(True):
        #reading the video frames...
        ret,frame=capture.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
        for(x,y,w,h) in faces:
            print(x,y,w,h)
            roi_gray=gray[y:y+h,x:x+w]#[ycord start x,ycord end]
            roi_color=frame[y:y+h,x:x+w]#[ycord start x,ycord end]        
        
            #recognising now
            id_,conf =recogniser.predict(roi_gray)
            if conf>=45  and conf<=85:
                print(id_)
                print(conf)
                print(labels[id_])
                font=cv2.FONT_HERSHEY_SIMPLEX
                name=labels[id_]
                color = (0,0,0)
                stroke= 2
                
                #accessing database names now
                terrorists =sqlite3.connect('terrorist.db') 
                tcur=terrorists.cursor()
                display_ter=tcur.execute('SELECT * FROM terrorists WHERE Terrorist_Name=?',(name,))
                show=(display_ter.fetchall())
                try:
                    tname = show[0][0]
                    tcountry = show[0][3]
                    tabout = show[0][5]
                    cv2.putText(frame,('Name    :'),(10,380),font,1,color,stroke,cv2.LINE_AA)
                    cv2.putText(frame,('Country  :'),(10,420),font,1,color,stroke,cv2.LINE_AA)  
                    cv2.putText(frame,('Status   :'),(10,460),font,1,color,stroke,cv2.LINE_AA)
                    #inputs
                    color2=(204,102,0)
                    color3=(0, 0, 255)
                    
                    cv2.putText(frame,name,(200,380),font,1,color2,stroke,cv2.LINE_AA)
                    cv2.putText(frame,tcountry,(200,420),font,1,color2,stroke,cv2.LINE_AA)
                    cv2.putText(frame,tabout,(200,460),font,1,color3,stroke,cv2.LINE_AA)
                    #engine.say(" terrorist recognised ")
                    #engine.runAndWait()
                except:
                    un='unknown'
                    cv2.putText(frame,un,(y,x-50),font,1,color,stroke,cv2.LINE_AA)
            if conf<45 and conf >=100:
                un='unknown'
                cv2.putText(frame,un,(y,x-50),font,1,color,stroke,cv2.LINE_AA)
            
            img_item=("face data\my image.png")
            cv2.imwrite(img_item,roi_color)
                
        #creating the raectangle to the face..
            color=(255,0,0)#BGR O-255
            stroke=2
            endcord_x=x+w  #width of rectangle
            endcord_y=y+h  #height of rectagle
            cv2.rectangle(frame,(x,y),(endcord_x,endcord_y),color,stroke)
                    
        
            #creating smile cascade
            smile=eye_cascade.detectMultiScale(roi_gray)
            for(ex,ey,ew,eh) in smile:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
        
        #displaying the results frame.....
        cv2.namedWindow('Analizing', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Analizing', 1368, 720)
        cv2.imshow('Analizing',frame)  #showing the frame...
        
        if cv2.waitKey(20)& 0xFF==ord('q'):
            break

    #when everythinng done,  relese capture

    capture.release()
    cv2.destroyAllWindows()
