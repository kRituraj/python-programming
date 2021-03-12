from array import *
MyArray = array("i",[1,3,4,6,89,6,4,2,5,55,67,32,2,11,76,37,81,46,7])


i = 0
even = 0
odd = 0

while(i < len(MyArray)):
    if (MyArray[i] %2 == 0):
        even = even + 1
        
    else:
        odd = odd + 1
    i = i + 1
print(even)
print(odd)
