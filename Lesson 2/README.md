Variable
--------
- A container for storing data values.
- The name can contain the characters “A-z”, “0-9” and “_”.
- The name must not start with a number.
- The name should be as short and descriptive as possible.
- A value can be written to several variables at the same time.
---------------------------------------


Built-in data types
-------------------
- Numbers:
  - int - signed integers
  - long - long integers, they can also be represented in octal and hexadecimal number system
  - float – floating point number
  - complex - consists of an ordered pair of real floating point numbers denoted by “x + yj” where “x” and “y” are the real numbers and “j” is the imaginary unit

- Text:
  - string - a set of characters presented in pairs of single or double quotes (maybe triple if, for example, quoting something)

- Boolean:
  - bool - whether the value is False or True

- Lists:
  - list - contain elements (even of different types) separated by “,” and enclosed in “[]”
  - tuple - a sequence data type that is similar to the list. Consists of a number of values separated by “,” and enclosed in “()”
!!!The elements and size of lists can be changed, but tuples cannot be updated. (i.e. tuples is like a read-only sheet)!!!
  - range() - returns a sequence of numbers starting at 0 by default and incrementing by 1 (default) and stopping before a specified number

- Mapping:
  - dictionaries - storing data values in key:value pairs. It is a type of collection that is ordered, mutable, and does not allow duplicates

- Set:
  - set - an unordered data collection type that is immutable (except that you can remove and add elements), has no duplicate elements, and has no indexes
  - frozenset - same as set, but cannot be added to or removed from

- Bytes:
  - byte - immutable sequences of single bytes
  - bytearray - mutable analog of byte objects
  - memoryview() - allows direct read and write access to an object's byte-oriented data without having to copy it first

- None Type:
  - none - indicates that an object has no value/has a value of “None”