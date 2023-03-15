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
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


tri_recursion(3)


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
