import FILEIO as f


#在總資材中搜尋找
def searchAll(name):
    print('搜尋', name)
    
    return 

#列出總資材
def getAll():
    
    return f.readAll()


#新增資材
def addItem(frm, tree, name, num):
    content = { 'amount': num, 'dam': '0'}
    f.updateItem(name, content)
    li = [name, num, '0']
    tree.insert('', 'end', values=li)
    print('新增', name, '數量', num)
    frm.destroy()
    return

#移除資材
def removeItem(name):
    f.removeItem(name)
    
    print('移除', name)
    return

#修改資材
def editItem(frm, tree, name, amount, dam):
    content = {'amount': amount, 'dam': dam}
    f.updateItem(name, content)
    for item in tree.get_children():
        if tree.item(item, 'value')[0] == name:            
            tree.item(item, values=[name, amount, dam])
            print('修改', name, amount, dam)
    frm.destroy()
    return

#列出借出中資材
def getLend():
    return f.readLend()


#借出資材
def lendout( data):
    f.saveLend(data)
    print(data['name'], '借了資材')
    return

#歸還資材
def giveBack( date, time):
    for i in getLend():
        if i['date']==date and i['time']==time:
            print('歸還', i['name'])
            f.giveBack(i)
    return

#清除資料
def clear():
    
    return
