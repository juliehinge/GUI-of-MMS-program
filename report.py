
import tkinter as tk
from tkinter import ttk
from tkinter import *


class Report:
    def __init__(self, master, info):

        global INPUT
        self.master = master
        self.master.title("MMS Report")


        self.main_frame = Frame(master)
        self.main_frame.pack()

        #scrollbar
        self.scroll = Scrollbar(self.main_frame,orient='horizontal')
        self.scroll.pack(side= BOTTOM,fill=X)


        style = ttk.Style(master)
        style.configure('Treeview', rowheight=40, rowwidth=10)  
        style.configure('Treeview.Heading', rowheight=50)


        self.tree = ttk.Treeview(self.main_frame, show=["headings"] , height = 5, yscrollcommand=self.scroll.set, xscrollcommand = self.scroll.set)

        self.tree.pack(pady = (10,0))

        self.scroll.config(command=self.tree.yview)

 
        self.tree['columns']= ('Name', 'Type','Expense','Credits', 'GasreductionRate', 'DeductionRate', 'PayPerCredit', 'DollarsAvailable')
        self.tree.column("Name",anchor=CENTER)
        self.tree.column("Type",anchor=CENTER)
        self.tree.column("Expense",anchor=CENTER)
        self.tree.column("Credits",anchor=CENTER)
        self.tree.column("GasreductionRate",anchor=CENTER)
        self.tree.column("DeductionRate",anchor=CENTER)
        self.tree.column("PayPerCredit",anchor=CENTER)
        self.tree.column("DollarsAvailable",anchor=CENTER)



        self.tree.heading("Name",text="Name")
        self.tree.heading("Type",text="Type")
        self.tree.heading("Expense",text="Expense")
        self.tree.heading("Credits",text="Credits")
        self.tree.heading("GasreductionRate",text="GasreductionRate")
        self.tree.heading("DeductionRate",text="DeductionRate")
        self.tree.heading("PayPerCredit",text="PayPerCredit")
        self.tree.heading("DollarsAvailable",text="DollarsAvailable")



        final = []
        for i, (k, v) in enumerate(info.items()):

            name = v[0]
            PpC = round(v[6][1], 2)
            total_credit = round(float(PpC) * float(v[5]),2)
            total_expense = "$" + str(v[5]) 
            Gasdeductionrate = v[6][2]
            dollar_available = "$" + str(v[5])
            D_rate = v[6][2]
            Type = v[6][0]
            final.append([name, Type, total_expense, total_credit, Gasdeductionrate, D_rate,PpC, dollar_available])



        for i, j in enumerate(final):
            if (i % 2) == 0:
                self.tree.insert(parent='',index='end',iid=i+1,text='', tags = ('even',), values=(j))
                self.tree.tag_configure('oddrow', background='white')
                self.tree.tag_configure('evenrow', background='gray97')
  
            else:
                self.tree.insert(parent='',index='end',iid=i+1,text='', tags = ('odd',), values=(j))
                self.tree.tag_configure('oddrow', background='white')
                self.tree.tag_configure('evenrow', background='gray97')
  
      
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()




        t_expense = 0
        total_credit = 0
        TotalDollarAvailable = 0
        total_drate = 0
        total_Gdrate = 0
        total_ppc = 0

        for v in info.values():
            t_expense += float(v[5])
            TotalDollarAvailable += float(v[5])
            PpC = round(float(v[6][1]), 2)
            total_ppc += PpC
            total_credit = round(float(PpC) * float(v[5]), 2)
            total_Gdrate += float(v[6][3])
            total_drate += float(v[6][2])

        
        AvgPayPerCredit = round(total_ppc/len(info.values()),2)
        AvgDeductionRate = round(total_drate/len(info.values()),2)
        AvgGasdeductionRate = round(total_Gdrate/len(info.values()),2)

        ttk.Label(self.frame_content, text="Total Expense:").grid(row=1, column=0, sticky = 'w', padx = 5)
        ttk.Label(self.frame_content, text="AvgGasdeductionRate:").grid(row=2, column=0, sticky = 'w',  padx = 5)
        ttk.Label(self.frame_content, text="AvgPayPerCredit:").grid(row=3, column=0, sticky = 'w', padx = 5)


        ttk.Label(self.frame_content, text="Total Credits:").grid(row=1, column=2, sticky = 'w',  padx = 5)
        ttk.Label(self.frame_content, text="AvgDeductionRate:").grid(row=2, column=2, sticky = 'w',  padx = 5)
        ttk.Label(self.frame_content, text="TotalDollarAvailable:").grid(row=3, column=2, sticky = 'w',  padx = 5)




        ttk.Label(self.frame_content, text=t_expense, font = ("bold",15)).grid(row=1, column=1, sticky='w',padx = 5,pady=5)
        ttk.Label(self.frame_content, text=AvgGasdeductionRate, font = ("bold",15)).grid(row=2, column=1, sticky='w',padx = 5,pady=5)
        ttk.Label(self.frame_content, text=AvgPayPerCredit, font = ("bold",15)).grid(row=3, column=1, sticky='w',padx = 5,pady=5)
        
        ttk.Label(self.frame_content, text=total_credit, font = ("bold",15)).grid(row=1, column=3, sticky='w',padx = 5,pady=5)
        ttk.Label(self.frame_content, text=AvgDeductionRate, font = ("bold",15)).grid(row=2, column=3, sticky='w',padx = 5, pady=5)
        ttk.Label(self.frame_content, text=TotalDollarAvailable, font = ("bold",15)).grid(row=3, column=3, sticky='w',padx = 5, pady=5)



        self.close = ttk.Button(self.frame_content, text = "Close", command = self.close_window).grid(row=4, column=1, sticky = 'w', padx = (0,10), pady = 10)



    








    def close_window(self):
        self.master.destroy()




