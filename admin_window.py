
import tkinter as tk
from tkinter import ttk
from tkinter import *
from select import Select
from add import Add
from slip import Slip
from report import Report


class Admin:
    def __init__(self, master, name):
        global INPUT
        self.master = master
        self.master.title("Session admin - "+ name)

        self.member_dict = self.return_dict()

        self.header_frame = Frame(self.master)
        self.header_frame.pack()

        ttk.Label(self.header_frame, text="Filters", font = ("bold", 30)).grid(row=0, column=0, columnspan = 2, sticky='w', pady=(0,20))

        ttk.Label(self.header_frame, text="Name:", font = "bold").grid(row=1, column=1, sticky='w')
        ttk.Label(self.header_frame, text="Email:", font = "bold").grid(row=1, column=3, sticky = 'w')

        self.entry_name = ttk.Entry(self.header_frame)
        self.entry_name.insert(0, "Filter by name")
     
        self.entry_email = ttk.Entry(self.header_frame)
        self.entry_email.insert(0, "Filter by email")


        self.entry_name.grid(row=1, column=2, sticky = 'w')
        self.entry_email.grid(row=1, column=4, sticky = 'w')


        self.main_frame = Frame(master)
        self.main_frame.pack()

        #scrollbar
        self.scroll = Scrollbar(self.main_frame,orient='vertical')
        self.scroll.pack(side= RIGHT,fill=Y)


        style = ttk.Style(master)
        style.configure('Treeview', rowheight=50)  
        style.configure('Treeview.Heading', rowheight=50)

        self.table = ttk.Treeview(self.main_frame, style="Treeview",show=["headings"] , height = 5, yscrollcommand=self.scroll.set, xscrollcommand = self.scroll.set)

        self.table.pack(pady = (10,0))

        self.scroll.config(command=self.table.yview)


        self.table['columns']= ('Name', 'Email','Phone')
        self.table.column("Name",anchor=CENTER)
        self.table.column("Email",anchor=CENTER)
        self.table.column("Phone",anchor=CENTER)

        self.table.heading("Name",text="Name")
        self.table.heading("Email",text="Email")
        self.table.heading("Phone",text="Phone")

        self.table.insert(parent='',index='end',iid=0,text='', tags = ('oddrow',), values=('Thomas Muller','thomas.muller@uts.com','99991111'))
        self.table.insert(parent='',index='end',iid=1,text='', tags = ('evenrow',), values=('Alice Stefan','alice.stefan@uts.com',"88881111"))
        self.table.insert(parent='',index='end',iid=2,text='', tags = ('oddrow',), values=('Lucy Lu','lucy.lu@uts.com','98981100'))
        self.table.insert(parent='',index='end',iid=3,text='', tags = ('evenrow',), values=('Andreas Brehme','andreas.b@uts.com','90001222'))
        self.table.insert(parent='',index='end',iid=4,text='', tags = ('oddrow',), values=('Ruddy Voller','ruddy.v@uts.com',"98980000"))
        self.table.insert(parent='',index='end',iid=5,text='', tags = ('evenrow',), values=('Monica Shwarz','monica.s@uts.com','92241188'))
            

        self.table.tag_configure('oddrow', background='white')
        self.table.tag_configure('evenrow', background='gray97')
                
    
        self.bottom_frame = Frame(self.master)
        self.bottom_frame.pack()


        self.add = ttk.Button(self.bottom_frame, text = "Add", command = self.add_user).grid(row=0, column=2, sticky = 'e', padx = (10,0))
        self.report = ttk.Button(self.bottom_frame, text = "Report", command = self.open_report).grid(row=0, column=6, sticky = 'w')
        self.close = ttk.Button(self.bottom_frame, text = "Close", command = self.close_window).grid(row=0, column=7, sticky = 'w', padx = (0,10))
        self.select = ttk.Button(self.bottom_frame, text = "Select", state = DISABLED, command = self.select_user).grid(row=0, column=4, sticky = 'w')
        self.slip = ttk.Button(self.bottom_frame, text = "Slip", state = DISABLED, command = self.open_slip).grid(row=0, column=5, sticky = 'w')
       

        self.detached_items = []
        self.selections = []

        self.table.bind("<ButtonRelease-1>", self.OnDoubleClick)
        
        self.entry_name.bind("<Button-1>", lambda event: self.name_clear())
        self.entry_name.bind('<Key>', lambda event: self.filter_name())
        self.entry_name.bind('<BackSpace>', lambda event: self.repopulate())
        self.entry_email.bind("<Button-1>", lambda event: self.email_clear())
        self.entry_email.bind('<Key>', lambda event: self.filter_email())
        self.entry_email.bind('<BackSpace>', lambda event: self.repopulate())
        self.entry_name.bind('<FocusOut>', lambda event: self.name_reinsert())
        self.entry_email.bind('<FocusOut>', lambda event: self.email_reinsert())


    def name_clear(self, event = None):
        self.entry_name.delete(0, tk.END)

    def email_clear(self, event = None):
        self.entry_email.delete(0, tk.END)

    def name_reinsert(self):
        self.entry_name.delete(0, tk.END)
        self.entry_name.insert(0, "Filter by name")
    
    def email_reinsert(self):
        self.entry_email.insert(0, "Filter by email")


    def filter_name(self, event = None):
        username = self.entry_name.get()
        # Only show filtered name
        for child in self.table.get_children():
            if (username.title() in (self.table.item(child)['values'][0].title())):
                self.selections.append(child)
            else:
                self.table.detach(child)
                self.detached_items.append(child)
                
        if len(self.detached_items) == 6:
            ttk.Label(self.main_frame, text="Memberships list not loaded").pack(side = TOP)




    def filter_email(self, event = None):
        email = self.entry_email.get()

        for child in self.table.get_children():
            if (email in (self.table.item(child)['values'][1])):
                self.selections.append(child)
            else:
                self.table.detach(child)
                self.detached_items.append(child)
        
        if len(self.detached_items) == 6:
            ttk.Label(self.main_frame, text="Memberships list not loaded").pack(side = TOP)

 







    def repopulate(self):
        for i in self.detached_items:
            self.table.reattach(i,'',0)
        self.detached_items.clear()
 

    def OnDoubleClick(self, event):
        self.delete = ttk.Button(self.bottom_frame, text = "Delete", command = self.delete_user ).grid(row=0, column=3, sticky = 'w')
        self.slip = ttk.Button(self.bottom_frame, text = "Slip", command = self.selectItem).grid(row=0, column=5, sticky = 'w')

        self.select = ttk.Button(self.bottom_frame, text = "Select", command = self.selectItem).grid(row=0, column=4, sticky = 'w')
      
        self.slip.bind('<ButtonRelease-1>', self.selectItem)
        self.select.bind('<ButtonRelease-1>', self.selectItem)


    def selectItem(self):
        curItem = self.table.focus()
        d = self.table.item(curItem)
        return d['values'][0]
   

    def OnDoubleClick(self, a):
        self.delete = ttk.Button(self.bottom_frame, text = "Delete", command = self.delete_user).grid(row=0, column=3, sticky = 'w')
        self.slip = ttk.Button(self.bottom_frame, text = "Slip", command = self.open_slip).grid(row=0, column=5, sticky = 'w')
        self.select = ttk.Button(self.bottom_frame, text = "Select", command = self.select_user).grid(row=0, column=4, sticky = 'w')



    def calc_type(self, expense):
        """Calculates and returns information based on the expense of the member"""

        if 0 <= float(expense) < 500:
            return "Bronze", 20, 0.05, 0.1 
        elif 500 <= float(expense) < 1500 :
            return "Silver", 10, 0.1, 0.15 
        elif 1500 <= float(expense) < 3000 :
            return "Gold", 8, 0.15, 0.2 
        elif 3000 <= float(expense) < 5000 :
            return "Diamond", 6, 0.2, 0.25 
        elif float(expense) >= 5000 :
            return "Platinum", 4, 0.25, 0.3 
        

    def return_dict(self):
        """Adding members already in the system and returning them"""
        member_dict = dict()

        name = ["Thomas Muller", "Alice Stefan", "Lucy Lu", "Andreas Brehme", "Ruddy Voller", "Monica Shwarz"]
        email = ["thomas.muller@uts.com", "alice.stefan@uts.com ", "lucy.lu@uts.com ", "andreas.b@uts.com", "ruddy.v@uts.com","monica.s@uts.com"]
        phone = ["99991111", "88881111","98981100","90001222","98980000","92241188"]
        address = ["3 Byern St. Sydney 2001 ", "24 Pitt St. Sydney 2001", "11 Hunter St. Sydney 2100", "91 Sussex St. Sydney 2100", "15 Stan St. Sydney 2100", "155 Jones St. Sydney 2001"]
        id = [13697480, 14517880, 13267102, 13678020, 13972870, 13859610]
        expense = [2134.5, 4512.2 , 158.4 ,7596.3, 1100.0 , 6741.2 ]

        for item in range(len(name)):
            Type = self.calc_type(expense[item])
            key = name[item]
            value = [name[item], email[item], phone[item], address[item], id[item], expense[item], Type]
            member_dict[key] = value
        
        return member_dict


    def delete_user(self):
        name = self.selectItem()
        for child in self.table.get_children():
            if (name in (self.table.item(child)['values'][0].title())):
                self.table.detach(child)

        self.member_dict.pop(name)


   
    def edit(self, new_info):

        name = self.selectItem()
        info = self.return_dict(name)
        select = Select(self.master, info)
        self.new_info = self.select.return_info()


       

    def select_user(self):
        name = self.selectItem()
        info = self.member_dict
           
        for child in self.table.get_children():
            if (name in (self.table.item(child)['values'][0].title())):
                self.table.delete(child)

        top1 = Toplevel()
        Select(top1, name, self.member_dict, self.table)
 



    def add_user(self):
        top1 = Toplevel()
        Add(top1, self.table, self.member_dict)
 

    def open_slip(self):
        name = self.selectItem()
        info = self.member_dict
        top1 = Toplevel()
        Slip(top1, name, info)



    def open_report(self):
        info = self.member_dict
        top1 = Toplevel()
        Report(top1, info)



 
    def close_window(self):
        self.master.destroy()