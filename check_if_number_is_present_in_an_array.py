from array import *
MyArray = array("i",[1,2,3,4,5,6,7,8,9,10])
num = int(input("enter the number you want to search : "))

i = 0
found = 0
while(i < len(MyArray)):
    if (num == MyArray[i]):
        print("number is present")
        found = 1
        break

    i = i + 1

if (found == 0):
        print("number is not present")