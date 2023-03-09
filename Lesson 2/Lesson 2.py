# Variables are containers for values
# To name a variable is good to be short and as descriptive as possible
# May contain the characters from “A-z”, “0-9” and “_”
# The name must not start with a number
name = "Loki"
age = 20
is_studying = True

# A value can be written to several variables at the same time
a = b = c = 1
d, e, f = 1, 2, "Jhon"

# There are different built-in data types in Python:

# Numeric Types -
num1 = 20  # int
num2 = 20.5  # float
num3 = 45.j  # complex

# Text Type -
txt1 = "Hello"  # string ("..", '..' or even """ .."" for quote)

# Sequence Types -
list1 = ["apple", "banana", 1, 2.5]  # list
list2 = ("apple", "banana", 1, 2.5)  # tuple
list3 = range(6)  # range

# Mapping Type -
map1 = {
    "name": "Loki",
    "age": 36
}  # dict

# Set Types -
set1 = {"abc", 34, True, 40, "male"}  # set
set2 = frozenset({"abc", 34, True, 40, "male"})  # frozen set

# Boolean Type -
bool1 = True  # bool (True or False)

# Binary Types -
bytes1 = b"Hello"  # bytes
bytes2 = bytearray(5)  # bytearray
bytes3 = memoryview(b"Hello")  # memoryview

# None Type -
none1 = None  # NoneType
