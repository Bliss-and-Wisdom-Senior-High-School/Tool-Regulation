from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
import func1 as f

window = Tk()

name = StringVar()
tool = StringVar()
amount = IntVar()

window.title("資材管理系統")

fm = Frame(window)
fm.pack(padx=50, pady=20)

welcomeLabel = Label(fm, text="資材管理系統", font=("Arial", 30, "bold"))

t = time.localtime()
txtdate = str(t[0])+"/"+str(t[1])+"/"+str(t[2])
dateLabel = Label(fm, text=txtdate, font=("Helvetica", 15))

nameLabel = Label(fm, text="借用人", font=("Helvetica", 15, "bold"))
inputName = Entry(fm, textvariable=name, width=20)

toolLabel = Label(fm, text="工具", font=("Helvetica", 15, "bold"))
inputTool = ttk.Combobox(fm, value=("a", "b", "c"))

amountLabel = Label(fm, text="數量", font=("Helvetica", 15, "bold"))
inputAmount = Entry(fm, width=20)

showListbox = Listbox(window, selectmode=EXTENDED)
showListbox.bind("<Button-3>", f.deleteListbox)

accurateButton = Button(fm, text="確認", font=("Helvetica", 10),
                        command=lambda:f.addToListbox(showListbox, inputName.get(), inputTool.get(), inputAmount.get()))

finalButton = Button(window, text="借出", font=("Helvetica", 15, "bold"),
                     command=lambda: f.Borrow(showListbox))

welcomeLabel.pack(side=TOP, fill=X, expand=YES)
dateLabel.pack()
nameLabel.pack(side=LEFT, pady=5)
inputName.pack(side=LEFT, pady=5, padx=10)
toolLabel.pack(side=LEFT, pady=5)
inputTool.pack(side=LEFT, pady=5, padx=10)
amountLabel.pack(side=LEFT, pady=5)
inputAmount.pack(side=LEFT, pady=5, padx=10)
accurateButton.pack(side=LEFT, pady=5, ipadx=2, ipady=2)
showListbox.pack(fill=X, expand=YES, pady=10, padx=60)
finalButton.pack(fill=X, expand=YES, pady=10, padx=370)

window.mainloop()
