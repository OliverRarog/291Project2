import os

os.system("sort -u -o tweets.txt tweets.txt")
os.system("sort -u -o terms.txt terms.txt")
os.system("sort -u -o dates.txt dates.txt")
os.system("perl break.pl < tweets.txt > tweetsOP.txt")
os.system("perl break.pl < terms.txt > termsOP.txt")
os.system("perl break.pl < dates.txt > dateOP.txt")
os.system("db_load -T -t hash -f tweetsOP.txt tweets.db")
os.system("db_load -T -t btree -f termsOP.txt terms.db")
os.system("db_load -T -t btree -f dateOP.txt dates.db")

