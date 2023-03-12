# Lists - Used to store multiple items in a single variable
# They are ordered, changeable, and allow duplicate values
list1 = ["Hello", "My", "name", "is"]

list1[1] = "again"
print(list1)

for item in list1:
    print(item)

# Indexing - 0 1 2 3..
names = ["Gosho", "Ivan", "Maria", "Stanislav", "Todor"]
print(names[2:4])

#  ex 1 - Find the largest number
numbers_list = [5, 10, 9, 1, 26, -3, 20]
number = numbers_list[0]

for x in numbers_list:
    if x > number:
        number = x
print(number)

# 2D List - Lists in list, just like matrix
matrix = [
    [1, 3, 4],
    [3, 9, 2],
    [8, 6, 7]
]

# Printing values one by one
for row in matrix:
    for col in row:
        print(col)

print(matrix[2][1:])  # Indexing is the same but with two [outer list][inner list]

# Methods for lists:
numbers_list = [5, 10, 9, 1, 26, -3, 20]
print(numbers_list)

numbers_list.append(2)  # Adds an element at the end of the list

numbers_list.insert(0, 69)  # Adds an element at the specified position (index, new element)

copy_list = numbers_list.copy()  # Returns a copy of the list
print(copy_list)

numbers_list.remove(26)  # Removes the first item with the specified value

numbers_list.clear()  # Removes all the elements from the list

numbers_list.pop()  # Removes the element at the specified position (if not specified - removes the last element)

print(numbers_list.index(26))  # Returns the index of the first element with the specified value
# (error when value is not found in the list)

print(numbers_list.count(26))  # Returns the number of elements with the specified value

numbers_list.sort()  # Sorts the list

numbers_list.reverse()  # Reverses the order of the list

names = ("Loki", "Toki")
numbers_list.extend(names)  # Add the elements of a list (or any iterable), to the end of the current list

# ex 2 - Remove duplicates from list
numbers_list2 = [3, 4, 3, 4, 5, 6]
duplicates = []

for item in numbers_list2:
    if item not in duplicates:
        duplicates.append(item)

print(duplicates)

# Tuples - Used to store multiple items in a single variable
# Ordered, unchangeable, and allow duplicate values
tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple1)

# You can create tuple with one item
tuple2 = ("apple",)
print(type(tuple2))

# NOT a tuple
tuple2 = ("apple")
print(type(tuple2))

# Unpacking - Extract the values back into variables
fruits = ("apple", "banana", "cherry")

green, yellow, red = fruits  # The number of variables must match the number of values
print(green, yellow, red)

(a, *b, c) = fruits  # Gets rest of the values if variables and values does not match
print(a, b, c)
