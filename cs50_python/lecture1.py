# print("Hello,world!")
# print("what's the problem with you?")

# Print Function in Python
name = input("what's your name? ")
print("Hello,",name)
print("Hello, "+ name)

# take multiple parameters
x = 10
y = 20
print(x + y)

#use sep to print out multiple paras, defalt value for sep is space
print("apple", "banana", "orange")
print("apple", "banana", "orange", sep=", ")

#use end to deefine what shoule be ending sign, default value is \n, but you can change
print("Hello, world", end = '!\n') 

#use file to print out to screen but you can always change it
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)

#formatting using f-string
name = "Leia"
age  = 32
print(f"Hello {name}, I believe you are {age} years old.")
print("Hello {}, I believe you are {} years old.".format(name, age))

#print out special chars
print("line 1\nLine 2") #new line
print("name\tAge") #prnt tab


#.strip() function 
name = "Leia    "
name = name.strip()
print(name)
text = "---Hello---"
print(text.strip('-'))

#.title / .capitalize
name = "  leia wang   "
name = name.strip().title()
print(name)


# print number
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)















