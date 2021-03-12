from array import *
MyArray = array("i",[1,2,3,4,5,6,7,8,9,10,11,15,15,3,4,20])

i = 0
sum = 0
while(i < len(MyArray)):
    sum = sum + MyArray[i]
    i = i + 1
print(sum)