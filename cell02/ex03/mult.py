#!/usr/bin/env python3

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
multiplication = a*b
print(int(a),str('x'),int(b),str("="), multiplication)

if multiplication < 0:
    print("The result is negative.")
elif multiplication > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")