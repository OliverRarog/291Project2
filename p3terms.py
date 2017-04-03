from bsddb3 import db
import re

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
#            print(rText)
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
#            print(rText)
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
#            print(rText)
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
            if iter[1] not in ids:
#                print(rText)
                ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

def returnTextWildcard(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()

    regex = "t-" + text + ".*"
 
#    print(regex)
    while iter:
        rText = iter[0].decode("utf-8")
        m = re.match(regex,rText)
        if m:
            if iter[1] not in ids:
#                print(rText)
                ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

def returnNameWildcard(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()

    regex = "n-" + text + ".*"
 
#    print(regex)
    while iter:
        rText = iter[0].decode("utf-8")
        m = re.match(regex,rText)
        if m:
            if iter[1] not in ids:
#                print(rText)
                ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

def returnLocWildcard(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()

    regex = "l-" + text + ".*"
 
#    print(regex)
    while iter:
        rText = iter[0].decode("utf-8")
        m = re.match(regex,rText)
        if m:
            if iter[1] not in ids:
#                print(rText)
                ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

def returnWildcard(text):
    ids = [] 
    
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()

    regexText = "t-" + text + ".*"
    regexName = "n-" + text + ".*"
    regexLoc  = "l-" + text + ".*"

    while iter:
        rText = iter[0].decode("utf-8")
        t = re.match(regexText, rText)
        n = re.match(regexName, rText)
        l = re.match(regexLoc, rText)

        if t or n or l:
            if iter[1] not in ids:
#                print(rText)
                ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 


#print("idt: played")
#idt = returnText("played")
#for id in idt:
#    print(id.decode("utf-8"))

#print("idn: nurse")
#idn = returnName("nurse")
#for id in idn:
#    print(id.decode("utf-8"))

#print("idl: germany")
#idl = returnLocation("germany")
#for id in idl:
#    print(id.decode("utf-8"))
#

#print("ida: germany")
#ida = returnAny("germany")
#for id in ida:
#    print(id.decode("utf-8"))

#print("idtw: ge")
#idtw = returnTextWildcard("ge")
#for id in idtw:
#    print(id.decode("utf-8"))

#print("Name wildcard: sim")
#idnw = returnNameWildcard("sim")
#for id in idnw:
#    print(id.decode("utf-8"))

#print("Loc wildcard: 8")
#idlw = returnLocWildcard("8")
#for id in idlw:
#    print(id.decode("utf-8"))

#print("Any wildcard: m")
#idw = returnWildcard("m")
#for id in idw:
#    print(id.decode("utf-8"))
