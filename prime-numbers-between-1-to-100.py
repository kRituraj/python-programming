from array import *

# declaring the array
MyArray = [None] * 100

#initializing the array
i = 0
while(i < 100):
    MyArray[i] = i + 1
    i = i + 1


j = 1
while(j < 100):
    if(MyArray[j] != 0):
        k = j + 1
        while(k < 100):
            if (MyArray[k] % MyArray[j] == 0):
                MyArray[k] = 0
            k = k + 1
    j = j +1

i = 0
while i < 100 :
    if (MyArray[i] != 0):
        print(MyArray[i],end = " ")
    i = i + 1
