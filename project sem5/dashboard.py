from tkinter import *
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        
        self.root.geometry("1600x800+0+0")
        self.root.config(bg="white")

        #===icons===
        self.logo_dash = ImageTk.PhotoImage(file="image/logo_p.png")


        #===title===
        title=Label(root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0 , y=0 , relwidth=1,height=50) 
        #===Menu====
        M_Frame=LabelFrame(root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1510,height=80)

        Btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white" , cursor="hand2" , command=self.add_course).place(x=20,y=5,width=200,height=40)
        Btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white" , cursor="hand2",command=self.add_student).place(x=260,y=5,width=200,height=40)
        Btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white" , cursor="hand2").place(x=500,y=5,width=200,height=40)
        Btn_view=Button(M_Frame,text="View student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white" , cursor="hand2").place(x=740,y=5,width=200,height=40)
        Btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white" , cursor="hand2").place(x=980,y=5,width=200,height=40)
        Btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white" , cursor="hand2").place(x=1220,y=5,width=200,height=40)
        
        #====content_window====
        bg_image = Image.open("image/bg.png")
        desired_width = 990  # Adjust this to your desired width
        resized_bg = bg_image.resize((desired_width, int(bg_image.height * (desired_width / bg_image.width))), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(resized_bg)
 
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180, width=desired_width, height=resized_bg.height)  # Update height based on resized image
       
       #====Update Detaila===
        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_student.place(x=400,y=620,width=320,height=100)

        self.lbl_course=Label(self.root, text="Total Course\n[0]",font=("gowdy old style",20),bd=10,relief=RIDGE,bg="blue",fg="white")
        self.lbl_course.place(x=733,y=620,width=320,height=100)
        
        self.lbl_result=Label(self.root, text="Total result\n[0]",font=("gowdy old style",20),bd=10,relief=RIDGE,bg="green",fg="white")
        self.lbl_result.place(x=1065,y=620,width=320,height=100)
        #===footer===
        footer=Label(self.root, text="Student Result Management System\n Contact us for any Technical Issue",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.new_win = Toplevel(root)
        self.new_obj = CourseClass(self.new_win)
    
    def add_student(self):
        self.new_win=Toplevel(root)
        self.new_obj=StudentClass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()