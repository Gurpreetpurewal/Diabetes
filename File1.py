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
db = client["project"]
user_data_collection = db["inputdata"]


class sign_up:
    def __init__(self,root):
        self.root = root
        self.root.title("Diabetes")
        self.root.geometry('1166x718')
        self.root.state('zoomed')
        #self.root.resizable(0,0)
        self.bg_frame = Image.open('guru2.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.backgroundpanel = tk.Label(self.root, image=photo)
        self.backgroundpanel.image = photo
        self.backgroundpanel.pack(fill='both', expand='yes')
        #login frame
        self.login_frame = tk.Frame(self.root, bg='#E0EEEE', width='650', height='500')
        self.login_frame.place(x=450, y=150)
        
        self.txt = 'Diabetes mellitus'
        self.heading = tk.Label(self.login_frame, text=self.txt, font=("Comic Sans MS", 20, "bold"),bg='#E0EEEE', fg='black')        
        self.heading.place(x=15,y=5,width=700,height=100) 
        
        #sign in images
        self.sign_in_image = Image.open('download44.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = tk.Label(self.login_frame, image=photo, bg='#E0EEEE')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=40,y=180)
        
        self.sign_in_label = tk.Label(self.login_frame, text='Sign Up',bg='#E0EEEE',fg='black',font=("Comic Sans MS", 10, "bold"))
        self.sign_in_label.place(x=320,y=100)
        
        #username
        self.username_label = tk.Label(self.login_frame,text='UserName',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.username_label.place(x=280,y=200)
        self.username_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.username_entry.place(x=380,y=200,width=200)
       
        
        
        #Email ID
        self.email_id_label = tk.Label(self.login_frame,text='Email_Id',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.email_id_label.place(x=280,y=250)
        self.email_id_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.email_id_entry.place(x=380,y=250,width=200)
        
        #password
        self.password_label = tk.Label(self.login_frame,text='Password',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.password_label.place(x=280,y=300)
        self.password_entry= tk.Entry(self.login_frame,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.password_entry.place(x=380,y=300,width=200)

        #login button
        self.loginButton = tk.Button(self.login_frame, text='Create',bg='#E0EEEE',fg='#6b6a69',command=self.userinput)
        #self.login = tk.Button(self.logn_button_label)
        self.loginButton.place(x=420,y=350)
        
        #back to front page
        self.loginButton = tk.Button(self.login_frame, text='login Page',bg='#E0EEEE',fg='#6b6a69',command=self.link)
        #self.login = tk.Button(self.logn_button_label)
        self.loginButton.place(x=500,y=350)
        
        self.message_label = tk.Label(self.login_frame, text="",fg='black') 
        self.message_label.place(x=400,y=380)
        
        self.root.mainloop()
        
    
    def userinput(self):
        name = self.username_entry.get()
        email = self.email_id_entry.get()
        password = self.password_entry.get()
        user_data = {
            "firstname": name,
            "email": email,
            "pass": password
        }
 
        # Insert user input data into MongoDB
        user_data_collection.insert_one(user_data)
 
        self.cleartaxt()
        self.message_label.config(text="Successfully account created")
 
    def cleartaxt(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.email_id_entry.delete(0, 'end')
    
    def link(self):
        # Close the current window
        root.destroy()
        
        # Run the second Python script using subprocess
        subprocess.Popen(["python", "link.py"])
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = sign_up(root)
    root.mainloop()
        
