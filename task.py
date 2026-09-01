# python task(1)
'''for i in range(10):
    print("data science")'''
#python task(2)
'''n = int(input("Enter number: "))
for i in range(1, n + 1):
    print(i)'''
#python task(3)
'''n = int(input("Enter number: "))
for i in range(n, 0, -1):
    print(i)'''
#python task(4)
'''n = int(input("Enter number: "))
for i in range(2, n + 1, 2):
    print(i)'''
#python task(5)
'''n=int(input("enter the number"))
for i in range(1,n+1,2):
    print(i)'''
#python task(6)
'''n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+1
    print(sum)'''
#python task(7)
'''n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)'''
#python task(8)
'''n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)'''
#pytho task(9)
'''n=int(input("enter the number:"))
count=0
for i in range(1,n+1):
    count+=1
    print(count)'''
#python task(10)
'''n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print("Reversed number =", rev)'''
#python task(11)
'''num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")'''
#python task(12)
'''a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)'''
#python task(13)
'''num = int(input("Enter a number: "))
if num % 2 == 0:
    print("positive")
else:
    print("negative")'''
#python task(14)
'''year = int(input("Enter year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")'''
#python task(15)
'''num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")'''
#python task(16)
'''marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")'''
#python task(17)
'''ch = input("Enter a character: ")
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")'''
#python task(18)
'''age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")'''
#python task(21)
'''a=100
b=0
t=1
count=0
while count<a:
    print(b)
    c=b+t
    b=t
    t=c
    count+=1'''
#python task(22)
'''a=121
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)'''
#python task(23)
'''a=153
b=0
t=a
while t>0:
    d=t%10
    b+=d**3
    t=t//10
print(b)'''
#python task(24)
'''n = int(input("Enter number: "))
for num in range(2, n + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)'''
#python task(24)
'''n = int(input("Enter number: "))
for num in range(2, n + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)'''
#python task(25)
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(gcd)'''
#python task(26)
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        print("LCM =", lcm)
        break
    lcm += 1'''
#python task(27)
'''n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
print("Sum of digits =", sum)'''
#python task(28)
'''n = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)'''
#python tak(31)
'''nums = [10, 25, 5, 40, 18]
largest = nums[0]
for i in nums:
    
    if i > largest:
        largest = i
print(largest)'''
#python task(32)
'''nums = [10, 25, 5, 40, 18]
smallest = nums[0]
for i in nums:
    if i < smallest:
        smallest = i
print("Smallest =", smallest)'''
#python task(33)
'''nums = [10, 20, 30, 40, 50]
total = 0
for i in nums:
    total += i
print("Sum =", total)'''
#python task(34)
'''nums = [10, 20, 30, 40, 50]
total = 0
for i in nums:
    total += i
average = total / len(nums)
print(average)'''
#python task(35)
'''num = [10, 15, 8, 21, 6, 9]
even = 0
odd = 0
for i in num:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)'''
#python task(36)
'''nums = [10, 25, 5, 40, 18]
nums.sort()
print("Second Largest =", nums[-2])'''
#python task spy number(37)
'''def spy():
    a=int(input("Enter first number: "))
    b=0
    c=1
    t=a
    while t>0:
        d=t%10
        b=(b*10)+d
        t=t//10
        print(b)
spy()'''
#task armstrong number
'''def arm():
    a=int(input("Enter first number: "))
    b=0
    t=a
    while t>0:
        d=t%10
        b+=d**3
        t=t//10
        print(b)
arm()'''
#fibona
'''def fia():
    a=10
    b=0
    t=1
    count=0
    while count<a:
        print(b)
        c=b+t
        b=t
        t=c
        count += 1
        print(c)
fia()'''
#with function palindrom
'''def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

word = input("Enter a word: ")
palindrome(word)'''
#spy number
'''def spy(n):
    t=n
    s=0
    p=1
    while t>0:
        d = t % 10
        s += d
        p *= d
        t //= 10

    if s == p:
        print("Spy Number")
    else:
        print("Not Spy Number")


n = int(input("Enter number: "))
spy(n)'''
#function(1)
'''def greet():
    print("Hello World")
greet()'''
#fuvction(2)
'''def welcome():
    print("Welcome to Python")
welcome()'''
#function(3)
'''def add(a,b):
    print("sum=",a + b)
add(10,20)'''
#function(4)
'''def square(sum):
    print(sum**2)
square(10)'''
#function (5)
'''def cube(sum):
    print(sum**3)
cube(10)'''
#function(6)
'''def odd_even(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
odd_even(10)'''
