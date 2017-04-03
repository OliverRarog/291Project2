import os

# tries to delete a file if it exits
def delFile(fileName):
	try:
		os.remove(fileName)
	except OSError:
		pass

# sort the file
os.system("sort -u -o tweets.txt tweets.txt")
os.system("sort -u -o terms.txt terms.txt")
os.system("sort -u -o dates.txt dates.txt")

# break up the files by key then \n then data
os.system("perl break.pl < tweets.txt > tweetsOP.txt")
os.system("perl break.pl < terms.txt > termsOP.txt")
os.system("perl break.pl < dates.txt > dateOP.txt")

# makes sure that there is no database, no chance of merging or overwriting 
delFile("tw.idx")
delFile("te.idx")
delFile("da.idx")

#load the database
os.system("db_load -T -t hash -f tweetsOP.txt tw.idx")
os.system("db_load -c duplicates=1 -T -t btree -f termsOP.txt te.idx")
os.system("db_load -c duplicates=1 -T -t btree -f dateOP.txt da.idx")


