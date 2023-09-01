from typing import Optional, Tuple, Union
from customtkinter import *
from tkinter import ttk
import sqlite3 as sq
import turtleRace
from tkinter import messagebox
from tkinter import *
conn = sq.connect('StudentData.db')
cursor = conn.cursor()
window = CTk()
#set_appearance_mode("dark")
#toplevel = CTkToplevel(window)
def toplevel3():
    delwindow = CTkToplevel(window)
    delwindow.geometry("400x200")
    delwindow.title("DELETE")
    entry = Entry(delwindow, width=90)
    label = Label(delwindow, text="ID: ", font=("Monospace", 20))
    label.grid(row=0, column=0, padx=5, pady=5)
    entry.grid(row=0, column=1, padx=5, pady=5)
    btn = Button(delwindow, text="Delete", width=40, height=2, font=("Monospace", 16))
    btn.grid(row=1, column=1, columnspan=2)
def toplevel2():

    wn = CTkToplevel(window)
    #wn.geometry("500x500")
    testLabel = CTkLabel(wn, text="ID:", font=CTkFont(size=15, weight='bold'))
    testLabel.grid(row=0, column=0, padx=5, pady=5)

    InfoLabel = CTkLabel(wn, text="Updating? :", font=CTkFont(size=15, weight='bold'))
    InfoLabel.grid(row=0, column=4, padx=5, pady=5)

    InfoEntry = CTkEntry(wn, width=200, placeholder_text="What do you wish to update?", corner_radius=3)
    InfoEntry.grid(row=0, column=5, padx=5, pady=5, columnspan=5)
    
    IDentry = CTkEntry(wn, corner_radius=3)
    IDentry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

    UpdateEntry = CTkEntry(wn, width=300, placeholder_text="Place Update Info", corner_radius=3)
    UpdateEntry.grid(row=2, column=0, padx=5, columnspan=10)

    UpdateEntryBtn = CTkButton(wn, text="UPDATE", corner_radius=3, width=300)
    UpdateEntryBtn.grid(row=3, column=0, columnspan=10, padx=5, pady=5)
    
    def Change():
        
        conn = sq.connect('StudentData.db')
        cursor = conn.cursor()

        ID = IDentry.get()
        NewInfo = InfoEntry.get()
        Update = UpdateEntry.get()
        cursor.execute(f"UPDATE Student_Data SET {NewInfo} = ? WHERE id = ?", (Update, ID))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Update Successful")
    UpdateEntryBtn = CTkButton(wn, text="UPDATE", corner_radius=3, width=300, command=Change)    
    UpdateEntryBtn.grid(row=3, column=0, columnspan=10, padx=5, pady=5)


def race():
    turtleRace.turtle()

def openTopLevel():
    """""
    global name, age, nationality, entry_year, email    
    conn = sq.connect('StudentData.db')
    cursor = conn.cursor()

    student_id = entry.get()

    query = "SELECT * FROM Student_Data WHERE id = ?"
    cursor.execute(query, (student_id))

    result = cursor.fetchone()

    if result:
        #print("Student ID: ", result[0])
        name.set(result[2])
        age.set(result[3])
        nationality.set(result[4])
        entry_year.set(result[7])
        email.set(result[8])
        
    else:
        print("No student found with the given ID")

    conn.close()
    """    
    #global toplevel
    root = CTkToplevel(window)
    root.title("Top Level")
    root.geometry("550x200")
    #toplevel.mainloop() 
    frame = CTkFrame(root, height=700, width=400)
    frame.pack(pady=5)

    searchLabel = CTkLabel(frame, width=400, text="SEARCH WIDGET", font=CTkFont(size=30, weight="bold"))
    searchLabel.grid(row=0, column=0, columnspan=7, pady=5)
    #s
    btn = CTkButton(frame, width=90, text="EXIT")
    btn.grid(row=0, column=8, padx=5)


    #The Labels

    NameLabel = CTkLabel(frame, text="Name: ")
    AgeLabel = CTkLabel(frame, text="Age:")
    NationalityLabel = CTkLabel(frame, text="Nationality: ")
    EntryYearLabel = CTkLabel(frame, text="Entry Year: ")
    EmailLabel = CTkLabel(frame, text="Email: ")

    NameLabel.grid(row=1, column=0)
    AgeLabel.grid(row=2, column=0)
    NationalityLabel.grid(row=3, column=0)
    EntryYearLabel.grid(row=4, column=0)
    EmailLabel.grid(row=5, column=0)

    #The Variables
    #global name, age, nationality, entry_year, email
    name = StringVar()
    Name = CTkLabel(frame, textvariable=name)
    Name.grid(row=1, column=1)

    age = StringVar()
    Age = CTkLabel(frame, textvariable=age)
    Age.grid(row=2, column=1)

    nationality = StringVar()
    Nationality = CTkLabel(frame, textvariable=nationality)
    Nationality.grid(row=3, column=1)

    entry_year = StringVar()
    EntryYear = CTkLabel(frame, textvariable=entry_year)
    EntryYear.grid(row=4, column=1)

    email = StringVar()
    Email = CTkLabel(frame, textvariable=email)
    Email.grid(row=5, column=1)
    #from here
    #global name, age, nationality, entry_year, email    
    conn = sq.connect('StudentData.db')
    cursor = conn.cursor()

    student_id = entry.get()

    query = "SELECT * FROM Student_Data WHERE id = ?"
    cursor.execute(query, (student_id))

    result = cursor.fetchone()

    if result:
        #print("Student ID: ", result[0])
        name.set(result[2])
        age.set(result[3])
        nationality.set(result[4])
        entry_year.set(result[7])
        email.set(result[8])
        
    else:
        print("No student found with the given ID")

    conn.close()          


