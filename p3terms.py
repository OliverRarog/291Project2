from bsddb3 import db
import fnmatch

def openTermsDB():
    database = db.DB()
    database.open("te.idx")
    cur = database.cursor()
    return database, cur

def closeTermsDB(database, cur):
    cur.close()
    database.close()

def returnText(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    text = "t-" + text
    
    while iter:
        rText = iter[0]
        if rText.decode("utf-8") == text:
            ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

def returnName(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    text = "n-" + text
    
    while iter:
        rText = iter[0]
        if rText.decode("utf-8") == text:
            ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

def returnLocation(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    text = "l-" + text
    
    while iter:
        rText = iter[0]
        if rText.decode("utf-8") == text:
            ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

def returnAny(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    textLoc  = "l-" + text
    textName = "n-" + text
    textText = "t-" + text
    
    while iter:
        rText = iter[0]
        if rText.decode("utf-8") == textLoc or rText.decode("utf-8") == textName or rText.decode("utf-8") == textText:
            ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

def returnWildcard(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    textText = "t-" + text + "*"
    
    while iter:
        rText = iter[0].decode("utf-8")
        filtered = fnmatch.filter(rText, textText)
#        print(filtered)
#        if rText.decode("utf-8") == :
#            ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 




idt = returnText("played")
idn = returnName("nurse")
idl = returnLocation("germany")
ida = returnAny("germany")
idw = returnWildcard("germ")

print("idt: played")
for id in idt:
    print(id.decode("utf-8"))

print("idn: nurse")
for id in idn:
    print(id.decode("utf-8"))

print("idl: germany")
for id in idl:
    print(id.decode("utf-8"))

print("ida: germany")
for id in ida:
    print(id.decode("utf-8"))

print("idw: germ")
for id in idw:
    print(id.decode("utf-8"))
