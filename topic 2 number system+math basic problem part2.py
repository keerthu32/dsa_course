"""
Example 1 Check if a number is Prime
input -> 2 Output -> prime

Concept
the prime number is which only divide by 1 and itself only

plan
--------------------------------------
--> take input from user
--> input = single integer : output = string
--> check the given number is less than or equal to 1 if yes its not prime
--> then move to next checking check the number if the number is divisble by its sequence number
--> **we shouldnot want go all number  we just move only till square root of the number
itself**
--> then its not prime break and return the answer
--> here i used specail im assign the number is prime if my assumtion wrong i said
false and conclude its not prime
--> covert to code
n=int(input("enter the number"))
prime=True
if n<2:
    prime=False
else:
    for i in range(2,int(n**2)+1):
        if n%2==0:
            prime False
            break
if prime:
    print(n,"is prime")
else:
    print(n,"not prime")
"""
n=int(input("enter the number"))
prime=True
if n<2:
    prime=False
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
if prime:
    print(n,"is prime")
else:
    print(n,"not prime")
"""
Core Example 2: Find GCD (Greatest Common Divisor)

input = a,b=18,12 Output = single integer

Concept
we have to take two number by using euclidean method if the number b divide a with
remainder than gcd(a,b)=gcd(b,r) :: gcd(a,b)=gcd
(b,a%b)

Plan
-------------------------------------------------
--> Take two number us input
--> we have to continue untill b becomes zero
--> apply the concept a,b=b,a%b
--> get gcd as a
--> convert to code
a=int(input("enter the number a : "))
b=int(input("enter the number b : "))
while b!=0:
    a,b=b,a%b
print("Gcd is : ",a)
"""

a=int(input("enter the number a : "))
b=int(input("enter the number b : "))
while b!=0:
    a,b=b,a%b
print("Gcd is : ",a)

"""
Core Example 3: LCM using GCD
input : two integers Output : single integer which is least common multiple

Concept
we have to take two number with gcd(a,b) we find the lcm by multiply a and b then
divide them by gcd of a,b we get answer

plan
------------------------------
--> take two number
--> find gcd using euclidean method
--> multiply a*b then divide them with gcd(a,b)
--> convert to code
a=int(input("enter the number a : "))
b=int(input("enter the number b : "))
lcma=a
lcmb=b
while b!=0:
    a,b=b,a%b
print("Gcd is : ",a)
print("Lcm is : ",((lcma*lcmb)//a))
"""
a=int(input("enter the number a : "))
b=int(input("enter the number b : "))
lcma=a
lcmb=b
while b!=0:
    a,b=b,a%b
