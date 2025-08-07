# very easy questions
# Declare a variable name and assign your name to it. Print it.
# Store your age in a variable and print "I am ___ years old".
# Create a variable x = 10, y = 3.5, and print their sum.
# Take your name as input and greet the user like: Hello, <name>!
# Convert the string "123" into an integer and print it.
print("Very Easy✨")



name =  "MiniCat"
print("My name is "+name)
age = 20
print(f"I am {age} years old")
x = 10
y = 3.5
print(f"Sum Of {x} and {y} is : {x+y}")

Askname = input("Enter your name : ")
print(f"Hello, {Askname}!")
Strnum = "123"
print(f"The String '{Strnum}' converted to integer {int(Strnum)}")
# Easy
# Take two numbers as input and print their sum and product.
# Ask the user to enter age, convert it to int, and print age + 5.
# Print the data type of 10, 10.5, "hello", and True.
# Write a program that takes a float input and prints it as an integer.
# Take input from user and print if it's a number or not using .isdigit().
print("Easy✨")

a=int(input("Enter number a = "))
b=int(input("Enter number b = "))
print(f"Sum of {a} and {b} is : {a+b}")
print(f"Product of {a} and {b} is : {a*b}")

age = input("Enter Your AGE :")
convertage = int(age)
print (f"Age is converted to interger is {convertage}")
print (f"After adding 5 to the given AGE is '{convertage + 5}'")

a = 10
b = 10.5
c = "hello"
d = True
print(f"Type of {a} is {type(a)}")
print(f"Type of {b} is {type(b)}")
print(f"Type of {c} is {type(c)}")
print(f"Type of {d} is {type(d)}")

x = float(input("Enter a Float number : "))
print(f"The Float {x} is Converted to interger is {int(x)}")

u = input("Enter something: ")
if u.isdigit():
    print("It is a NUMBER")
else:
    print("It is NOT a NUMBER")
# Medium
# Create a variable that stores your full name and print the number of characters.
# Ask the user to enter a number, convert it to float, and print the square.
# Swap values of two variables and print them.
# Take an input string and print the first and last characters.
# Write a program to read an integer and convert it into a string, then print its type.
print("Medium✨")

fullname = "Chinnodaaaaaa"
print(f"The Count of the {fullname} is {len(fullname)}")

d = int(input("Enter a number : "))
e = float(d)
print(f"The number u entered is {d} that converted into {e} now Square of that number is : {e**2}")

sa = input("Enter number a : ")
sb = input("Enter number b : ")
temp = sa
sa = sb
sb = temp
print(f"The Swapping of {sa} and {sb} values is : {sa} and {sb}")

name = str(input("Enter a string value : "))
print(f"The first chara of the given string is :{name[0]} ")
print(f"The Last chara of the given string is : {name[-1]}")

num = int(input("Enter a Integer value : "))
st = str(num)
print(f"The given number is {num} that converted String is : '{st}'")
print(f"type is : {type(st)}")
# Hard
# Ask for user's name and age, then print:
# "Hello <name>, in 5 years you'll be <age+5> years old!"
# Take two string inputs, check if they can be added as numbers. If yes, add and print sum.
# Write a program to take input for marks in 3 subjects, convert to int, calculate average.
# Ask user to enter a number. Convert it to int, float, and str, and print all types.
print("Hard✨")
name1 = input("Enter a name : ")
age1 = int(input("Enter your Age : "))
print(f"Hello {name1}, in 5 years you'll be {age1 + 5} years old!")

a1 = input("Enter any a val : ")
b1 = input("Enter any b val : ")
if a1.isdigit() and b1.isdigit():
    sum = int(a1) + int(b1)
    print(f"Sum of {a1} and {b1} is : {sum}")
else:
    print("The given values are not numbers so we cant add them....")

m1 = int(input("Enter Sub1 marks : "))
m2 = int(input("Enter sub2 marks : "))
m3 = int(input("Enter sub3 marks : "))
avg2 = (m1 + m2 + m3) / 3
print(f"The AVG of given marks is : {avg2}")

r = int(input("Enter a Number : "))
print(f"The given number {r} is convrted to 3 diff Datatypes : ")
i=int(r)
s=str(r)
f=float(r)
print(f"The converted values are : {i} , '{s}' , {f}")
print(type(i),type(s),type(f))
# Very Hard
#  Write a program that:
# Takes name, birth year, and height in cm as input
# Calculates the user's age in 2025
# Converts height to meters (1m = 100cm)
# Prints output like:
# "Hi <name>! You're <age> years old and <height> meters tall."
# Build a mini calculator that:
# Takes 2 inputs (as strings), converts them to floats
# Ask the user what operation to perform: +, -, *, /
# Performs the operation and prints the result
print("Very Hard✨")
na = input("Enter your name : ")
by = int(input("Enter your birth year : "))
hcm = int(input("Enter your height : "))
curtyr = 2025
presentage = curtyr - by 
m = hcm / 100
print(f"Hi {na}! You're {presentage} years old and {m} meters tall.")

n1 = float ( input("enter 1st number : "))
n2 = float ( input("enter 2nd number : "))
e = input("Enter any operation in this list [+ , / , * , -] : ")
if (e == '+'):
    print(n1 + n2)
elif (e == '/'):
    print(n1/n2)
elif (e == '*'):
    print(n1*n2)
else:
    print(n1-n2)

