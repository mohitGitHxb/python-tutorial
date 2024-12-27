from concurrent.futures import ThreadPoolExecutor


# 1. Basic For Loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# 2. Enumerate - Getting index and value simultaneously
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 3. Range-based For Loop
for i in range(5):  # 0 to 4
    print(i)

# 4. Range with start, stop, step
for i in range(1, 10, 2):  # Odd numbers from 1 to 9
    print(i)

# 5. Reverse Loop
for i in reversed(range(5)):
    print(i)

# 6. Nested For Loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # New line after each row

# 7. Comprehension-based For Loop
squared = [x**2 for x in range(5)]
print(squared)

# 8. Conditional Comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# 9. Nested Comprehension
nested_comp = [[x*y for x in range(3)] for y in range(3)]
print(nested_comp)

# 10. Zip - Iterating multiple lists simultaneously
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 11. Else with For Loop
for i in range(5):
    print(i)
else:
    print("Loop completed normally")

# 12. Breaking and Continuing
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break  # Exit loop
    print(i)

# 13. Dictionary Iteration
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
for name, score in student_scores.items():
    print(f"{name}: {score}")

# 14. Iterating Keys
for name in student_scores.keys():
    print(name)

# 15. Iterating Values
for score in student_scores.values():
    print(score)

# 16. Advanced Unpacking
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"X: {x}, Y: {y}")

# 17. Infinite Iterator with iter() and next()
def infinite_counter():
    num = 0
    while True:
        # yield: Returns a value and pauses the function
        yield num
        num += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter))

# 18. Custom Iterator
class CustomRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

for num in CustomRange(1, 5):
    print(num)

# 19. Itertools for Advanced Iteration
import itertools

# Permutations
for perm in itertools.permutations([1, 2, 3]):
    print(perm)

# Combinations
for combo in itertools.combinations([1, 2, 3, 4], 2):
    print(combo)

# 20. Generator Expression
gen = (x**2 for x in range(5))
for squared in gen:
    print(squared)

# 21. Flattening Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)

# 22. Parallel Processing with For Loop

def process_item(item):
    return item * 2

items = [1, 2, 3, 4, 5]
with ThreadPoolExecutor() as executor:
    results = list(executor.map(process_item, items))
print(results)