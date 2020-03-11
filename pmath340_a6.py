#!/usr/bin/python3
import math
s = int(input("Input to check if sum of squares:"))
x = math.sqrt(s)
x = math.floor(x)
for i in range(2,x):
    for j in range(2,x):
        if i*i + j*j == s :
            print(i)
            print(j)
        
