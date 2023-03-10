import random  # For the exercise

# While loop - Execute a set of statements as long as a condition is true
i = 1

while i < 6:
    print(i)
    i += 1
print("Done")  # While in the loop it doesn't execute anything after it

while i < 6:
    print(i)
    if i == 4:
        break  # Stops the loop even if the while condition is true
    i += 1

while i < 6:
    i += 1  # If we didn't swap print(i) with i += 1, it will be infinite loop
    if i == 4:  # (because continue returns to the statement)
        continue  # Stops the current iteration, and continue with the next
    print(i)

while i < 6:
    print(i)
    i += 1
else:  # When the statement is not true
    print("i is no longer less than 6")

# Nested while loops
while i < 4:
    j = i
    while j < 4:  # The "inner loop" will be executed one time for each iteration of the "outer loop"
        print(j, i)
        j += 1
    print("")
    i += 1
print("Complete!")

# ex 1 - Guessing game
win_number = random.randint(1, 11)
num_of_tries = 0
max_tries = 3

print("Winning number is from 1 to 10.")
print("You have three guesses.")

while num_of_tries < max_tries:
    print(f"Number of guesses: {num_of_tries}")
    num_of_tries += 1
    guessed_num = int(input("Guess: "))

    if guessed_num == win_number:
        print("Congrats! You guessed it!")
        break
    elif guessed_num > win_number and num_of_tries < max_tries:
        print("Down.")
    elif guessed_num < win_number and num_of_tries < max_tries:
        print("Up.")

else:
    print("You lose! Good luck next time.")
    print(f"The winning number was: {win_number}.")

# ex 2 - Car game
command = ""
is_car_started = False

while True:

    command = input("> ").lower()

    if command == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")

    elif command == "start":
        if is_car_started:
            print("The car is already started.")
        else:
            is_car_started = True
            print("Car started.. Ready to go!")

    elif command == "stop":
        if not is_car_started:
            print("The car is already stopped.")
        else:
            is_car_started = False
            print("Car stopped.")

    elif command == "quit":
        break

    else:
        print("I don't understand.")
        print("Print help for the controls.")


# For loop - Used for iterating over a sequence
# (list, tuple, dictionary, set, string or function range(start num, finish num, step))

# List
fruits_list = ["apple", "banana", "cherry"]
for item in fruits_list:
    print(item)

# Tuple
fruits_tuple = ("apple", "banana", "cherry")
for item in fruits_tuple:
    print(item)

# Dictionary
fruits_dictionary = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red"
}

for item in fruits_dictionary:
    print(item, fruits_dictionary[item])  # It will print only the key if it's not added dict_name[key]

# Set
fruits_set = {"apple", "banana", "cherry"}
for item in fruits_set:
    print(item)

# String
for item in "fruits_string":
    print(item)

# Range
for item in range(4, 10, 2):
    print(item)

for item in range(4, 12, 2):
    if item == 10:
        break  # Stops the loop even if the while condition is true
    print(item)

for item in range(4, 12, 2):
    if item == 8:
        continue  # Stops the current iteration, and continue with the next
    print(item)

for item in range(1, 4):
    print(item)
else:  # When the loop is finished it will execute else
    print("GOOOOOOOO!")  # If there is a successful break - else will not be executed

# Nested for loops
list1 = [1, 2, 3]
list2 = [1, 2, 3]

for x in list1:
    for y in list2:  # The "inner loop" will be executed one time for each iteration of the "outer loop"
        print(x, y)
    print("")

# ex 3 - Shopping cart
items_and_prices = {
    "Berserk": 60.99,
    "Elden ring": 120.0,
    "Skull: The hero slayer": 5.59
}
final_price = 0

for item in items_and_prices:
    final_price += items_and_prices[item]

print(f"Total price: {final_price}")

# ex 3 - But better (I guess)
for item, price in items_and_prices.items():
    final_price += price

# ex 4 - Print "F" with list
numbers = [5, 2, 5, 2, 2]

for x in numbers:
    for y in range(x):
        print("x", end="")
    print("")

# ex 4 - Second way
for x in numbers:
    print("x" * x)
