# Basic String Methods

# 1. lower() - Converts all characters to lowercase
text = "HELLO WORLD"
lowercase_text = text.lower()
print(lowercase_text)  # Output: hello world

# Advanced usage: Normalizing user input
user_input = "UsErNaMe"
normalized_input = user_input.lower()
print(normalized_input)  # Output: username

# 2. upper() - Converts all characters to uppercase
text = "hello world"
uppercase_text = text.upper()
print(uppercase_text)  # Output: HELLO WORLD

# Advanced usage: Creating constants or formatting
CONSTANT = "database_connection".upper()
print(CONSTANT)  # Output: DATABASE_CONNECTION

# 3. strip() - Removes whitespace from both ends
text = "   hello world   "
trimmed_text = text.strip()
print(trimmed_text)  # Output: "hello world"

# Advanced usage: Cleaning user input
user_input = "   john@example.com   "
cleaned_email = user_input.strip()
print(cleaned_email)  # Output: "john@example.com"

# 4. replace() - Replaces occurrences of a substring
text = "Hello, World!"
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Output: Hello, Python!

# Advanced usage: Multiple replacements
message = "I love apples and apple pie"
modified_message = message.replace("apple", "banana")
print(modified_message)  # Output: I love bananas and banana pie

# 5. split() - Splits string into a list
text = "apple,banana,cherry"
fruits = text.split(',')
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Advanced usage: Parsing complex strings
log_entry = "2023-06-15 | ERROR | Database connection failed"
parts = log_entry.split('|')
print(parts)  # Output: ['2023-06-15 ', ' ERROR ', ' Database connection failed']

# 6. join() - Joins list elements into a string
fruits = ['apple', 'banana', 'cherry']
fruit_string = ', '.join(fruits)
print(fruit_string)  # Output: "apple, banana, cherry"

# Advanced usage: Creating CSV-like strings
data = ['John', '30', 'Engineer']
csv_row = ','.join(data)
print(csv_row)  # Output: "John,30,Engineer"

# 7. startswith() - Checks if string starts with a prefix
text = "Hello, World!"
is_greeting = text.startswith("Hello")
print(is_greeting)  # Output: True

# Advanced usage: Filtering strings
emails = ['john@example.com', 'admin@system.com', 'user@domain.com']
admin_emails = [email for email in emails if email.startswith('admin')]
print(admin_emails)  # Output: ['admin@system.com']

# 8. endswith() - Checks if string ends with a suffix
filename = "document.pdf"
is_pdf = filename.endswith(".pdf")
print(is_pdf)  # Output: True

# Advanced usage: File type validation
files = ['image.jpg', 'document.pdf', 'script.py']
image_files = [f for f in files if f.endswith(('.jpg', '.png', '.gif'))]
print(image_files)  # Output: ['image.jpg']

# 9. find() - Returns index of first occurrence of substring
text = "Hello, World!"
index = text.find("World")
print(index)  # Output: 7

# Advanced usage: Checking substring existence
def is_valid_email(email):
    return email.find('@') != -1

print(is_valid_email("john@example.com"))  # Output: True
print(is_valid_email("invalid_email"))     # Output: False

# 10. format() - Formats string with placeholders
name = "Alice"
age = 30
formatted_string = "My name is {} and I'm {} years old".format(name, age)
print(formatted_string)  # Output: "My name is Alice and I'm 30 years old"

# Advanced usage: Named placeholders
person = {"name": "Bob", "age": 25}
formatted_string = "My name is {name} and I'm {age} years old".format(**person)
print(formatted_string)  # Output: "My name is Bob and I'm 25 years old"

# 11. count() - Counts occurrences of a substring
text = "hello hello world"
hello_count = text.count("hello")
print(hello_count)  # Output: 2

# Advanced usage: Complex counting
def count_word_occurrences(text, word):
    return text.lower().count(word.lower())

sample_text = "Python Python is Amazing amazing"
print(count_word_occurrences(sample_text, "python"))  # Output: 2

