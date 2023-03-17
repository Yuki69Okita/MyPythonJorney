Function:
--------
- A block of code which only runs when it is called
- You can pass data, known as parameters, into a function
- It can return data as a result
---------
To create function:
--------
1. def func_name(): ...
2. Two empty lines before and after a function
--------
To call one:
---------
1. func_name()
	- After defining a function
------
Parameters and Arguments:
------------
- Parameter:
  - The variable listed inside the parentheses in the function definition
- Argument:
  - The value that is sent to the function when it is called
- Function must be called with the correct number of arguments
- "*"
  - If you do not know how many arguments that will be passed into your function (returns tuple)
- "**" 
  - The function will receive a dictionary of arguments
- Keyword Arguments: 
  - Sends arguments with the "key=value" syntax
- You can send any data types of argument to a function 
  - It will be treated as the same data type inside the function
-------
Statements:
---------
- return - Returns a value to the function
- pass - Avoid getting error by empty code
------
Recursion:
------
- A defined function can call itself
- Examples:
  - tri_recursion()
  - fibonacci()
--------
Pass by:
--------
- Value
  - No effect on original argument
- Reference
  - Effect on original argument
- Mixed
-------
Function Object:
-----------
- Pass by argument to another function
- Assigning a function to a variable
---------
Lambda expression:
---------------
- Anonymous function
  - Can take any number of arguments, but only one expression
- Differences between non-anonymous and anonymous function (example)
----------
Exercises:
----------

- Exercise 1 - Emojis convertor but function
	- When user input some text with emojis - convert emojis in real ones
    - Without changing anything else

- Exercise 2 - Counter
	- Make simple recursion function
