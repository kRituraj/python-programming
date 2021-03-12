from array import *

arr = [7,0,5,9,10,1,6,8,7,4]
min_difference = 5

i = 0
while(i < len(arr)):
    j = i + 1
    while(j < len(arr)):
        if ((arr[i] - arr[j] == min_difference) or (arr[j] - arr[i] == min_difference)):
            print("Minimum difference is between : " + str(arr[i]) + " and " + str(arr[j]))
        j = j + 1
        
    i = i + 1