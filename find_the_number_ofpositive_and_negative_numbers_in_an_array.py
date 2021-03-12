from array import *
MyArray = array("i",[1,2,-3,4,5,6,7,8,9,-1,33,-65,3])

i = 0
positive = 0
negative = 0
while(i < len(MyArray)):
    if (MyArray[i] >= 0):
        positive = positive + 1
    else:
        negative = negative + 1
    i = i + 1
print("total positive elements are : "+str(positive))
print("total negative elements are : "+str(negative))