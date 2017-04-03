from bsddb3 import db

def openDateDB():
    database = db.DB()
    database.open("da.idx")
    cur = database.cursor()
    return database, cur

def closeDateDB(database, cur):
    cur.close()
    database.close()

#date is a string
#returns a list of ids as byte literals
def exactDate(date):
    database, cur = openDateDB()
    ids = []
    iter = cur.first()
    while iter:
        idate = iter[0]
        #print(idate.decode("utf-8"))
        if idate.decode("utf-8") == date:
            ids.append(iter[1])
        iter = cur.next()
    closeDateDB(database, cur)
    return ids

def lessThanDate(date):
    database, cur = openDateDB()
    ids = []
    iter = cur.first()
    while iter:
        idate = iter[0]
        if idate.decode("utf-8") < date:
            ids.append(iter[1])
        iter = cur.next()
    closeDateDB(database,cur)
    return ids

def greaterThanDate(date):
    database, cur = openDateDB()
    ids = []
    iter = cur.first()
    while iter:
        idate = iter[0]
        if idate.decode("utf-8") > date:
            ids.append(iter[1])
        iter = cur.next()
    closeDateDB(database,cur)
    return ids

#ids = exactDate("2012/03/11")
#print(len(ids))
#for id in ids:
#    print(id.decode("utf-8"))
    
            
