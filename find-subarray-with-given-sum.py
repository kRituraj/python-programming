from array import *

arr = [1,3,5,7,9,2,4,6,8,0]
sum = 15

l = 0
s = arr[0]
i = 1
while (i <= len(arr)):

    while ((s > sum) and (l < i-1)):
        s = s - arr[l]
        l = l + 1
    if (s == sum):
        print(str(l) +" and " +str(i-1))
    if (i < len(arr)):
        s = s + arr[i]
    i = i + 1
print ("No subarray found") 