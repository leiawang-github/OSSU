#-*- coding: utf-8 -*-


#conditions in python

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
	print("x is smaller than y.")
if x > y:
	print("x is greater than y.")
if x == y:
	print("x equals y.")

# we use elif to make above code faster: since now if the first or any conditions
# meet, we excute; in other words, we don't have to run into all the 
# conditions 
	
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
	print("x is smaller than y.") #if this condition is meet, then we dont excute more
elif x > y:
	print("x is greater than y.")
elif x == y:
	print("x equals y.")

#we improve the codes by use else,since now if we exclude first two conditions,
# x=y is the only option
	
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
	print("x is smaller than y.") #if this condition is meet, then we dont excute more
elif x > y:
	print("x is greater than y.")
else:
	print("x equals y.")

# here is another good example explaining how python take priority to conditions 
score = int(input("Score is: "))

if score >= 90:
	print("A")
elif score >= 80:
	print("B")
elif score >= 70:
	print("C")
elif score >= 60:
	print("D")
else:
	print("F")


#Functions in python
	
def is_odd(n):
	if n % 2 == 1:
		return True
	else:
		return False
	
# improved version:
def is_odd(n):
	return True if n % 2 ==1 else False

# even impr0ved vrsion
def is_odd(n):
	return ( n % 2)
	
n = int(input("Is this number odd?"))
if is_odd(n):
	print("Yes it is an odd number")
else:
	print("No it is not odd number")

# 判断是否是闰年

year = int(input("Please enter a year number: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	print("闰年")
else:
	print("不是闰年")


	