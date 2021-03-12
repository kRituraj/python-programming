from array import *
arr = [22,44,66,88,11,33,55,77,99]

smallest = arr[0]
largest = arr[1]

if (smallest > largest):
    smallest = arr[1]
    largest = arr[0]
    
i = 0
while(i < len(arr)):
    if (smallest > arr[i]):
        smallest = arr[i]
    i = i + 1
#print(smallest)
i = 0
while(i < len(arr)):
    if (largest < arr[i]):
        largest = arr[i]
    i = i + 1
#print(largest)
range = (largest - smallest)
print(range)
coefficient = (largest - smallest)/(largest + smallest)
print(coefficient)

