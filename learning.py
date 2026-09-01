if statement:
'''a=100
if a==10:
    print("the give number is equal to 100")
else:
    print("the given number is not equal to 100")'''
from encodings import kz1048
from operator import truediv
from typing import TypedDict

#if and elif statement
'''a=75
if a>=80:
    print("grade A")
elif a>=60:
    print("grade B")
else:
    print("grade c")'''
#else statement
'''num=5
if num>0:
    print("positive number")
else:
    print("negative number")'''
#nested if else statement
'''age=18
ID=True
if age>=18:
    if id:
        print("allwoed")
    else:
        print("not allwoed")
else:
    print("not eligbil")'''
#elif and if condition
'''num=20
if num>=0:
    print("positive number")
elif num<=0:
    print("negative number")
else:
    print("zero")'''
#for condition
'''for i in range(5,0,-1):
    print(i)'''
#for break condition
'''for i in range(5):
    if i==3:
        break
    print(i)'''
#for nested loop
'''for i in range(2):
    for j in range(3):
        print(i,j)'''
#string for loop
'''a="python"
for i in a:
    print(i)'''
#end function for loop
'''a="karthi sumi"
for i in a:
    print(i,end=" ")'''
'''for i in range(1,51,3):
    print(i)'''
#while loop incriment
'''i=1
while i<=5:
    print(i)
    i+=1'''
#while loop dcri
'''i=5
while i>=1:
    print(i)
    i-=1'''
#print 1 to 10 numbers
'''num=1
while num<=10:
    print(num)
    num+=1'''
#even number
'''k=2
while k<=20:
    print(k)
    k+=2'''
#revers
'''num=1234
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)'''
#palandrum
'''a=121
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)'''
#spy number
'''a=123
b=0
c=1
t=a
while t>0:
    d=t%10
    b=b+d
    c=c*d
    t=t//10
print(b)'''
#armstrong number
'''a=153
b=0
t=a
while t>0:
    d=t%10
    b+=d**3
    t=t//10
print(b)'''
#fibonacci
'''a=10
b=0
t=1
count=0
while count<a:
    print(b)
    c=b+t
    b=t
    t=c
    count+=1'''
#break
'''num=[10,20,30,40,50]
for i in num:
    if i==40:
        break
    print(i)'''
#conditine
'''for i in range(1,10):
    if i==5:
        continue
    else:
        print(i)'''
#pass
'''a=true
if a==true:
    print("python")
else:
    pass'''
#string
'''a="student"
print(a.capitalize())
print(a.lower())
print(a.upper())
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(len(a))
print(a.count("t"))
print(a.index("e"))
print(a.split("d"))
print(a.isascii())
print(a[5])
print(a[1:5])
print(a.center(1,"*"))'''
#slicing model
a = "sumithrakarthi"
'''print(a[0:4])
print(a[0:11])
print(a[0:14])
print(a[::-1])
print(a[:-1])
print(a[1::2])'''
#data types list[]
'''a=[10,20,30,40,50]
print(a)
print(type(a))
print(a[4])
a.append(60)
print(a)
print(a.count(40))
print(a.index(40))
a.extend([70,80,90,100])
print(a)
print(a.reverse())
print(a)
print(a.pop())
print(a)
print(a.__len__())'''
#trupes() data types
'''a=(10,20,30,40,50)
print(a.index(40))
print(a.count(40))'''
#data types set{}
'''a1={1,2,3,4,5}
a2={5,6,7,8,9,10}
print(a1.union(a2))
print(a1.difference(a2))
print(a1.symmetric_difference(a2))
print(a1.intersection(a2))'''
#disctionary
'''def student():
    data={"name":"sumithra","age":20,"branch":"AI&DS"}
    print(data)
student()'''
#list
'''name = {"sumithra"}
age = {20}
gender = {"male"}
    print(name, age, gender)'''
#dict
'''a={"name":["sumithra","sunl","subash"],
   "age":[20,19,18],
   "gender":["female","male","male"]}
print(a.get("name"))
print(a.keys())
print(a.values())
print(a.items())
a.update({"phone":9080148939})
print(a)
print(a.popitem())
print(a)
new=a.copy()
print(new)
a.clear()
print(a)'''
#pre_defined functions type(1)
'''print()
input()
range()
len()
min()
max()
help()
type()
tuple()
sum()
set()
list()'''
#user defined functions type(2)
#without argument
'''def course():
    c="python"
    print(c)
course()'''
#with argument
'''def detail(name,course):
    print("name:",name)
    print("course:",course)
detail("sumithra","python")'''
#types(1)positional arguments
'''def positional(name,course):
    print(f"i am {name} and i am learning {course}")
positional("sumithra","python")'''
#not now positional
'''def positional(name,course):
    print(f"i am {name} and i am learning {course}")
positional("sumithra","python")'''
#key wordstype(2)
'''def keywords(name,course):
    print(f"i am {name} and i am learning {course}")
keywords("sumithra","python")'''
#default argument type(3)
'''def  hello(name,course="data"):
    print(f"i am {name} and i am learning {course}")
hello("sumithra")'''
#variable or arbitrary argument
'''def demo(*num):
    total=0
    for i in num:
        total+=i
    print("total:",total)
demo(5,10)
demo(3,4,5,5)'''
#table
'''a=int(input("enter the a number:"))
for i in range(1,21):
    print(a,"x",i,"=",a*i)'''
#star
'''for i in range(1,5):
    print(" ",(5-i), "*",(2*i-1))
for j in range(4,0,-1):
    print(" ",(5-j),"*",(2*j-1))'''
