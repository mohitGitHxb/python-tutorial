# Python Sets: Comprehensive Guide

# 1. Basic Set Creation
# Multiple ways to create sets
def set_creation_methods():
    # Literal notation
    fruits_set = {'apple', 'banana', 'cherry'}
    print(fruits_set)

    # Using set() constructor
    numbers_set = set([1, 2, 3, 4, 5])
    print(numbers_set)

    # Creating an empty set
    empty_set = set()
    print(empty_set)

    # Set from string (creates set of unique characters)
    char_set = set("hello")
    print(char_set)  # Output: {'h', 'e', 'l', 'o'}

# 2. Set Methods Demonstration
def set_methods():
    # add() - Adds a single element
    fruits = {'apple', 'banana'}
    fruits.add('cherry')
    print(fruits)

    # update() - Adds multiple elements
    fruits.update(['date', 'elderberry'])
    print(fruits)

    # remove() - Removes a specific element
    fruits.remove('banana')
    print(fruits)

    # discard() - Removes element without raising error if not found
    fruits.discard('grape')  # No error
    print(fruits)

    # pop() - Removes and returns an arbitrary element
    item = fruits.pop()
    print(item)

    # clear() - Removes all elements
    fruits.clear()
    print(fruits)

# 3. Set Operations
def set_operations():
    # Union
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    
    # Multiple ways to perform union
    print(set1.union(set2))  # Method
    print(set1 | set2)       # Operator

    # Intersection
    print(set1.intersection(set2))  # Method
    print(set1 & set2)              # Operator

    # Difference
    print(set1.difference(set2))  # Method
    print(set1 - set2)            # Operator

    # Symmetric Difference
    print(set1.symmetric_difference(set2))  # Method
    print(set1 ^ set2)                     # Operator

# 4. Advanced Set Techniques
def advanced_set_techniques():
    # Set Comprehension
    squared_set = {x**2 for x in range(1, 6)}
    print(squared_set)

    # Filtering with set comprehension
    even_squared_set = {x**2 for x in range(1, 11) if x % 2 == 0}
    print(even_squared_set)

# 5. Set Methods in Detail
def comprehensive_set_methods():
    # isdisjoint() - Check if sets have no common elements
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}
    print(set1.isdisjoint(set2))  # True

    # issubset() / <= operator
    set3 = {1, 2}
    set4 = {1, 2, 3, 4}
    print(set3.issubset(set4))  # True
    print(set3 <= set4)         # True

    # issuperset() / >= operator
    print(set4.issuperset(set3))  # True
    print(set4 >= set3)           # True

# 6. Practical Use Cases
def set_use_cases():
    # Removing duplicates
    def remove_duplicates(items):
        return set(items)

    duplicate_list = [1, 2, 2, 3, 3, 4, 4, 5]
    unique_items = remove_duplicates(duplicate_list)
    print(unique_items)

    # Finding unique elements
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    unique_to_list1 = set(list1) - set(list2)
    unique_to_list2 = set(list2) - set(list1)
    print("Unique to list1:", unique_to_list1)
    print("Unique to list2:", unique_to_list2)

# 7. Performance and Memory Efficiency
def set_performance():
    import sys
    import timeit

    # Membership testing
    test_list = list(range(10000))
    test_set = set(test_list)

    # Compare membership testing time
    list_time = timeit.timeit('5000 in test_list', globals=locals(), number=10000)
    set_time = timeit.timeit('5000 in test_set', globals=locals(), number=10000)

    print(f"List membership time: {list_time}")
    print(f"Set membership time: {set_time}")

    # Memory comparison
    print("List memory:", sys.getsizeof(test_list))
    print("Set memory:", sys.getsizeof(test_set))

# 8. Frozenset - Immutable Set
def frozenset_demo():
    # Create an immutable set
    immutable_set = frozenset([1, 2, 3])
    
    # Can be used as dictionary key or in another set
    test_dict = {immutable_set: 'frozen set as key'}
    print(test_dict)

# 9. Set Algebraic Operations
def set_algebraic_operations():
    # Custom set operations
    def venn_diagram(set1, set2):
        return {
            'union': set1.union(set2),
            'intersection': set1.intersection(set2),
            'difference_set1': set1.difference(set2),
            'difference_set2': set2.difference(set1),
            'symmetric_difference': set1.symmetric_difference(set2)
        }

    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    venn_result = venn_diagram(set_a, set_b)
    print(venn_result)

