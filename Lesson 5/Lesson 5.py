x = 10
y = 7

# Arithmetic Operators
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y)  # Exponentiation
print(x // y)  # Floor division

# Assignment Operators
num = 99  # Assign
print(num)

num += 2  # x = x + ..
print(num)

num -= 2  # x = x - ..
print(num)

num *= 2  # x = x * ..
print(num)

num /= 2  # x = x / ..
print(num)
# Division is making the number float
num = int(num)

num %= 5  # x = x % ..
print(num)

num //= 2  # x = x // ..
print(num)

num **= 2  # x = x ** ..
print(num)

num &= 2  # x = x & ..
print(num)

num |= 2  # x = x | ..
print(num)

num ^= 2  # x = x ^ ..
print(num)

num >>= 2  # x = x >> ..
print(num)

num <<= 2  # x = x << ..
print(num)

# Comparison Operators
print(x == y)  # Equal
print(x != y)  # Not equal
print(x > y)  # Greater than
print(x < y)  # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to

# Logical Operators
print(x < y and 7 < 10)  # and - Returns True if both statements are true
print(x < y or 10 > 11)  # or - Returns True if one of the statements is true
print(not(x < y))  # not() - Reverse the result, returns False if the result is true

# Identity Operators
list1 = ["apple", "banana"]
list2 = ["apple", "banana"]
list3 = list1
print(list1 is list3)  # is - Returns True if both variables are the same object
print(list1 is list2)

# Membership Operators
print("banana" in list1)  # in - Returns True if a sequence with the specified value is present in the object
print("banana" not in list1)  # not in - Returns True if a sequence with the specified value is not present in the object

# Bitwise Operators
print(x & y)  # Sets each bit to 1 if both bits are 1
print(x | y)  # Sets each bit to 1 if one of two bits is 1
print(x ^ y)  # Sets each bit to 1 if only one of two bits is 1
print(~x)  # Inverts all the bits
print(x >> 2)  # Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(x << 2)  # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# Operator Precedence:
# ()
# **
# +x  -x  ~x
# *  /  //  %
# +  -
# <<  >>
# &
# ^
# |
# ==  !=  >  >=  <  <=
# not
# and
# or
print(100 + 5 * 3)
