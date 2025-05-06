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

greeting = "Hey!"
print(type(greeting))





