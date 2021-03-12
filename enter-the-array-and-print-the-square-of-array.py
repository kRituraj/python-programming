from array import *
MyArray = array("i",[1,3,5,7,9,2,4,6,8,10,25,15,55,23])

i = 0
square = 1
while(i < len(MyArray)):
    square = MyArray[i] * MyArray[i]
    i = i + 1
    print(square,end = " ")