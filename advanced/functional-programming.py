# 1. map() Function
"""
Applies a function to every item in an iterable
Syntax: map(function, iterable)
"""

# Basic usage
def square(x):
    return x ** 2

# Using map with a function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Map with lambda
squared_lambda = list(map(lambda x: x ** 2, numbers))
print(squared_lambda)  # Output: [1, 4, 9, 16, 25]

# Map with multiple iterables
def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [10, 20, 30]
added_lists = list(map(add, list1, list2))
print(added_lists)  # Output: [11, 22, 33]

# 2. filter() Function
"""
Filters elements based on a function that returns True/False
Syntax: filter(function, iterable)
"""

# Basic filtering
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Filter with lambda
even_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(even_lambda)  # Output: [2, 4, 6, 8, 10]

# Filtering complex objects
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

high_performers = list(filter(lambda student: student['grade'] >= 80, students))
print(high_performers)

# 3. reduce() Function
"""
Applies a function of two arguments cumulatively to the items of a sequence
Syntax: reduce(function, iterable[, initializer])
"""
from functools import reduce

# Sum of list
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

# With initial value
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_initial)  # Output: 25

# Complex reduction
def custom_max(x, y):
    return x if x > y else y

max_number = reduce(custom_max, numbers)
print(max_number)  # Output: 5

# 4. zip() Function
"""
Creates an iterator of tuples where the i-th tuple contains 
the i-th element from each of the input iterables
"""

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'San Francisco', 'Chicago']

# Combine multiple lists
combined = list(zip(names, ages, cities))
print(combined)  
# Output: [('Alice', 25, 'New York'), ('Bob', 30, 'San Francisco'), ('Charlie', 35, 'Chicago')]

# Unzipping
unzipped_names, unzipped_ages, unzipped_cities = zip(*combined)
print(unzipped_names)  # Output: ('Alice', 'Bob', 'Charlie')

# 5. enumerate() Function
"""
Adds a counter to an iterable and returns it as an enumerate object
"""

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start enumeration from a different number
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry

# 6. any() and all() Functions
"""
any(): Returns True if any element is True
all(): Returns True if all elements are True
"""

numbers = [1, 2, 3, 4, 5]
print(any(num > 4 for num in numbers))  # Output: True
print(all(num > 0 for num in numbers))  # Output: True

# 7. itertools Module (Advanced Iteration)
import itertools

# Combinations
numbers = [1, 2, 3]
combinations = list(itertools.combinations(numbers, 2))
print(combinations)  # Output: [(1, 2), (1, 3), (2, 3)]

# Permutations
permutations = list(itertools.permutations(numbers, 2))
print(permutations)  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 8. functools.partial
"""
Creates a new function with partial application of arguments
"""
from functools import partial

def multiply(x, y):
    return x * y

# Create a new function with one argument fixed
double = partial(multiply, 2)
print(double(4))  # Output: 8

# 9. operator Module Functions
import operator

# Efficient alternative to lambda functions
numbers = [1, 2, 3, 4, 5]
product = reduce(operator.mul, numbers)
print(product)  # Output: 120

# Sorting with operator
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by specific key
sorted_students = sorted(students, key=operator.itemgetter('grade'), reverse=True)
print(sorted_students)

# 10. Advanced Functional Composition
def compose(*functions):
    def inner(arg):
        for f in reversed(functions):
            arg = f(arg)
        return arg
    return inner

# Create a composition of functions
def add_ten(x):
    return x + 10

def double(x):
    return x * 2

def square(x):
    return x ** 2

composed_func = compose(double, square, add_ten)
print(composed_func(3))  # Output: ((3+10)^2)*2