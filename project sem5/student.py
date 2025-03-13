from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk , messagebox
import sqlite3
class StudentClass:
    def __init__(self,root):
        self.root=root
        self.root.maxsize(1350,550)
        self.root.minsize(1350,550)
        self.root.title("Student Result Management System")
        
        self.root.geometry("1300x480+100+200")
        self.root.config(bg="white")
        self.root.focus_force()

        
        
        #====Variables====
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin =StringVar()


        #====Title====
        title = Label(self.root , text="Manage Students Detail",font=("goudy old style",25,"bold"),bg="#036d7d",fg="white").place(x=0 , y=20 , width="1350" )

        #====widgets====
        #====Column1====
        lbl_Roll_no =  Label(self.root, text="Roll No.",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=80)
        lbl_Name = Label(self.root, text="Name",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=130 )
        lbl_Email = Label(self.root, text="Email",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=180 )
        lbl_gender = Label(self.root,text="Gender",font=("gouudy old style",15,"bold"),bg="white").place(x=30 , y=225)
        lbl_state = Label(self.root, text="State",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=270 )
        lbl_address = Label(self.root, text="Address",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=325 )
        lbl_pin = Label(self.root, text="Pin",font=("gouudy old style" ,15,"bold"),bg="white").place(x=495 , y=270 )
        
        #====Entry Fields====
        self.txt_roll = Entry(self.root, textvariable=self.var_roll,bg="#ffffed")
        self.txt_roll.place(x=120 , y=80 , width=170 , height=25)

        self.txt_name = Entry(self.root, textvariable=self.var_name , bg="#ffffed")
        self.txt_name.place(x=120 , y=130 , width=170 ,height=25 )
        
        self.txt_email= Entry(self.root,textvariable=self.var_email,bg="#ffffed")
        self.txt_email.place(x=120 , y=180 , width=170 ,height=25)

        self.txt_state= Entry(self.root,textvariable=self.var_state,bg="#ffffed")
        self.txt_state.place(x=120 , y=275 , width=120 ,height=25)


        self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),font=("goudy old style",15,"bold"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=120 , y=228 ,width=170 ,height=25)
        self.txt_gender.current(0)

        #====Columns=====
        lbl_D_O_B =  Label(self.root, text="D.O.B",font=("gouudy old style" ,15,"bold"),bg="white").place(x=350 , y=80)
        lbl_Contact = Label(self.root, text="Contact",font=("gouudy old style" ,15,"bold"),bg="white").place(x=350 , y=130 )
        lbl_Admission = Label(self.root, text="Admission",font=("gouudy old style" ,15,"bold"),bg="white").place(x=350 , y=180 )
        lbl_Course = Label(self.root,text="Course",font=("gouudy old style",15,"bold"),bg="white").place(x=350 , y=225)
        lbl_city = Label(self.root, text="City",font=("gouudy old style" ,15,"bold"),bg="white").place(x=250 , y=270 )
        #====Entry====
        self.course_list=[]
        self.fetch_course()

        #====Columns 2 Entry====
        self.txt_DOB = Entry(self.root, textvariable=self.var_dob,bg="#ffffed")
        self.txt_DOB.place(x=460 , y=80 , width=170 , height=25)

        self.txt_Contact = Entry(self.root, textvariable=self.var_contact , bg="#ffffed")
        self.txt_Contact.place(x=460 , y=130 , width=170 ,height=25 )
        
        self.txt_admission= Entry(self.root,textvariable=self.var_a_date,bg="#ffffed")
        self.txt_admission.place(x=460 , y=180 , width=170 ,height=25)

        self.txt_city= Entry(self.root,textvariable=self.var_city,bg="#ffffed")
        self.txt_city.place(x=320 , y=275 , width=160 ,height=25)

        self.txt_pin= Entry(self.root,textvariable=self.var_pin,bg="#ffffed")
        self.txt_pin.place(x=550 , y=275 , width=160 ,height=25)

        
        self.txt_course= ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style" ,15,"bold"),state="readonly",justify="center")
        self.txt_course.place(x=460 , y=230 , width=170 ,height=25)
        self.txt_course.set("Empty")

        #====text_address====
        self.txt_address = Text(self.root,bg="#ffffed")
        self.txt_address.place(x=120 , y=330 ,width=600 ,height=120 )

        #====Buttons====
        self.btn_add = Button(self.root,text="Save",font=("Gouudy old style",15),cursor="hand2",fg="Black",bg="#87cefa",command=self.add )
        self.btn_add.place(x=200 , y=470 , width=110 , height=40)
        self.btn_update = Button(self.root,text="Update",font=("Gouudy old style",15),cursor="hand2",fg="Black",bg="#7cfc00",command=self.update)
        self.btn_update.place(x=330 , y=470 , width=110 , height=40)
        self.btn_Delete = Button(self.root,text="Delete",font=("Gouudy old style",15),cursor="hand2",fg="Black",bg="pink",command=self.delete)
        self.btn_Delete.place(x=460 , y=470 , width=110 , height=40)
        self.btn_Clear = Button(self.root,text="Clear",font=15 ,cursor="hand2",fg="Black",bg="orange",command=self.clear)
        self.btn_Clear.place(x=590 , y=470 , width=110 , height=40)

        #====Search panel====
        self.var_search=StringVar()
        lbl_search_couse = Label(self.root,text="Search By",font=("gouudy old style",15,"bold"),bg="white").place(x=800,y=80)
        self.txt_search=Entry(self.root,textvariable=self.var_search,bg="lightyellow").place(x=950 , y=85 , width=200)
        self.btn_search=Button(self.root,text="Search",font=("bold",15),fg="Black" , bg="purple",cursor="hand2",command=self.search).place(x=1200 , y=75 , width=110 , height=40)
    
        #===content====
        self.c_Frame = Frame(self.root,border=2)
        self.c_Frame.place(x=800,y=150,width=510,height=340)
        scrolly=Scrollbar(self.c_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.c_Frame,orient=HORIZONTAL)
        self.student_table=ttk.Treeview(self.c_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(fill=X,side=BOTTOM)
        scrolly.pack(fill=Y,side=RIGHT)
        scrollx.config(command=self.student_table.xview,cursor="hand2")
        scrolly.config(command=self.student_table.yview,cursor="hand2")

        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("admission",text="Admission")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("state",text="State")
        self.student_table.heading("city",text="City")
        self.student_table.heading("pin",text="Pin")
        self.student_table.heading("address",text="Address")
        self.student_table["show"]="headings"
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("admission",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("state",width=150)       
        self.student_table.column("city",width=100)
        self.student_table.column("pin",width=100)
        self.student_table.column("pin",width=200)
       
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_data)
        #self.student_table.bind("<ButtonRelease-1>",self.delete)
        self.show()
       

    def clear(self):
        self.txt_roll.config(state="normal")
        self.show()
       # self.txt_roll.config(state="normal")
        self.var_roll.set(" ")
        self.var_roll.set(" ")
        self.var_name.set(" ")
        self.var_email.set(" ")
        self.var_gender.set(" ")
        self.var_dob.set(" ")
        self.var_contact.set(" ")
        self.var_a_date.set(" ")
        self.var_course.set(" ")
        self.var_state.set(" ")
        self.var_city.set(" ")
        self.var_pin.set(" ")
        self.txt_address.delete('1.0',END)
        self.txt_course.set("Empty")
        self.txt_gender.current(0)

      
       
                        
        
        #====================================================

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Student should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select a Student",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from Student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student Deleted Sucessfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def get_data(self,ev):
        try:
            if True:
                self.txt_roll.config(state="readonly")
                r=self.student_table.focus()
                content=self.student_table.item(r)
                row=content["values"]
        
                self.var_roll.set(row[0])
                self.var_name.set(row[1])
                self.var_email.set(row[2])
                self.var_gender.set(row[3])
                self.var_dob.set(row[4])
                self.var_contact.set(row[5])
                self.var_a_date.set(row[6])
                self.var_course.set(row[7])
                self.var_state.set(row[8])
                self.var_city.set(row[9])
                self.var_pin.set(row[10])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[11])
           

        except Exception as e:
             messagebox.showerror("Error",f"Error due to {str(e)}")


      
    
    def update(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select student from table",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=? ",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get()
                        
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess","Student Updated Sucessfully",parent=self.root )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
        

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No. Already Present",parent=self.root)
                else:
                    cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                       # self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess","Student Added Sucessfully",parent=self.root )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

       
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from student where roll LIKE '%{self.var_roll.get()}%' ")
            rows=cur.fetchall()
            if rows!=None:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
            else:
                messagebox.showinfo("Eror")

        except Exception as ex:
            messagebox.showerror("Eror",f"Error due to {str(ex)}")


    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Eror",f"Error due to {str(ex)}")

        
    def fetch_course(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        v=[]
        try:
            cur.execute("select name from course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        
                
        except Exception as ex:
            messagebox.showerror("Eror",f"Error due to {str(ex)}")


 
        

if __name__=="__main__":
    root=Tk()
    obj=StudentClass(root)
    root.mainloop() 