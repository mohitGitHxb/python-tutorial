# Dunder Methods Demonstration
class AdvancedNumber:
    def __init__(self, value):
        self.value = value
    
    # Representation Methods
    def __str__(self):
        """String representation for users"""
        return f"AdvancedNumber({self.value})"
    
    def __repr__(self):
        """Detailed string representation for developers"""
        return f"AdvancedNumber(value={self.value})"
    
    # Comparison Methods
    def __eq__(self, other):
        """Equal comparison"""
        if isinstance(other, AdvancedNumber):
            return self.value == other.value
        return self.value == other
    
    def __lt__(self, other):
        """Less than comparison"""
        if isinstance(other, AdvancedNumber):
            return self.value < other.value
        return self.value < other
    
    # Arithmetic Methods
    def __add__(self, other):
        """Addition"""
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value + other.value)
        return AdvancedNumber(self.value + other)
    
    def __sub__(self, other):
        """Subtraction"""
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value - other.value)
        return AdvancedNumber(self.value - other)

    def __mul__(self, other):
        """Multiplication"""
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value * other.value)
        return AdvancedNumber(self.value * other)

    def __truediv__(self, other):
        """Division"""
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value / other.value)
        return AdvancedNumber(self.value / other)

    # Unary Operations
    def __neg__(self):
        """Negation"""
        return AdvancedNumber(-self.value)

    # Type Conversion
    def __int__(self):
        """Convert to int"""
        return int(self.value)

    def __float__(self):
        """Convert to float"""
        return float(self.value)

    # Context Management
    def __enter__(self):
        """Enter the runtime context related to this object"""
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the runtime context related to this object"""
        print("Exiting context")

# Example usage of dunder methods
if __name__ == "__main__":
    num1 = AdvancedNumber(10)
    num2 = AdvancedNumber(5)

    print(num1)  # Calls __str__
    print(repr(num1))  # Calls __repr__

    print(num1 + num2)  # Calls __add__
    print(num1 - num2)  # Calls __sub__
    print(num1 * num2)  # Calls __mul__
    print(num1 / num2)  # Calls __truediv__

    print(num1 == num2)  # Calls __eq__
    print(num1 < num2)  # Calls __lt__

    with num1 as n:
        print(f"Inside context with {n}")

    print(int(num1))  # Calls __int__
    print(float(num1))  # Calls __float__