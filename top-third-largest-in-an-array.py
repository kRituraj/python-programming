from array import *

arr = [2,1,4,3,5,7,6,9,8,0]

i = 0
while(i < len(arr)):
    j = i + 1
    while(j < len(arr)):
        if (arr[i] < arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j = j + 1
    i = i + 1

print("top thirid largest element in this array is :  "+str(arr[2]))