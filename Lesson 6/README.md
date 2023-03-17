Module:
------
- A set of methods/functions ready to be used somewhere else
-------------------

To create one:
-------------
1. New file with extension .py
2. Type whatever function or variable you need
---------------

To use one:
-----------
1. Type import + name of the file you created (somewhere in the first lines)
2. For func - type name of the module. and func name (example: mymodule.greeting("Jhon"))
3. For variable - name of the module. and name of the variable.. (example: a = nymodule.person1["age"])
----------------

Rename the module:
-------------------
1. Add "as" and name in the line with the import (example: import mymodule as mm)
2. You ca use it everywhere in the file as mm
-----------------------

Check what modules you have:
------------------------------
1. With help('modules')
----------------------------------------

Check what func or variable have in the module:
--------------------------------------------------
1. With dir() (example: print(dir(mymodule))
-----------------------------------------------------

Import something from the module without everything in it:
----------------------------------------------------------------
1. Add from name of the module import name of the variable of function
---------------------------------------------------------------------------------

Some funcutions/methods:
-----------------------
- round() - rounds the number up
- abs() - always returns positive number
- math.ceil() - returns round ceil number
- math.floor() - returns round flor number
- math.sqrt() - returns the square root of x
- math.sin() - returns the sine of x radians
- math.degrees() - onverts angle x from radians to degrees
- math.pi - the mathematical constant π = 3.141592…
--------------------------------------------


If statement:
---------------------
- If – used to determine whether a block will be used or not
- elif (else if) – used after if, to give a second (or more) condition/s that the code can pass through
- else - used after the last "elif" or after "if" (if there is no elif), because if none of the conditions is true - to execute this
- they can be writen shorter 
- Nested ifs - if in the if (if the main if is not true then the second even is not checked)
- pass - you can type it in the if (cannot be empty) for future code
--------------------------------------------


Exercises:
----------
- Exercise 1 - Discount:
   - A house is selling for 1 million dollars
   - If buyer has good credit - 20% discount
   - If not - 10% discount
   - Print the result
   
- Exercise 2 - Username length:
  - If the username is less than 3 - print "Name must be at least 3 characters"
  - If the username is more than 50 - print "Name must be maximum of 50 characters"
  - Otherwise - print "Name looks good!"
  
- Exercise 3 - Weight convertor:
  - You need to get user input for weight
  - After that ask for L - lbs and K - kg (not case-sensitive)
  - Print the result after conversion