# 12. isalpha() - Checks if string contains only alphabetic characters
text1 = "HelloWorld"
text2 = "Hello123"
print(text1.isalpha())  # Output: True
print(text2.isalpha())  # Output: False

# Advanced usage: Input validation
def validate_name(name):
    return name.isalpha() and len(name) > 2

print(validate_name("John"))    # Output: True
print(validate_name("John123")) # Output: False

# 13. isdigit() - Checks if string contains only digits
text1 = "12345"
text2 = "123.45"
print(text1.isdigit())  # Output: True
print(text2.isdigit())  # Output: False

# Advanced usage: Numeric input validation
def validate_numeric_input(input_string):
    return input_string.isdigit() and int(input_string) > 0

print(validate_numeric_input("100"))   # Output: True
print(validate_numeric_input("-50"))   # Output: False

# 14. isalnum() - Checks if string contains only alphanumeric characters
text1 = "Hello123"
text2 = "Hello World"
print(text1.isalnum())  # Output: True
print(text2.isalnum())  # Output: False

# Advanced usage: Username validation
def validate_username(username):
    return username.isalnum() and 3 <= len(username) <= 20

print(validate_username("john_doe123"))  # Output: False
print(validate_username("johndoe123"))   # Output: True

# 15. center() - Centers the string within a specified width
text = "python"
centered_text = text.center(10, '-')
print(centered_text)  # Output: "--python--"

# Advanced usage: Formatting output
def create_banner(message, width=20):
    return message.center(width, '*')

print(create_banner("Welcome"))  # Output: "*******Welcome*******"

# 16. zfill() - Adds zeros to the left of the string
number = "42"
zero_padded = number.zfill(5)
print(zero_padded)  # Output: "00042"

# Advanced usage: Formatting numeric strings
def format_account_number(number):
    return number.zfill(10)

print(format_account_number("1234"))  # Output: "0000001234"

# 17. partition() - Splits string into three parts
text = "hello:world:python"
parts = text.partition(":")
print(parts)  # Output: ('hello', ':', 'world:python')

# Advanced usage: Parsing structured strings
def parse_key_value(text):
    key, separator, value = text.partition("=")
    return key.strip(), value.strip()

config = "database = localhost"
key, value = parse_key_value(config)
print(key, value)  # Output: database localhost

# 18. swapcase() - Swaps case of characters
text = "HeLLo WoRLd"
swapped_text = text.swapcase()
print(swapped_text)  # Output: hEllO wOrld

# Advanced usage: Text transformation
def anonymize_text(text):
    return text.swapcase()

print(anonymize_text("John Doe"))  # Output: jOHN dOE

# 19. title() - Converts first character of each word to uppercase
text = "hello world python programming"
titled_text = text.title()
print(titled_text)  # Output: "Hello World Python Programming"

# Advanced usage: Name formatting
def format_name(full_name):
    return full_name.title()

print(format_name("john doe smith"))  # Output: John Doe Smith

# 20. encode() and decode() - String encoding and decoding
text = "Hello, 世界"
utf8_encoded = text.encode('utf-8')
decoded_text = utf8_encoded.decode('utf-8')
print(utf8_encoded)    # Output: b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(decoded_text)    # Output: Hello, 世界

# Advanced usage: Handling different character encodings
def safe_encode(text, encoding='utf-8'):
    try:
        return text.encode(encoding)
    except UnicodeEncodeError:
        return text.encode(encoding, errors='ignore')

print(safe_encode("Hello, 世界"))  # Safely encodes the text

# 21. expandtabs() - Replaces tabs with spaces
text = "Hello\tWorld\tPython"
expanded_text = text.expandtabs(4)
print(expanded_text)  # Output: Replaces tabs with 4-space indentation

# Advanced usage: Custom text formatting
def format_tabular_data(data):
    return data.expandtabs(10)

print(format_tabular_data("Name\tAge\tCity"))

