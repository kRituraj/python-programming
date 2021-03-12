from array import *

arr = array("i",[1,2,3,4,5,6,7,8,9,10])
n = int(input("enter the number from you which you want to rotate : "))

i = 0
while(i < len(arr)-1):
    if (n > len(arr) or n < 0):
        print("invalid input")
        break
    else:
        i = 0
        while(i < n):
            j = 0
            temp = arr[0]
            while(j < len(arr)-1):
                arr[j] = arr[j+1]
                arr[j+1] = temp
                j = j + 1
            i = i + 1
        
        i = 0
        while(i < len(arr)):
            print(arr[i],end = " ")
            i = i + 1