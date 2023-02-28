"""
For the "New project"
 - you just need to select the folder you want
   and the desired settings and modifications
"""

# Some printing
print("Hello world!")
print(123)
print("Aaaa 123" * 2)


# To see the result you need to press shift+F10
# He reads it line by line and performs them
# It is case-sensitive

# There are 3 types of comments:
# Single line - # ..
# Multi line - """..""" or '''..'''
# Docstring - (not exactly comment, it's documentation) """..""" or '''..'''

def get_name(name):
    """Reterns name

    :param name: dsad
    :return: sdadsadasd
    """
    return name


print(get_name.__doc__)