# 22. index() - Finds substring position (raises ValueError if not found)
text = "Hello, World!"
try:
    position = text.index("World")
    print(position)  # Output: 7
except ValueError:
    print("Substring not found")

# Advanced usage: Safe substring searching
def safe_index(text, substring):
    try:
        return text.index(substring)
    except ValueError:
        return -1

print(safe_index("Hello World", "World"))    # Output: 6
print(safe_index("Hello World", "Python"))   # Output: -1

# 23. rindex() - Finds last occurrence of substring
text = "Hello Hello World"
last_hello_pos = text.rindex("Hello")
print(last_hello_pos)  # Output: 6

# Advanced usage: Finding last meaningful occurrence
def find_last_meaningful_word(text):
    words = text.split()
    return words[-1] if words else ""

print(find_last_meaningful_word("Python is an amazing programming language"))
# Output: language

# 24. capitalize() - Capitalizes first character
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello world"

# Advanced usage: Smart sentence capitalization
def smart_capitalize(text):
    return '. '.join(sentence.capitalize() for sentence in text.split('. '))

print(smart_capitalize("hello world. python is awesome"))
# Output: "Hello world. Python is awesome"

# 25. rfind() - Finds last occurrence of substring
text = "Hello Hello World"
last_occurrence = text.rfind("Hello")
print(last_occurrence)  # Output: 6

# Advanced usage: Complex text analysis
def extract_last_section(text, separator):
    return text.rfind(separator)

file_path = "/home/user/documents/report.pdf"
last_slash = extract_last_section(file_path, "/")
print(file_path[last_slash+1:])  # Output: report.pdf

# 26. maketrans() and translate() - Character mapping
# Simple character replacement
translation_table = str.maketrans('aeiou', '12345')
text = "hello world"
translated_text = text.translate(translation_table)
print(translated_text)  # Output: h2ll4 w4rld

# Advanced usage: Complex text obfuscation
def obfuscate_text(text):
    # Remove vowels and replace with numbers
    trans_table = str.maketrans({
        'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5',
        'A': '1', 'E': '2', 'I': '3', 'O': '4', 'U': '5'
    })
    return text.translate(trans_table)

print(obfuscate_text("Hello World"))  # Output: H2ll4 W4rld

# 27. removeprefix() and removesuffix() (Python 3.9+)
text = "prefix_hello_world_suffix"
without_prefix = text.removeprefix("prefix_")
without_suffix = text.removesuffix("_suffix")
print(without_prefix)   # Output: hello_world_suffix
print(without_suffix)   # Output: prefix_hello_world

# Advanced usage: URL and file path processing
def clean_url(url):
    return url.removeprefix("https://").removeprefix("www.")

print(clean_url("https://www.example.com"))  # Output: example.com

# 28. format_map() - Advanced string formatting with dictionaries
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
template = "My name is {name} and I'm {age} years old"
formatted_text = template.format_map(vars(person))
print(formatted_text)  # Output: My name is Alice and I'm 30 years old

# Advanced dictionary-based formatting
def format_with_defaults(template, data):
    defaults = {"name": "Unknown", "age": "N/A"}
    defaults.update(data)
    return template.format_map(defaults)

print(format_with_defaults("Name: {name}, Age: {age}", {"name": "Bob"}))
# Output: Name: Bob, Age: N/A

# 29. casefold() - Aggressive lowercase conversion
text1 = "ß"  # German Eszett
text2 = "HELLO"

print(text1.casefold())  # Output: ss
print(text2.casefold())  # Output: hello

# Advanced usage: Case-insensitive comparison
def case_insensitive_compare(str1, str2):
    return str1.casefold() == str2.casefold()

print(case_insensitive_compare("Straße", "strasse"))  # Output: True

# 30. isprintable() - Checks if all characters are printable
text1 = "Hello World"
text2 = "Hello\nWorld"
text3 = "Hello\tWorld"

print(text1.isprintable())  # Output: True
print(text2.isprintable())  # Output: False
print(text3.isprintable())  # Output: False

