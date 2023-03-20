import numpy  # For the arrays

# Exceptions - When the event occurs during program execution, it disrupts the normal flow of instructions
# When an error occurs - Will normally stop and generate an error message

# try - Lets you test a block of code for errors
try:
    user_input = int(input("Number: "))
    print(user_input)
# except - Lets you handle the error (you can have many excepts)
except ValueError:
    print("Please Type a Number!")
# else - Lets you execute this code when there is no error
else:
    print("Nothing went wrong.")
# finally - Lets you execute code, regardless of the result
finally:
    print("Finished.")

x = -1

if x < 0:
    # raise - Used to raise an exception
    raise Exception("Sorry, no numbers below zero")


# Array - Used to store multiple elements (but not of the same types) in a single variable
x = numpy.array([1, 10, 5, 8])
print(x * 2)

"""
Similarities between list and array:
- Sorting Data
- Mutable
- Indexing
- Slicing Operations
-----------------------------------
Differences between list and array:
- List:
    - Different Datatypes
    - You can't do operations
    - Built-in
    
- Array:
    - Similar Datatypes
    - You can do operations
    - numpy needed
-----------------------------------
Advantages:
- Less memory
- Fast
- Better when using math operations
"""

