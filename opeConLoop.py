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

