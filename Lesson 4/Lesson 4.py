# Problem with quotes in quotes
# It's going to be an error if there are 2 pairs of quotes with the same type in one string
#course1 = "Python for "Beginners""

# But if you switch 1 pair of quotes to other type, it will be okay
course2 = "Python for 'Beginners'"
course3 = """
This course will be
for
'...'
"""

# You can get indexes for every character in the string
course4 = "Python for Beginners"
         # 0123456789.. (indexes, they are starting from 0)
print(course4[0])

# You can take any symbol from back to front (but the number is written with a minus, etc. countdown)
print(course4[-6])

# You can get character set
print(course4[3:8])

# If you don't write a number, it takes default number
print(course4[:8])
print(course4[:])

# You can save it in variable
another = course4[3:7]
print(another)

# You can type negative and positive numbers (but some logic needed because it's not showing anything)
print(course4[1:-1])
print(course4[5:3])

first_name = "Jhon"
last_name = "Shmith"

# Concatenation string - concatenating strings end-to-end to create a new string
message = first_name + " [" + last_name + "] is a coder."
print(message)

# Formatted string
msg = f"{first_name} [{last_name}] is a coder."
print(msg)

# len() - shows how many characters there are in a string
print(len(course4))

# .upper() - it creates new string with uppercase
print(course4.upper())

# .lower() - it creates new string with lowercase
print(course4.lower())

# .find() - finding an symbol's index (case-sensitive)
print(course4.find("f"))

# replace() - it creates new string where you can replace symbols
print(course4.replace("P", "F"))

# boolean expression - true or false
print("python" in course4)
