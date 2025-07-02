"""
 Example 1: Count number of digits in a number
 input : a number with digits
 output : single digits

 Plan
 -----------------------------------
 --> take a input from user
 --> i dont know the range where i have to stop the loop so i use while loop here
 --> i want loop inside number of each digit one by one using the modulus im lessing
 the number each digit i
 --> i use count variable having the value as zero which is use for the count the digits of number
 -->i will add the how many number im lessing with this i count how many digits are there
 --> convert-to-code
 n=int(input("enter the number"))
 count=0
 while n>0:
    count+=1
    n=n//10
print(count)
"""
n=int(input("enter the number to count their digits "))
count=0
while n>0:
    count+=1
    n=n//10
print("count of their digits is :" ,count)

"""
Example 2: Sum of digits
input : number with more digits
output : single digit addition of all digits

plan
--------------------------------------
--> take a input from user
--> it's similar to above but we have add digits of the number
--> using the modulus (%) will have the answer remainder will add the remainder to sum
--> to continue the loop and make divide the number  untill number becomes 0
--> convert to code
n=int(input("enter the number for suming their digits "))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("sum of their digits are :")
"""
n=int(input("enter the number for suming their digits "))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("sum of their digits are :",sum)

"""

Example 3: product of digits
input : number with more digits
output : single digit multiply of all digits

plan
--------------------------------------
--> take a input from user
--> it's similar to above but we have add products of the number
--> using the modulus (%) will have the answer remainder will multiply the remainder to sum
--> to continue the loop and make divide the number  untill number becomes 0
--> convert to code
n=int(input("enter the number for suming their digits "))
sum=1
while n>0:
    rem=n%10
    mul=mul*rem
    n=n//10
print("sum of their digits are :")
"""
n=int(input("enter the number for product their digits "))
mul=1
while n>0:
    rem=n%10
    mul=mul*rem
    n=n//10
print("products of their digits are :",mul)
"""
Example 4: Check Palindrome Number

Concept:
when we reverse the number,if  the number given and reversed number have same order
looks same then it is palindrome 121--> reversed 121 are palindrome
123-->321 are not palindrome
Planning idea
----------------------------------------------
-->Take input from user
-->remove each element from last using %10
-->the last will stored in the rev variable where will stored the number of digits
in reversed using rev=rev*10+last rev=0
--> enter same number but reducing last digit by//10 this will reduce the last digit
and enter to process again for 
--> convert to code
n=int(input("enter the number you want find it is palindrome or not"))
rev=0
temp=n num is assigning to temporary variable to get proper processing
while n>0:
    last=n%10
    rev=rev*10+last
    n=n//10
if temp==n:
    print("This is palindrome number",n)
else:
    print("This is not palindrome number",n)
"""
n=int(input("enter the number you want find it is palindrome or not"))
rev=0
temp=n # num is assigning to temporary variable to get proper processing
while n>0:
    last=n%10
    rev=rev*10+last
    n=n//10
if temp==rev:
    print(temp,"is palindrome number")
else:
    print(temp,"This is not palindrome number")

"""
Example 5: Count even and odd digits in a number
input : number in digits
output : single integer but two output count of even digit and odd digit

Plan
------------------------------------------
-->Take input from user
-->removing last digit using num%10
--> to do again and again to get whole digit count we use while loop with condition
n>0: to do how much digit exizt we use n=n//10
--> by this we can get count but we have condition here that if the number divisible
by 2 then it should taken to even count then if not it should to taken to odd count
-->convert-to-python
n=int(input("enter the number you want count its odd and even digits separetly"))
even_c=0 # even count store here
odd_c=0 # odd cout store here
while n>0:
    rem=n%10
    if rem%2==0:
        even_c+=1
    else:
        odd_c+=1
    n=n//10
print("number of even count from the given number",even_c)
print("number of odd count from the given number",odd_c)
"""
n=int(input("enter the number to know how many is even and odd digits it have"))
even_c=0 # even count store here
odd_c=0 # odd cout store here
while n>0:
    rem=n%10
    if rem%2==0:
        even_c+=1
    else:
        odd_c+=1
    n=n//10
