#!/usr/bin/env python3

a = int(input("Enter a number less than 25 : "))
if a<25:
    while a<=25:
        print("Inside the loop,my variable is",a)
        a +=1
else:
    print("Error")
    