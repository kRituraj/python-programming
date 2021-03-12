
#arr[i] = i

from array import *

arr = array("i",[-1,4,-1,7,5,-1,2,-1,3,8,0])

i = 0
while(i < len(arr)):
    if (arr[i] >= 0 and arr[i] != i):
        temp = arr[i]
        arr[i] = arr[temp]
        arr[temp] = temp
    else:
        i = i + 1
print(arr)

'''
from array import *

arr = array("i",[-1,4,-1,7,5,-1,2,-1,3,8,0])

i = 0
while(i < len(arr)):
    if (arr[i] != -1 and arr[i] != i):
        x = arr[i]
        while(arr[x] != -1 and arr[x] != x):
            y = arr[x]
            arr[x] = x
            x = y
        arr[x] = x

        if (arr[i] != i):
            arr[i] = -1
        
    i = i + 1
print(arr)

'''