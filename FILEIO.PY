import json

'''
savefile.txt 記錄總資材
lendout.txt 記錄借出中資材

'''

def updateItem(name, content):
    try:
        f = open("storage//savefile.txt", "r")
        json.loads(f.read())
    except (FileNotFoundError, ValueError) as e:
        print("File not exist or invalid JSON, recreating savefile.txt...")
        print(e)
        f = open("storage//savefile.txt", "w")
        f.write("{}")
    fr = open("storage//savefile.txt", "r")
    savefile = json.loads(fr.read())
    savefile[name] = content
    fw = open("storage//savefile.txt", "w")
    fw.write(json.dumps(savefile, indent=4))
    
def removeItem(name):
    try:
        f = open("storage//savefile.txt", "r")
        json.loads(f.read())
    except (FileNotFoundError, ValueError) as e:
        print("File not exist or invalid JSON, recreating savefile.txt...")
        print(e)
        f = open("storage//savefile.txt", "w")
        f.write("{}")
    fr = open("storage//savefile.txt", "r")
    savefile = json.loads(fr.read())
    del savefile[name]
    fw = open("storage//savefile.txt", "w")
    fw.write(json.dumps(savefile, indent=4))
    

def readAll():
    try:
        f = open("storage//savefile.txt", "r")
        json.loads(f.read())
    except (FileNotFoundError, ValueError) as e:
        print("Cannot find file or file corrupted.")
        f = open("storage//savefile.txt", "w")
        f.write("{}")
        return {}
    fr = open("storage//savefile.txt", "r")
    savefile = json.loads(fr.read())
    return savefile

def clearAll():
    f = open("storage//savefile.txt", "w")
    f.write("{}")
    clearLend()


def saveLend(data):
    try:
        f = open("storage//lendout.txt", "r")
        json.loads(f.read())
    except (FileNotFoundError, ValueError) as e:
        print("File not exist or invalid JSON, recreating savefile.txt...")
        print(e)
        f = open("storage//savefile.txt", "w")
        f.write("[]")
    fr = open("storage//lendout.txt", "r")
    savefile = json.loads(fr.read())
    savefile.append(data)
    fw = open("storage//lendout.txt", "w")
    fw.write(json.dumps(savefile, indent=4))
    
def giveBack(data):
    try:
        f = open("storage//lendout.txt", "r")
        json.loads(f.read())
    except (FileNotFoundError, ValueError) as e:
        print("File not exist or invalid JSON, recreating savefile.txt...")
        print(e)
        f = open("storage//savefile.txt", "w")
        f.write("[]")
    fr = open("storage//lendout.txt", "r")
    savefile = json.loads(fr.read())
    savefile.remove(data)
    fw = open("storage//lendout.txt", "w")
    fw.write(json.dumps(savefile, indent=4))
    

def readLend():
    try:
        f = open("storage//lendout.txt", "r")
        json.loads(f.read())
    except (FileNotFoundError, ValueError) as e:
        print("Cannot find file or file corrupted.")
        f = open("storage//lendout.txt", "w")
        f.write("[]")
    fr = open("storage//lendout.txt", "r")
    savefile = json.loads(fr.read())
    return savefile

def clearLend():
    f = open("storage//lendout.txt", "w")
    f.write("[]")
    
