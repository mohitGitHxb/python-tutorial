# Array Methods in Python (Using Lists as Arrays)

# 1. append() - Add a single element to the end of the array
arr = [1, 2, 3]
arr.append(4)
print(arr)  # Output: [1, 2, 3, 4]

# Advanced usage: Conditional appending
def add_if_unique(arr, element):
    if element not in arr:
        arr.append(element)
    return arr

unique_arr = add_if_unique([1, 2, 3], 4)
print(unique_arr)  # Output: [1, 2, 3, 4]

# 2. extend() - Add multiple elements to the end of the array
arr = [1, 2, 3]
arr.extend([4, 5, 6])
print(arr)  # Output: [1, 2, 3, 4, 5, 6]

# Advanced usage: Flattening nested lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = []
for sublist in nested_list:
    flattened.extend(sublist)
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

# 3. insert() - Insert an element at a specific index
arr = [1, 2, 3]
arr.insert(1, 4)
print(arr)  # Output: [1, 4, 2, 3]

# Advanced usage: Inserting with validation
def safe_insert(arr, index, element):
    if 0 <= index <= len(arr):
        arr.insert(index, element)
    return arr

# 4. remove() - Remove the first occurrence of a specific element
arr = [1, 2, 3, 2, 4]
arr.remove(2)
print(arr)  # Output: [1, 3, 2, 4]

# Advanced usage: Safe removal
def safe_remove(arr, element):
    try:
        arr.remove(element)
    except ValueError:
        print(f"{element} not found in the array")
    return arr

# 5. pop() - Remove and return an element at a specific index
arr = [1, 2, 3, 4]
removed_element = arr.pop(1)
print(removed_element)  # Output: 2
print(arr)  # Output: [1, 3, 4]

# Advanced usage: Efficient stack operations
def stack_operations(arr):
    if arr:
        return arr.pop()  # Remove and return top element
    return None

# 6. index() - Find the index of the first occurrence of an element
arr = [1, 2, 3, 2, 4]
index = arr.index(2)
print(index)  # Output: 1

# Advanced usage: Finding all indices
def find_all_indices(arr, element):
    return [i for i, x in enumerate(arr) if x == element]

# 7. count() - Count occurrences of an element
arr = [1, 2, 2, 3, 2, 4]
count = arr.count(2)
print(count)  # Output: 3

# 8. sort() - Sort the array in-place
arr = [3, 1, 4, 1, 5, 9, 2]
arr.sort()
print(arr)  # Output: [1, 1, 2, 3, 4, 5, 9]

# Advanced usage: Custom sorting
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
students.sort(key=lambda x: x['grade'], reverse=True)

# 9. reverse() - Reverse the array in-place
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)  # Output: [5, 4, 3, 2, 1]

# 10. copy() - Create a shallow copy of the array
original = [1, 2, 3]
arr_copy = original.copy()
arr_copy[0] = 4
print(original)  # Output: [1, 2, 3]
print(arr_copy)  # Output: [4, 2, 3]

# Advanced Array Manipulation Techniques
# Using list comprehensions and functional programming
# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6]

# Map transformation
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25, 36]

# Best Practices:
# 1. Use list comprehensions for concise transformations
# 2. Prefer list methods over manual implementations
# 3. Be cautious with in-place modifications
# 4. Use copy() for creating independent copies
# 5. Leverage functional programming techniques
# Advanced Array Methods and Techniques Continued

# 11. clear() - Remove all elements from the array
arr = [1, 2, 3, 4, 5]
arr.clear()
print(arr)  # Output: []

# Advanced usage: Resetting data structures
class DataProcessor:
    def __init__(self):
        self.data = []
    
    def reset(self):
        self.data.clear()

# 12. Slicing - Advanced array manipulation
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
first_half = arr[:5]  # First 5 elements
second_half = arr[5:]  # Last 5 elements
print(first_half)  # Output: [0, 1, 2, 3, 4]

