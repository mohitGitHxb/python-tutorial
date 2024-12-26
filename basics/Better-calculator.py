class Calculator:
    def add(self, x, y):
        """Return the sum of x and y."""
        return x + y

    def subtract(self, x, y):
        """Return the difference of x and y."""
        return x - y

    def multiply(self, x, y):
        """Return the product of x and y."""
        return x * y

    def divide(self, x, y):
        """Return the quotient of x and y. Raises ValueError if y is zero."""
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

def get_number(prompt):
    """Get a number from the user, handling invalid input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    """Get a valid operation from the user."""
    operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in operations:
            return operation
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

def main():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator!")
    
    while True:
        # Get user input
        num1 = get_number("Enter the first number: ")
        operation = get_operation()
        num2 = get_number("Enter the second number: ")

        # Perform calculation
        calculator = Calculator()
        try:
            if operation == '+':
                result = calculator.add(num1, num2)
            elif operation == '-':
                result = calculator.subtract(num1, num2)
            elif operation == '*':
                result = calculator.multiply(num1, num2)
            elif operation == '/':
                result = calculator.divide(num1, num2)

            print(f"The result of {num1} {operation} {num2} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

        # Ask if the user wants to continue
        continue_calculating = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_calculating != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()