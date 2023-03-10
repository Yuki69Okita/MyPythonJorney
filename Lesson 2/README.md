Variable
--------
- A container for storing data values
- The name can contain the characters “A-z”, “0-9” and “_”
- The name must not start with a number
- The name should be as short and descriptive as possible
- A value can be written to several variables at the same time
----------------------------------------


Built-in data types
-------------------
1. Numbers:
    - int 
      - Signed integers
    - float
      - Floating point number
    - complex 
      - Consists of an ordered pair of real floating point numbers denoted by “x + yj” 
      - Where “x” and “y” are the real numbers and “j” is the imaginary unit

2. Text:
    - string 
      - a set of characters presented in pairs of single or double quotes (maybe triple if quoting something)

3. Boolean:
    - bool 
        - Whether the value is False or True

4. Lists:
    - list
        - Contain elements (even of different types) separated by “,” and enclosed in “[]”
        - Elements and size of lists can be changed
    - tuple
      - A sequence data type that is similar to the list
      - Consists of a number of values separated by “,” and enclosed in “()”
      - Elements and size of tuples cannot be updated (i.e. tuples is like a read-only sheet)
    - range()
      - Returns a sequence of numbers starting at 0 by default and incrementing by 1 (default) and stopping before a specified number

5. Mapping:
    - dictionaries
      - Storing data values in "key":"value" pairs
      - It is a type of collection that is ordered, mutable, and does not allow duplicates

6. Set:
    - set
      - An unordered data collection type that is immutable (except that you can remove and add elements), has no duplicate elements, and has no indexes
    - frozenset
      - Same as set, but cannot be added to or removed from

7. Bytes:
    - byte
      - Immutable sequences of single bytes
    - bytearray
      -  Mutable analog of byte objects
    - memoryview()
      -  Allows direct read and write access to an object's byte-oriented data without having to copy it first

8. None Type:
    - None
      - Indicates that an object has no value/has a value of “None”
