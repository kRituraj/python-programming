
lower = 1
upper = 301

print("Prime numbers are : ")

for num in range(lower, upper):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end = ", ")