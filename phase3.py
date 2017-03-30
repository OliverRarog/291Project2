import xml.etree.ElementTree as ET
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

results(b'000000001')
