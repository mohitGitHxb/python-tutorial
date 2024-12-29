import logging
import os


import sys
from contextlib import suppress
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter a number.")

try:
    # Some code that might raise exceptions
    result = 10 / int(input("Enter a number: "))
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("No exceptions were raised")

try:
    file = open("example.txt", "r")
    # Process file
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # This will always run, even if an exception occurs


class CustomError(Exception):
    """A custom exception class"""
    pass

def check_positive(value):
    if value <= 0:
        raise CustomError("Value must be positive")
    return value

try:
    check_positive(-5)
except CustomError as e:
    print(e)



try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("An error occurred") from e
except ValueError as ve:
    print(f"Caught: {ve}")




logging.basicConfig(level=logging.ERROR)

try:
    # Some risky operation
    result = 10 / 0
except Exception as e:
    logging.error(f"An error occurred: {e}", exc_info=True)



# Suppress specific exceptions
with suppress(FileNotFoundError):
    os.remove("somefile.tmp")


def global_exception_handler(exctype, value, traceback):
    print(f"Uncaught exception: {exctype.__name__}: {value}")

sys.excepthook = global_exception_handler

def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

try:
    result = divide(10, 0)
except AssertionError as e:
    print(e)


'''def process_data(data):
    try:
        # Perform operations
        result = some_complex_operation(data)
    except ValueError as ve:
        # Handle specific value errors
        print(f"Value error: {ve}")
        # Optionally log or take corrective action
    except TypeError as te:
        # Handle type-related errors
        print(f"Type error: {te}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error: {e}")
        # Optionally re-raise if needed
        raise
    else:
        # Run if no exceptions occurred
        return result
    finally:
        # Cleanup code that always runs
        cleanup_resources()'''

'''
Best Practices:

    Be specific with exception types
    Avoid catching all exceptions with bare except:
    Use logging for production environments
    Create custom exceptions for specific error scenarios
    Provide meaningful error messages
    Clean up resources in finally blocks

Remember:

    Use exceptions for exceptional circumstances
    Don't use exceptions for flow control
    Handle exceptions at the appropriate level of abstraction


'''