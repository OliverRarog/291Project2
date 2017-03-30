import os

os.system("sort -u -o tweets.txt tweets.txt")
os.system("sort -u -o terms.txt terms.txt")
os.system("sort -u -o dates.txt dates.txt")
os.system("perl break.pl < tweets.txt > tweetsOP.txt")
os.system("perl break.pl < terms.txt > termsOP.txt")
os.system("perl break.pl < dates.txt > dateOP.txt")

