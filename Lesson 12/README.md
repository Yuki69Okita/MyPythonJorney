Class:
--------
- "Blueprint" for creating objects
- Name needs to be with uppercase words
------------
Constructor:
------
- \_\_init__() 
  - Assign values to object properties or other operations when the object is being created
- self
  - Reference to the current instance of the class, and is used to access variables that belongs to the class
- \_\_str__()
  - Controls what should be returned when the class object is represented as a string
----------
Statement:
---------
- pass
  - Avoid getting error for empty class
---------
Inheritance:
-----------
- Allows to define a class that inherits all the methods and properties from another class
- Parent class
  - The class being inherited from
- Child class
  - The class that inherits from another class
- The child's \_\_init__() function overrides the inheritance of the parent's \_\_init__() function
  - super() or name of the parent class - Will make the child class inherit all the methods and properties from its parent