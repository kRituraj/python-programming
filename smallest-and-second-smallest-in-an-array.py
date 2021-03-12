from array import *

arr = array("i",[-43,-44,-6,13,23,10,-21,55])

if (arr[0] < arr[1]):

    smallest = arr[0]
    second_smallest = arr[1]
    
    largest = arr[1]
    second_largest = arr[0]
else:

    smallest = arr[1]
    second_smallest = arr[0]

    largest = arr[0]
    second_largest = arr[1]



i = 2

while(i < len(arr)):

    if (smallest > arr[i]):

        second_smallest = smallest
        smallest = arr[i]
        

    elif (smallest < arr[i] and second_smallest > arr[i]):

        second_smallest = arr[i]

    elif (largest < arr[i]):

        second_largest = largest
        largest = arr[i]

    elif (largest > arr[i] and second_largest < arr[i]):

        second_largest = arr[i]

    i = i + 1

    product1 = smallest * second_smallest
    product2 = largest * second_largest

if (product1 < product2):
    print("two elemets are " +str(largest) +" and " +str(second_largest))
else:
    print("two elemets are " +str(smallest) +" and " +str(second_smallest))
