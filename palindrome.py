num = int(input("enter the number"))
temp = num
rev = 0
while(num>0):
    rev = rev * 10 + num % 10
    num = num // 10
if (temp == rev):
    print("it is palindrome")
else:
    print("it is  not palindrome")