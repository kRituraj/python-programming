
#merge array to make array palindrome 

from array import *

arr = [1,3,5,7,12,4]

operations = 0

i = 0
j = len(arr)-1
while(i <= j):
    if (arr[i] == arr[j]):
        i = i + 1
        j = j - 1
    elif (arr[i] > arr[j]):
        j = j - 1
        arr[j] = arr[j] + arr[j + 1]
        operations = operations + 1
    elif (arr[i] < arr[j]):
        i= i + 1
        arr[i] = arr[i] + arr[i - 1]
        operations = operations + 1

print("total operations are : " +str(operations))