# Advanced Set Methods and Techniques

# 10. Additional Set Methods
def advanced_set_methods():
    # copy() - Create a shallow copy of the set
    original_set = {1, 2, 3, 4}
    set_copy = original_set.copy()
    print("Copied Set:", set_copy)

    # difference_update() - Remove elements found in another set
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    set1.difference_update(set2)
    print("After difference_update:", set1)  # Output: {1, 2}

    # intersection_update() - Update set with intersection
    set3 = {1, 2, 3, 4, 5}
    set4 = {3, 4, 5, 6, 7}
    set3.intersection_update(set4)
    print("After intersection_update:", set3)  # Output: {3, 4, 5}

    # symmetric_difference_update() - Update with symmetric difference
    set5 = {1, 2, 3, 4}
    set6 = {3, 4, 5, 6}
    set5.symmetric_difference_update(set6)
    print("After symmetric_difference_update:", set5)  # Output: {1, 2, 5, 6}

# 11. Set Filtering and Transformation
def set_filtering():
    # Filter set using comprehension
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    # Even numbers
    even_numbers = {x for x in numbers if x % 2 == 0}
    print("Even Numbers:", even_numbers)
    
    # Prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    prime_numbers = {x for x in numbers if is_prime(x)}
    print("Prime Numbers:", prime_numbers)

# 12. Advanced Set Combinations
def set_combinations():
    # Cartesian product of sets
    def set_cartesian_product(set1, set2):
        return {(x, y) for x in set1 for y in set2}
    
    colors = {'red', 'blue'}
    sizes = {'small', 'large'}
    product = set_cartesian_product(colors, sizes)
    print("Cartesian Product:", product)

    # Powerset (all possible subsets)
    def powerset(original_set):
        from itertools import chain, combinations
        return set(chain.from_iterable(combinations(original_set, r) for r in range(len(original_set)+1)))
    
    base_set = {1, 2, 3}
    power_set = powerset(base_set)
    print("Powerset:", power_set)

# 13. Set Reduction Techniques
def set_reduction():
    # Reduce set to specific condition
    def reduce_set(input_set, condition):
        return {x for x in input_set if condition(x)}
    
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    
    # Reduce to numbers greater than 5
    reduced_set = reduce_set(numbers, lambda x: x > 5)
    print("Reduced Set:", reduced_set)

# 14. Set Matching and Similarity
def set_matching():
    # Jaccard Similarity
    def jaccard_similarity(set1, set2):
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union != 0 else 0
    
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    similarity = jaccard_similarity(set_a, set_b)
    print("Jaccard Similarity:", similarity)

# 15. Set-based Caching
def set_caching():
    # Memoization using sets
    class SetBasedMemoizer:
        def __init__(self):
            self.computed_results = {}
        
        def memoize(self, func):
            def wrapper(*args):
                # Convert args to hashable tuple
                key = tuple(args)
                
                # Check if result is already computed
                if key not in self.computed_results:
                    result = func(*args)
                    self.computed_results[key] = result
                
                return self.computed_results[key]
            return wrapper
    
    # Example usage
    memoizer = SetBasedMemoizer()
    
    @memoizer.memoize
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    # Compute and cache Fibonacci numbers
    fib_results = {fibonacci(i) for i in range(10)}
    print("Fibonacci Set:", fib_results)
    print("Computed Results:", memoizer.computed_results)

# 16. Set-based Data Cleaning
def set_data_cleaning():
    # Remove duplicates and normalize data
    def clean_data(data_list):
        # Convert to lowercase
        normalized = {str(item).lower().strip() for item in data_list}
        return normalized
    
    messy_data = ['Apple', 'banana', 'APPLE', '  Cherry  ', 'banana']
    cleaned_data = clean_data(messy_data)
    print("Cleaned Data:", cleaned_data)

# Main execution
if __name__ == "__main__":
    set_creation_methods()
    set_methods()
    set_operations()
    advanced_set_techniques()
    comprehensive_set_methods()
    set_use_cases()
    set_performance()
    frozenset_demo()
    set_algebraic_operations()
    advanced_set_methods()
    set_filtering()
    set_combinations()
    set_reduction()
    set_matching()
    set_caching()
    set_data_cleaning()