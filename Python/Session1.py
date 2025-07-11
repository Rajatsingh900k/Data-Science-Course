#Print funtion is an inbuilt python function that is used to print the output to the console.
print("Hello World")  # This will print "Hello World" to the console.
# The print function can also take multiple arguments, which will be printed with a space in between.
print("Hello", "World")  # This will print "Hello World" to the console.
# You can also use the print function to print variables.
name = "Rajat"
age = 23
print("My name is", name, "and I am", age, "years old")  # This will print "My name is Rajat and I am 23 years old" to the console.
# You can also use the print function to print formatted strings using f-strings.   
print(f"My name is {name} and I am {age} years old")  # This will print "My name is Rajat and I am 23 years old" to the console.
# You can also use the print function to print formatted strings using the format method.
print("My name is {} and I am {} years old".format(name, age))  # This will print "My name is Rajat and I am 23 years old" to the console.
# You can also use the print function to print formatted strings using the % operator.
print("My name is %s and I am %d years old" % (name, age))  # This will print "My name is Rajat and I am 23 years old" to the console.
# You can also use the print function to print a string with a specific separator.
print("Hello", "World", sep=", ")  # This will print "Hello, World" to the console.
# You can also use the print function to print a string with a specific end character.
print("Hello", end="!")  # This will print "Hello!" to the console without a newline at the end.
# You can also use the print function to print a string with a specific file.
with open("output.txt", "w") as f:
    print("Hello World", file=f)  # This will write "Hello World" to the file output.txt.
# You can also use the print function to print a string with a specific flush option.
print("Hello World", flush=True)  # This will print "Hello World" to the console and flush the output buffer.
# You can also use the print function to print a string with a specific width.
print("Hello World", width=20)  # This will print "Hello World" with a width of 20 characters, padding with spaces.
# You can also use the print function to print a string with a specific alignment.
print("Hello World".center(20))  # This will print "   Hello World    " with a total width of 20 characters, centered.
# You can also use the print function to print a string with a specific fill character.
print("Hello World".ljust(20, '-'))  # This will print "Hello World--------" with a total width of 20 characters, left-aligned and filled with '-'.
# You can also use the print function to print a string with a specific precision.
print(f"{3.14159:.2f}")  # This will print "3.14" with a precision of 2 decimal places.
# You can also use the print function to print a string with a specific format.
print("{:.2f}".format(3.14159))  # This will print "3.14" with a precision of 2 decimal places.
# You can also use the print function to print a string with a specific type.
print("{:d}".format(42))  # This will print "42" as an integer.
# You can also use the print function to print a string with a specific type using f-strings.
print(f"{42:d}")  # This will print "42" as an integer.
# You can also use the print function to print a string with a specific type using the % operator.
print("%d" % 42)  # This will print "42" as an integer.
# You can also use the print function to print a string with a specific type using the str() function.
print(str(42))  # This will print "42" as a string.
# You can also use the print function to print a string with a specific type using the repr() function.
print(repr(42))  # This will print "42" as a string representation of the integer.
# You can also use the print function to print a string with a specific type using the ascii() function.
print(ascii(42))  # This will print "42" as an ASCII representation of the integer.
# You can also use the print function to print a string with a specific type using the format() function.
print(format(42, 'd'))  # This will print "42" as an integer.
# You can also use the print function to print a string with a specific type using the format() function with a specific type.
print(format(42, 's'))  # This will print "42" as a string.
# You can also use the print function to print a string with a specific type using the format() function with a specific type and precision.
print(format(3.14159, '.2f'))  # This will print "3.14" with a precision of 2 decimal places.
# You can also use the print function to print a string with a specific type using the format() function with a specific type and width.
print(format(42, '5d'))  # This will print "   42" with a width of 5 characters, right-aligned.
# You can also use the print function to print a string with a specific type using the format() function with a specific type, width, and fill character.
print(format(42, '05d'))  # This will print "00042" with a width of 5 characters, right-aligned and filled with '0'.
# You can also use the print function to print a string with a specific type using the format() function with a specific type, width, fill character, and alignment.
print(format(42, '<5d'))  # This will print "42   " with a width of 5 characters, left-aligned.
# You can also use the print function to print a string with a specific type using the format() function with a specific type, width, fill character, alignment, and precision.
print(format(3.14159, '<10.2f'))  # This will print "3.14      " with a width of 10 characters, left-aligned and with a precision of 2 decimal places.
# You can also use the print function to print a string with a specific type using the format function with a specific type, width, fill character, alignment, precision, and type.
print(format(3.14159, '<10.2f'))  # This will print "3.14      " with a width of 10 characters, left-aligned and with a precision of 2 decimal places.
# You can also use the print function to print a string with a specific type using the format function with a specific type, width, fill character, alignment, precision, type, and locale.

# Data Types in Python
# Python has several built-in data types, including:
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range
# 3. Text Type: str
# 4. Mapping Type: dict
# 5. Set Types: set, frozenset
# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview
# 8. None Type: NoneType
# Each data type has its own characteristics and methods that can be used to manipulate the data.
# For example, you can use the len() function to get the length of a sequence type
# or the type() function to get the type of a variable.
# You can also use the isinstance() function to check if a variable is of a specific type
# or the issubclass() function to check if a class is a subclass of another class.
# Additionally, you can use the built-in functions like int(), float(), str(), list(),
# tuple(), dict(), set(), and frozenset() to convert between different data types.
# Python also supports type hinting, which allows you to specify the expected data type of a variable or function parameter.
# This can help with code readability and can be used by static type checkers to catch potential type errors before runtime.
# Type hinting can be done using the typing module, which provides various type hints like List, Dict, Tuple, etc.
# For example, you can use List[int] to indicate that a variable is expected to be a list of integers,
# or Dict[str, int] to indicate that a variable is expected to be a dictionary with string keys and integer values.

#int
print(2) # This will print 2 as an integer.
#float or decimal
print(2.5) # This will print 2.5 as a float.
#complex
print(2 + 3j) # This will print (2+3j) as a complex number.
#list
print([1, 2, 3])  # This will print [1, 2, 3] as a list.
#tuple
print((1, 2, 3))  # This will print (1, 2, 3) as a tuple.
#boolean
print(True)  # This will print True as a boolean.
print(False)  # This will print False as a boolean.
#string or text
print("Hello World")  # This will print "Hello World" as a string.
#dict or mapping
print({"name": "Rajat", "age": 23})  # This will print {"name": "Rajat", "age": 23} as a dictionary.
#set or distinct collection
print({1, 2, 3})  # This will print {1, 2, 3} as a set.
#list or array
print([1, 2, 3])  # This will print [1, 2, 3] as a list.
#difference between list and tuple
# A list is mutable, meaning you can change its elements, while a tuple is immutable, 
# meaning you cannot change its elements after creation.
# For example:
my_list = [1, 2, 3]
my_list[0] = 4  # This will change the first element of the list
print(my_list)  # This will print [4, 2, 3]
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This will raise a TypeError because tuples are immutable
print(my_tuple)  # This will print (1, 2, 3)
# The main difference between a list and a tuple is that a list is mutable (can be changed) while a tuple is immutable (cannot be changed).
# You can also use the type() function to check the type of a variable. 