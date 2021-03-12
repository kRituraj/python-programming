from array import *
MyArray = array("i",[1,2,3,4,5,6,7,8,9,10,23,11,54,28,10])
num = int(input("enter the number you want to search : "))

i = 0
count = 0
found = 0
while(i <len(MyArray)):
    if(num == MyArray[i]):
        count = count + 1
        found = 1
    i = i + 1
print("number is present " + str(count) +" times")
if found == 0:
    print("number is not present in the array")