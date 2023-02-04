import tkinter as tk
from tkinter import ttk
from tkinter import *
from error import Error
from select import Select

class Slip:
    def __init__(self, master, name, info):
        super().__init__()
        global INPUT


        self.master = master
        self.master.title(name + " SLIP report")

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text="Membership Slip:", font = ("bold", 20)).grid(row=0, column=0, sticky = 'w', columnspan = 2, pady = (50,10))

        ttk.Label(self.frame_content, text="Total Credits:").grid(row=1, column=0, sticky = 'w', padx = 5)
        ttk.Label(self.frame_content, text="Total Expense:").grid(row=2, column=0, sticky = 'w',  padx = 5)
        ttk.Label(self.frame_content, text="Gasdeduction Rate:").grid(row=3, column=0, sticky = 'w', padx = 5)


        ttk.Label(self.frame_content, text="Pay per credite:").grid(row=1, column=2, sticky = 'w',  padx = 5)
        ttk.Label(self.frame_content, text="Dollar Available:").grid(row=2, column=2, sticky = 'w',  padx = 5)
        ttk.Label(self.frame_content, text="Deduction Rate:").grid(row=3, column=2, sticky = 'w',  padx = 5)

        info = info[name]

        PpC = round(float(info[6][1]), 2)
        total_credit = round(PpC * float(info[5]),2)
        total_expense = "$" + str(info[5]) 
        Gasdeductionrate = info[6][2]
        dollar_available = "$" + str(round(total_credit/200,2))
        D_rate = info[6][2]



        ttk.Label(self.frame_content, text=total_credit, font = ("bold",15)).grid(row=1, column=1, sticky='w',padx = 5,pady=5)
        ttk.Label(self.frame_content, text=total_expense, font = ("bold",15)).grid(row=2, column=1, sticky='w',padx = 5,pady=5)
        ttk.Label(self.frame_content, text=Gasdeductionrate, font = ("bold",15)).grid(row=3, column=1, sticky='w',padx = 5,pady=5)
        
        ttk.Label(self.frame_content, text=PpC, font = ("bold",15)).grid(row=1, column=3, sticky='w',padx = 5,pady=5)
        ttk.Label(self.frame_content, text=dollar_available, font = ("bold",15)).grid(row=2, column=3, sticky='w',padx = 5, pady=5)
        ttk.Label(self.frame_content, text=D_rate, font = ("bold",15)).grid(row=3, column=3, sticky='w',padx = 5, pady=5)



        self.close = ttk.Button(self.frame_content, text = "Close", command = self.close_window).grid(row=4, column=1, sticky = 'w', padx = (0,10), pady = 10)



    def close_window(self):
        self.master.destroy()

        