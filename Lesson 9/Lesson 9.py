# Dictionaries - Used to store data values in key:value pairs
# They are ordered, changeable and do not allow duplicates
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# You can get item value with variable_name[key]
# If key is not in the dict - Returns Error
print(car["year"])

# get() - Returns the value of the item with the specified key
# If key is not in the dict - Returns None
print(car.get("year"))

# If you add value with non-existing key - It will return this value
print(car.get("is_good", True))

# keys() - Returns a list of all the keys in the dictionary
print(car.keys())

# values() - Returns a list of all the values in the dictionary
print(car.values())

# items() - Returns each item in a dictionary, as tuples in a list
print(car.items())

# Edit value of a key
car["year"] = 2001

# update() - Updates the dictionary with the items from the given argument
car.update({"year": 2001})

# Same with adding elements, just with new key names and their values
car["is_bad"] = False
car.update({"is_good": True})

# pop() - Removes the item with the specified key name
car.pop("year")

# popitem() - Removes the last inserted item
car.popitem()

# del - Removes what you point to it
del car["brand"]

# clear() - Clears the elements in the variable
car.clear()

# ex 1 - Mapping numbers
numbers_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
phone_number = input("Numbers: ")
output = ""

for char in phone_number:
    output += numbers_mapping.get(char, "!") + " "
print(output)

# ex 2 - Emojis convertor
emoji_mapping = {
    ":)": "\U0001F60A",
    ":(": "\U00002639",
    "<3": "\U0001F970"
}
user_input = input("> ").split(" ")
output = ""

for element in user_input:
    output += emoji_mapping.get(element, element) + " "
print(output)
