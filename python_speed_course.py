# DATA TYPES
# Integers - Whole negative and positive numbers
# Floats - Negative and Positive decimal numbers
# Strings - series of chars wrapped around '' or ""
# Boolean - True (1) or False (0)

# _____________________________________________________________________________________________________________________________

# OUTPUT & PRINTING
print('Hello World!')
print(5.0)
print(5.0, "Hello World!")
print(5.0, "Hello World!", 5, True)
print('Hello World!', end='\n')
print()

# _____________________________________________________________________________________________________________________________

# VARIABLES & INPUTS
name = input('Hey Beautiful! Enter your name here: ')
print('Hi', name, '!')
print()

# _____________________________________________________________________________________________________________________________

# ARITHMETIC OPERATIONS
x = 5
y = 10

value_1 = x + y
value_2 = x - y
value_3 = x * y
value_4 = x ** y # 5^10
value_5 = x / y
value_6 = x // y # removes the decimal values - in 0.5, it removes the .5 and keeps the 0
value_7 = x % y # returns the remainder after division

print(value_1)
print(value_2)
print(value_3)
print(value_4)
print(value_5)
print(value_6)
print(value_7)
print(y - 2)
print( (x + y) * 2 )
print()

num = input("Enter num: ")
# print(num - 2)
# the num variable is treated as a string so to perform a calculation, you have to convert it to an int or float
print(int(num) - 2)
print(float(num) - 2)
print()

intNum = int(input("Enter int num: "))
print(intNum - 2)
print()

floatNum = float(input("Enter float num: "))
print(floatNum - 2)
print()

# _____________________________________________________________________________________________________________________________

# STRING METHODS
# class.xyz CALLED METHODS
# xyz() CALLED IN-BUILT FUNCTIONS

greeting = "Hey!"
print(type(greeting))
print(greeting.upper())
print(greeting.lower())
print(greeting.capitalize())

print(len(greeting))
print(greeting.count('h'))
print(greeting.lower().count('h'))
print(greeting.lower().count('H'))
print()

x = "Hey!"
y = 3
z = "Yes!"
print(x * y)
print(x + z)
print()

# _____________________________________________________________________________________________________________________________

# CONDITIONAL OPERATORS

x = "hey"
y = "hey"
z = "heyy"
print(x == y)
print(x == z)
print()

print('a' > 'Z')
print(ord('a'))
print(ord('Z'))
print()

print(2 > 3)
print(2 >= 2)
print(2 < 3)
print(2 <= 2)
print(2 == 2)
print(2 != 2)
print()

# _____________________________________________________________________________________________________________________________

# CONDITIONALS

x = 5
y = 8
z = 11

value_1 = x == y # false
value_2 = y > x  # true
value_3 = z + 1 > x + 5  # true

print(value_1)
print(value_2)
print(value_3)

value_4 = value_1 or value_2  # this equals to true if one of the two values is true
value_5 = value_1 and value_2 # this equals to true if only both values are true
value_6 = not value_2         # flips the actual value 

print(value_4)
print(value_5)
print(value_6)
print()

# _____________________________________________________________________________________________________________________________

# IF / ELSE IF / ELSE

name = input("Enter name: ")

if (name == "shruthi"):
    print("oh hey lovely!")
    print()

elif (name == "vaibhav"):
    print("oh hey monkey boy")
    print()

elif (name == "latha" or name == "srinivas"):
    print("oh hi beautiful people")
    print()

else:
    print("oh its you ", name)
    print()

# _____________________________________________________________________________________________________________________________

# LISTS AND TUPLES
# len(), .append(), .extend([]), .pop()

x = [4, True, "hey"]  # unordered lists [1,2,3] you can modify them AND tuples (1,2,3) cannont be modified as they are immutable
y = "beautiful"

print(x)
print(y)

x_length = len(x)
y_length = len(y)
print(x_length)
print(y_length)

x.append("apples")
print(x)

x.extend(['oranges', 'banannas', 'strawberries'])
print(x)

x.pop()  # removes the last element from the list, then prints the list 
print(x)

x.pop(0) # removes the 0th element from the list
print(x)

x.pop(2)
print(x)

zeroth = x[0]
first = x[1]
second = x[2]
third = x[3]
print(zeroth, first, second, third)

print()

# _____________________________________________________________________________________________________________________________

# FOR LOOPS 
# start, stop, step

# stop
for i in range(10):  # stop @ 10
    print(i)

print()
    
# start, stop
for i in range(5,10):  # start @ 5, stop @ 10
    print(i)

print()

# start, stop, step
for i in range(5, 20, 5):  # start @ 5, stop @ 20, step by 5
    print(i)

print()

# start @ 10, stop @ -1, step by -1
for i in range(10, -1, -1):
    print(i)
print()

for i in [121, 422, 499, 892]:
    print(i)
print()

input = [1, 22, 333, 4444, 55555]
for i in range(len(input)):
    print(input[i])
print()

for i, element in enumerate(input):  # printing both elements in the array AND its indexes using enumerate
    print(i, element)
print()

# _____________________________________________________________________________________________________________________________

# WHILE LOOPS
# while condition is true, do the following

counter = 0

while counter < 10: 
    counter = counter + 1
    print(counter)












