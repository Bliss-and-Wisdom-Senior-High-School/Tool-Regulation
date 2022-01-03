import FILEIO as f


#在總資材中搜尋找
def searchAll(name):
    print('搜尋', name)
    
    return 

#列出總資材
def getAll():
    
    return f.readAll()

#取出指定資材
def getItem(item):
    data = getAll()
    
    return data[item]

#新增資材
def addItem(frm, tree, name, num):
    content = { 'amount': num, 'dam': '0', 'lending': '0'}
    f.updateItem(name, content)
    li = [name, num, '0', '0']
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
def editItem(frm, tree, name, amount, dam, lending):
    content = {'amount': amount, 'dam': dam, 'lending': lending}
    f.updateItem(name, content)
    for item in tree.get_children():
        if tree.item(item, 'value')[0] == name:   
            tree.item(item, values=[name, amount, dam, lending])
            print('修改', name, amount, dam, lending)
    frm.destroy()
    return

def editAmount(tree, tool, amount):
    content = getItem(tool)
    content['lending'] = str(int(content['lending']) + amount)
    f.updateItem(tool, content)
    for item in tree.get_children():
        if tree.item(item, 'value')[0] == tool:
            remain = str(int(content['amount']) - int(content['lending']) - int(content['dam']))
            tree.item(item, values=[tool, content['amount'], content['dam'], content['lending'], remain])
            print('修改數量', tool, content['amount'], content['dam'], content['lending'])
    
    return

#列出借出中資材
def getLend():
    return f.readLend()


#借出資材
def lendout( data):
    for i in data['tools']:
        item = getItem(i['tool'])
        # item['lending'] = str(int(item['lending']) + int(i['amount']))
        f.updateItem(i['tool'], item)
    f.saveLend(data)
    print(data['name'], '借了資材')
    return

#歸還資材
def giveBack( date, time):
    for i in getLend():
        if i['date']==date and i['time']==time:
            for j in i['tools']:
                item = getItem(j['tool'])
                item['lending'] = str(int(item['lending']) - int(j['amount']))
            print('歸還', i['name'])
            f.giveBack(i)
    return

def debug():
    data = getAll()
    lend = getLend()
    for i in data:
        data[i]['lending'] = '0'
    for i in lend:
        for j in i['tools']:
            if not 'lending' in data[j['tool']]:
                data[j['tool']]['lending'] = j['amount']
            else:
                data[j['tool']]['lending'] = str(int(data[j['tool']]['lending']) + int(j['amount']))
            print(data[j['tool']])
    f.saveAll(data)

#清除資料
def clear():
    
    return

# debug()