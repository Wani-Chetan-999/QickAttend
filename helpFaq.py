from tkinter import *
from tkinter import ttk
import importlib
from PIL import Image, ImageTk

class HelpFaq:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1536x768+0+0")
        self.root.title("QuickAttend")
        
        img = Image.open("Images_GUI/scan2.jpg")  # Load the .png icon
        img = img.resize((200, 200), Image.LANCZOS)  # Resize to 128x128
        icon = ImageTk.PhotoImage(img)

        # Set the resized icon
        self.root.iconphoto(False, icon)

        # Header image
        img=Image.open(r"Images_GUI\bg3.jpg")
        img = img.resize((1536, 90), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1536, height=130)

        # Background image
        bg1=Image.open(r"Images_GUI\mainbg2.jpeg")
        bg1 = bg1.resize((1536, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=90, width=1536, height=768)

        # Title section
        title_lb1 = Label(
            bg_img,
            text="Help Support & FAQ's ",
            font=("verdana", 30, "bold"),
            bg="white",
            fg="navyblue",
        )
        title_lb1.place(x=0, y=0, width=1536, height=55)

        # Scrollable help content
        self.create_help_content(bg_img)
        
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

    def create_help_content(self, parent):
        # Scrollable container for help content
        container = Frame(parent, bg="#f9f9f9", bd=0)
        canvas = Canvas(container, bg="#f9f9f9", highlightthickness=0)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg="#f9f9f9")

        self.scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.place(x=250, y=90, width=1100, height=580)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Add help content
        self.add_help_content()

        # Add Step-by-step Instructions
        self.add_instructions()

    def add_help_content(self):
        # Title
        # Module Descriptions
        modules = [
            {
                "title": "Main Menu",
                "details": (
                    "The Main Menu serves as the entry point to the system, providing easy navigation "
                    "to all other modules. \n From here, you can access Student Registration, Training the Dataset, "
                    "and Mark Attendance modules. \n It ensures a user-friendly experience for seamless operations."
                ),
            },
            {
                "title": "Student Registration",
                "details": (
                    "In this module, you can register students by capturing their images and associating "
                    "them with unique identifiers. \n It ensures that all students have a clear, high-quality set of "
                    "images for the face recognition system to work accurately."
                ),
            },
            {
                "title": "Train Dataset",
                "details": (
                    "This module trains the system using the collected student images. \n The training algorithm "
                    "creates a dataset to recognize individual faces during attendance marking. \n It is a crucial step "
                    "to ensure the system functions effectively."
                ),
            },
            {
                "title": "Mark Attendance",
                "details": (
                    "The Mark Attendance module uses real-time face detection and recognition to identify students. \n"
                    "and record their attendance. This is done by comparing live images from the camera to the trained dataset."
                ),
            },
        ]

        # for module in modules:
        #     self.create_module_section(module["title"], module["details"])

        # FAQ Section
        Label(
            self.scrollable_frame,
            text="Frequently Asked Questions",
            font=("times new roman", 24, "bold"),
            bg="#f9f9f9",
            fg="#007bff",
        ).pack(anchor="w", pady=20, padx=30)

        faqs = [
            {
                "question": "How do I register a new student?",
                "answer": (
                    "To register a new student, open the Student Registration module (student.py). "
                    "Capture clear, high-quality images of the student to ensure accuracy in face recognition."
                ),
            },
            {
                "question": "How do I train the system on new data?",
                "answer": (
                    "Run the Train Dataset module (train.py). It processes the student images and updates the "
                    "system’s recognition capabilities with the latest information."
                ),
            },
            {
                "question": "How do I mark attendance?",
                "answer": (
                    "Execute the Mark Attendance module (detect.py). The system uses live camera feeds to detect "
                    "faces and record attendance in a CSV file."
                ),
            },
            {
                "question": "Can I view attendance reports?",
                "answer": (
                    "Yes, all attendance records are saved in a CSV file. You can open and view these records "
                    "using spreadsheet software such as Microsoft Excel."
                ),
            },
            {
                "question": "What if a face is not detected?",
                "answer": (
                    "Ensure the face is well-lit and positioned in front of the camera. Additionally, confirm "
                    "that the student is registered and the data has been trained properly."
                ),
            },
        ]

        for faq in faqs:
            self.create_faq_section(faq["question"], faq["answer"])

        # Add social media section
        self.create_social_media_section()

    def create_module_section(self, title, details):
        """Create a detailed module section."""
        Label(
            self.scrollable_frame,
            text=title,
            font=("times new roman", 18, "bold"),
            bg="#f9f9f9",
            fg="#007bff",
        ).pack(anchor="w", pady=8, padx=30)

        for detail in details.split('\n'):  # Split the details if you want each on a new line.
            Label(
                self.scrollable_frame,
                text=f"• {detail}",  # Adds bullet points before each detail.
                font=("Arial", 12),
                bg="#f9f9f9",
                fg="#333",
                wraplength=1100,  # Wrapping text to avoid long horizontal scrolling.
                justify="left",  # Makes sure the text is aligned left.
            ).pack(anchor="w", pady=10, padx=50)  

    def create_faq_section(self, question, answer):
        """Create an FAQ with a dropdown effect."""
        frame = Frame(self.scrollable_frame, bg="#f9f9f9", bd=1, relief="solid")
        frame.pack(fill="x", padx=30, pady=10)

        # FAQ Question
        question_btn = Button(
            frame,
            text=question,
            font=("times new roman", 15, "bold"),
            bg="#007bff",
            fg="white",
            bd=0,
            padx=10,
            pady=5,
            anchor="w",
            relief="flat",
            command=lambda: self.toggle_faq_answer(answer_frame),
        )
        question_btn.pack(fill="x")

        # FAQ Answer (initially hidden)
        answer_frame = Frame(frame, bg="#f9f9f9")
        answer_label = Label(
            answer_frame,
            text=answer,
            font=("times new roman", 15),
            bg="#f9f9f9",
            fg="#333",
            wraplength=1100,
            justify="left",
        )
        answer_label.pack(anchor="w", padx=20, pady=5)

        # Hide the answer initially
        answer_frame.pack(fill="x", padx=10, pady=5)
        answer_frame.pack_forget()

    def toggle_faq_answer(self, frame):
        """Toggle the visibility of the FAQ answer."""
        if frame.winfo_viewable():
            frame.pack_forget()
        else:
            frame.pack(fill="x", padx=10, pady=5)

    def create_social_media_section(self):
        """Create a social media contact section."""
        social_frame = Frame(self.scrollable_frame, bg="#f9f9f9", pady=20)
        social_frame.pack(fill="x", side="bottom", pady=20)  # Place the social_frame at the bottom

        Label(
            social_frame,
            text="Connect with us on Social Media          ",
            font=("times new roman", 18, "bold"),
            bg="#f9f9f9",
            fg="#007bff",
        ).pack(anchor="center", pady=10)

        social_icons = [
            ("Website", r"Images_GUI\web.png"),
            ("Facebook", r"Images_GUI\fb.png"),
            ("YouTube", r"Images_GUI\yt.png"),
            ("Gmail", r"Images_GUI\gmail.png"),
            ("LinkedIn", r"Images_GUI\linkedin.png")
        ]

        # Create buttons and pack them horizontally at the bottom
        for name, icon_path in social_icons:
            icon = Image.open(icon_path)
            icon = icon.resize((40, 40), Image.LANCZOS)
            photo = ImageTk.PhotoImage(icon)

            btn = Button(
                social_frame,
                text=name,
                image=photo,
                compound="left",  # Adjust the text and image position to center
                font=("times new roman", 15, "bold"),
                bg="white",
                fg="#333",
                padx=20,
                pady=5,
                relief="flat",
            )
            btn.photo = photo  # Keep a reference to avoid garbage collection
            btn.pack(side="left", padx=20)  # Pack buttons horizontally
    def add_instructions(self): 
        """Add step-by-step instructions for using the system."""
        
        # Title
        Label(
            self.scrollable_frame,
            text="Step-by-Step Instructions",
            font=("Times New Roman", 22, "bold"),
            bg="#f9f9f9",  # Light background
            fg="Black",
            pady=10,
            anchor="center",  # Center the text within the label
            ).pack(fill="x", padx=30, pady=15)
            
        instructions = [
            ("📄", "Start by registering a new student using the Student Registration module."),
            ("📸", "Capture clear images of the student for face recognition."),
            ("🔄", "After capturing the images, train the system with the Train Dataset module."),
            ("📝", "Once the dataset is trained, you can use the Mark Attendance module to record student attendance."),
            ("✅", "Ensure that students' faces are detected correctly during the attendance marking process."),
            ("📊", "Check attendance records by accessing the saved CSV files.")
        ]
        
        # Add instructions with icons and improved styling
        for icon, instruction in instructions:
            # Container frame for each instruction
            frame = Frame(self.scrollable_frame, bg="#f9f9f9")
            frame.pack(fill="x", pady=8, padx=50)

            # Instruction icon and text
            Label(
                frame,
                text=icon,
                font=("Arial", 18),  # Icon size
                bg="#f9f9f9",
                fg="#007bff",
                padx=10,
                anchor="w",
            ).pack(side="left")
            
            Label(
                frame,
                text=instruction,
                font=("Times New Roman", 16),
                bg="#f9f9f9",
                fg="#333",
                wraplength=1100,
                justify="left",
            ).pack(side="left", fill="x", padx=10)

    # def add_instructions(self):
    #     """Add step-by-step instructions for using the system."""
    #     Label(
    #         self.scrollable_frame,
    #         text="Step-by-Step Instructions",
    #         font=("times new roman", 20, "bold"),
    #         bg="#f9f9f9",
    #         fg="#007bff",
    #     ).pack(anchor="w", pady=20, padx=30)

    #     instructions = [
    #         "1. Start by registering a new student using the Student Registration module.",
    #         "2. Capture clear images of the student for face recognition.",
    #         "3. After capturing the images, train the system with the Train Dataset module.",
    #         "4. Once the dataset is trained, you can use the Mark Attendance module to record student attendance.",
    #         "5. Ensure that students' faces are detected correctly during the attendance marking process.",
    #         "6. Check attendance records by accessing the saved CSV files."
    #     ]

    #     for instruction in instructions:
    #         Label(
    #             self.scrollable_frame,
    #             text=instruction,
    #             font=("times new roman", 15),
    #             bg="#f9f9f9",
    #             fg="#333",
    #             wraplength=1100,
    #             justify="left",
    #         ).pack(anchor="w", pady=5, padx=50)


if __name__ == "__main__":
    root = Tk()
    obj = HelpFaq(root)
    root.mainloop()