sideframe = CTkFrame(window, height=650)
sideframe.grid(row=0, column=0, rowspan=10, pady=5, padx=2)
#Side Buttons
NavBarLabel = CTkLabel(sideframe, text="Nav-Bar", font=CTkFont(size=20, weight="bold"))
NavBarLabel.grid(row=0, column=0, pady=10)
updatebtn = CTkButton(sideframe, width=120, text="Create new", font=CTkFont(size=17, weight='normal'), corner_radius=3)
updatebtn.grid(row=1, column=0, columnspan=3, pady=20)

deletebtn = CTkButton(sideframe, width=120, text="Update", font=CTkFont(size=17, weight='normal'), corner_radius=3, command=toplevel2)
deletebtn.grid(row=3, column=0, columnspan=3, pady=20, padx=5)

clearbtn = CTkButton(sideframe, width=120, text="Delete", font=CTkFont(size=17, weight='normal'), corner_radius=3, command=toplevel3)
clearbtn.grid(row=5, column=0, columnspan=3, pady=20)
def changeTheme():
    #set_appearance_mode("dark")
    if toggle._onvalue:
       (set_appearance_mode("dark"))
    else:
       (set_appearance_mode("light"))
toggle = CTkSwitch(sideframe, text="Theme", command=changeTheme)
toggle.grid(row=8, column=0, pady=10)

Option = CTkOptionMenu(sideframe, corner_radius=3, values=["save", "save as"], font=CTkFont(size=17, weight='normal'))
Option.grid(row=6, column=0, pady=10, padx=5)

GameBtn = CTkButton(sideframe, text='\U0001F422', corner_radius=3, command=race)
GameBtn.grid(row=7, column=0, pady=10, padx=5)


#Search Frame
SearchFrame = CTkFrame(window, height=100, width=1066)
SearchFrame.grid(row=0, column=1, padx=8, columnspan=14)
entry = CTkEntry(SearchFrame, width=980, placeholder_text="Enter Student ID: ")
entry.grid(row=0, column=0, columnspan=8, pady=5)
btn = CTkButton(SearchFrame, width=90, text="\U0001F50D", corner_radius=3, command=openTopLevel)
btn.grid(row=0, column=8, padx=5)

mainFrame = CTkScrollableFrame(window, height=540, width=1058)
mainFrame.grid(row=1, column=1, rowspan=8, columnspan=10, padx=10, pady=5)
tree = ttk.Treeview(mainFrame, height=500, columns=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9"), show="headings")
tree.pack(fill=BOTH, expand=True)
tree.column("column1", width=80)
#tree.configure(height=30)
tree.heading("column2", text="NULL")
tree.heading("column3", text="NAME")
tree.heading("column4", text="AGE")
tree.heading("column5", text="NATIONALITY")
tree.heading("column6", text="COURSE")
tree.heading("column7", text="SEMESTERS")
tree.heading("column8", text="YEAR OF ENTRY")
tree.heading("column9", text="EMAIL")
style = ttk.Style()
style.configure("Treeview", font=("Arial", 15))

cursor.execute("SELECT * FROM Student_Data")
rows = cursor.fetchall()

for row in rows:
    tree.insert("", END, values=row)

conn.close()



window.mainloop()