# Advanced slicing techniques
# Step slicing
every_second = arr[::2]  # Every second element
reversed_arr = arr[::-1]  # Reverse the array
print(every_second)  # Output: [0, 2, 4, 6, 8]

# Slice assignment
arr[2:5] = [20, 30, 40]  # Replace a portion of the array
print(arr)  # Output: [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# 13. Advanced Filtering Techniques
# Using filter() function
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Advanced filtering with multiple conditions
def complex_filter(x):
    return x > 5 and x % 2 == 0

complex_filtered = list(filter(complex_filter, numbers))
print(complex_filtered)  # Output: [6, 8, 10]

# 14. Nested Array Operations
nested_arr = [[1, 2], [3, 4], [5, 6]]

# Flattening nested arrays
def flatten_array(nested_list):
    return [item for sublist in nested_list for item in sublist]

flattened = flatten_array(nested_arr)
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

# 15. Advanced Sorting Techniques
# Multi-level sorting
students = [
    {'name': 'Alice', 'grade': 85, 'age': 22},
    {'name': 'Bob', 'grade': 85, 'age': 20},
    {'name': 'Charlie', 'grade': 92, 'age': 21}
]

# Sort by grade (descending), then by age (ascending)
sorted_students = sorted(students, key=lambda x: (-x['grade'], x['age']))
print(sorted_students)

# 16. Functional Programming Techniques
from functools import reduce

# Reduce - Cumulative operations
numbers = [1, 2, 3, 4, 5]

# Sum of all elements
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)  # Output: 15

# Product of all elements
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# 17. Advanced Array Transformations
# Pivot and group operations
data = [
    {'category': 'A', 'value': 10},
    {'category': 'B', 'value': 20},
    {'category': 'A', 'value': 15},
    {'category': 'B', 'value': 25}
]

# Group by category and sum values
from itertools import groupby
from operator import itemgetter

def group_and_aggregate(data):
    # Sort the data by category first
    sorted_data = sorted(data, key=itemgetter('category'))
    
    # Group and aggregate
    grouped = {}
    for key, group in groupby(sorted_data, key=itemgetter('category')):
        grouped[key] = sum(item['value'] for item in group)
    
    return grouped

result = group_and_aggregate(data)
print(result)  # Output: {'A': 25, 'B': 45}

# 18. Advanced Array Validation
def validate_array(arr, 
                   min_length=0, 
                   max_length=float('inf'), 
                   element_type=None):
    """
    Comprehensive array validation
    
    :param arr: Input array to validate
    :param min_length: Minimum required length
    :param max_length: Maximum allowed length
    :param element_type: Expected type of elements
    :return: Boolean indicating validity
    """
    if not isinstance(arr, list):
        return False
    
    if not (min_length <= len(arr) <= max_length):
        return False
    
    if element_type:
        return all(isinstance(x, element_type) for x in arr)
    
    return True

# Usage examples
print(validate_array([1, 2, 3], min_length=3, max_length=5, element_type=int))
print(validate_array(['a', 'b'], min_length=2, max_length=3, element_type=str))

# 19. Performance Optimization Techniques
import timeit

# Comparing list comprehension vs map
def list_comprehension(arr):
    return [x * 2 for x in arr]

def map_method(arr):
    return list(map(lambda x: x * 2, arr))

# Benchmark
large_arr = list(range(10000))
print("List Comprehension Time:", 
      timeit.timeit(lambda: list_comprehension(large_arr), number=100))
print("Map Method Time:", 
      timeit.timeit(lambda: map_method(large_arr), number=100))






# Advanced Array Techniques - Part 3

# 20. Advanced Chunking Techniques
def chunk_array(arr, chunk_size):
    """
    Split array into fixed-size chunks
    
    Args:
        arr (list): Input array
        chunk_size (int): Size of each chunk
    
    Returns:
        list: List of chunked arrays
    """
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

