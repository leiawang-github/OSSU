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

