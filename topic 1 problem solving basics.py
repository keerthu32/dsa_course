"""
Sample sums
A Basic Problem
inputs : Two integers a and b
output : their sum a+b

plan
---------------------------------------
-> get input from user a and b using int(input()) functions
-> processing with adding formula a+b stored in c
-> print their sum using print() c
---------------------------------------
so simply we use input to get input and print to print the results
"""

a=int(input("enter number a : "))
b=int(input("enter number b : "))
print("Sum : ",a+b) 
"""
2
inputs : get an integer
output : "even" or "Odd"

plan
---------------------------------------
-> get an input from user using input() as int
-> if the number is divided by with out leaving any remainder then the number is even
-> So, in computer we use % for finding remainder if any number % (divided) by two gives remainder 0 then its even else no
-> if number%2==0:
       print even
   else:
       print odd:
----------------------------------------
so convert this to python language using syntax
""" 
number=int(input("enter the number you want to know"))
if number%2==0:
    print("Even")
else:
    print("Odd")
"""
3
input : a single integer
output : it must print horizonatly from 1 to given number

plan
--------------------------------------
-> get an input  from user using input() as int
-> now we have to print from 1 to give input
-> Means 1 2 3 4 5 if n=5
then its format starting with one add with 1 +1 till given number occur then here
reapet a same thing again and again in same format
a=1
here i gave a+=1
now im giving condtion this have to done till the number i said
-> converting into logic using loop
i=1
while i>5:
    i+=1
    print (i,end= "") or simply in python we use for loop only for sequnce only
-> since we need only sequence order of number we directly use for loop like
-> for i in range(n):
         print(i,end="")
end will create space in horizontal in same line
"""
n= int(input("enter the number you want to create sequence from 1 to your number "))
""" Remember always
for loop start iteration in default starts with 0 so we have to
do on our own when we want other number we should said before and it finish before the
number we given so we should add 1 to the number in range
"""

for i in range(1,n+1):
    print(i,end=" ")


"""
input : a single integer
output : addition of their own seqeunece adding from 1 to n

 plan
 -------------------------------------
 -> iterate each number then starting from 1
 -> then store that in one variable which act as place holder then add another number to number stored
 -> we have to repeat the method untill it reaches the given number
 -> converting into python language
   variable_to_store(number iteration) =0
    for i in in (1,n):
        variable_to_store(number iteration)=variable_to_store(number iteration)+i
    print variable_to_store(number iteration)
---------------------------------------
converting into python language
"""
n=int(input("\n enter the number"))
suming=0
for i in range(1,n+1):
    suming+=i
print(suming)

"""
input : List-- Stored more data types
output : To find Largest number in the list

plan
---------------------------------------
--> take a simple list =[3,7,8,8,2,1,14,20]
-->now we have move inside the list in each one compare with before element
--> find the maximum
--> converting to python language
    for i in lst:
        maximum=lst[0]
        if i>maximum:
            maximum=1
    print(maximum)
"""
lst=[3,7,8,8,2,1,14,20]

for i in lst:
    maximum=lst[0]
    if i>maximum:
        maximum=i
print(maximum)
#------------------------------------------------------------
"""
Practice Task
Task 1: Print numbers from 1 to N
Input: 5
Output: 1 2 3 4 5

Plan
----------------------------------------
-->taking input from user
-->loop should start from 1 to the number given
-->print result one by one when generating
Convert-to-python
number=int(input("enter the number")
for i in range(1,number+1):
    print(i)
----------------------------------------
"""
number=int(input("\n enter the number "))
for i in range(1,number+1):
    print(i,end=" ")
"""
Task 2: Sum of Even Numbers from 1 to N
Input: 10
Output: 2 + 4 + 6 + 8 + 10 = 30

input : single integer
output : single integer
Plan
----------------------------------------
-->this task similar to above but we have add as cumulative
--> loop through an integer
-->check if it is divisble b 2 then add using assigning operator
-->instead of printing store the i into sum variable =0
--> add the elements using assigning operator to sum
assigning operator +=
Convert-to-Code
num=int(input("enter the number"))
for i in range(1,num+1):
    sum=sum+i
print(sum)
"""
sum=0
num=int(input("\n enter the number to add even number from you given "))
for i in range(1,num+1):
    if i%2==0:
        sum=sum+i
print(sum)
"""
Task 3: Count how many numbers are divisible by 3 between 1 to N
Input: 15
Output: 5 (3, 6, 9, 12, 15)

input : single integer
output : single integer with tuple containing output

Plan
----------------------------------------
--> take input from user
--> loop through it
--> check with condition if i%3==0:
--> enter that number to new list using append method list.append(i)
-->simantenously count the numbers which enter after the checking to list
--> we need both output both count and list of the number divisible by 3
--> but it should not be list type so change it tuple by using tuple() function
convert-to-code
number=int(input(enter the number))
count=0 ----- when you want to store as result from loop as single integer
you need to assign 0 to variable where you want to store result
lst=[]
for i in range(1,number+1):
    if i%3==0:
        lst.append(i)
        count+=1
print(count,tuple(lst))
"""
number=int(input("\n enter the number count of divisble of 3 "))
count=0
lst=[]
for i in range(1,number+1):
    if i%3==0:
        lst.append(i)
        count+=1
print(count,tuple(lst))
"""
Task 4: Find the factorial of a number
Input: 4
Output: 4 × 3 × 2 × 1 = 24
input : single integer
output : single integer

Plan
--------------------------------
-->take number from user
--> we have to loop but we dont the length because it want to move reverse before 0
-->we will use while loop
assigning condition while >0 it must run the below code till this condition satisfy
--> taking this number storing to another variable were we want to store our multiple of factorial 
--> then will do of the number given-1 then it starts reducing
-->convert- to-code
n=int(input("enter the number"))
mul=1
while n>0:
    mul=mul*n
    n=n-1
print(mul)
"""
n=int(input("\n enter the number for factorial "))
mul=1
while n>0:
    mul=mul*n
    n=n-1
print(mul)

"""
Task 5: Reverse the digits of a number
Input: 1234
Output: 4321

Plan
------------------------------------
--> input : the number with four digits
--> output : the number with four digit reverse the input
--> just take input
--> by using %10 separate last digit from a number
--> then add the last element as reverse in order by
--> rev=0 n=1234
    rev=rev*10+last element --> 0*10+4 =4 ,4*10+3=43,43*10+2=432,432*10+1=4321
--> then we have to do same thing for remaining number so we use n=n//10 
Convert-to-code
n=1234
rev=0
while>0:
    div=n%10
    rev=rev*10+div # anything multiple with 0 will give 0
    n=n//10
print(rev)
"""
n=int(input("enter the number for reversing"))
rev=0
while n>0:
    div=n%10
    rev=rev*10+div # anything multiple with 0 will give 0
    n=n//10
print(rev)