# Example usage
data = list(range(1, 11))
chunked_data = chunk_array(data, 3)
print(chunked_data)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

# 21. Advanced Deduplication Techniques
def advanced_deduplicate(arr, keep='first'):
    """
    Sophisticated deduplication with multiple strategies
    
    Args:
        arr (list): Input array
        keep (str): Deduplication strategy 
                    'first' - keep first occurrence
                    'last' - keep last occurrence
                    'max' - keep max value
    
    Returns:
        list: Deduplicated array
    """
    if keep == 'first':
        seen = set()
        return [x for x in arr if not (x in seen or seen.add(x))]
    
    elif keep == 'last':
        return list(dict.fromkeys(reversed(arr)))[::-1]
    
    elif keep == 'max':
        return list(dict.fromkeys(arr))

# Usage examples
numbers = [1, 2, 3, 2, 4, 1, 5]
print(advanced_deduplicate(numbers, 'first'))  # [1, 2, 3, 4, 5]
print(advanced_deduplicate(numbers, 'last'))   # [3, 2, 4, 1, 5]

# 22. Advanced Partitioning
def partition_array(arr, predicate):
    """
    Partition array based on a predicate function
    
    Args:
        arr (list): Input array
        predicate (callable): Condition function
    
    Returns:
        tuple: (matched, unmatched) lists
    """
    matched = []
    unmatched = []
    
    for item in arr:
        if predicate(item):
            matched.append(item)
        else:
            unmatched.append(item)
    
    return matched, unmatched

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = partition_array(data, lambda x: x % 2 == 0)
print("Even:", even)
print("Odd:", odd)

# 23. Advanced Windowing Techniques
from collections import deque

class SlidingWindow:
    def __init__(self, size):
        self.size = size
        self.window = deque(maxlen=size)
    
    def add(self, item):
        self.window.append(item)
    
    def get_window(self):
        return list(self.window)
    
    def get_moving_average(self):
        return sum(self.window) / len(self.window) if self.window else 0

# Example usage
window = SlidingWindow(3)
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
moving_averages = []

for item in data:
    window.add(item)
    if len(window.get_window()) == window.size:
        moving_averages.append(window.get_moving_average())

print("Moving Averages:", moving_averages)

# 24. Advanced Transformation Techniques
def advanced_transform(arr, 
                       transform_func=None, 
                       filter_func=None, 
                       reduce_func=None):
    """
    Comprehensive array transformation
    
    Args:
        arr (list): Input array
        transform_func (callable, optional): Transformation function
        filter_func (callable, optional): Filtering function
        reduce_func (callable, optional): Reduction function
    
    Returns:
        list or any: Transformed result
    """
    # Initial transformation
    if transform_func:
        arr = list(map(transform_func, arr))
    
    # Optional filtering
    if filter_func:
        arr = list(filter(filter_func, arr))
    
    # Optional reduction
    if reduce_func:
        return reduce(reduce_func, arr)
    
    return arr

# Usage examples
data = [1, 2, 3, 4, 5]
transformed = advanced_transform(
    data, 
    transform_func=lambda x: x * 2,
    filter_func=lambda x: x > 5,
    reduce_func=lambda x, y: x + y
)
print(transformed)  # 24

# 25. Advanced Parallel Processing
from multiprocessing import Pool

def parallel_array_process(arr, process_func, num_processes=None):
    """
    Parallel array processing
    
    Args:
        arr (list): Input array
        process_func (callable): Processing function
        num_processes (int, optional): Number of parallel processes
    
    Returns:
        list: Processed results
    """
    with Pool(processes=num_processes) as pool:
        return pool.map(process_func, arr)

# Example usage
def heavy_computation(x):
    return x ** 2

data = list(range(1, 11))
parallel_results = parallel_array_process(data, heavy_computation)
print(parallel_results)

# 26. Type-Safe Array Operations
from typing import TypeVar, List, Callable
from functools import reduce

T = TypeVar('T')
U = TypeVar('U')

