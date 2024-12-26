
# Simple calculator but with proper Documentation
class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    This class provides methods to add, subtract, multiply, and divide two numbers.
    """

    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.

        @param a: The first number.
        @param b: The second number.
        @return: The sum of a and b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtract one number from another.

        @param a: The number to be subtracted from.
        @param b: The number to subtract.
        @return: The result of a - b.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.

        @param a: The first number.
        @param b: The second number.
        @return: The product of a and b.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divide one number by another.

        @param a: The numerator.
        @param b: The denominator.
        @return: The result of a / b.

        @raises ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


def main():
    """
    Main function to demonstrate the Calculator class.

    This function creates an instance of the Calculator class and performs
    some basic arithmetic operations, printing the results to the console.
    """
    calc = Calculator()

    print("Addition: 5 + 3 =", calc.add(5, 3))
    print("Subtraction: 5 - 3 =", calc.subtract(5, 3))
    print("Multiplication: 5 * 3 =", calc.multiply(5, 3))
    print("Division: 5 / 3 =", calc.divide(5, 3))

    try:
        print("Division by zero: 5 / 0 =", calc.divide(5, 0))
    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()