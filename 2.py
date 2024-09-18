# Task 2
# Write a Python program that asks the user to input a number and checks if it is a prime number.
# If the number is not prime, display its divisors.

num = int(input("enter number:"))

if (num % 2 == 0 or num % 3 == 0) and (num != 2 and num != 3):
    if num % 2 == 0:
        print("not a prime, can be divided by: " + "2")
    if num % 3 == 0:
        print("not a prime, can be divided by: " + "3")
else:
    print("prime")