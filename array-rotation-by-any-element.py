from array import *

arr = array("i",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
n = int(input("enter the element from where you want to rotate the array : "))

i = 0
while(i < n):
    temp = arr[0]
    j = 0
    while(j < len(arr)-1):
        arr[j] = arr[j+1]
        arr[j+1] = temp
        j = j + 1
    i = i + 1

i = 0 
while(i < len(arr)):
    print(arr[i],end = " ")
    i = i + 1