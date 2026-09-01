##Electricity Consumption Category
units = int(input("Enter electricity units: "))
if units <= 100:
    print("Low")
elif units <= 300:
    print("Moderate")
elif units <= 500:
    print("High")
else:
    print("Very High")
##Product Purchase Eligibility
age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
price = float(input("Enter product price: "))

if age >= 18 and income >= 15000 and price <= income * 0.5:
    print("Purchase Allowed")
else:
    print("Purchase Rejected")
##Integer Check
num = int(input("Enter an integer: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

print("Even" if num % 2 == 0 else "Odd")

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5)

##Login System – Maximum

username = "admin"
password = "1234"

for i in range(3):
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username and p == password:
        print("Login Successful")
        break
    else:
        print("Incorrect username/password")
else:
    print("Account Locked")
##Unique Values

numbers = [10, 20, 10, 30, 20, 40, 50, 30]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique values:", unique)

##Electricity Bill Calculation
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
elif units <= 300:
    bill = units * 5
else:
    bill = units * 7

print("Electricity Bill: ₹", bill)

##Star Pattern
for i in range(1, 6):
    print(" " * (5 - i), end="")
    print("* " * (2 * i - 1))





    
