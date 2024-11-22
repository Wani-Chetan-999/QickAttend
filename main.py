from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk 
from login import Login
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from timeTable import TimeTable
import os
from helpFaq import HelpFaq

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1566x864+0+0")
        self.root.title("QuickAttend")
        
        # self.root.iconphoto("Images_GUI/icon.png")
        
        img = Image.open("Images_GUI/scan2.jpg")  # Load the .png icon
        img = img.resize((200, 200), Image.LANCZOS)  # Resize to 128x128
        icon = ImageTk.PhotoImage(img)

        # Set the resized icon
        self.root.iconphoto(False, icon)

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"Images_GUI\bg3.jpg")
        img=img.resize((1536,90),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1536,height=90)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\main3.jpg")
        bg1=bg1.resize((1566,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=90,width=1536,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Attendance Managment System Using Facial Recognition",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1566,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"Images_GUI\student2.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=310,y=100,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=310,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"Images_GUI\scan3.png")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=540,y=100,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Mark Atttendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=540,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"Images_GUI\atten.png")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=770,y=100,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=770,y=280,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"Images_GUI\help6.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.HelpFaq,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=1010,y=100,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.HelpFaq,text="Help Support",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=1010,y=280,width=180,height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"Images_GUI\trainB1.png")
        tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=310,y=340,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data Train",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=310,y=520,width=180,height=45)

        # Photo   button 6
        pho_img_btn=Image.open(r"Images_GUI\face5.png")
        pho_img_btn=pho_img_btn.resize((180,180),Image.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=540,y=340,width=180,height=180)

        pho_b1_1 = Button(bg_img,command=self.open_img,text="Datasets",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=540,y=520,width=180,height=45)

        # TimeTables   button 7
        dev_img_btn=Image.open(r"Images_GUI\dev.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.LANCZOS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        dev_b1.place(x=770,y=340,width=180,height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="Generate Time Table",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        dev_b1_1.place(x=770,y=520,width=180,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"Images_GUI\exit3.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2", bg="lightblue")
        exi_b1.place(x=1010,y=340,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        exi_b1_1.place(x=1010,y=520,width=180,height=45)
       
        # Back Button IMG
        back_btn=Image.open(r"Images_GUI\back.jpg")
        back_btn=back_btn.resize((50,50),Image.LANCZOS)
        self.back_img=ImageTk.PhotoImage(back_btn)

        # std_b1 = Button(bg_img,command=self.back,image=self.back_img,cursor="hand2")
        button = Button(bg_img, command=self.back,image=self.back_img,bd=0, cursor="hand2",highlightthickness=0, relief=FLAT)
        button.place(x=10,y=0,width=45,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=TimeTable(self.new_window)
    
    def HelpFaq(self):
        self.new_window=Toplevel(self.root)
        self.app=HelpFaq(self.new_window)

    def Close(self):
        self.root.destroy()
        
    def back(self):
        # Hide the current window (Main window)
        self.root.withdraw()
        self.new_window=Toplevel(self.root)
        self.app=Login(self.new_window)

    # def run(self):
    #     self.root.mainloop()
    
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
