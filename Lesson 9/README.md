Dictionaries:
------
- Used to store data values in key:value pairs
- They are ordered, changeable and do not allow duplicates
------------------------
How to get keys and values:
-----
- You can get item value with variable_name[key]
  - If key is not in the dict - Returns Error
- get() - Returns the value of the item with the specified key
  - If key is not in the dict - Returns None
  - If you add value with non-existing key - It will return this value
- keys() - Returns a list of all the keys in the dictionary
- values() - Returns a list of all the values in the dictionary
- items() - Returns each item in a dictionary, as tuples in a list
-----
How to edit and add values:
---
- variable_name[key] = value
- update() - Updates the dictionary with the items from the given argument
----
How to delete:
---
- pop() - Removes the item with the specified key name
- popitem() - Removes the last inserted item
- del - Removes what you point to it
- clear() - Clears the elements in the variable
---
Exercises:
----------

- Exercise 1 - Mapping numbers
	- When user type 123 - print One Two Three


- Exercise 2 - Emojis convertor
	- When user input some text with emojis - convert emojis in real ones
    - Without changing anything else