# Advanced usage: Input validation
def validate_printable_input(text):
    return text.isprintable() and len(text) > 0

print(validate_printable_input("Hello"))      # Output: True
print(validate_printable_input("Hello\n"))    # Output: False

# 31. isspace() - Checks if string contains only whitespace
text1 = "   "
text2 = " \t\n\r"
text3 = "Hello "

print(text1.isspace())  # Output: True
print(text2.isspace())  # Output: True
print(text3.isspace())  # Output: False

# Advanced usage: Whitespace cleaning
def clean_whitespace(text):
    return text if text.strip() else "Empty"

print(clean_whitespace("   "))    # Output: Empty
print(clean_whitespace("Hello"))  # Output: Hello

# 32. isnumeric() - Checks if string contains only numeric characters
text1 = "12345"
text2 = "½"  # Fraction
text3 = "123.45"

print(text1.isnumeric())  # Output: True
print(text2.isnumeric())  # Output: True
print(text3.isnumeric())  # Output: False

# Advanced usage: Numeric validation with unicode support
def validate_numeric_unicode(text):
    return text.isnumeric() and float(text.replace('½', '0.5')) > 0

print(validate_numeric_unicode("½"))  # Output: True
print(validate_numeric_unicode("10½"))  # Output: True

# 33. ljust() and rjust() - Left and right justification
text = "Python"
left_justified = text.ljust(10, '-')
right_justified = text.rjust(10, '*')

print(left_justified)   # Output: Python----
print(right_justified)  # Output: ****Python

# Advanced usage: Formatted table printing
def create_table_row(data, width=20):
    return f"{data['name'].ljust(10)}{str(data['age']).rjust(10)}"

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

print("Name      Age")
for row in data:
    print(create_table_row(row))

# 34. rsplit() - Split from the right side
text = "apple,banana,cherry,date"
split_limit = text.rsplit(',', 2)
print(split_limit)  # Output: ['apple,banana', 'cherry', 'date']

# Advanced usage: Parsing complex strings
def extract_file_extension(filename):
    return filename.rsplit('.', 1)[-1] if '.' in filename else ''

print(extract_file_extension("document.txt"))    # Output: txt
print(extract_file_extension("image.backup.jpg"))  # Output: jpg

# 35. splitlines() - Splits string into lines
text = "Hello\nWorld\rPython\r\nProgramming"
lines = text.splitlines()
print(lines)  # Output: ['Hello', 'World', 'Python', 'Programming']

# Advanced usage: Cleaning and processing multiline text
def process_text_lines(text):
    return [line.strip() for line in text.splitlines() if line.strip()]

multiline_text = """
Hello
  World  
Python
"""
print(process_text_lines(multiline_text))
# Output: ['Hello', 'World', 'Python']

# 36. Custom string method using __add__
class CustomString(str):
    def repeat(self, n):
        return self * n
    
    def __add__(self, other):
        return CustomString(super().__add__(other.upper()))

custom_str = CustomString("hello")
print(custom_str.repeat(3))  # Output: hellohellohello
print(custom_str + CustomString(" world"))  # Output: hello WORLD

# 37. Dynamic string method composition
def create_string_processor(transformations):
    def process_string(text):
        for transform in transformations:
            text = getattr(text, transform)()
        return text
    return process_string

# Create a processor that converts to uppercase and removes spaces
uppercase_no_space = create_string_processor(['upper', 'replace'])
print(uppercase_no_space("hello world", ' ', ''))  # Output: HELLOWORLD

# 38. String Slicing and Advanced Manipulation
text = "Python Programming"

# Basic slicing
print(text[0:6])        # Output: Python
print(text[:6])         # Output: Python
print(text[7:])         # Output: Programming
print(text[-11:])       # Output: Programming

# Advanced slicing with step
print(text[::2])        # Output: Pto rgamn
print(text[::-1])       # Output: gnimmargorP nohtyP

