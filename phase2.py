import os

os.system("sort -u -o tweets.txt tweets.txt")
os.system("sort -u -o terms.txt terms.txt")
os.system("sort -u -o dates.txt dates.txt")
os.system("perl break.pl < tweets.txt > tweetsOP.txt")
os.system("perl break.pl < terms.txt > termsOP.txt")
os.system("perl break.pl < dates.txt > dateOP.txt")
os.system("db_load -T -t hash -f tweetsOP.txt tw.idx")
os.system("db_load -T -t btree -f termsOP.txt te.idx")
os.system("db_load -T -t btree -f dateOP.txt da.idx")

#######################
# extra db_dump for verification

os.system("db_dump -k -d a -f tweetdecomp.txt tw.idx")
os.system("db_dump -k -d a -f termdecomp.txt te.idx")
os.system("db_dump -k -d a -f datedecomp.txt da.idx")

