from array import *

def binarySearch(MyArray,n):

    l = 0
    u = len(MyArray) - 1
    while(l <= u):
        mid = int((l + u) / 2)
        if (MyArray[mid] == n):
            return 1
        else:
            if MyArray[mid] < n:

                l = mid + 1
#                u = len(MyArray) - 1

            elif MyArray[mid] > n:

#                l = 0
                u = mid - 1

    return 0

MyArray = array("i",[2,3,4,5,6,8,9,10])
n = int(input("enter the number"))

x = binarySearch(MyArray,n)
if x == 1:
    print("number is present")
else:
    print("number is not present")