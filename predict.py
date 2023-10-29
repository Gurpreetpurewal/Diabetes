import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import pymongo
from pymongo import MongoClient
import subprocess
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import tree
from io import BytesIO

class diabetestmainframe:
    def __init__(self,root):
        
        self.root = root
        self.root.title("Diabetes mellitus")
        self.root.geometry('1000x600')        
        self.gui()
        self.loading()
        self.trainmodel()
        
        
    def gui(self):
        self.backgroundframe = Image.open('guru2.png')
        photo = ImageTk.PhotoImage(self.backgroundframe)
        self.background_panel = tk.Label(self.root, image=photo)
        self.background_panel.image = photo
        self.background_panel.pack(fill='both', expand='yes')
        #login frame
        self.framedata = tk.Frame(self.root, bg='#E0EEEE', width='750', height='600')

        self.framedata.place(x=450, y=150)
        
        self.txt = 'Do not own it because it does not belong to you!!'
        self.heading = tk.Label(self.framedata, text=self.txt, font=("Comic Sans MS", 20, "bold"),bg='#E0EEEE', fg='Black')        
        self.heading.place(x=15,y=5,width=700,height=100)        
        #sign in images
        
        #userage
        self.user_gender = tk.Label(self.framedata,text='Pregnancies',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.user_gender.place(x=15,y=210)
        self.gender_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.gender_entry.place(x=300,y=210,width=200)
        
        #usergender
        self.user_age = tk.Label(self.framedata,text='Glucose',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.user_age.place(x=15,y=235)
        self.user_age_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.user_age_entry.place(x=300,y=235,width=200)
        
        #user_hyper
        self.user_hyper = tk.Label(self.framedata,text='BloodPressure',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.user_hyper.place(x=15,y=260)
        self.user_hyper_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.user_hyper_entry.place(x=300,y=260,width=200)
        
        #heartdisease
        self.heartdisease = tk.Label(self.framedata,text='SkinThickness',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.heartdisease.place(x=15,y=290)
        self.heartdisease_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.heartdisease_entry.place(x=300,y=290,width=200)
        
        #smoking_history
        self.smoking_his = tk.Label(self.framedata,text='Insulin',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.smoking_his.place(x=15,y=320)
        self.smoking_his_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.smoking_his_entry.place(x=300,y=320,width=200)
        
        #bmi
        self.BMI = tk.Label(self.framedata,text='BMI',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.BMI.place(x=15,y=350)
        self.BMI_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.BMI_entry.place(x=300,y=350,width=200)
        
        #HbA1c_level
        self.Hblevel = tk.Label(self.framedata,text='DiabetesPedigreeFunction',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.Hblevel.place(x=15,y=390)
        self.Hblevel_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.Hblevel_entry.place(x=300,y=390,width=200)
        
        #blood_glucose
        self.bloodglucose = tk.Label(self.framedata,text='Age',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.bloodglucose.place(x=15,y=420)
        self.bloodglucose_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=("Comic Sans MS", 10, "bold"))
        self.bloodglucose_entry.place(x=300,y=420,width=200)
        
        
        #blood_glucose
        self.Diabetes = tk.Label(self.framedata,text='Any Diabetes History',bg='#E0EEEE',font=("Comic Sans MS", 10, "bold"),fg='#4f4e4d')
        self.Diabetes.place(x=15,y=450)
        self.Diabetes_entry= tk.Entry(self.framedata,highlightthickness=0,bg='white',fg='#6b6a69',font=('yu gothic vi',10,'bold'))
        self.Diabetes_entry.place(x=300,y=450,width=200)
  
        self.predict_button = tk.Button(self.framedata, text="Predict", command=self.predict_diabetes)
        self.predict_button.place(x=580,y=450)

        # Decision Tree Graph button
        self.graph_button = tk.Button(self.framedata, text="Show Decision Tree Graph", command=self.show_decision_tree_graph)
        self.graph_button.place(x=580,y=400)
        
        
        
    def loading(self):
        # Connect to MongoDB and fetch the dataset
        client = MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.rlyzjps.mongodb.net/")
        db = client["project"]
        collection = db["decisiontree"]
        data = list(collection.find())
        self.df = pd.DataFrame(data)  # Assuming data is stored as a DataFrame
        categorical_columns = self.df.select_dtypes(include=['object']).columns

        # Apply Label Encoding or One-Hot Encoding to each categorical column
        for column in categorical_columns:
            # Option 1: Label Encoding
            self.df[column] = self.df[column].astype('category')
            self.df[column] = self.df[column].cat.codes

    
    def trainmodel(self):
        self.X = self.df.drop("Outcome", axis=1)
        print(self.X)
        
        self.y = self.df["Outcome"]
        print(self.y)
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Create and train the decision tree classifier
        self.model = DecisionTreeClassifier()
        self.model.fit(X_train, y_train)

    def predict_diabetes(self):
        gender = int(self.gender_entry.get())
        age = int(self.user_age_entry.get())
        user_hyper = int(self.user_hyper_entry.get())
        heartd = int(self.heartdisease_entry.get())
        smoking = int(self.smoking_his_entry.get())
        bmi = int(self.BMI_entry.get())
        Hblevel = int(self.Hblevel_entry.get())
        glucose = int(self.bloodglucose_entry.get())
        dib = float(self.Diabetes_entry.get())
        userdata = {
                    'Pregnancies': gender, 
                    'Glucose': age,
                    'BloodPressure': user_hyper, 
                    'SkinThickness': heartd, 
                    'Insulin': smoking,
                    'BMI':bmi,
                    'DiabetesPedigreeFunction': Hblevel, 
                    'Age': glucose,
                    "Outcome": dib
                    }
    
       
        userdata_array = np.array([list(userdata.values())])

        # Make a prediction using the model
        prediction = self.model.predict(userdata_array)
        print(prediction)
        
        if prediction[0] == 1:
            messagebox.showerror("Alert","The model predicts a High risk of a Diabetes.")
        else:
            messagebox.showerror("The model predicts a low risk of a Diabetes attack.")
            
    def show_decision_tree_graph(self):
        plt.figure(figsize=(12, 8))
        tree.plot_tree(self.model, filled=True, feature_names=self.X.columns.tolist(), class_names=["No Heart Attack", "Heart Attack"])
        plt.title("Diabetes Decision Tree Graph")
        img_data = BytesIO()
        plt.savefig(img_data, format="png")
        img_data.seek(0)

        # Create a new window to display the graph
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Decision Tree Graph")
        img = tk.PhotoImage(data=img_data.read())
        img_label = tk.Label(graph_window, image=img)
        img_label.image = img
        img_label.pack()
        img_data.close()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = diabetestmainframe(root)
    root.mainloop()
