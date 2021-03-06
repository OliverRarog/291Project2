import xml.etree.ElementTree as ET
import re, sys, p3dates, p3terms
from bsddb3 import db

#bid is the id as a byte literal
#finds the data for the ids given by iterating through tw.idx
#prints the data by extracting the info from the xml
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


# given multiple result sets from multiple queries, only return ids who are common in each result set
def intersectResults(idArray):
    if(len(idArray )< 1):
        return []
    intersected = idArray[0]
    for array in idArray:
        intersected = list(set(array).intersection(intersected))
    return intersected

# main interface
def interface():
    while(1):
        queryStr = input("Please enter your query or type 'exit!' to quit: ")
        queryStr.strip()
        queries = queryStr.split()
        if(queryStr == 'exit!'):
            sys.exit(0)
        
        idArrays = []
        for query in queries:
            if(query.startswith("text:")):
                query = query[5:] # remove prefix
                if(len(query) < 1):
                    continue
                # if we need to do wildcard
                if(query[-1] == '%'):
                    if(not query[:-1].isalnum):
                        print('Query text must only contain alphanumeric characters! Rejecting query text:%s' % query)
                        continue
                    idArrays.append(p3terms.returnTextWildcard(query[:-1].lower()))
                elif(not query.isalnum()):
                    print('Rejecting query text:%s as it contains non alphanumeric characters!' % query)
                    continue
                # do text matching
                else:
                    idArrays.append(p3terms.returnText(query.lower()))
                
            
            elif (query.startswith("name:")):
                query = query[5:] # remove prefix
                # if we need to do wildcard
                if(len(query) < 1):
                    continue
                if(query[-1] == '%'):
                    if(not query[:-1].isalnum):
                        print('Query text must only contain alphanumeric characters! Rejecting query name:%s' % query)
                        continue
                    idArrays.append(p3terms.returnNameWildcard(query[:-1].lower()))   
                elif(not query.isalnum()):
                    print('Rejecting query name:%s as it contains non alphanumeric characters!' % query)
                    continue
                # do name matching
                else:
                    idArrays.append(p3terms.returnName(query.lower()))
                
            elif (query.startswith("location:")):
                query = query[9:] # remove prefix
                # if we need to do wildcard
                if(len(query) < 1):
                    continue
                if(query[-1] == '%'):
                    if(not query[:-1].isalnum):
                        print('Query text must only contain alphanumeric characters! Rejecting query location:%s' % query)
                        continue
                    idArrays.append(p3terms.returnLocWildcard(query[:-1].lower())) 
                elif(not query.isalnum()):
                    print('Rejecting query location:%s as it contains non alphanumeric characters!' % query)
                    continue
                # do location matching
                else:
                    idArrays.append(p3terms.returnLocation(query.lower()))
                
            elif (query.startswith("date:")):
                query = query[5:] # remove prefix
                if(not validateDateFormat(query)):
                    print('Rejecting query date:%s! All dates must be in the form YYYY/MM/DD' % query)
                    continue
                # do exacte date matching
                idArrays.append(p3dates.exactDate(query))
            
            elif (query.startswith("date<")):
                query = query[5:] # remove prefix
                if(not validateDateFormat(query)):
                    print('Rejecting query date<%s! All dates must be in the form YYYY/MM/DD' % query)
                    continue
                # do < date matching
                idArrays.append(p3dates.lessThanDate(query))
                
            elif (query.startswith("date>")):
                query = query[5:] # remove prefix
                if(not validateDateFormat(query)):
                    print('Rejecting query date>%s! All dates must be in the form YYYY/MM/DD' % query)
                    continue
                # do > date matching
                idArrays.append(p3dates.greaterThanDate(query))

            else:
                if(len(query) < 1):
                    continue
                if(query[-1] == '%'):
                    if(not query[:-1].isalnum):
                        print('Non-prefixed queries must only contain alphanumeric characters! Rejecting query %s' % query)
                        continue
                    # do alphanum query matching with wildcard
                    idArrays.append(p3terms.returnWildcard(query[:-1].lower()))
                elif(not query.isalnum()):
                    print('Non-prefixed queries must only contain alphanumeric characters! Rejecting query %s' % query)
                    continue
                # do non-wildcard alphanum matching
                else:
                    idArrays.append(p3terms.returnAny(query.lower()))

        # get only results common to each individual query
        result = intersectResults(idArrays)
        for rs in result:
            # print results
            results(rs)



interface()
