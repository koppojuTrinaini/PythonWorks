# ✅ EASY LEVEL QUESTIONS
# Check if a number is even or odd.
# Find the largest of 3 numbers using if-else.
# Check if a number is positive, negative or zero.
# Print numbers from 1 to 10 using a for loop.
# Print the multiplication table of a number.
# Find the sum of first N natural numbers.
# Check if a year is a leap year.
# Print all even numbers from 1 to 50.
# Use break to stop loop when a number is found.
# Use continue to skip odd numbers in a loop.


num = int(input("Enter a number : "))
if (num % 2 == 0):
    print("The number is EVEN")
else:
    print("The number is ODD")

a, b, c = map(int, input("Enter 3 inputs separated by space: ").split())
print(f"A : {a} , B : {b} , C : {c}")
if ( a > b):
    if (a > c):
        print("A is big")
    else:
        print("C is big")
else:
    if(b>c):
        print("B is big")
    else:
        print("C is big")

num = float(input("Enter a number : "))
if (num > 0):
    print("It is a positive")
elif (num < 0):
    print("It is a Negative")
else:
    print("It is Zero")

for i in range(1,11):
    print(i)

t = int(input("Enter a number to genarate table for that num from 1 to 10 multiple : "))
if(t>0):
    for i in range(1, 11):
        print(f"{t} x {i} = {t * i}")

na = int(input("Enter a number : "))
sum=0
for i in range ( 1 , na+1):
    sum = sum  + i
print(f"Sum of all {na} natural numbers: {sum}")

print("check whether the year is leap year or not")
y = int(input("Enter year : "))
if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
    print(f"{y} is a Leap year")
else:
    print(f"{y} It is not a leap year")

print("Printing even numbers from 1 to 50")
for i in range(1,51):
    if (i % 2 == 0):
        print(i)   

target = int(input("Enter the number to search : "))

for i in range(1, 101):  # Example range from 1 to 100
    if i == target:
        print(f"Number {target} found! Stopping the loop.")
        break
    print(f"Checked {i}, not the number.")

for i in range(1,101):
    if (i % 2 != 0):
        continue
    print(i)

# ⚡ MEDIUM LEVEL QUESTIONS
# Count how many numbers from 1 to N are divisible by 3 or 5.
# Calculate factorial of a number using loop.
# Reverse a number using a while loop.
# Check if a number is prime.
# Check if a number is an Armstrong number.
# Find the GCD of two numbers.
# Print Fibonacci sequence up to N terms.
# Find sum of digits of a number.
# Find the maximum digit in a number.
# Check whether a character is a vowel or consonant using conditions.

print("Count how many numbers from 1 to N are divisible by 3 or 5")
n4 = int(input("Enter N value : "))
for i in range(1 , n4 + 1):
    if(i % 3 == 0 or i % 5 == 0):
        print(i)

print("Calculate factorial of a number using loop.")
n5 = int(input("Enter number : "))
tol = 1
while n5 > 0 :
    tol *= n5
    n5 -= 1
print(f"Factorial is : { tol }") 

n=int(input("Enter : "))
rev = 0
rem = 0
while (n != 0):
    rem = n % 10 
    rev = rev * 10 + rem
    n = n // 10
print(rev) 



