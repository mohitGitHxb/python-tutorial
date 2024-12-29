# Python Dictionaries: Comprehensive Guide

# 1. Dictionary Creation Methods
def dictionary_creation():
    # Literal notation
    student = {
        'name': 'John Doe',
        'age': 25,
        'courses': ['Math', 'Computer Science']
    }
    print("Literal Dict:", student)

    # dict() constructor
    employee = dict(
        name='Jane Smith',
        age=30,
        department='IT'
    )
    print("Constructor Dict:", employee)

    # Dictionary comprehension
    squared_dict = {x: x**2 for x in range(1, 6)}
    print("Comprehension Dict:", squared_dict)

    # Fromkeys method
    default_dict = dict.fromkeys(['a', 'b', 'c'], 0)
    print("Fromkeys Dict:", default_dict)

# 2. Basic Dictionary Methods
def dictionary_methods():
    # get() - Safely retrieve values
    user = {'username': 'johndoe', 'email': 'john@example.com'}
    
    # Default value if key doesn't exist
    phone = user.get('phone', 'No phone number')
    print("Phone:", phone)

    # keys(), values(), items()
    print("Keys:", list(user.keys()))
    print("Values:", list(user.values()))
    print("Items:", list(user.items()))

    # pop() - Remove and return value
    email = user.pop('email')
    print("Popped Email:", email)
    print("Updated User:", user)

    # popitem() - Remove last inserted item (Python 3.7+)
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    last_item = test_dict.popitem()
    print("Last Item:", last_item)

# 3. Advanced Dictionary Techniques
def advanced_dictionary_operations():
    # Merging dictionaries
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    
    # Python 3.9+ method
    merged_dict = dict1 | dict2
    print("Merged Dict:", merged_dict)

    # Update method
    dict1.update(dict2)
    print("Updated Dict:", dict1)

    # Nested dictionaries
    complex_dict = {
        'users': {
            'john': {'age': 25, 'city': 'New York'},
            'jane': {'age': 30, 'city': 'San Francisco'}
        }
    }
    print("Nested Dict:", complex_dict)

# 4. Dictionary Comprehensions
def dictionary_comprehensions():
    # Basic comprehension
    squared_dict = {x: x**2 for x in range(1, 6)}
    print("Squared Dict:", squared_dict)

    # Conditional comprehension
    even_squared_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print("Even Squared Dict:", even_squared_dict)

    # Transforming existing dictionary
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    transformed_dict = {k.upper(): v*10 for k, v in original_dict.items()}
    print("Transformed Dict:", transformed_dict)

# 5. Dictionary Sorting and Filtering
def dictionary_sorting_filtering():
    # Sorting dictionaries
    prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
    
    # Sort by keys
    sorted_by_keys = dict(sorted(prices.items()))
    print("Sorted by Keys:", sorted_by_keys)

    # Sort by values
    sorted_by_values = dict(sorted(prices.items(), key=lambda x: x[1]))
    print("Sorted by Values:", sorted_by_values)

    # Filtering dictionary
    def filter_dictionary(dictionary, condition):
        return {k: v for k, v in dictionary.items() if condition(k, v)}
    
    # Filter items with value > 0.30
    filtered_prices = filter_dictionary(prices, lambda k, v: v > 0.30)
    print("Filtered Prices:", filtered_prices)

# 6. Advanced Dictionary Techniques
def advanced_dictionary_techniques():
    # Default Dictionary
    from collections import defaultdict
    
    # Automatically create default values
    word_count = defaultdict(int)
    text = "hello world hello python world"
    for word in text.split():
        word_count[word] += 1
    print("Word Count:", dict(word_count))

    # Ordered Dictionary
    from collections import OrderedDict
    
    # Maintains insertion order
    ordered_dict = OrderedDict()
    ordered_dict['first'] = 1
    ordered_dict['second'] = 2
    ordered_dict['third'] = 3
    print("Ordered Dict:", ordered_dict)

# 7. Dictionary Performance and Memory
def dictionary_performance():
    import sys
    import timeit

    # Memory comparison
    small_dict = {'a': 1, 'b': 2, 'c': 3}
    print("Dictionary Memory Size:", sys.getsizeof(small_dict))

    # Membership testing performance
    test_dict = {i: i for i in range(10000)}
    
    # Compare membership testing time
    dict_time = timeit.timeit('5000 in test_dict', globals=locals(), number=10000)
    print(f"Dictionary Membership Time: {dict_time}")

# 8. Dictionary Type Hinting
def type_hinting_demo():
    from typing import Dict, Union

    # Type-hinted dictionary
    def process_user_data(users: Dict[str, Union[str, int]]) -> Dict[str, str]:
        return {name: f"Processed {name}" for name in users}

    user_data = {
        'john': 25,
        'jane': 30
    }
    processed = process_user_data(user_data)
    print("Processed Users:", processed)

