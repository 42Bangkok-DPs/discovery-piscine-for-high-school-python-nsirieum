#!/usr/bin/env python3

table = 0

while table <= 10:
    a=0
    print("Table de "+ str(table) + ":", end=' ')

    while a<= 10:
        result = a * table
        print(str(result) , end = ' ')
        a += 1
    
    print()
    table += 1