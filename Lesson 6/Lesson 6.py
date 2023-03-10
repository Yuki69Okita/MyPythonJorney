import math  # Built-in module
import mymodule  # New module
from mymodule import person1  # New module but just import somthing from it

print(round(2.6))  # Returns round ceil number
print(abs(-2.6))  # Always returns positive number

# From math module
print(math.ceil(2.6))  # Returns round ceil number
print(math.floor(2.6))  # Returns round flor number
print(math.sqrt(2))  # Returns the square root of x
print(math.sin(2))  # Returns the sine of x radians
print(math.degrees(2))  # Converts angle x from radians to degrees
print(math.pi)  # The mathematical constant π = 3.141592…

# Function and variable from the module
mymodule.greeting("Jon")

a = mymodule.person1["age"]
print(a)

# Importing the variable from the module
print(person1)

# If statement
num1, num2 = 6, 5

if num1 == num2:  # Prints the result if it's true, otherwise it will be ignored (or it will go to the next statement)
    print("=")

if num1 < num2:  # It's not true, so it's going to the next statement
    print("True!")
elif num1 == num2:  # Not true, next (else if)
    print("It's True!")
else:  # If all statements are false, it will execute this line of code
    print("False!")

# Short version:
print("First number") if num1 > num2 else print("=") if num1 == num2 else print("Second number")

# Nested Ifs
num3, num4 = 7, 6
if num3 == num4:
    if num1 > 5:  # Even if it's true, the main is not (so it will not execute)
        print("The numbers are bigger from 5")
    print("Both numbers are equal")

# If statement can't be empty, so you can type pass (like a container for future code)
if num1 > num2:
    pass


# Some exercise
# ex 1 - Discounts
house_price = 1000000
is_credit_good = False
credit = "bad"

if is_credit_good:
    percent = house_price / 100 * 20
    credit = "good"
else:
    percent = house_price / 100 * 10

house_price -= percent
print(f"The house is selling for {house_price} dollars (with discount {percent}) because your credit was {credit}.")

# ex 1 - But better (I guess)
house_price = 1000000
is_credit_good = False
credit = "bad"

percent = house_price / 100 * 10
if is_credit_good:
    percent = house_price / 100 * 20
    credit = "good"

house_price -= percent
print(f"The house is selling for {house_price} dollars (with discount {percent}) because your credit was {credit}.")


# ex 2 - Username length
username = input("Username: ")
username_length = len(username)

if username_length < 3:
    print("Name must be at least 3 characters")
elif username_length > 50:
    print("Name must be maximum of 50 characters")
else:
    print("Name looks good!")


# ex 3 - Weight convertor
weight = float(input("Weight: "))
unit = input("Type (L)bs or (K)g ").lower()

if unit == "l":
    kg = weight / 0.45
    print(f"You are {math.floor(kg)} pounds.")
elif unit == "k":
    lbs = weight * 0.45
    print(f"You are {math.floor(lbs)} kilos.")
else:
    print("Please type l for lbs or k for kg.")
