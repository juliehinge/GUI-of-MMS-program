
import tkinter as tk
from tkinter import ttk
from tkinter import *
from admin_window import Admin


class Login:
    def __init__(self, master):

        global INPUT

        self.master = master
        self.frame = tk.Frame(self.master)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text="Login", font = ("bold", 20)).grid(row=0, column=0, sticky = 'w', padx = 30, pady = (30,10))
        ttk.Label(self.frame_content, text="Email:", font = ("bold", 15)).grid(row=1, column=0, sticky='w', padx = (30,10))
        ttk.Label(self.frame_content, text="Password:", font = ("bold", 15)).grid(row=2, column=0, sticky = 'w', padx=(30,10))

        self.entry_username = ttk.Entry(self.frame_content,background = 'green')
        self.entry_password = ttk.Entry(self.frame_content)
        self.entry_password.config(show = "•")

        self.entry_username.grid(row=1, column=1, columnspan = 4, padx = (0,20))
        self.entry_password.grid(row=2, column=1, columnspan = 4, padx = (0,20))

        self.Btn1 = ttk.Button(self.frame_content, text = "OK", width = 5, command = lambda:self.verify()).grid(row=4, column=1, pady=20)
        self.Btn1 = ttk.Button(self.frame_content, text = "Cancel", width = 5, command = lambda:self.verify()).grid(row=4, column=2, sticky='w', padx = (0,10),pady=20)

        self.myText = StringVar(self.frame_content, value=' ')
        self.text = ttk.Label(self.frame_content, textvariable = self.myText, foreground ="red").grid(row=3, column=1, pady = 5, sticky='w')


    def verify(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "john.smith@uts.com" and password == "user222":
            self.open_admin_window("John Smith")
        
        elif username == "jane.tyler@uts.com" and password == "super123":
             self.open_admin_window("Jane Tyler")


        else:
           # self.open_admin_window()
            self.myText.set("Incorrect login details!")

        
    def open_admin_window(self, username):
    
        self.master = tk.Tk() # create another Tk instance
        self.app = Admin(self.master, username) # create Demo2 window
     
