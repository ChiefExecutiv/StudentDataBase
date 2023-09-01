import customtkinter as ck
from tkinter import messagebox
from tkinter import ttk
import sqlite3
ck.set_appearance_mode("dark")
conn = sqlite3.connect('StudentData.db')

table_create_query  = '''CREATE TABLE IF NOT EXISTS Student_Data
(id INTEGER PRIMARY KEY AUTOINCREMENT,StudentID INT, Name TEXT, Age INT, Nationality TEXT, Course TEXT, Num_Semesters INT, EntryYear INT, Email TEXT, Password TEXT)'''
conn.execute(table_create_query)
#Insert Data 

def InsertData(Name, Age, Nationailty, Course, Num_Semesters, EntryYear, Email, password):
     conn = sqlite3.connect('StudentData.db')
     cursor = conn.cursor()
     cursor.execute('''INSERT INTO Student_Data (Name, Age, Nationality, Course, Num_Semesters, EntryYear, Email, password) VALUES
     (?, ?, ?, ?, ?, ?, ?, ?)''',(Name, Age, Nationailty, Course, Num_Semesters, EntryYear, Email, password))
     conn.commit()
     conn.close()
window = ck.CTk()
frame = ck.CTkFrame(window)
frame.pack()
def GetInfo():
    email = EmailLabel.get()
    password = PassWORDLabel.get()
    name1 = firstnameLabel.get()
    name2 = lastnameLabel.get()
    NAme = name1 + " " + name2
    COurse = courseEntry.get()
    semesters = numSemesters.get()
    entryYear = courseYear.get()
    NAtionality = NaTionality.get()
    Birth = BirthLabel.get()
    InsertData(NAme, Birth, NAtionality, COurse, semesters, entryYear, email, password)
    Messagebox = messagebox.showinfo("Success", "Account Created Successfully")
    




user_info_Frame = ck.CTkScrollableFrame(frame, width=500)
user_info_Frame.grid(row=0, column=0, padx=20, pady=20)

EmailLabel = ck.CTkEntry(user_info_Frame, placeholder_text="example@gmail.com", corner_radius=5, width=200)
EmailLabel.grid(row=0, column=0, padx=10, pady=10)

PassWORDLabel = ck.CTkEntry(user_info_Frame, placeholder_text="Create Password", width=200)
PassWORDLabel.grid(row=1, column=0, padx=10, pady=10)

firstnameLabel = ck.CTkEntry(user_info_Frame, placeholder_text="First Name")
firstnameLabel.grid(row=2, column=0, padx=5, pady=10)
lastnameLabel = ck.CTkEntry(user_info_Frame, placeholder_text="Last Name")
lastnameLabel.grid(row=2, column=1, padx=5, pady=10) 

BirthLabel = ck.CTkEntry(user_info_Frame, placeholder_text="Age", width=200)
BirthLabel.grid(row=3, column=0, padx=10, pady=10)
NaTionality = ck.CTkComboBox(user_info_Frame, values=["Ugandan", "Kenyan", "Tanzania", "Rwanda", "Other"])
NaTionality.grid(row=3, column=1, padx=10, pady=10)

CourseLabel = ck.CTkLabel(user_info_Frame, text="COURSE INFO", font=ck.CTkFont(size=16, weight="bold"))
CourseLabel.grid(row=4, column=0)

course = ck.CTkLabel(user_info_Frame, text="Course: ", font=ck.CTkFont(size=12, weight="bold"))
courseEntry = ck.CTkEntry(user_info_Frame)

course.grid(row=5, column=0)
courseEntry.grid(row=5, column= 1)

courseYear = ck.CTkEntry(user_info_Frame, placeholder_text="Year of Entry")
courseYear.grid(row=5, column=2, pady=10)
numSemesters = ttk.Spinbox(user_info_Frame, from_=0, to=10, width=20, font=("Monospace", 20))
numSemesters.grid(row=6, column=1, columnspan=2, sticky="w")
SemesterLabel = ck.CTkLabel(user_info_Frame, text="Semesters:", font=ck.CTkFont(size=12, weight="bold"))
SemesterLabel.grid(row=6, column=0)

submitButton = ck.CTkButton(frame, text="SUBMIT", width=500, command=GetInfo)
submitButton.grid(row=1, column=0, padx=10)

window.mainloop()