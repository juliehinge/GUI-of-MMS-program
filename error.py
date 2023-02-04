from tkinter import *
from tkinter import ttk
import tkinter as tk

class Error:
    def __init__(self, master, error_list):
        super().__init__()
        global INPUT

        self.master = master
        self.master.title("Input Exceptions")

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
 
        ttk.Label(self.frame_content, text="Form Validation Errors", font = ("bold", 20)).grid(row=0, column=0, columnspan = 2, padx = 40, pady = (50,20))


        for i, message in enumerate(error_list):
            ttk.Label(self.frame_content, text = message).grid(row=i+1, column = 0, sticky = "w", padx = 50 )


        self.okay = ttk.Button(self.frame_content, text = "Okay", command = self.close_window).grid(row=len(error_list)+1, column=0, padx = (0,10), pady = 20)



    def close_window(self):
        self.master.destroy()

