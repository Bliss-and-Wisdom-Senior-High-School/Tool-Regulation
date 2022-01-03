from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import function as f
from functools import partial
import time


class GUI:
    def __init__(self, window=None):
        #定義變數
        self.name = IntVar(window)
        self.lendData = {
            'name': '',
            'date': '',
            'time': '',
            'tools': []
        }
        self.notebook = ttk.Notebook(window)
        self.treeLendCount = -1
        # self.font = ttk.font('Arial', 16)
        
        #Treeview font size
        style = ttk.Style()
        style.configure('Treeview', font=(None, 16))
        style.configure('Treeview.Heading', font=('Arial', 16))

        style.configure('.', font=('Arial', 16))
        # style.configure('Notebook', font=(None, 16))
        # style.configure('Notebook.Heading', font=(None, 16))
        
        #視窗設定
        window.title('資材管理系統')
        window.resizable(1, 1)
        # window.config(bg="")-----------------------------------------------------------------------------------------------------------
        # window.iconbitmap()
        
        #標題
        self.titleLabel = Label(window, text = '資材管理系統', font=('Arial', 40))
        self.t = time.localtime()
        self.txtdate = str(self.t[0])+"年 "+str(self.t[1])+"月 "+str(self.t[2])+"日"
        self.dateLabel = Label(window, text=self.txtdate, font=("Helvetica", 15))
        
        
        #借資材 
        self.lendFrm = Frame(self.notebook)
        self.lendFrm.pack(padx=50, pady=20)
        
        lendTopFrm = Frame(self.lendFrm)
        nameLabel = Label(lendTopFrm, text="借用人", font=("Helvetica", 16, "bold"))
        self.inputName = Entry(lendTopFrm, width=20)
        
        toolLabel = Label(lendTopFrm, text="工具", font=("Helvetica", 16, "bold"))
        self.inputTool = ttk.Combobox(lendTopFrm, height = 8, value=[i for i in f.getAll()])

        fun = partial(self.lendRemain)
        self.inputTool.bind("<<ComboboxSelected>>", fun)
        
        amountLabel = Label(lendTopFrm, text="數量", font=("Helvetica", 16, "bold"))
        self.inputAmount = Entry(lendTopFrm, width=20)
        
        self.remainNum = StringVar()
        self.remainNum.set('')
        remainLabel = Label(lendTopFrm, text="剩餘", font=('Helvetica', 16, 'bold'))
        self.remainAmount = Label(lendTopFrm, textvariable=self.remainNum, font=('Helvetica', 16, 'bold'), width=5)

        self.showListbox = Listbox(self.lendFrm, selectmode=EXTENDED, height=10, width=50, font=("Helvetica", 15, "bold"))
        
        accurateButton = Button(lendTopFrm, text="確認", font=("Helvetica", 14),
                                command=lambda: self.addToListbox(self.inputName.get(),
                                                                  self.inputTool.get(),
                                                                  self.inputAmount.get()))
        
        lendSouthFrm = Frame(self.lendFrm)
        
        deleteButton = Button(lendSouthFrm, text="刪除", font=("Helvetica", 15, "bold"),
                              command=lambda: self.deleteListbox())
        deleteButton.grid(row=1, column=1, pady=10, padx=50)
        
        finalButton = Button(lendSouthFrm, text="借出", font=("Helvetica", 16, "bold"),
                             command=lambda: self.lend())
        finalButton.grid(row=1, column=2, pady=10, padx=50)
        
        ##Pack
        lendTopFrm.pack(padx=20, pady=20)
        nameLabel.pack(side=LEFT, pady=5)
        self.inputName.pack(side=LEFT, pady=5, padx=10)
        toolLabel.pack(side=LEFT, pady=5)
        self.inputTool.pack(side=LEFT, pady=5, padx=10)
        amountLabel.pack(side=LEFT, pady=5)
        self.inputAmount.pack(side=LEFT, pady=5, padx=10)
        remainLabel.pack(side=LEFT, pady=5, padx=10)
        self.remainAmount.pack(side=LEFT, pady=5, padx=10)
        accurateButton.pack(side=LEFT, pady=5, ipadx=2, ipady=2)
        self.showListbox.pack( expand=YES, pady=10, padx=60)
        lendSouthFrm.pack(pady=20, padx=15)
        
        
        #還資材 
        self.backFrm = Frame(self.notebook)
        self.backFrm.pack(padx=50, pady=20)
        
        ##列表
        area1 = ('日期', '時間', '借用人', '資材', '數量')
        ac1 = ("date", "time", "name", "tool", "amount")
        data1 = f.getLend()
        
        self.treeLend = ttk.Treeview(self.backFrm, columns=ac1, show='headings', height=20)
        vsb1 = ttk.Scrollbar(orient='vertical', command=self.treeLend.yview)
        self.treeLend.configure( yscrollcommand = vsb1.set)
        
        for i in range(len(ac1)):
            self.treeLend.column(ac1[i], width=200, anchor='center')
            self.treeLend.heading(ac1[i], text=area1[i]) 
        self.treeLendCount = -1
        for i in data1:
            self.treeLend.insert('', 'end',
                    values=[i['date'], i['time'], i['name'],
                            i['tools'][0]['tool'], i['tools'][0]['amount']])
            self.treeLendCount += 1
            for j in i['tools'][1:]:
                self.treeLend.insert('', 'end', values=['', '', '', j['tool'], j['amount']])
                self.treeLendCount += 1
        self.treeLend.pack( side=TOP, padx=50, pady=30) 

        ##工具列
        backToolFrm = Frame(self.backFrm)
        
        backBtn = Button(backToolFrm, text='歸還', font=('Arial', 16), width=10,
                         command= lambda: self.back())
        backBtn.grid(row=1, column=1, padx=20, pady=15)
        
        backToolFrm.pack( pady=10)
                
        #總資材 
        self.allFrm = Frame(self.notebook)
        tf1 = Frame(self.allFrm)

        ##查尋欄
        self.searchFrm = Frame(tf1)
        self.inputNameLabel = Label(self.searchFrm, text='查尋資材', font = ('Arial', 16), width=10)
        self.inputNameLabel.grid(row=1, column=1, pady=5, padx=10)
        defaultName = StringVar()
        defaultName.set('')
        self.inputNameAll = ttk.Combobox(self.searchFrm, font=('Arial', 16), width=15,
                                  height=8, values=[i for i in f.getAll()])
        self.inputNameAll.grid(row=1, column=2, padx=10, pady=10)
        self.searchBtn = Button(self.searchFrm, font=('Arial', 16), text='搜尋', width=6,
                                command=lambda: f.searchAll(self.inputNameAll.get()))
        self.searchBtn.grid(row=1, column=3, pady=5, padx=10)
        self.searchFrm.grid(row=1, column=1, padx=10, pady=10)
        
        ##列表
        area = ('器材名稱', '器材數量', '損壞數量', '外借中', '剩餘數量')
        ac = ('name', 'amount', 'damaged', 'lending', 'remain')
        data = f.getAll()
        
        self.treeAll = ttk.Treeview(tf1, columns=ac, show='headings', height=18)
        vsb = ttk.Scrollbar(orient='vertical', command=self.treeAll.yview)
        self.treeAll.configure( yscrollcommand = vsb.set)
        
        for i in range(len(ac)):
            self.treeAll.column(ac[i], width=250, anchor='center')
            self.treeAll.heading(ac[i], text=area[i])
        for i in data:
            li = [i]
            for j in data[i].values():
                li.append(j)
            li.append(str(int(li[1]) - int(li[2]) - int(li[3])) )
            # if len(li)<len(ac):
            #     li.append('0')
            self.treeAll.insert('', 'end', values=li)
        self.treeAll.grid(row=2, column=1, padx=50, pady=10)
        
        
        ##工具列
        self.toolBarFrm = Frame(tf1)
        self.addBtn = Button(self.toolBarFrm, font=('Arial', 16), text='新增資材', width=8,
                             command= lambda: self.addItem())
        self.addBtn.grid(row=1, column=1, pady=5, padx=10)
        self.removeBtn = Button(self.toolBarFrm, font=('Arial', 16), text='移除資材', width=8,
                                command=lambda: self.removeItem())
        self.removeBtn.grid(row=1, column=2, pady=5, padx=10)
        self.editBtn = Button(self.toolBarFrm, font=('Arial', 16), text='修改資材', width=8,
                              command=lambda: self.editItem())
        self.editBtn.grid(row=1, column=3, padx=10, pady=5)
        
        
        #Pack and Grid
        self.titleLabel.pack( expand=YES, padx=10, pady=10)
        self.dateLabel.pack()
        tf1.pack(expand=YES, padx=10, pady=10)
        self.allFrm.pack( expand=YES, padx=10, pady=10)
        self.toolBarFrm.grid(row=3, column=1, padx=10, pady=10)

        #notebook
        self.notebook.add(self.lendFrm, text='借資材')
        self.notebook.add(self.backFrm, text='還資材')
        self.notebook.add(self.allFrm, text='總資材')
        self.notebook.pack(padx=10, pady=10, fill=BOTH, expand=TRUE)
        
        
    def addItem(self):
        w = Toplevel()
        w.title('新增器材')
        
        lbl = Label(w, text='新增器材', font=('Arial', 20))
        frm = Frame(w)
        
        nameLb = Label(frm, text='器材名稱', font=('Arial', 16))
        nameLb.grid(row=1, column=1, padx=20, pady=15)
        self.nameIn = Entry(frm, font=('Arial', 16), width=10)
        self.nameIn.grid(row=1, column=2, padx=20, pady=15)
        
        numLb = Label(frm, text='器材數量', font=('Arial', 16))
        numLb.grid(row=2, column=1, padx=20, pady=15)
        self.numIn = Entry(frm, font=('Arial', 16), width=10)
        self.numIn.grid(row=2, column=2, padx=20, pady=15)
        
        # tree = self.treeAll
        confirmBtn = Button(frm, text='確定', font=('Arial', 14),
                            command= lambda: self.addConfirm(w))
        confirmBtn.grid(row=3, column=1, padx=20, pady=15)
        cancelBtn = Button(frm, text='取消', font=('Arial', 14), command= w.destroy)
        cancelBtn.grid(row=3, column=2, padx=20, pady=15)
        
        lbl.pack(pady=10)
        frm.pack(padx=20, pady=15)
    
    def addConfirm(self, w):

        if self.nameIn.get() == "" or self.numIn.get() == "":
            messagebox.showinfo("提醒", "請填寫完整的資料")
        else:
            try:
                if int(self.numIn.get())<=0:
                    messagebox.showinfo("提醒", "請填寫完整的資料")
                else:
                    self.inputTool.delete('0', 'end')
                    self.inputTool.insert('end', self.nameIn.get())
                    f.addItem(w, self.treeAll, self.nameIn.get(), self.numIn.get()) 
            except ValueError as e:
                messagebox.showinfo("提醒", "請輸入正確、完整的借用資料")
                self.inputAmount.delete(0, END)

    
    def removeItem(self):

        ans = messagebox.askyesno("移除資材", "您確定要移除這項資材嗎？")
        if ans == 1:
            if not self.treeAll.selection():
                messagebox.showinfo('提醒', '請先選取項目')
            else:
                for i in self.treeAll.selection():
                    # print(self.treeAll.item(i, 'value')[0])
                    f.removeItem(self.treeAll.item(i, 'value')[0])
                    self.treeAll.delete(i)
        return
    
    def editItem(self):
        w = Toplevel()
        w.title('修改資材')
        
        lbl = Label(w, text='移除資材', font=('Arial', 20))
        frm = Frame(w)
        
        nameLbl = Label(frm, text='選擇欲修改資材', font=('Arial', 16))
        nameLbl.grid(row=1, column=1, padx=10, pady=10)
        
        self.liCom = ttk.Combobox(frm, font=('Arial', 16), width=15,
                                  height=8, values=[i for i in f.getAll()])
        self.liCom.grid(row=1, column=2, padx=10, pady=10)
        
        amountLbl = Label(frm, text='資材數量', font=('Arial', 16))
        amountLbl.grid(row=2, column=1, padx=10, pady=10)
        
        self.amount = StringVar()
        self.amount.set('0')
        amountIn = Entry(frm, textvariable=self.amount, font=('Arial', 16), width=16)
        amountIn.grid(row=2, column=2, padx=10, pady=10)
        
        damLbl = Label(frm, text='損壞數量', font=('Arial', 16))
        damLbl.grid(row=3, column=1, padx=10, pady=10)
        
        self.dam = StringVar()
        self.dam.set('0')
        damIn = Entry(frm, textvariable=self.dam, font=('Arial', 16), width=16)
        damIn.grid(row=3, column=2, padx=10, pady=10)
        
        lendLbl = Label(frm, text='外借數量', font=('Arial', 16))
        lendLbl.grid(row=4, column=1, padx=10, pady=10)
        
        self.lendTxt = StringVar()
        self.lendTxt.set('0')
        self.lendNum = Label(frm, textvariable=self.lendTxt, font=('Arial', 16), width=16)
        self.lendNum.grid(row=4, column=2, padx=10, pady=10)
        
        func = partial(self.callbackFunc)
        self.liCom.bind("<<ComboboxSelected>>", func)
        
        fr = Frame(w)
        okBtn = Button(fr, text='確認', font=('Arial', 16),
                       command=lambda: f.editItem(w, self.treeAll, self.liCom.get(),
                                                  self.amount.get(), damIn.get(), self.lendTxt.get()))
        okBtn.grid(row=1, column=1, padx=20, pady=15)
        
        cancelBtn = Button(fr, text='取消', font=('Arial', 14), command= w.destroy)
        cancelBtn.grid(row=1, column=2, padx=20, pady=15)

        lbl.pack(padx=20, pady=10)
        frm.pack(padx=20, pady=10)
        fr.pack(padx=20, pady=10)
        
    def callbackFunc(self, event):
        name = self.liCom.get()
        data = f.getAll()
        self.amount.set(data[name]['amount'])
        self.dam.set(data[name]['dam'])
        if 'lending' not in data[name]:
            data['name'] = '0'
        self.lendTxt.set(data[name]['lending'])
    
    def lendRemain(self, event):
        item = f.getItem(self.inputTool.get())
        remain = str(int(item['amount']) - int(item['dam']) - int(item['lending']))
        self.remainNum.set(remain)
    
    def addToListbox(self, name, tool, amount):
        print(name, tool, amount, 'add to list box')
        if name == "" or tool == "" or amount == "":
            messagebox.showinfo("提醒", "請輸入正確、完整的借用資料")
        elif tool not in f.getAll():
            messagebox.showinfo('提醒', '請輸入正確、完整的借用資料')
        else:
            try:
                if int(amount) + int(f.getItem(tool)['lending']) > int(f.getItem(tool)['amount']):
                    messagebox.showinfo("提醒", "數量超過現有數量")
                else:
                    f.editAmount(self.treeAll, tool, int(amount))
                    tools = {"tool": tool, "amount": amount}
                    self.lendData['tools'].append(tools)
                    
                    self.showListbox.insert("end",  f' {tool} x {amount}')
            except ValueError as e:
                messagebox.showinfo("提醒", "請輸入正確、完整的借用資料")
                self.inputAmount.delete(0, END)
                
    def deleteListbox(self):
        ans=0
        if self.showListbox.curselection() != ():
            ans = messagebox.askyesno("刪除", "確定要刪除嗎？")
        if ans == 1:
            index = self.showListbox.curselection()
            for i in reversed(index):
                self.showListbox.delete(i)
                f.editAmount(self.treeAll, self.lendData['tools'][i]['tool'], -int(self.lendData['tools'][i]['amount']))
                self.lendData['tools'].pop(i)

    def lend(self):
        if self.showListbox.size() == 0:
            messagebox.askyesno("提醒", "您沒有借用任何資材，是嗎？")
        elif not self.inputName.get():
            messagebox.showinfo('提醒', '請先輸入借用人性名!')
        else:
            ans = messagebox.askyesno("借用", "您確定要借出嗎？")
            if ans == 1:
                f.lendout(self.lendData)
                
                self.lendData['name'] = self.inputName.get()
                now = time.localtime()
                self.lendData['date'] = f'{now[0]:2d}/{now[1]:2d}/{now[2]:2d}'
                self.lendData['time'] = f'{now[3]:2d}/{now[4]:2d}/{now[5]:2d}'
                self.treeLend.insert('', 'end',
                                     value=(self.lendData['date'], self.lendData['time'], self.lendData['name'],
                                            self.lendData['tools'][0]['tool'], self.lendData['tools'][0]['amount']))
                # self.treeAll
                self.treeLendCount += 1
                for i in self.lendData['tools'][1:]:
                    self.treeLend.insert('', 'end', value=('', '', '', i['tool'], i['amount']))
                    self.treeLendCount += 1
                
                self.lendData['tools'] = []
                self.inputName.delete(0, END)
                self.inputTool.delete(0, END)
                self.inputAmount.delete(0, END)
                self.showListbox.delete('0','end')
                self.remainNum.set('')
    
    def back(self):
        ans = messagebox.askyesno("歸還", "您要歸還資材嗎？")
        if ans == 1:
            for i in self.treeLend.selection():
                temp = i
                print(self.treeLend.index(temp), self.treeLendCount)
                while self.treeLend.index(temp) != self.treeLendCount and not self.treeLend.item(self.treeLend.next(temp), 'value')[0]:
                    self.delete(self.treeLend.next(temp))
                while not self.treeLend.item(temp, 'value')[0]:
                    t = self.treeLend.prev(temp)
                    self.delete(temp)
                    temp = t
                li = self.treeLend.item(temp, 'value')
                f.giveBack(li[0], li[1]) #回傳時間
                self.delete(temp)
    
    def delete(self, item):
        li = self.treeLend.item(item, 'value')
        print('li', li)
        self.treeLend.delete(item)
        self.treeLendCount -= 1
        f.editAmount(self.treeAll, li[3], -int(li[4]))

window = Tk()
GUI(window)
window.mainloop()