import sys

# The following line prints a string
print("hello world!")
# The following lines prints a string with color
print("\x1b[31mhello world!\x1b[0m")
print("\x1b[32mhello world!\x1b[0m")
print("\x1b[33mhello world!\x1b[0m")
print("\x1b[34mhello world!\x1b[0m")
print("\x1b[35mhello world!\x1b[0m")
print("\x1b[36mhello world!\x1b[0m")
print("\x1b[37mhello world!\x1b[0m")
# complex print string with color and formatting
print("\x1b[31;1mHi this is a bold red string!\x1b[0m","\x1b[32;2mHi this is a dim green string!\x1b[0m","\x1b[33;3mHi this is a italicized yellow string!\x1b[0m")

# all color combinations
# Define ANSI escape codes for colors and styles
# foreground_colors = {
#     "Black": 30,
#     "Red": 31,
#     "Green": 32,
#     "Yellow": 33,
#     "Blue": 34,
#     "Magenta": 35,
#     "Cyan": 36,
#     "White": 37,
# }

# background_colors = {
#     "Black": 40,
#     "Red": 41,
#     "Green": 42,
#     "Yellow": 43,
#     "Blue": 44,
#     "Magenta": 45,
#     "Cyan": 46,
#     "White": 47,
# }

# styles = {
#     "Reset": 0,
#     "Bold": 1,
#     "Dim": 2,
#     "Italic": 3,
#     "Underline": 4,
#     "Blink": 5,
#     "Reverse": 7,
#     "Hidden": 8,
# }

# # Print all combinations
# for fg_name, fg_code in foreground_colors.items():
#     for bg_name, bg_code in background_colors.items():
#         for style_name, style_code in styles.items():
#             print(f"\x1b[{style_code};{fg_code};{bg_code}m{fg_name} on {bg_name} with {style_name}\x1b[0m")



# Example of escape sequences in Python

# New line
print("Hello,\nWorld!")  # Output: Hello,
                          #         World!

# Tab
print("Hello,\tWorld!")  # Output: Hello,    World! (with a tab space)

# Carriage return
print("Hello, World!\rPython")  # Output: Python, World! (overwrites "Hello, ")

# Bell (may not produce a visible output in some environments)
print("Hello,\aWorld!")  # Output: Hello, (may produce a beep sound)

# Backspace
print("Hello,\bWorld!")  # Output: HellWorld! (removes the 'o')

# Form feed (may not produce a visible output in some environments)
print("Hello,\fWorld!")  # Output: Hello, (may move to the next page in some environments)

# Vertical tab (may not produce a visible output in some environments)
print("Hello,\vWorld!")  # Output: Hello, (may move down vertically in some environments)





# Example demonstrating all parameters of the print() function

# Define some variables for demonstration
name = "Alice"
age = 30
height = 5.5
hobbies = ["reading", "hiking", "coding"]

# Using the print function with various parameters
print("Demonstrating print() parameters:")

# 1. Basic print with multiple objects
print("Name:", name, "Age:", age, "Height:", height)

# 2. Custom separator
print("Hobbies:", *hobbies, sep=", ")

# 3. Custom end character
print("This is the first line.", end=" ")
print("This is the second line.")

# 4. Using the file parameter to write to a file
# with open('output.txt', 'w') as f:
#     print("This will be written to a file.", file=f)

# 5. Flushing output
import time
print("Loading...", end="", flush=True)
time.sleep(5)  # Simulate a delay
print(" Done!")

# 6. Printing with different data types
print("Data types:", "String:", name, "Integer:", age, "Float:", height)

# 7. Formatted output using f-string
print(f"Formatted output: Name: {name}, Age: {age}, Height: {height}")

# 8. Printing a list with unpacking
print("Hobbies list:", *hobbies)

# 9. Custom separator and end
print("Python", "is", "fun", sep=" - ", end="!\n")





# Program to demonstrate different data types in Python

# 1. Integer
integer_value = 42
print("Integer:", integer_value)

# 2. Float
float_value = 3.14
print("Float:", float_value)

# 3. String
string_value = "Hello, World!"
print("String:", string_value)

# 4. List (mutable)
list_value = [1, 2, 3, 4, 5]
print("List:", list_value)

# 5. Tuple (immutable)
tuple_value = (1, 2, 3, 4, 5)
print("Tuple:", tuple_value)

# 6. Dictionary (key-value pairs)
dict_value = {
    "name": "Alice",
    "age": 30,
    "height": 5.5
}
print("Dictionary:", dict_value)

# 7. Set (unordered collection of unique elements)
set_value = {1, 2, 3, 4, 5}
print("Set:", set_value)

# 8. Boolean
boolean_value_true = True
boolean_value_false = False
print("Boolean True:", boolean_value_true)
print("Boolean False:", boolean_value_false)

# 9. NoneType
none_value = None
print("NoneType:", none_value)

# 10. Demonstrating type() function
print("\nData Types:")
print("Type of integer_value:", type(integer_value))
print("Type of float_value:", type(float_value))
print("Type of string_value:", type(string_value))
print("Type of list_value:", type(list_value))
print("Type of tuple_value:", type(tuple_value))
print("Type of dict_value:", type(dict_value))
print("Type of set_value:", type(set_value))
print("Type of boolean_value_true:", type(boolean_value_true))
print("Type of none_value:", type(none_value))

# max value of int
print("\nMax value of int:", sys.maxsize)

# min value of int
print("\nMin value of int:", -sys.maxsize - 1)


