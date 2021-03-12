from array import *
MyArray = array("i",[1,2,3,4,5,6,7,8,9,10])

i = 0
even = 1
odd = 1
while (i < len(MyArray)):
    if (MyArray[i] %2 == 0):
        even = MyArray[i] * MyArray[i]
        print(even , end = " ")
    else:
        odd = MyArray[i] * MyArray[i] * MyArray[i]
        print(odd , end = " ")
    i = i + 1