# 39. Complex String Validation
def advanced_password_validator(password):
    """
    Advanced password validation with multiple checks
    """
    checks = [
        lambda p: len(p) >= 8,                  # Minimum length
        lambda p: any(c.isupper() for c in p),  # At least one uppercase
        lambda p: any(c.islower() for c in p),  # At least one lowercase
        lambda p: any(c.isdigit() for c in p),  # At least one digit
        lambda p: any(not c.isalnum() for c in p)  # At least one special character
    ]
    
    return all(check(password) for check in checks)

# Password validation examples
passwords = [
    "simple",           # Weak
    "StrongPass123!",   # Strong
    "weakpassword",     # Weak
    "12345678"          # Weak
]

for pwd in passwords:
    print(f"{pwd}: {advanced_password_validator(pwd)}")

# 40. Dynamic String Formatting
class StringFormatter:
    @staticmethod
    def format_with_padding(text, width=10, fill_char=' ', align='center'):
        """
        Dynamic string formatting with multiple alignment options
        """
        if align == 'center':
            return text.center(width, fill_char)
        elif align == 'left':
            return text.ljust(width, fill_char)
        elif align == 'right':
            return text.rjust(width, fill_char)

# Usage examples
formatter = StringFormatter()
print(formatter.format_with_padding("Python", width=10))  # Centered
print(formatter.format_with_padding("Python", width=10, align='left', fill_char='-'))
print(formatter.format_with_padding("Python", width=10, align='right', fill_char='*'))

# 41. Advanced Text Transformation
def text_transformer(text):
    """
    Complex text transformation pipeline
    """
    transformations = [
        lambda t: t.lower(),            # Convert to lowercase
        lambda t: t.replace(' ', '_'),  # Replace spaces with underscores
        lambda t: t.strip(),            # Remove leading/trailing whitespaces
        lambda t: f"transformed_{t}"    # Add prefix
    ]
    
    result = text
    for transform in transformations:
        result = transform(result)
    
    return result

print(text_transformer("  Hello World  "))  # Output: transformed_hello_world

# 42. Unicode and Normalization
import unicodedata

def normalize_unicode_text(text):
    """
    Normalize unicode text for consistent comparison
    """
    # Normalize to decomposed form
    normalized = unicodedata.normalize('NFKD', text)
    
    # Remove non-ascii characters
    ascii_text = normalized.encode('ascii', 'ignore').decode('ascii')
    
    return ascii_text

# Unicode comparison examples
print(normalize_unicode_text("café"))  # Output: cafe
print(normalize_unicode_text("naïve"))  # Output: naive

# 43. String Template with Advanced Substitution
from string import Template

class AdvancedTemplate:
    @staticmethod
    def safe_substitute(template_str, **kwargs):
        """
        Safe template substitution with default values
        """
        template = Template(template_str)
        default_values = {
            'username': 'Guest',
            'age': 'Unknown'
        }
        default_values.update(kwargs)
        
        return template.safe_substitute(default_values)

# Usage
template_str = "Hello, $username! You are $age years old."
print(AdvancedTemplate.safe_substitute(template_str, username="Alice"))
print(AdvancedTemplate.safe_substitute(template_str, age=30))

# 44. Regex-based String Manipulation
import re

def advanced_string_cleaner(text):
    """
    Advanced text cleaning with regex
    """
    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

# Cleaning examples
dirty_texts = [
    "Hello, World! 123",
    "  Multiple   Spaces  ",
    "Special@#$Chars"
]

for text in dirty_texts:
    print(advanced_string_cleaner(text))

# 45. Internationalization Support
def transliterate(text, lang='en'):
    """
    Basic transliteration support
    """
    transliterations = {
        'ru': {
            'а': 'a', 'б': 'b', 'в': 'v',
            # Add more transliterations
        }
    }
    
    if lang not in transliterations:
        return text
    
    for char, replacement in transliterations[lang].items():
        text = text.replace(char, replacement)
    
    return text

print(transliterate("привет", lang='ru'))  # Basic Russian transliteration