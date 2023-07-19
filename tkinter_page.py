import  tkinter
from tkinter import ttk
from tkinter import messagebox
def enter_data():
    #user info
    Acceptable =accept_var.get()
    if Acceptable == "Accepted":
        # user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()

        #courage info
        registration_status= reg_statu_var.get()
        numcourse = numcourses_spinbox.get()
        numsemesters = numsemester_spinbox.get()

        print("First name:" ,firstname,"Last name:",lastname)
        print("Title:",title,"Age:",age,"Nationality:",nationality)
        print("#Courses:",numcourse,"#Semesters:",numsemesters)
        print("Registration",registration_status)
        print("---------------------------------------------------------------------------------------")
    else:
        tkinter.messagebox.showwarning(title = " Error",message ="You have a not accepted the term")

window = tkinter.Tk()
window.title("Data Entry form")
frame = tkinter.Frame(window)
frame.pack()

#saving user information
user_info_frame = tkinter.LabelFrame( frame,text="user Information")
user_info_frame.grid(row =0,column=0,padx=20,pady=10)

first_name_lable = tkinter.Label(user_info_frame,text="First name")
first_name_lable.grid(row =0,column=0)

last_name_lable = tkinter.Label(user_info_frame,text="Last name")
last_name_lable.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry= tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_lable = tkinter.Label(user_info_frame,text="Title")
title_combobox = ttk.Combobox(user_info_frame,values = [""," Mr.","Ms.","Dr."])
title_lable.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_lable = tkinter.Label(user_info_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18,to=125)
age_lable.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_lable = tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame,values=["America","India","Africa","Asia","china","Pakistan","Europe"])
nationality_lable.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

    #saving couse info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1,column=0,sticky="news", padx=20,pady=10)

registered_lable = tkinter.Label(courses_frame,text="Registration Status")

reg_statu_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame,text="Currently registered",variable= reg_statu_var,onvalue='Registered',offvalue='Not Registered')


registered_lable.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_lable =  tkinter.Label(courses_frame,text="#Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame,from_=0,to="infinity")
numcourses_lable.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)


numsemesterlable =  tkinter.Label(courses_frame,text="#Semesters")
numsemester_spinbox = tkinter.Spinbox(courses_frame,from_=0,to="infinity")
numsemesterlable.grid(row=0,column=2)
numsemester_spinbox.grid(row=1,column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#accept terms
term_fram = tkinter.LabelFrame(frame,text="Terms and Conditions")
term_fram.grid(row=2,column=0,sticky="news",padx=20,pady=10)

accept_var = tkinter.StringVar(value="Not accepted")
term_check = tkinter.Checkbutton(term_fram,text="I accept the terms and conditions",variable= accept_var,onvalue= "Accepted",offvalue="Not Accepted")
term_check.grid(row=0,column=0)

#Button
button = tkinter.Button(frame,text="Enter Data",command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)

window.mainloop()