import sys

print("Hello world")
s = sys.argv[1:] 
s1 = s[0]
s2 = s1.split()
pattern = "^"
for i in range(len(s2)):
    pattern = pattern + s2[i] + "." + "*" 


#import library regex
import re

#baca db
import pandas as pd
db = pd.read_csv("db.csv")

#mengubah menjadi array 2D
db1 = db.values
for i in range(0,len(db)-1):
    x = re.findall(pattern,db1[i][0])
    if(x):
        print(db1[i][1])