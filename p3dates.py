from bsddb3 import db

def openDateDB():
    database = db.DB()
    database.open("da.idx")
    cur = database.cursor()
    return database, cur

def closeDateDB(database, cur):
    cur.close()
    database.close()

#example query: date:2011/01/01
#input: 2011/01/01 (string)
#returns a list of ids as byte literals
#iterates through the database
#if date from database = date
#add the id from database to the return list
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

#example query: date<2011/01/01
#behaves like exactDate
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

#example query: date>2011/01/01
#behaves like exactDate
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
    
            
