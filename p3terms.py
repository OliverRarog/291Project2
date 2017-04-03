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

# Function that returns any record matches on text:___ queries
def returnText(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    text = "t-" + text

#   Append any matches in the list of terms to the list of matched ids
    while iter:
        rText = iter[0]

        if rText.decode("utf-8") == text and iter[1] not in ids:
            ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

# Function that returns any record matches on name:___ queries
def returnName(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    text = "n-" + text
   
#   Add any matched name queries into the list of ids to return
    while iter:
        rText = iter[0]

        if rText.decode("utf-8") == text and iter[1] not in ids:
            ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

# Function that returns any record matches on location:___ queries
def returnLocation(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    text = "l-" + text
    
#   Add any matched name queries into the list of ids to return
    while iter:
        rText = iter[0]

        if rText.decode("utf-8") == text and iter[1] not in ids:
            ids.append(iter[1])
        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

# Function that returns any record matches on any field of name/text/location 
def returnAny(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()

#   Covering all possible text fields
    textLoc  = "l-" + text
    textName = "n-" + text
    textText = "t-" + text
   
#   If the input query matches any text/name/location header
#   Add it to the list of returned ids if the id is not already contained.
    while iter:
        rText = iter[0]

        if rText.decode("utf-8") == textLoc or rText.decode("utf-8") == textName or rText.decode("utf-8") == textText:

            if iter[1] not in ids:
                ids.append(iter[1])

        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

# post-appended Wildcard search of the returnText function
def returnTextWildcard(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    regex = "t-" + text + ".*"
 
    while iter:
        rText = iter[0].decode("utf-8")
        matched = re.match(regex,rText)

        if matched and iter[1] not in ids:
            ids.append(iter[1])

        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

# post-appended Wildcard search of the returnName function
def returnNameWildcard(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    regex = "n-" + text + ".*"
 
    while iter:
        rText = iter[0].decode("utf-8")
        matched = re.match(regex,rText)

        if matched and iter[1] not in ids:
            ids.append(iter[1])

        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

# post-appended Wildcard search of the returnLocation function
def returnLocWildcard(text):
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()
    regex = "l-" + text + ".*"
 
    while iter:
        rText = iter[0].decode("utf-8")
        matched = re.match(regex,rText)

        if matched and iter[1] not in ids:
            ids.append(iter[1])

        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 

# post-appended Wildcard search of the returnAny function
def returnWildcard(text):
    ids = [] 
    
    database, cur = openTermsDB()
    ids = []
    iter = cur.first()

#   Regex matches for all possible fields   
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
                ids.append(iter[1])

        iter = cur.next()
   
    closeTermsDB(database, cur)
    return ids 


