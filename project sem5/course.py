from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk , messagebox
import calendar
import datetime
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.maxsize(1350,550)
        self.root.minsize(1350,550)
        self.root.title("Student Result Management System")
        
        self.root.geometry("1300x480+100+200")
        self.root.config(bg="white")
        self.root.focus_force()

        
        
        #====Variables====
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_date = StringVar()


        #====Title====
        title = Label(self.root , text="Manage Course Details",font=("goudy old style",25,"bold"),bg="#036d7d",fg="white").place(x=0 , y=20 , width="1350" )

        #====widgets====
        lbl_course_name = Label(self.root, text="Course Name",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=80)
        lbl_course_date = Label(self.root, text="Date",font=("gouudy old style" ,15,"bold"),bg="white").place(x=500 , y=80)
        lbl_Duration = Label(self.root, text="Duration",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=130 )
        lbl_Charge = Label(self.root, text="Charges",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=180 )
        lbl_description = Label(self.root, text="Description",font=("gouudy old style" ,15,"bold"),bg="white").place(x=30 , y=240 )
        
        #====Entry Fields====
        self.txt_course_name = Entry(self.root, textvariable=self.var_course,bg="#ffffed")
        self.var_date=datetime.datetime.now()
        self.txt_course_name.place(x=200 , y=85 , width=200)

        self.txt_course_date = Entry(self.root, textvariable=self.var_date,bg="#ffffed")
        self.txt_course_date.place(x=550 , y=85 , width=200)

        self.txt_Duration = Entry(self.root, textvariable=self.var_duration , bg="#ffffed")
        self.txt_Duration.place(x=200 , y=135 , width=200 )
        self.txt_Charge = Entry(self.root, textvariable=self.var_charges,bg="#ffffed")
        self.txt_Charge.place(x=200 , y=190 , width=200 )

        self.txt_description = Text(self.root,bg="#ffffed")
        self.txt_description.place(x=200 , y=240 ,width=500 ,height=150 )

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


        scrolly=Scrollbar(self.c_Frame,orient=VERTICAL,cursor="hand2")
        scrollx=Scrollbar(self.c_Frame,orient=HORIZONTAL,cursor="hand2")
        self.course_table=ttk.Treeview(self.c_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(fill=X,side=BOTTOM)
        scrolly.pack(fill=Y,side=RIGHT)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)


        self.course_table.heading("cid",text="Course ID")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("duration",text="Duration")
        self.course_table.heading("charges",text="Charges")
        self.course_table.heading("description",text="Description")
        self.course_table["show"]="headings"
        self.course_table.column("cid",width=100)
        self.course_table.column("name",width=100)
        self.course_table.column("duration",width=100)
        self.course_table.column("charges",width=100)
        self.course_table.column("description",width=150)
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        #self.course_table.bind("<ButtonRelease-1>",self.delete)
        self.show()

    def clear(self):
        self.show()
        self.var_course.set(" ")
        self.var_duration.set("")
        self.var_charges.set(" ")
        self.txt_description.delete('1.0',END)
        self.var_search.set(" ")
        self.txt_course_name.config(state="normal")
        #====================================================

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select a course",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course Deleted Sucessfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def get_data(self,ev):
        self.txt_course_name.config(state="readonly")
        r=self.course_table.focus()
        content=self.course_table.item(r)
        row=content["values"]
    
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])
      
    
    def update(self): 
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","select course from tale",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charge=?,description=? where name=? ",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess","Course Updated Sucessfully",parent=self.root )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
        

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course Name Already Present",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charge,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess","Course Added Sucessfully",parent=self.root )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

       
    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%' ")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Eror",f"Error due to {str(ex)}")


    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Eror",f"Error due to {str(ex)}")

 
        

if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop() 