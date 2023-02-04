from tkinter import *
from tkinter import ttk
import tkinter as tk
from login import Login
from admin_window import Admin # dont forget to delete

class Intro:
    def __init__(self, master):
        super().__init__()
        global INPUT

        self.master = master

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.image = PhotoImage(file = "loGo.png")
        self.logo = self.image.subsample(7, 7) 

        ttk.Label(self.frame_header, image = self.logo).grid(row=0, column=0, padx = 100)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text="Membership Management System").grid(row=4, column=2, columnspan = 2, padx = 100, pady = (50,10))

        self.login = ttk.Button(self.frame_content, text = "Login", command = self.open_login_window).grid(row=5, column=2, sticky = 'e', padx = (0,10))
        self.exit = ttk.Button(self.frame_content, text = "Exit", command = master.destroy).grid(row=5, column=3, sticky = 'w', padx = (10,0))



    def open_login_window(self):
        name = "Jane Tyler"
     #   self.master.destroy() # close the current window
        self.master = tk.Tk() # create another Tk instance
      #  self.app = Admin(self.master, name) # create Demo2 window
        self.app = Login(self.master) # create Demo2 window

      #  self.master.mainloop()