# 9. Dictionary-based Caching
def dictionary_caching():
    # Memoization decorator
    def memoize(func):
        cache = {}
        def wrapper(*args):
            if args not in cache:
                cache[args] = func(*args)
            return cache[args]
        return wrapper

    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    # Compute Fibonacci numbers
    fib_results = {n: fibonacci(n) for n in range(10)}
    print("Fibonacci Cache:", fib_results)
# 10. Additional Dictionary Methods and Techniques

# setdefault() Method
def setdefault_method():
    # Provides default value if key doesn't exist
    user_preferences = {}
    
    # If key doesn't exist, it's created with default value
    theme = user_preferences.setdefault('theme', 'light')
    print("Theme:", theme)
    print("Updated Dict:", user_preferences)

    # Another example with more complex default
    user_data = {}
    user_data.setdefault('skills', []).append('Python')
    user_data.setdefault('skills', []).append('JavaScript')
    print("User Skills:", user_data)

# Dictionary Unpacking
def dictionary_unpacking():
    # Merging dictionaries with unpacking
    base_config = {'debug': False, 'log_level': 'INFO'}
    dev_config = {**base_config, 'debug': True}
    print("Merged Config:", dev_config)

    # Function with dictionary unpacking
    def create_user(**kwargs):
        default_user = {
            'name': 'Anonymous',
            'age': 0,
            'active': False
        }
        return {**default_user, **kwargs}

    user1 = create_user(name='John', age=30)
    print("Created User:", user1)

# Reverse Mapping
def reverse_dictionary():
    # Create a reverse mapping
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    
    # Simple reverse
    reverse_dict = {v: k for k, v in original_dict.items()}
    print("Reversed Dict:", reverse_dict)

    # Handling multiple keys with same value
    complex_dict = {'a': 1, 'b': 2, 'c': 2}
    
    # Reverse with list of keys
    def reverse_with_lists(dictionary):
        reverse_map = {}
        for key, value in dictionary.items():
            reverse_map.setdefault(value, []).append(key)
        return reverse_map

    multi_reverse = reverse_with_lists(complex_dict)
    print("Multi-Key Reverse:", multi_reverse)

# Dictionary Accumulation
def dictionary_accumulation():
    # Grouping and accumulating data
    transactions = [
        {'category': 'food', 'amount': 50},
        {'category': 'transport', 'amount': 30},
        {'category': 'food', 'amount': 40},
        {'category': 'entertainment', 'amount': 60}
    ]

    # Accumulate by category
    def accumulate_by_category(transactions):
        result = {}
        for transaction in transactions:
            category = transaction['category']
            amount = transaction['amount']
            result[category] = result.get(category, 0) + amount
        return result

    category_totals = accumulate_by_category(transactions)
    print("Category Totals:", category_totals)

# Dictionary Chaining
from collections import ChainMap
def dictionary_chaining():
    # Combine multiple dictionaries
    default_settings = {'color': 'blue', 'font': 'Arial'}
    user_settings = {'color': 'green'}
    system_settings = {'resolution': '1080p'}

    # ChainMap allows searching through multiple dictionaries
    combined_settings = ChainMap(user_settings, default_settings, system_settings)
    
    print("Color:", combined_settings['color'])  # Uses user_settings
    print("Font:", combined_settings['font'])    # Uses default_settings
    print("Resolution:", combined_settings['resolution'])  # Uses system_settings

# Dictionary Validation
def dictionary_validation():
    # Validate dictionary structure
    def validate_user_dict(user_dict):
        required_keys = {'name', 'email'}
        optional_keys = {'age', 'location'}
        
        # Check for required keys
        missing_keys = required_keys - set(user_dict.keys())
        if missing_keys:
            raise ValueError(f"Missing required keys: {missing_keys}")
        
        # Validate key types
        type_checks = {
            'name': str,
            'email': str,
            'age': (int, type(None)),
            'location': (str, type(None))
        }
        
        errors = []
        for key, expected_type in type_checks.items():
            if key in user_dict and not isinstance(user_dict.get(key), expected_type):
                errors.append(f"Invalid type for {key}")
        
        if errors:
            raise ValueError(f"Validation errors: {errors}")
        
        return True

    # Example usage
    try:
        valid_user = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'age': 30
        }
        validate_user_dict(valid_user)
        print("User dictionary is valid")
    except ValueError as e:
        print(f"Validation failed: {e}")

# Main execution
if __name__ == "__main__":
    dictionary_creation()
    dictionary_methods()
    advanced_dictionary_operations()
    dictionary_comprehensions()
    dictionary_sorting_filtering()
    advanced_dictionary_techniques()
    dictionary_performance()
    type_hinting_demo()
    dictionary_caching()
    setdefault_method()
    dictionary_unpacking()
    reverse_dictionary()
    dictionary_accumulation()
    dictionary_chaining()
    dictionary_validation()