import sys
import xml.etree.ElementTree as ET
import re

def pullTerms(text):
	# given text, pulls terms based on specs
	termsRe = re.findall('[0-9a-zA-Z_]+', text)
	results = []
	for term in termsRe:
		if(len(term) < 3):
			continue
		results.append(term.lower())
	return results

def pullNames(text):
	# pulls names from text
	namesRe = re.findall('[0-9a-zA-Z_]+', text)
	results = []
	for name in namesRe:
		if(len(name) < 3):
			continue
		results.append(name.lower())
	return results

def pullLocations(text):
	# pulls locations from text
	locsRe = re.findall('[0-9a-zA-Z_]+', text)
	results = []
	for loc in locsRe:
		if(len(loc) < 3):
			continue
		results.append(loc.lower())
	return results

# opens all files for use, exits if not possible
try:
	termsFile = open('terms.txt', 'w')
except IOError:
	print('Could not open file terms.txt for use. Exiting...')
	sys.exit(0)
try:
	datesFile = open('dates.txt', 'w')
except IOError:
	print('Could not open file dates.txt for use. Exiting...')
	sys.exit(0)
try:
	tweetsFile = open('tweets.txt', 'w')
except IOError:
	print('Could not open file tweets.txt for use. Exiting...')
	sys.exit(0)

while(True):
	fileName = input('Please enter the name of the file you wish to read data from: ')
	try:
		inputFile = open(fileName)
		break
	except IOError:
		print('Could not open file %s for use. Make sure that is exists in this directory' % fileName)



tree = ET.parse(inputFile)
currId = 0
Ids = []
for child in tree.iter():
	# changes id of tweet	
	if(child.tag == 'id'):
		currId = child.text
		record = currId + ":<status>"
		Ids.append(currId)
	if(child.text is None):
			continue
	# this block writes the terms.txt file	
	if(child.tag == 'text'):
		terms = pullTerms(str(child.text))
		for term in terms:
			termsFile.write('t-%s:%s\n' % (term, currId))
	if(child.tag == 'name'):
		names = pullNames(str(child.text))
		for name in names:
			termsFile.write('n-%s:%s\n' % (name, currId))
	if(child.tag == 'location'):
		locs = pullLocations(str(child.text))
		for loc in locs:
			termsFile.write('l-%s:%s\n' % (loc, currId))
	
	# this block write the dates.txt file	
	if(child.tag == 'created_at'):
		datesFile.write('%s:%s\n' % (child.text, currId))

# gets info for the tweets.txt file
inputFile.seek(0)
line = inputFile.readline()
while(not line.startswith("<status>")):
	 line = inputFile.readline()

# for each id, get xml data
for Id in Ids:
	record = Id + ":" + line
	tweetsFile.write(record)
	line = inputFile.readline()