def type_safe_reduce(
    array: List[T], 
    reducer: Callable[[T, T], T], 
    initial: T = None
) -> T:
    """
    Type-safe reduction operation
    
    Args:
        array (List[T]): Input array
        reducer (Callable): Reduction function
        initial (T, optional): Initial value
    
    Returns:
        T: Reduced result
    """
    if not array:
        return initial
    
    return reduce(reducer, array, initial)

# Example usage
numbers = [1, 2, 3, 4, 5]
total = type_safe_reduce(numbers, lambda x, y: x + y, 0)
print("Total:", total)








# Remaining Advanced Array Methods and Techniques

# 1. Combination and Permutation Techniques
from itertools import combinations, permutations

# Generate all combinations
numbers = [1, 2, 3, 4]
# 2-element combinations
combo = list(combinations(numbers, 2))
print("Combinations:", combo)

# Generate all permutations
perms = list(permutations(numbers, 2))
print("Permutations:", perms)

# 2. Advanced Zip Operations
def advanced_zip(*arrays):
    """
    Enhanced zip with flexible handling
    
    Args:
        *arrays: Multiple input arrays
    
    Returns:
        List of zipped elements
    """
    max_length = max(len(arr) for arr in arrays)
    
    # Pad shorter arrays with None
    padded_arrays = [
        arr + [None] * (max_length - len(arr)) 
        for arr in arrays
    ]
    
    return list(zip(*padded_arrays))

# Usage
arr1 = [1, 2, 3]
arr2 = ['a', 'b']
arr3 = [True, False, True]

zipped = advanced_zip(arr1, arr2, arr3)
print("Advanced Zip:", zipped)

# 3. Advanced Accumulation
from itertools import accumulate
from operator import add

numbers = [1, 2, 3, 4, 5]
# Cumulative sum
cumulative_sum = list(accumulate(numbers))
print("Cumulative Sum:", cumulative_sum)

# Custom accumulation
cumulative_product = list(accumulate(numbers, lambda x, y: x * y))
print("Cumulative Product:", cumulative_product)

# 4. Advanced Grouping
from itertools import groupby
from operator import itemgetter

# Complex grouping
data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 25, 'city': 'Chicago'}
]

def group_by_complex(data, key):
    """
    Advanced grouping with flexible key selection
    
    Args:
        data (list): Input data
        key (str): Grouping key
    
    Returns:
        Dict of grouped elements
    """
    # Sort data by the key first
    sorted_data = sorted(data, key=itemgetter(key))
    
    # Group and convert to dict
    grouped = {}
    for k, group in groupby(sorted_data, key=itemgetter(key)):
        grouped[k] = list(group)
    
    return grouped

# Group by age
age_groups = group_by_complex(data, 'age')
print("Age Groups:", age_groups)

# 5. Advanced Array Rotation
def rotate_array(arr, k, direction='right'):
    """
    Rotate array with multiple strategies
    
    Args:
        arr (list): Input array
        k (int): Rotation steps
        direction (str): Rotation direction
    
    Returns:
        Rotated array
    """
    n = len(arr)
    k = k % n  # Normalize rotation steps
    
    if direction == 'right':
        return arr[-k:] + arr[:-k]
    else:
        return arr[k:] + arr[:k]

# Usage
numbers = [1, 2, 3, 4, 5]
rotated_right = rotate_array(numbers, 2)
rotated_left = rotate_array(numbers, 2, direction='left')
print("Rotated Right:", rotated_right)
print("Rotated Left:", rotated_left)

# 6. Advanced Searching Techniques
def binary_search(arr, target):
    """
    Implement binary search with additional features
    
    Args:
        arr (list): Sorted input array
        target: Element to search
    
    Returns:
        Index of target or insertion point
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # Insertion point

# Usage
sorted_numbers = [1, 3, 5, 7, 9]
print("Binary Search:", binary_search(sorted_numbers, 6))