# 1. Basic Lambda Function Syntax
"""
Lambda functions are small, anonymous functions
Syntax: lambda arguments: expression
"""

# Simple addition lambda
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# 2. Lambda with Different Number of Arguments
# Single argument
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # Output: 24

# 3. Lambda in Built-in Functions
# Sorting with lambda
fruits = ['apple', 'banana', 'cherry', 'date']

# Sort by length
sorted_fruits = sorted(fruits, key=lambda x: len(x))
print(sorted_fruits)  # Output: ['date', 'apple', 'banana', 'cherry']

# Sort by last character
sorted_fruits_last = sorted(fruits, key=lambda x: x[-1])
print(sorted_fruits_last)

# 4. Lambda with Map Function
# Transform list elements
numbers = [1, 2, 3, 4, 5]

# Convert to squared values
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# 5. Lambda with Filter Function
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# 6. Lambda with Reduce Function
from functools import reduce

# Calculate product of list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# 7. Advanced Conditional Lambda
# Ternary-like operation
get_parity = lambda x: "Even" if x % 2 == 0 else "Odd"
print(get_parity(4))  # Output: Even
print(get_parity(7))  # Output: Odd

# 8. Lambda with Dictionary Sorting
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda student: student['grade'], reverse=True)
print(sorted_students)

# 9. Complex Transformation Lambda
# Transform complex data structures
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]

# Extract names
names = list(map(lambda x: x['name'], data))
print(names)  # Output: ['Alice', 'Bob', 'Charlie']

# 10. Lambda with Error Handling
def safe_divide(func):
    return lambda x, y: func(x, y) if y != 0 else "Cannot divide by zero"

divide = safe_divide(lambda x, y: x / y)
print(divide(10, 2))   # Output: 5.0
print(divide(10, 0))   # Output: Cannot divide by zero

# 11. Recursive-like Lambda (Advanced)
# Factorial using lambda and reduce
from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n+1)) if n > 0 else 1
print(factorial(5))  # Output: 120

# 12. Multi-line Lambda Simulation
# Simulate multi-line lambda with function
complex_operation = lambda x: (
    x ** 2 if x < 10 else
    x ** 3 if x < 20 else
    x ** 4
)
print(complex_operation(5))   # Output: 25
print(complex_operation(15))  # Output: 3375

# 13. Lambda with Class Methods
class Calculator:
    def __init__(self, operation):
        self.operation = operation
    
    def calculate(self, x, y):
        return self.operation(x, y)

# Different calculator instances
add_calc = Calculator(lambda x, y: x + y)
mult_calc = Calculator(lambda x, y: x * y)

print(add_calc.calculate(5, 3))    # Output: 8
print(mult_calc.calculate(5, 3))   # Output: 15

# 14. Decorator-like Lambda
def logger(func):
    return lambda *args: (print(f"Calling with {args}"), func(*args))[1]

@logger
def add(x, y):
    return x + y

add(3, 4)  # Prints: Calling with (3, 4) and returns 7

# 15. Advanced Functional Composition
def compose(*functions):
    return lambda x: reduce(lambda v, f: f(v), reversed(functions), x)

# Create a composition of functions
double = lambda x: x * 2
square = lambda x: x ** 2
add_ten = lambda x: x + 10

composed_func = compose(double, square, add_ten)
print(composed_func(3))  # Output: ((3+10)^2)*2