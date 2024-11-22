from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
import importlib
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class TimeTable:
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
        img=Image.open(r"Images_GUI\bg3.jpg")
        img=img.resize((1536,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1536,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg3.jpg")
        bg1=bg1.resize((1536,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1536,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Generate Time Table",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1546,height=45)
        
        # Back Button IMG
        back_btn=Image.open(r"Images_GUI\back.jpg")
        back_btn=back_btn.resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(back_btn)

        # std_b1 = Button(bg_img,command=self.back,image=self.back_img,cursor="hand2")
        button = Button(bg_img, command=self.back,image=self.back_img,bd=0, cursor="hand2",highlightthickness=0, relief=FLAT)
        button.place(x=10,y=0,width=45,height=45)
    
    def back(self):
        self.root.destroy()  # Destroy the current window completely
        main_module = importlib.import_module('main')
        main_root = main_module.tk.Tk()  # Create a new root window for the main page
        main_app = main_module.Face_Recognition_System(main_root)  # Initialize the main window class
        main_root.mainloop()


if __name__ == "__main__":
    root=Tk()
    obj=TimeTable(root)
    root.mainloop()