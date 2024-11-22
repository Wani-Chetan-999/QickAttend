from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1566x864+0+0")
        self.root.title("Train Pannel")
        
        
        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images_GUI\bg3.jpg")
        img=img.resize((1536,90),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1536,height=90)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg2.jpg")
        bg1=bg1.resize((1566,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=90,width=1536,height=768)

        #title section
        title_lb1 = Label(bg_img,text="Training Data Set",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1536,height=45)
        
        # Back Button IMG
        back_btn=Image.open(r"Images_GUI\back.jpg")
        back_btn=back_btn.resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(back_btn)

        # std_b1 = Button(bg_img,command=self.back,image=self.back_img,cursor="hand2")
        button = Button(bg_img, command=self.back,image=self.back_img,bd=0, cursor="hand2",highlightthickness=0, relief=FLAT)
        button.place(x=10,y=0,width=45,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"Images_GUI\train7.png")
        std_img_btn=std_img_btn.resize((240,220),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=650,y=230,width=240,height=220)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=650,y=450,width=240,height=45)
        
        #Back Button
        back_btn=Image.open(r"Images_GUI\back.jpg")
        back_btn=back_btn.resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(back_btn)

        # std_b1 = Button(bg_img,command=self.back,image=self.back_img,cursor="hand2")
        button = Button(bg_img, command=self.back,image=self.back_img,bd=0, cursor="hand2",highlightthickness=0, relief=FLAT)
        button.place(x=10,y=0,width=45,height=45)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)

    def back(self):
        self.root.destroy()  # Destroy the current window completely
        main_module = importlib.import_module('main')
        main_root = main_module.tk.Tk()  # Create a new root window for the main page
        main_app = main_module.Face_Recognition_System(main_root)  # Initialize the main window class
        main_root.mainloop()


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()