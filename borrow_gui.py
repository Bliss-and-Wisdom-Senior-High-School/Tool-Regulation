from tkinter import *
from tkinter import ttk
import time
import func1 as f


class BorrowGUI:
    def __init__(self, window=None):
        
        window.title("資材管理系統")
        
        self.fm = Frame(window)
        self.fm.pack(padx=50, pady=20)
        
        welcomeLabel = Label(self.fm, text="資材管理系統", font=("Arial", 30, "bold"))
        
        t = time.localtime()
        txtdate = str(t[0])+"/"+str(t[1])+"/"+str(t[2])
        dateLabel = Label(self.fm, text=txtdate, font=("Helvetica", 15))
        
        nameLabel = Label(self.fm, text="借用人", font=("Helvetica", 15, "bold"))
        self.inputName = Entry(self.fm, width=20)
        
        toolLabel = Label(self.fm, text="工具", font=("Helvetica", 15, "bold"))
        self.inputTool = ttk.Combobox(self.fm, value=("a", "b", "c"))
        
        amountLabel = Label(self.fm, text="數量", font=("Helvetica", 15, "bold"))
        self.inputAmount = Entry(self.fm, width=20)
        
        self.showListbox = Listbox(window, selectmode=EXTENDED)
        
        accurateButton = Button(self.fm, text="確認", font=("Helvetica", 10),
                                command=lambda:f.addToListbox(self.showListbox, self.inputName.get(), self.inputTool.get(), self.inputAmount.get()))
        
        deleteButton = Button(window, text="刪除", font=("Helvetica", 15, "bold"),
                              command=lambda: f.deleteListbox(self))
        
        finalButton = Button(window, text="借出", font=("Helvetica", 15, "bold"),
                             command=lambda: f.Borrow(self))
        
        welcomeLabel.pack(side=TOP, fill=X, expand=YES)
        dateLabel.pack()
        nameLabel.pack(side=LEFT, pady=5)
        self.inputName.pack(side=LEFT, pady=5, padx=10)
        toolLabel.pack(side=LEFT, pady=5)
        self.inputTool.pack(side=LEFT, pady=5, padx=10)
        amountLabel.pack(side=LEFT, pady=5)
        self.inputAmount.pack(side=LEFT, pady=5, padx=10)
        accurateButton.pack(side=LEFT, pady=5, ipadx=2, ipady=2)
        self.showListbox.pack(fill=X, expand=YES, pady=10, padx=60)
        deleteButton.pack(side=LEFT, expand=YES, pady=10, padx=30)
        finalButton.pack(side=LEFT, expand=YES, pady=10, padx=30)
        
window = Tk()
BorrowGUI(window)
window.mainloop()
