#!/usr/bin/env python3
#coding by ay abdullahi #

import random

print("spin game")
player = input("Enter your name:")
print("welcome %s, \nchoose a number betwwen 1and 20:" %player)
num = int(input("Enter number"))
spam = random.randint(1,20)
print(spam)
if num == spam:
    print("score!")
else:
    print("loose!")    
