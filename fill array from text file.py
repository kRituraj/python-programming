from array import *
from collections import Counter

text_file = open("D:\\numbers.txt","r")
abc = []
lines = text_file.readlines()
text_file.close()
for line in lines:
    abc.append(line[0:-1])
print (abc,end = " ")