from tkinter import *
import tkinter as tk
from intro import Intro


def main():
    root = tk.Tk()

    intro = Intro(root)
    root.title("MMS - SuperMarket Mode")
   # root.iconbitmap('book.ico')
    photo = PhotoImage(file = "book.png")
    root.iconphoto(False, tk.PhotoImage(file="book.png"))
    root.mainloop()
    



if __name__ == '__main__':
    main()

