from tkinter import *

import sqlite3
import cv2
import numpy as np
import datetime
#Main frame work

root = Tk()
root.title("Software Security and Safety Project")
width = 800
height = 560
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)



#==============================VARIABLES======================================
USERNAME = StringVar()
PASSWORD = StringVar()
input1 = IntVar()
input2 = IntVar()
input3 = IntVar()
counter = 0

d = datetime.date.today()
todaysdate = d.day
 
#==============================FRAMES=========================================
Top = Frame(root, bd=2,  relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
 


#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin')")
        conn.commit()



def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            CheckNumbers()
        else:
            lbl_text.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")   
    cursor.close()
    conn.close()

def CheckNumbers():

	addition  = int(input3.get() + input2.get() + input1.get())

	if addition is todaysdate:
		USERNAME.set("")
		PASSWORD.set("")
		input1.set("")
		input2.set("")
		input3.set("")
		FailWindow()

	else:
		lbl_text.config(text="Secondary authentication FAILED", fg="red")
		USERNAME.set("")
		PASSWORD.set("")   


 
def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Software Security and Safety Project")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    content = Label(Home, text="Welcome to Lakehead University!", fg="red", font=('times new roman', 30)).pack()
    btn_back = Button(Home, text='Back', command=LogoutWindow).pack(pady=20, fill=X)


def HomeWindowHR():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Software Security and Safety Project")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    content = Label(Home, text="Welcome to Human Resources!", fg="red", font=('times new roman', 30)).pack()
    content2 = Label(Home, text="Access your Personal Data", fg="blue", font=('times new roman', 15)).pack()
    content3 = Label(Home, text="ALL employess and student data", fg="blue", font=('times new roman', 15)).pack()
    content4 = Label(Home, text="Teaching Evaluations based on Department", fg="blue", font=('times new roman', 15)).pack()
    content5 = Label(Home, text="Employee Timecards", fg="blue", font=('times new roman', 15)).pack()
    btn_back = Button(Home, text='Logout', command=LogoutWindow).pack(pady=20, fill=X)

def HomeWindowRegistrar():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Software Security and Safety Project")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Login!", font=('times new roman', 20)).pack()
    content = Label(Home, text="Welcome to the Registrar Office!", fg="red", font=('times new roman', 30)).pack()
    content2 = Label(Home, text="Access your Personal Data", fg="blue", font=('times new roman', 15)).pack()
    content3 = Label(Home, text="Student transcripts", fg="blue", font=('times new roman', 15)).pack()
    content4 = Label(Home, text="Submitted Requests", fg="blue", font=('times new roman', 15)).pack()
    btn_back = Button(Home, text='Logout', command=LogoutWindow).pack(pady=20, fill=X)

def FailWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Arithmetic Identity")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="ACCESS DENIED", fg="red", font=('times new roman', 30)).pack()
    content = Label(Home, text="Sorry you have failed secondary authentication 3 times,", fg="red", font=('times new roman', 20)).pack()
    content4 = Label(Home, text=" please try again in an hour", fg="red", font=('times new roman', 20)).pack()
    content2 = Label(Home, text="|", fg="red", font=('times new roman', 20)).pack()
    content3 = Label(Home, text="0:59", fg="blue", font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

 
def Back():
    Home.destroy()
    root.deiconify()


def LogoutWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Software Security and Safety Project")
    width = 800
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    lbl_home = Label(Home, text="Successfully Logged OUT!", font=('times new roman', 30)).pack()
    content = Label(Home, text="Please login below", fg="blue", font=('times new roman', 17)).pack()
    btn_back = Button(Home, text='Login', command=Back).pack(pady=20, fill=X)



#==============================LABELS=========================================
lbl_title = Label(Top, text = "Software Security and Safety Project", font=('arial', 15))
lbl_title.pack(fill=X)
lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
lbl_hint = Label(Form, text = "Secondary Authentication", fg="blue", font=('arial', 15), bd=15)
lbl_hint.grid(row=2, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=7, columnspan=2)
 
#==============================ENTRY WIDGETS==================================

username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)
input_1 = Entry(Form, textvariable=input1, show="*", font=(14))
input_1.grid(row=3, column=1)
input_2 = Entry(Form, textvariable=input2, show="*", font=(14))
input_2.grid(row=4, column=1)
input_3 = Entry(Form, textvariable=input3, show="*", font=(14))
input_3.grid(row=5, column=1)

 
#==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=6, columnspan=2)
btn_login.bind('<Return>', Login)




#==============================INITIALIATION==================================
if __name__ == '__main__':
    root.mainloop()