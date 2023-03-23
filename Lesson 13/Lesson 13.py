import os
# File Handling - The process of creating, reading, writing, and manipulating files on a computer's file system
# open() - Takes two parameters (filename, mode)
"""
Modes:
------
"r" - Read - Default value (opens a file for reading, error if the file does not exist)
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

If the file should be handled as binary or text mode:
-----------------------------------------------------
"t" - Text (default value) - Text mode
"b" - Binary - Binary mode (e.g. images)
"""
f = open("demo.txt", "w")
# write() - Writes in the file (will overwrite the entire file)
f.write("Omg! What?")
# close() - Closes open file (always do that after you opened a file)
f.close()


f = open("demo.txt", "a")
f.write("\nOmg!")
f.close()


f = open("demo.txt", "rt")
# read() - Returns the whole text (you can specify how many characters you want to return)
print(f.read())
f.close()


f = open("demo.txt", "rt")
# readline() - Returns one line (you can specify how many characters you want to return)
# If the function is written several times – it will return each subsequent line
# If there is a number - second time will return from the symbol to the end of the line
print(f.readline(4))
print(f.readline())
f.close()


f = open("demo.txt", "rt")
for line in f:
    print(line.strip())
f.close()


# remove() - Deletes a file (os module)
# os.remove("demo.txt")


# rmdir() - Deletes an entire folder (os module)
# os.rmdir("..")
