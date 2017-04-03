import xml.etree.ElementTree as ET
import re, sys
from bsddb3 import db

#id as a byte literal
#finds the data for the ids given
#prints the data
#probably needs to be debugged
def results(bid):
    database = db.DB()
    database.open("tw.idx")
    cur = database.cursor()
    iter = cur.first()
    while iter:
        iid = iter[0]
        if iid == bid:
            root = ET.fromstring(iter[1].decode("utf-8"))
            for child in root.iter():
                if(child.text != None):
                    if(child.tag == 'id'):
                        print("Id: " + child.text)
                    if(child.tag == 'created_at'):
                        print("Created at: " + child.text)
                    if(child.tag == 'text'):
                        print("Text: " + child.text)
                    if(child.tag == 'name'):
                        print("Name: " + child.text)
                    if(child.tag == 'location'):
                        print("Location: " + child.text)
                    if(child.tag == 'description'):
                        print("Description: " + child.text)
                    if(child.tag == 'url'):
                        print("URL: " + child.text)
            print("")
        iter = cur.next()
    cur.close()
    database.close()

# checks if query is YYYY/MM/DD
def validateDateFormat(date):
    try:
        mat=re.match('(\d{4})[/.](\d{2})[/.](\d{2})$', date)
        if mat is not None:
            return True
    except ValueError:
        pass
    return False

def interface():
    while(1):
        queryStr = input("Please enter your query or type 'exit' to quit: ")
        queryStr.strip()
        queries = queryStr.split()
        if(queryStr == 'exit'):
            sys.exit(0)

        for query in queries:
            if(query.startswith("text:")):
                query = query[5:]
                if(query[-1] == '%'):
                    print("wildcard text")
                elif(not query.isalnum()):
                    print('Reject query text:%s as it contains non alphanumeric characters!' % query)
                    continue
                # do text matching
                
            
            elif (query.startswith("name:")):
                query = query[5:]
                if(query[-1] == '%'):
                    print("wildcard name")
                elif(not query.isalnum()):
                    print('Reject query name:%s as it contains non alphanumeric characters!' % query)
                    continue
                # do name matching
                
            
            elif (query.startswith("location:")):
                query = query[9:]
                if(query[-1] == '%'):
                    print("wildcard location")
                elif(not query.isalnum()):
                    print('Reject query location:%s as it contains non alphanumeric characters!' % query)
                    continue
                # do location matching
                
            
            elif (query.startswith("date:")):
                query = query[5:]
                if(not validateDateFormat(query)):
                    print('Reject query date:%s! All dates must be in the form YYYY/MM/DD' % query)
                    continue
                # do exacte date matching
            
            elif (query.startswith("date<")):
                query = query[5:]
                if(not validateDateFormat(query)):
                    print('Reject query date<%s! All dates must be in the form YYYY/MM/DD' % query)
                    continue
                # do < date matching
                
            
            elif (query.startswith("date>")):
                query = query[5:]
                if(not validateDateFormat(query)):
                    print('Reject query date>%s! All dates must be in the form YYYY/MM/DD' % query)
                    continue
                # do > date matching

                
            
            else:
                if(query[-1] == '%'):
                    if(not query[:-1].isalnum):
                        print('Non-prefixed queries must only contain alphanumeric characters! Rejecting query %s' % query)
                        continue
                    # do alphanum query matching with wildcard
                    pass
                elif(not query.isalnum()):
                    print('Non-prefixed queries must only contain alphanumeric characters! Rejecting query %s' % query)
                    continue
                # do non-wildcard alphanum matching



interface()