print("Gcd is : ",a)
print("Lcm is : ",((lcma*lcmb)//a))

"""
LCM and GCD for more than two nubers

Concept
We have to compare two number then  find gcd then we take the answer of two with next
number then take gcd of it  this process will continue untill comparing all numbers

Plan
-------------------------------------------------------
--> take an input from user in list
--> then take the first two number from the list find gcd with the result it do the
same process with next element to find gcd
--> we find lcm using gcd just take a and b multiply by them then divide with gcd
--> then take each two number find gcd then find lcm repeat the same process
--> convert to code
lst=[]
num=int(input("enter the number you want to add to list")
for i in range(n):
    lst.append(i)
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
first=lst[0]
length=len(lst)
for i in range(length):
    first=gcd(first,lst[i])
print(first)
firstl=lst[0]
length=len(lst)
for i in range(length):
    firstl=lcm(firstl,lst[i])
print(firstl)
"""
lst=[]
num=int(input("enter the number how many number you want to add to list"))
for i in range(num):
    m=int(input("enter the number"))
    lst.append(m)
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
first=lst[0]
length=len(lst)
for i in range(length):
    first=gcd(first,lst[i])
print("Gcd of the list",first)
firstl=lst[0]
length=len(lst)
for i in range(length):
    firstl=lcm(firstl,lst[i])
print("lcm of the list",firstl)

"""
Core Example 4: Count number of digits without loop 

Hint
use string

plan
------------------------------------------------------
--> take input from user
--> using builtin function len()

convert to code
n=input("enter the number to count the number")
length=len(n)
print(length)
"""
n=input("enter the number to count the number")
length=len(n)
print("the count of the number is ",length)

"""
Task 1: Count the number of 0s in a number (like in 104050)

plan
--------------------------------------------------------
--> take input from user
--> just take loop in the given input
--> convert each digit into int then check if the digit ==0
if yes count how many
--> convert to code
n=input("enter the number will count its 0s")
count=0
for digit in n:
    if int(digit)==0:
        count+=1
print(count)
"""
n=input("enter the number will count its 0s")
count=0
for digit in n:
    if int(digit)==0:
        count+=1
print("the count of 0's is ",count)

lst=[]
num=int(input("enter the number how many number you want to add to list for chcking prime"))
for i in range(num):
    m=int(input("enter the number"))
    lst.append(m)

for num in lst:
    prime=True
    if num<2:
        prime=False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                prime=False
                break
    if prime:
        print(num,"is prime")
    else:
        print(num,"not prime")

"""
 Check whether a number is perfect square
 
Concept
the number is equal to sqaure of it square root
4 -> sqrt(4) -> 2    : 2*2==4 hence this is square root

input : 4
output : perfect square

plan
----------------------------------------------------------------------
--> take input from user in single digit
--> take sqrt of the input
--> square the sqrt input if square of sqrt(input)==input is perfect sqaure else not
--> if number is less than 0 then cannot be perfect square
--> convert to code
n=int(input("enter the input"))
if n<0:
    print("negative number cannot be a perfect square")
else:
    sqrtn=n**0.5
    if sqrtn*sqrtn==n:
        print("perfect square")
    else:
        print("not perfect square")

"""
n=int(input("enter the input to know whether is perfect square "))
if n<0:
    print("negative number cannot be a perfect square")
else:
    sqrtn=int(n**0.5)
    if sqrtn*sqrtn==n:
        print("perfect square")
    else:
        print("not perfect square")

"""
Task Find sum of digits until a single digit remains
Example: 9875 → 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

plan
-------------------------------------------------------
--> take input from user as string
--> then check its length if it not equal to 1 continue futher process
--> use for loop in the input to get single element
--> convert each element to integer add and store the element into a
--> Then assign the again to result as string to check the length and go to further
untill the length of result get single
convert to code
result =input("enter the number to sum of digits untill a single digit remains")
if len(result)!= 1:
    a=0
    for i in result:
        a+=int(i)
    result=str(a)
print("the sum of digits untill the single digit remains",result)
"""
result =input("enter the number to sum of digits untill a single digit remains ")
while len(result)>1:
    a=0
    for i in result:
        a+=int(i)
    result=str(a)
print("the sum of digits untill the single digit remains",result)

"""

Advanced Example 1: Sieve of Eratosthenes (All primes ≤ N)

Concept

The Sieve of Eratosthenes is an algorithm that:
Efficiently finds all prime numbers ≤ n
Works by marking multiples of each prime as non-prime
Leaves only the prime numbers unmarked        

plan
------------------------------------------------------------
--> Take input from user
--> assume the all number as prime number in the sequence are prime
--> prime[0]=prime[1]=False
--> for loop start from 2 to given
--> consider 2 as prime now get that number into another loop to make its multiple
number cannot be prime hence put false
--> if the number is still true take that number as output
--> convert to code
n=int(input("enter the number which number are the prime number using sieve method"))
prime=[True]*n+1
prime[0]=prime[1]=False
for i in range(2,int(n**0.5)+1):
    if prime[i]:
        for j in range(i*i,n+1,2):
            if prime[j]=False
for i in range(n):
    if prime[i]:
        print(i,end="")
"""
n=int(input("enter the number which number are the prime number using sieve method "))
prime=[True]*(n+1)
prime[0]=prime[1]=False
for i in range(2,int(n**0.5)+1):
    if prime[i]:
        for j in range(i*i,n+1,2):
            prime[j]=False
for i in range(n):
    if prime[i]:
        print(i,end=" ")
        