print("number of even count from the given number",even_c)
print("number of odd count from the given number",odd_c)

"""
Task
Task 1: Find the reverse of a number
Input: 1234 → Output: 4321

Plan
----------------------------------
-->take input
--> use while loop
--> store reverse number in reverse variable
using rem=n%10
sum=sum*10+rem
convert-to code
n=int(input("enter the number you want find it is palindrome or not"))
rev=0
temp=n # num is assigning to temporary variable to get proper processing
while n>0:
    last=n%10
    rev=rev*10+last
    n=n//10
print(rev)
"""
n=int(input("enter the number you want reverse"))
rev=0
temp=n # num is assigning to temporary variable to get proper processing
while n>0:
    last=n%10
    rev=rev*10+last
    n=n//10
print(rev)

"""
Task 2: Find first and last digit of a number
Input: 1546 → Output: First = 1, Last = 6

--> take the input from user
--> to get last digit i use mod10
-->now to get first digit i use
while n>10:
n=n//10
dividing till last one then get first digit
-->
convert to code
n=int(input("enter the number"))
last=n%10
while n>10:
    n=n//10
first=n
print("first = ",first,"last = ",last)
"""
n=int(input("enter the number you will get its last and first digit "))
last=n%10
while n>10:
    n=n//10
first=n
print("first = ",first,"last = ",last)

"""

Task 8: Check if a number is Armstrong
(Example: 153 → 1³ + 5³ + 3³ = 153)
Input: 153 → Output: Armstrong

concept
we have take digits from a number
cube each number
add all the digits and save it in variable
if the added number == given number then it is armstrong

plan
------------------------------------------
--> take input from user
--> by using the n%10 take the last digit
--> cube it and add it summing variable which used to store the summing values
--> then repeat this processing using while loop
--> check with original number and each digits cube and summing number is equal then
it is armstrong
--> convert to code
n=int(input("enter the number you want to whether it is armstrong or not"))
sum=0
temp=n
while n>0:
    last=n%10
    sum=sum+last**3
    n=n//10
if temp==sum:
    print(temp,"is armstrong")
else:
    print(temp,"not armstrong")
"""
n=int(input("enter the number you want to whether it is armstrong or not "))
sum=0
temp=n
while n>0:
    last=n%10
    sum=sum+last**3
    n=n//10
if temp==sum:
    print(temp,"is armstrong")
else:
    print(temp,"not armstrong")
"""
 Task 5: Convert a number from Binary to decimal (basic logic)
Input: 1010 → output: 10

Concept
if you want to convert decimal to binary we have to divide by 2 take remainder alone
till the number 0 or less than 0

plan
---------------------------------------------------
--> take input from user
--> then divide and get remainder alone using %2
--> stored in binary variable as string
--> if we get remainder we get last one
--> to have same thing that position we use the remainder+binary
-->1010 it will have for the 10
convert to code
n=int(input("enter the number"))
binary-""
decimal=0
power=0
for digit in reversed(binary):
    decimal+=int(digit)+2**power
    power+=1
print(decimal)
"""
n=input("enter the number to convert to decimal")
binary=""
decimal=0
power=0
for digit in reversed(n):
    decimal+=int(digit)*2**power
    power+=1
print(decimal)
"""
 Task 6: Convert a number from decimal to binary (basic logic)
Input: 1010 → Input: 10

Concept
if you want to convert decimal to binary divide the number take its remainder is stored
in the first in first out order
we have to repeat the step untill quotient becomes zero or number becomes zero

plan
------------------------------------------------------
--> take input from user
--> use while loop because we dont know limit
--> divide the number with take a remainder convert it into string add it to the string
in first in first out
--> then we have to repeat the process untill number becomes zero here we use n//2
--> convert to code
n=int(input("enter the number to convert into binary"))
binary=""
while n>0:
    binary=str(n%2)+binary
    n=n//2
print(binary)
"""
n=int(input("enter the number to convert into binary"))
binary=""
while n>0:
    binary=str(n%2)+binary
    n=n//2
print(binary)




    


