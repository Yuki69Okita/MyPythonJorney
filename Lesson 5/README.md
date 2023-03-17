Operators:
---------
- Used to perform operations on variables and values:

1. Arithmeric Operators:
    - "+"	  - Addition		
    - "-"	  - Subtraction		
    - "*"	  - Multiplication	
    - "/" - 	Division		
    - "%" -	Modulus	(x % y = remainder)	
    - "**" -	Exponentiation
    - "//"  - Floor division (rounds down)

2. Assignment Operators:
    - "=" 
        -	x = 3
    - "+="  
        -  x = x + 3
    - "-="  
        -	x = x - 3	
    - "*=3"
        - x = x * 3	
    - "/="	
        - x = x / 3	
    - "%="
        - x = x % 3	
    - "//=" 
        -	x = x // 3	
    - "**="	
        - x = x ** 3	
    - "&="
        - x = x & 3	
    - "|="
        - x = x | 3	
    - "^="
        - x = x ^ 3	
    - ">>="
        - x = x >> 3	
    - "<<="
        - x = x << 3

3. Comparison Operators:
    - "=="  -	Equal
    - "!="  -	Not equal
    - ">" -	Greater than
    - "<" -	Less than	
    - ">=" -	Greater than or equal to
    - "<=" -	Less than or equal to

4. Logical Operators:
    - "and" - 	Returns True if both statements are true	
    - "or"  -	Returns True if one of the statements is true
    - "not" -	Reverse the result, returns False if the result is true

5. Identity Operators:
    - "is"  - 	Returns True if both variables are the same object
    - "is not"  -	Returns True if both variables are not the same object

6. Membership Operators:
    - "in"  - 	Returns True if a sequence with the specified value is present in the object
    - "not in"  -	Returns True if a sequence with the specified value is not present in the object

7. Bitwise Operators:
    - "&"  (AND) - Sets each bit to 1 if both bits are 1	
    - "|" (OR) -	Sets each bit to 1 if one of two bits is 1	
    - "^" (XOR) - Sets each bit to 1 if only one of two bits is 1	
    - "~" (NOT) - Inverts all the bits	
    - "<<"  (Zero fill left shift) - Shift left by pushing zeros in from the right and let the leftmost bits fall off
    - ">>"  (Signed right shift) - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
---------------------------------


Operator Precedence:
-------------------
- Describes the order in which operations are performed:

    - "()"
    - "**"
    - "+x" / "-x" / "~x"
    - "*" /  "/" /  "//" /  "%"
    - "+"  -	
    - "<<" / ">>"
    - "&"	
    - "^"
    - "|"	
    - "==" / "!=" / ">" / ">=" / "<" / "<=" / "is" / "is not" / "in" / "not in"
    - "not"	
    - "and"
    - "or"
