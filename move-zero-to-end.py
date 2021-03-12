from array import *

arr = array("i",[0,12,2,3,0,4,0,5,0,0,6,7,8,10,0,9])

i = 0
count = 0
while(i < len(arr)):
    if (arr[i] != 0):
        temp = arr[i]
        arr[i] = arr[count]
        arr[count] = temp
        count = count + 1
    i = i + 1

print(arr)