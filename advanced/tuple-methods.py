# Tuple Methods in Python

# 1. count() - Returns the number of times a specified value appears in the tuple
numbers = (1, 2, 2, 3, 2, 4, 2)
count_of_twos = numbers.count(2)
print(count_of_twos)  # Output: 4

# Advanced usage: Frequency analysis
def get_element_frequency(tuple_data):
    unique_elements = set(tuple_data)
    return {elem: tuple_data.count(elem) for elem in unique_elements}

sample_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
frequency_dict = get_element_frequency(sample_tuple)
print(frequency_dict)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}

# 2. index() - Returns the index of the first occurrence of a specified value
fruits = ('apple', 'banana', 'cherry', 'banana')
banana_index = fruits.index('banana')
print(banana_index)  # Output: 1

# Advanced usage: Finding multiple occurrences
def find_all_indices(tuple_data, value):
    return [index for index, item in enumerate(tuple_data) if item == value]

multi_fruits = ('apple', 'banana', 'cherry', 'banana', 'date', 'banana')
all_banana_indices = find_all_indices(multi_fruits, 'banana')
print(all_banana_indices)  # Output: [1, 3, 5]

# Additional Tuple Techniques (Not Methods, but Useful Operations)

# 3. Tuple Unpacking
coordinates = (10, 20)
x, y = coordinates
print(x, y)  # Output: 10 20

# Advanced usage: Multiple return values
def get_user_info():
    return ('John', 25, 'Developer')

name, age, profession = get_user_info()
print(name, age, profession)  # Output: John 25 Developer

# 4. Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Advanced usage: Dynamic tuple creation
def merge_categories(*category_tuples):
    return tuple(item for categories in category_tuples for item in categories)

electronics = ('laptop', 'phone')
clothing = ('shirt', 'pants')
merged_categories = merge_categories(electronics, clothing)
print(merged_categories)  # Output: ('laptop', 'phone', 'shirt', 'pants')

# 5. Tuple Repetition
original_tuple = (1, 2)
repeated_tuple = original_tuple * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

# Advanced usage: Creating pattern or padding
def create_padded_sequence(base_tuple, length):
    repetitions = (length + len(base_tuple) - 1) // len(base_tuple)
    return (base_tuple * repetitions)[:length]

pattern = create_padded_sequence((0, 1), 7)
print(pattern)  # Output: (0, 1, 0, 1, 0, 1, 0)

# 6. Nested Tuple Operations
nested_tuple = ((1, 2), (3, 4), (5, 6))
flattened = tuple(item for sublist in nested_tuple for item in sublist)
print(flattened)  # Output: (1, 2, 3, 4, 5, 6)

# 7. Tuple Comparison
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 < tuple2)  # Output: True (compares elements lexicographically)

# Advanced Tuple Techniques and Operations

# 8. Slicing Tuples
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing
print(numbers[2:7])    # Output: (2, 3, 4, 5, 6)
print(numbers[:4])     # Output: (0, 1, 2, 3)
print(numbers[6:])     # Output: (6, 7, 8, 9)
print(numbers[::2])    # Output: (0, 2, 4, 6, 8)
print(numbers[::-1])   # Output: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0) - Reverse

