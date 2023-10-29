# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import PIL
from PIL import ImageTk
from PIL import Image
import pymongo
from pymongo import MongoClient
import subprocess

client = MongoClient('mongodb+srv://gurpreet:gurpreet@cluster0.rlyzjps.mongodb.net/')
datebase = client['project']
db_person = datebase['inputdata']


class sign_up:
    def __init__(self,root):
        self.root = root
        self.root.title("Diabetes")
        self.root.geometry('1166x718')
        self.bg_frame = Image.open('guru2.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = tk.Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        #login frame
        self.login_frame = tk.Frame(self.root, bg='#E0EEEE', width='750', height='400')
        self.login_frame.place(x=420, y=150)
        
        self.txt = 'Do not own it because it does not belong to you!!'
        self.header = tk.Label(self.login_frame, text=self.txt, font=("Comic Sans MS", 20, "bold"),bg='#E0EEEE', fg='black')        
        self.header.place(x=15,y=5,width=700,height=100)

        #middle image
        self.centerimage = Image.open('download44.png')
        photo = ImageTk.PhotoImage(self.centerimage)
        self.centerimage_label = tk.Label(self.login_frame, image=photo, bg='#E0EEEE')
        self.centerimage_label.image = photo
        self.centerimage_label.place(x=20,y=150)
        
        self.sign_in_label = tk.Label(self.login_frame, text='Sign In',bg='#E0EEEE',fg='black',font=("Comic Sans MS", 10, "bold"))
        self.sign_in_label.place(x=530,y=150)
        
        #username
        self.email_id = tk.Label(self.login_frame,text='Email ID',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.email_id.place(x=370,y=200)
        self.email_id= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.email_id.place(x=470,y=200,width=200)
        
        #password
        self.password = tk.Label(self.login_frame,text='password',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.password.place(x=370,y=250)
        self.password= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"),show="*")
        self.password.place(x=470,y=250,width=200)
        
        #login button
        self.loginButton = tk.Button(self.login_frame, text="Login",font=("Comic Sans MS", 10, "bold"),bg='#E0EEEE',fg='#6b6a69',command=self.user_credentials) 
        #self.login = tk.Button(self.logn_button_label)
        self.loginButton.place(x=480,y=300)
       
        self.sign_up_button = tk.Button(self.login_frame,text='SignUp',font=("Comic Sans MS", 10, "bold"),fg='#6b6a69',bg='#E0EEEE',command=self.sign_in)
        self.sign_up_button.place(x=540,y=300)

    def sign_in(self):
        # Close the current window
        root.destroy()
        
        # Run the second Python script using subprocess
        subprocess.Popen(["python", "File1.py"])
        
    def user_credentials(self):
        email = self.email_id.get()
        pas = self.password.get()
        user = db_person.find_one({'email':email,'pass':pas})
        
        if user:
            messagebox.showerror("Login","Successfully Login")
            self.predict()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            
    
    def predict(self):
        # Close the current window
        root.destroy()
        
        # Run the second Python script using subprocess
        subprocess.Popen(["python", "predict.py"])
        
if __name__ == "__main__":
    root = tk.Tk()
    app = sign_up(root)
    root.mainloop()
