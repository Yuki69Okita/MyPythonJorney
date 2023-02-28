# To get user's input you need to use input() function
# It can be saved in variable
# You can type some explanatory text in the brackets
# In this explanatory text, last symbol needs to be space (because the text sticks together with the input)
name = input("What is your name? ")
print("Hello", name)

# The output is always string
age = input("Your age? ")
print(type(age))

# Implicit Type Conversion (automatically converts)
value1 = 10.3
value2 = "5.5"
print(type(value1))
print(type(value2))

# Explicit Type Conversion (change by the user):
txt = "10010"
char = "4"
tup = (("Key", "No"), ("Age", 3), ("Cool", "Kinda"))

# String converting to int base 2
int1 = int(txt, 2)
print("After converting to integer base 2:")
print(int1)

# String converting to float
float1 = float(txt)
print("After converting to float:")
print(float1)

# Character converting to integer
ord1 = ord(char)
print("After converting character to integer:")
print(ord1)

# Integer converting to hexadecimal string
hex1 = hex(56)
print("After converting 56 to hexadecimal string:")
print(hex1)

# Integer converting to octal string
oct1 = oct(56)
print("After converting 56 to octal string:")
print(oct1)

# String converting to tuple
tuple1 = tuple(txt)
print("After converting string to tuple:")
print(tuple1)

# String converting to set
set1 = set(txt)
print("After converting string to set:")
print(set1)

# String converting to list
list1 = list(txt)
print("After converting string to list:")
print(list1)

# Integer converting to complex number
complex1 = complex(5, 2)
print("After converting integer to complex number:")
print(complex1)

# Integer converting to string
str1 = str(5)
print("After converting integer to string:")
print(str1)

# Tuple converting to expression dictionary
dict1 = dict(tup)
print("After converting tuple to dictionary:")
print(dict1)

# Converting ASCII value to characters
chr1 = chr(102)
print(chr1)
