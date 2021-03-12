from array import *


MyArray = [None] * 20
MyArray1 = [None] * 20

i = 0
while(i < 20):
    MyArray[i] = i + 1
    i = i + 1

j = 0
i = 19

while(j < 20):
    MyArray1[j] = MyArray[i]
    j = j + 1
    i = i - 1

i = 0
while(i < 20):
    print(MyArray1[i],end = " ")
    i = i + 1