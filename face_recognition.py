# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1566x864+0+0")
        self.root.title("QuickAttend")
        
        img = Image.open("Images_GUI/scan2.jpg")  # Load the .png icon
        img = img.resize((200, 200), Image.LANCZOS)  # Resize to 128x128
        icon = ImageTk.PhotoImage(img)

        # Set the resized icon
        self.root.iconphoto(False, icon)

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images_GUI\main3.jpg")
        img=img.resize((1536,864),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1536,height=90)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg3.jpg")
        bg1=bg1.resize((1536,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=90,width=1536,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1536,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=700,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=700,y=350,width=180,height=45)
        
        # Back Button IMG
        back_btn=Image.open(r"Images_GUI\back.jpg")
        back_btn=back_btn.resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(back_btn)

        # std_b1 = Button(bg_img,command=self.back,image=self.back_img,cursor="hand2")
        button = Button(bg_img, command=self.back,image=self.back_img,bd=0, cursor="hand2",highlightthickness=0, relief=FLAT)
        button.place(x=10,y=0,width=45,height=45)
    #=====================Attendance===================

    def mark_attendance(self,i,r,n):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID="+str(id))
                n=cursor.fetchone()
                n="+".join(n)

                cursor.execute("select Roll_No from student where Student_ID="+str(id))
                r=cursor.fetchone()
                r="+".join(r)

                cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=cursor.fetchone()
                i="+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll-No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()
        
    def back(self):
        self.root.destroy()  # Destroy the current window completely
        main_module = importlib.import_module('main')
        main_root = main_module.tk.Tk()  # Create a new root window for the main page
        main_app = main_module.Face_Recognition_System(main_root)  # Initialize the main window class
        main_root.mainloop()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()