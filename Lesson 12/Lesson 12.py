# Class - "Blueprint" for creating objects
class MyClass:  # The class name needs to be with uppercase words
    person = "JoJo"  # Attribute

    def age(self):  # Method
        return 20


# Creating object
person1 = MyClass()
print(person1.person)
print(person1.age())


class Person:
    # __init__() - Assign values to object properties or other operations when the object is being created
    # self - Reference to the current instance of the class, and is used to access variables that belongs to the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__() - Controls what should be returned when the class object is represented as a string
    def __str__(self):
        return f"Hi, I am {self.name} and I'm {self.age} years old."


x = Person("JoJo", 20)
print(x)


# pass - Avoid getting an error for empty class
class ClassName:
    pass


# Inheritance - Allows to define a class that inherits all the methods and properties from another class
# Parent class - The class being inherited from
class Mammals:
    def walk(self):
        print("walk")


# Child class - The class that inherits from another class
class Dog(Mammals):
    pass


dog1 = Dog()
dog1.walk()


class Person:
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def printname(self):
        print(self.firstname, self.lastname)


# The child's __init__() function overrides the inheritance of the parent's __init__() function
# super() or name of the parent class - Will make the child class inherit all the methods and properties from its parent
class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


x = Student("Mike", "Olsen")
x.printname()
