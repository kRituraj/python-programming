from array import *

arr = array("i",[4,6,8,2,1,7,9,0,3,5])

i = 0
while(i < len(arr)):
    j = i + 1
    while(j < len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j = j + 1
    i = i + 1


i = 0
while(i < len(arr)):
    print(arr[i],end = " ")
    i = i + 1
