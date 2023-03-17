# Function - a block of code which only runs when it is called
# You can pass data, known as parameters, into a function
# It can return data as a result

# Creating a function
def my_function():
    print("Hello from a function")


# Calling a function
my_function()


# Parameter - The variable listed inside the parentheses in the function definition
# Argument - The value that is sent to the function when it is called
def hello_function(name):
    print(f"Hello {name}")


hello_function("Jon")  # Function must be called with the correct number of arguments


# * - If you do not know how many arguments that will be passed into your function (returns tuple)
def kids_names(*kids):
    print("Hello " + kids[1])


kids_names("Emil", "Toby", "Lux")


# ** - The function will receive a dictionary of arguments
def kid_info(**kid):
    print("His name is " + kid["name"])


kid_info(name="Emil", age="19")  # Keyword Arguments - Sends arguments with the key = value syntax


# Default Parameter Value
def countries(country="India"):
    print("I am from " + country)


countries("Brazil")
countries()  # If you don't pass value, it will get default (in this case India)


# You can send any data types of argument to a function - it will be treated as the same data type inside the function
def favorite_fruits(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

favorite_fruits(fruits)


# return - Stops the function and returns a value
def calculate(x):
    return 5 * x


print(calculate(3))


# pass - Avoid getting error
def pass_func():
    pass


# Recursion - A defined function can call itself
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)  # Recursion case - Where function calls itself
        print(result)
    else:
        result = 0
    return result  # Base case - Breaks the loop


tri_recursion(3)
"""
=> k = 3 => if 3 > 0 (true) => tri_recursion(3 - 1) (saved in stack) => 2
=> k = 2 => if 2 > 0 (true) => tri_recursion(2 - 1) (saved in stack) => 1
=> k = 1 => if 1 > 0 (true) => tri_recursion(1 - 1) (saved in stack) => 0
=> k = 0 => if 1 > 0 (false) => else => return result
=> (0) => 0
=> (1) => 1 + (0) => 1 + 0 => 1
=> (2) => 2 + (1) => 2 + 1 + (0) => 2 + 1 + 0 => 3
=> (3) => 3 + (2) => 3 + 2 + (1) => 3 + 2 + 1 + (0) => 3 + 2 + 1 + 0 => 6
"""


# ex1 - Emoji convertor but function
def emoji_convertor(msg):
    emoji_mapping = {
        ":)": "\U0001F60A",
        ":(": "\U00002639",
        "<3": "\U0001F970"
    }
    output = ""
    for element in msg.split(" "):
        output += emoji_mapping.get(element, element) + " "
    return output


print(emoji_convertor("Hello :("))


# ex2 - Counter
def counter(i):
    if i == 0:
        return
    else:
        print(i)
        return counter(i - 1)


counter(3)


# Fibonacci - 0, 1 (sum with previous 2 numbers) -> 1 -> 2 -> 3
def fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return fibonacci(idx - 1) + fibonacci(idx - 2)


print(fibonacci(3))
"""
=> (3)
=> (2) + (1)
=> (1) + (0) + 1
=> 1 + 0 + 1
"""


# Pass by value - No effect on original argument
def add_3(num):
    num += 3
    return num


print(add_3(5))


# Pass by reference - Effect on original argument
def update_list(lst):
    lst.append(4)
    return lst


list1 = [1, 2, 3]
list2 = update_list(list1)
print(list1)


# Mixed (by value and reference)
def add_numbers(a, b):
    return a + b


def calculate(operation, a, b):
    result = operation(a, b)
    print(result)


calculate(add_numbers, 9, 4)


# Function object
# Pass by argument to another function
def say_hello(name):
    print(f"Hello, {name}!")


def greet_name(gr_name):
    gr_name("Emil")


greet_name(say_hello)


# Assigning a function to a variable
def update_idx_0(lst):
    lst[0] = 0
    return lst


list3 = [1, 2]
list4 = update_idx_0(list3)
print(list4)


# Lambda expression (Anonymous function) - Can take any number of arguments, but only one expression
add_numbers = lambda x, y: x + y  # Not recommended
print(add_numbers(3, 4))


# Differences between non-anonymous and anonymous function
# Non-anonymous:
def sort_by_number(sort_list):
    return sort_list[0]


list5 = [(3, 'apple'), (1, 'banana'), (2, 'orange')]
list5.sort(key=sort_by_number)
print(list5)

# Anonymous:
list6 = [(3, 'apple'), (1, 'banana'), (2, 'orange')]
list6.sort(key=lambda x: x[0])
print(list6)
