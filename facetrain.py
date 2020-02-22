import os
from PIL import Image
import numpy as np
import cv2
import pickle
import pyttsx3 as p




                              #defining cascade classifier..........
#face cascade=vc2.CascadeClassifier("D:\my python\6th sem\my project work\face recognition\cascades\data\haarcascade_frontalface_alt2.xml")
engine=p.init()

def train():
    face_cascade=cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
    recogniser = cv2.face.LBPHFaceRecognizer_create()

    basedir=os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(basedir,'images')
    
    current_id=0
    label_ids={}
    y_labels=[]
    x_train=[]
    
    for root,dirs,files in os.walk(image_dir):
        for file in files:
            if file.format('png') or file.format('jpg'):
                path=os.path.join(root,file)
                label=os.path.basename(root).replace(" "," ").lower()
                print(label,path)
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id= current_id+1
                id_=label_ids[label]
            
                print(label_ids)
                #y_labels.append(label) #some number
                #x_train.append(path)    #verify this image,turn into a NUMPY ARRAY
                pil_image= Image.open(path).convert("L")   #grayScale
                
                #resizing images for training
                size =(110,110)
                final_image=pil_image.resize(size,Image.ANTIALIAS)
                image_array = np.array(pil_image,'uint8')
                #print(image_array)
                
                #detecting faces now
                faces=face_cascade.detectMultiScale(image_array,scaleFactor=1.3,minNeighbors=5)
                for(x,y,w,h) in faces:
                    #print(x,y,w,h)
                    roi=image_array[y:y+h,x:x+w]#[ycord start x,ycord end]
                    x_train.append(roi)
                    y_labels.append(id_)
                    
    #print(y_labels)
    #print(x_train)           
 
    with open('labels.pickle','wb') as file:
        pickle.dump(label_ids,file)         
            
        recogniser.train(x_train,np.array(y_labels))
        recogniser.save("trainer.yml")               
