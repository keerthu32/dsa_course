"""
Build a Python program that:

Takes a single number as input

Performs multiple analyses:

Count of digits

Sum of digits

Product of digits

Reverse of number

Even/Odd digit count

Check if it’s a palindrome

Check if it’s an Armstrong number

plan
----------------------------------------------------------
--> take a input from the user
--> convert to string make find it length to count
--> take the string loop and convert the number and add all number store in the sum_digits
--> repeat same for product but multiply it
--> reverse the number using reverse method or use [::1]
--> while using for loop find each number is divide by 2 if yes count as even or odd
--> if the string and its reversed are same then said its palindrome
--> while looping each number cube them and add and store in variable then check
if the real number and added number are same mention it is armstrong
convert to code
m=int(input("enter the number how much you want to enter for process"))
sum=0
mul=1
cube=0
even_c=0
odd_c=0
palindrome=True
armstrong=True
for i in range(m):
    n=input("enter the number now for process")
    count=len(n)
    for i in n:
        sum+=int(i)
    for i in n:
        mul*=int(i)
    reversed=n[::-1]
    for i in n:
        if int(i)%2==0:
            even_c+=1
        else:
            odd_c+=1
    if n==n[::-1]:
        palindrome=True
    else:
        palindrome=False
    for i in n:
        cube+=int(i)**3
    if n==cube:
        armstrong
    else:
        armstrong=False
    print("count of the digit is : ",count)
    print("sum of digits :",mul)
    print("Reverse of number",reversed)
    print("Even count of digits ",even_c)
    print("Odd count of digits ",odd_c)
    print("Palindrome or not",palindrome)
    print("Armstrong or not",armstrong)
"""
m=int(input("enter the number how much you want to enter for process"))
suml=0
mul=1
cube=0
even_c=0
odd_c=0
for i in range(1,m+1):
    n=input("enter the number now for process")
    temp=n
    count=len(n)
    for i in n:
        suml+=int(i)
    for i in n:
        mul*=int(i)
    reverse=n[::-1]
    for i in n:
        if int(i)%2==0:
            even_c+=1
        else:
            odd_c+=1
    print("count of the digit is : ",count)
    print("sum of digits :",suml)
    print("product of digits :",mul)
    print("Reverse of number",reverse)
    print("Even count of digits ",even_c)
    print("Odd count of digits ",odd_c)
    if n==n[::-1]:
        print(n,"is palindrome")
    else:
        print(n,"is not palindrome")
    for i in n:
        cube+=int(i)**3
    if int(n)==cube:
        print(n,"is armstrong")
    else:
        print(n,"is not armstrong")


