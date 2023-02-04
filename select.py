import tkinter as tk
from tkinter import ttk
from tkinter import *
from error import Error

class Select:

    def __init__(self, master, name, info, table):
        #super().__init__()

        global INPUT
        self.master = master
        self.member_dict = info
        self.table = table

        info = info[name]
        name = info[0]
        email = info[1]
        phone = info[2]
        address = info[3]
        id = info[4]
        expense = info[5]
        Type = info[6][0]

        self.master.title("Accessing file: "+ name)

        self.frame = tk.Frame(self.master)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text="Personal Details", font = ("bold", 30)).grid(row=0, column=0, sticky='w', padx = (50,0), pady=(20,20))

        ttk.Label(self.frame_content, text="Name:").grid(row=1, column=0, sticky='w', padx = (50,15), pady = 5)
        ttk.Label(self.frame_content, text="Email:").grid(row=2, column=0, sticky = 'w',padx = (50,15),pady = 5)
        ttk.Label(self.frame_content, text="Phone:").grid(row=3, column=0, sticky='w', padx = (50,15),pady = 5)
        ttk.Label(self.frame_content, text="Address:").grid(row=4, column=0, sticky='w', padx = (50,15),pady = (5,15))


        self.entry_name = ttk.Entry(self.frame_content)
        self.entry_email = ttk.Entry(self.frame_content)
        self.entry_phone = ttk.Entry(self.frame_content)
        self.entry_address = ttk.Entry(self.frame_content)

        self.entry_name.grid(row=1, column=1, sticky = 'w')
        self.entry_email.grid(row=2, column=1, sticky = 'w')
        self.entry_phone.grid(row=3, column=1, sticky = 'w')
        self.entry_address.grid(row=4, column=1, sticky = 'w', pady = (0,10))



        self.entry_name.insert(0, name)
        self.entry_email.insert(0, email)
        self.entry_phone.insert(0, phone)
        self.entry_address.insert(0, address)



        self.frame1 = Frame(self.master, highlightbackground="white", highlightthickness=0.5,width=600, height=2, bd= 0)
        self.frame1.pack()

        
        self.main_frame = Frame(master)
        self.main_frame.pack()


        ttk.Label(self.main_frame, text="Membership Details", font = ("bold", 25)).grid(row=0, column=0, sticky='w', padx = (50,0), pady=(20,20))

        ttk.Label(self.main_frame, text="ID:").grid(row=1, column=0, sticky='w', padx = (50,15), pady = 5)
        ttk.Label(self.main_frame, text="Expense:").grid(row=2, column=0, sticky = 'w',padx = (50,15),pady = 5)
        ttk.Label(self.main_frame, text="Type:").grid(row=3, column=0, sticky='w', padx = (50,15),pady = 5)



        self.entry_id = ttk.Entry(self.main_frame)
        self.entry_expense = ttk.Entry(self.main_frame)
        
  

        ttk.Label(self.main_frame, text=Type, font = ("bold",15)).grid(row=3, column=1, sticky='w')


        self.entry_id.grid(row=1, column=1, sticky = 'w')
        self.entry_expense.grid(row=2, column=1, sticky = 'w')
 
      
        self.entry_id.insert(0, id)
        self.entry_expense.insert(0, expense)


        self.bottom_frame = Frame(self.master)
        self.bottom_frame.pack()



        self.n = self.entry_name.get()
        self.e = self.entry_email.get()
        self.p = self.entry_phone.get()
        self.a = self.entry_address.get()

        self.i = self.entry_id.get()
        self.e = self.entry_expense.get()



        self.add = ttk.Button(self.bottom_frame, text = "Add", state = DISABLED).grid(row=0, column=2, sticky = 'e', padx = (10,0), pady = 10)
        self.update = ttk.Button(self.bottom_frame, text = "Update", command = self.validation).grid(row=0, column=3, sticky = 'w', pady = 10)
        self.close = ttk.Button(self.bottom_frame, text = "Close", command = self.close_window).grid(row=0, column=4, sticky = 'w', padx = (0,10), pady = 10)


    def get_phone(self):
        new_info = []
        info = [self.n, self.e, self.p, self.a, self.i, self.e]
        entries = [self.entry_name, self.entry_email, self.entry_phone, self.entry_address, self.entry_id, self.entry_expense]
      
        for i, entry in zip(info, entries):
            i = ""
            entry.insert(0, i)
            new_info.append(entry.get())
  
      
        return new_info


    def validation(self):
        new_info = self.get_phone()
        errors = []

        name = new_info[0]
        email = new_info[1]
        phone = new_info[2]
        address = new_info[3]
        id = new_info[4]
        expense = new_info[5]

        # Checking that the name is correct
        if " " not in name:
            errors.append("Incorrect name pattern!")
        elif type(name) != str:
            errors.append("Incorrect name pattern!")

        elif " " in name:
            full_name = name.split(" ")
            if (full_name[0].isupper == False) or (full_name[1] == False):
                errors.append("Incorrect name pattern!")

        #Checking that the email is correct
        if "@" not in email:
            errors.append("Incorrect email pattern!")
        
        # Checking that the phone number is correct
        if len(str(phone)) != 8:
            errors.append("Incorrect phone pattern!")

        #Checking that the address is correct
        address = address.split(" ")
        if (address[0].isdigit() == False) or (address[-1].isdigit() == False):
           
            errors.append("Incorrect address pattern!")

        # Checking that the id is correct
        if len(id) != 8:
            errors.append("Incorrect ID pattern!")   

        if len(errors) == 0:
            # Close window since there are no errors
    
            if name not in self.member_dict.keys():   
                self.member_dict.update({name: [name, email, phone, address, id, expense, self.calc_type(expense)]})

                num = len(self.member_dict)
                self.table.insert(parent='',index='end',iid=num,text='', tags = (num,), values=(name, email, phone))
                self.master.destroy()
            else:
                self.master.destroy()

        else:
            # Open error window
            top1 = Toplevel()
            Error(top1, errors)

        return errors




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







    def close_window(self):
        self.master.destroy()

