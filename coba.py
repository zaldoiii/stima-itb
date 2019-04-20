import sys

s = sys.argv[1:] 
print(s[0])

import pandas as pd
db = pd.read_csv('db.csv')

matrix = db.values

for i in range(0,len(matrix)):
    for j in range(0,2):
        print(matrix[i][j])

import re

str = "hello asdfasdfasdfa world"

#Check if the string ends with 'world':

x = re.findall("^hello.*world$", str)
print(x);
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")

pattern = "hello world"
text = "hello my cozy world g fchgf j"
pattern1 = pattern.split()
print(pattern1[0])
print(pattern1[len(pattern1)-1])
cari = "^" + pattern1[0] + ".*" + pattern1[len(pattern1)-1] 
print(cari)

def cariRegex(pattern, matriks):
        for i in range(0,len(matrix)):
                for j in range(0,2):
                        print(matrix[i][j])


y = re.findall(cari, text);

print(y)