# Advanced slicing with step and negative indexing
def advanced_slice_demo(tuple_data):
    return {
        'first_half': tuple_data[:len(tuple_data)//2],
        'last_half': tuple_data[len(tuple_data)//2:],
        'every_third': tuple_data[::3],
        'reversed_odd_indices': tuple_data[-1::-2]
    }

sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced_results = advanced_slice_demo(sample_tuple)
print(sliced_results)

# 9. Tuple Comprehensions (Generator Expression)
# Create tuples dynamically
squares = tuple(x**2 for x in range(1, 6))
print(squares)  # Output: (1, 4, 9, 16, 25)

# Advanced comprehension with filtering
even_squares = tuple(x**2 for x in range(1, 11) if x % 2 == 0)
print(even_squares)  # Output: (4, 16, 36, 64, 100)

# 10. Tuple Transformation Methods
# Converting to other data types
numbers_tuple = (1, 2, 3, 4, 5)

# Convert to list
numbers_list = list(numbers_tuple)
print(numbers_list)  # Output: [1, 2, 3, 4, 5]

# Convert to set (removes duplicates)
numbers_set = set(numbers_tuple)
print(numbers_set)  # Output: {1, 2, 3, 4, 5}

# 11. Advanced Tuple Unpacking
# Multiple-level unpacking
nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple
print(a, b, c, d)  # Output: 1 2 3 4

# Unpacking with * operator
first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)  # Output: 1 [2, 3, 4] 5

# 12. Tuple Sorting (External Function)
unsorted_tuple = (5, 2, 8, 1, 9)
sorted_tuple = tuple(sorted(unsorted_tuple))
print(sorted_tuple)  # Output: (1, 2, 5, 8, 9)

# Sorting with key function
names = ('Alice', 'bob', 'Charlie', 'david')
sorted_names = tuple(sorted(names, key=str.lower))
print(sorted_names)  # Output: ('Alice', 'bob', 'Charlie', 'david')

# 13. Named Tuples (Advanced Tuple Usage)
from collections import namedtuple

# Creating a named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating instances
alice = Person('Alice', 30, 'New York')
bob = Person('Bob', 25, 'San Francisco')

print(alice.name)  # Output: Alice
print(bob.age)     # Output: 25

# 14. Tuple Membership and Checking
fruits = ('apple', 'banana', 'cherry')

# Membership testing
print('banana' in fruits)      # Output: True
print('grape' not in fruits)   # Output: True

# 15. Tuple Iteration Techniques
def iterate_with_index(tuple_data):
    for index, value in enumerate(tuple_data):
        print(f"Index {index}: {value}")

colors = ('red', 'green', 'blue')
iterate_with_index(colors)
# Output:
# Index 0: red
# Index 1: green
# Index 2: blue

# 16. Tuple Zipping
names = ('Alice', 'Bob', 'Charlie')
ages = (25, 30, 35)
cities = ('New York', 'San Francisco', 'Chicago')

# Zip tuples together
combined = tuple(zip(names, ages, cities))
print(combined)  
# Output: (('Alice', 25, 'New York'), ('Bob', 30, 'San Francisco'), ('Charlie', 35, 'Chicago'))

# Practical Use Cases
def create_user_records(*args):
    return tuple(zip(*args))

user_records = create_user_records(
    ['name', 'Alice', 'Bob'],
    ['age', 25, 30],
    ['city', 'NY', 'SF']
)
print(user_records)


# Additional Tuple Techniques and Advanced Operations

# 17. Tuple Comparison Operators
def tuple_comparison_demo():
    # Lexicographic comparison
    print((1, 2, 3) < (1, 2, 4))  # Output: True
    print((1, 2, 3) == (1, 2, 3))  # Output: True
    print((1, 2, 3) > (1, 1, 5))  # Output: True

    # Complex comparisons
    tuple1 = (1, 'a', 3)
    tuple2 = (1, 'b', 2)
    print(tuple1 < tuple2)  # Output: True (compares element by element)

# 18. Tuple Memory Efficiency Demonstration
def memory_comparison():
    import sys
    
    # Compare memory usage between list and tuple
    small_list = [1, 2, 3, 4, 5]
    small_tuple = (1, 2, 3, 4, 5)
    
    print("List memory:", sys.getsizeof(small_list))
    print("Tuple memory:", sys.getsizeof(small_tuple))

# 19. Advanced Tuple Packing and Unpacking
def advanced_unpacking():
    # Extended unpacking
    a, *middle, b = (1, 2, 3, 4, 5)
    print(a)       # Output: 1
    print(middle)  # Output: [2, 3, 4]
    print(b)       # Output: 5

    # Function with multiple return values
    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers)

    lowest, highest, total = get_stats([1, 2, 3, 4, 5])
    print(lowest, highest, total)  # Output: 1 5 15

# 20. Tuple Immutability Tricks
def immutability_demonstration():
    # Attempting to modify a tuple
    try:
        immutable_tuple = (1, 2, 3)
        # immutable_tuple[0] = 4  # This would raise a TypeError
    except TypeError as e:
        print("Cannot modify tuple:", e)

    # Create a "modified" tuple
    original = (1, 2, 3)
    modified = original[:1] + (4,) + original[2:]
    print(modified)  # Output: (1, 4, 3)

# 21. Recursive Tuple Processing
def recursive_tuple_processing():
    def deep_sum(tuple_data):
        total = 0
        for item in tuple_data:
            if isinstance(item, tuple):
                total += deep_sum(item)
            elif isinstance(item, (int, float)):
                total += item
        return total

    nested_tuple = (1, (2, 3), (4, (5, 6)), 7)
    print(deep_sum(nested_tuple))  # Output: 28

# 22. Tuple as Dictionary Keys
def tuple_as_dict_key():
    # Tuples can be used as dictionary keys (unlike lists)
    coordinate_values = {
        (0, 0): 'Origin',
        (1, 0): 'Right',
        (0, 1): 'Up'
    }
    print(coordinate_values[(0, 0)])  # Output: Origin

# 23. Functional Programming with Tuples
def functional_tuple_operations():
    from functools import reduce

    # Reduce operation on tuples
    numbers = (1, 2, 3, 4, 5)
    product = reduce(lambda x, y: x * y, numbers)
    print(product)  # Output: 120

    # Map operation
    squared_tuple = tuple(map(lambda x: x**2, numbers))
    print(squared_tuple)  # Output: (1, 4, 9, 16, 25)

# 24. Tuple Caching and Memoization
def fibonacci_memoization():
    def memoized_fibonacci():
        cache = {}
        def fibonacci(n):
            if n in cache:
                return cache[n]
            if n <= 1:
                return n
            result = fibonacci(n-1) + fibonacci(n-2)
            cache[n] = result
            return result
        return fibonacci

    fib = memoized_fibonacci()
    fib_sequence = tuple(fib(i) for i in range(10))
    print(fib_sequence)  # Output: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)

# 25. Tuple Type Hinting (Python 3.9+)
def type_hinting_demo():
    from typing import Tuple

    # Type-hinted tuple
    def process_coordinates(point: Tuple[int, int, int]) -> float:
        x, y, z = point
        return (x**2 + y**2 + z**2) ** 0.5

    distance = process_coordinates((3, 4, 5))
    print(distance)  # Output: 7.071067811865475

# Demonstrate all functions
if __name__ == "__main__":
    tuple_comparison_demo()
    memory_comparison()
    advanced_unpacking()
    immutability_demonstration()
    recursive_tuple_processing()
    tuple_as_dict_key()
    functional_tuple_operations()
    fibonacci_memoization()
    type_hinting_demo()