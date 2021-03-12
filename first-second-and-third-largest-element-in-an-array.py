from array import *

arr = [3,1,5,6,9,2,4,7,8,0]

first = arr[0]
second = arr[1]
third = arr[2]

i = 3
while(i < len(arr)):

    if (arr[i] > first):

        third = second
        second = first
        first = arr[i]

    elif (arr[i] > second):

        third = second
        second = arr[i]
 
    elif (arr[i] > third):
        third = arr[i]

    i = i + 1

print("third largest element in this array is : "+str(third))
