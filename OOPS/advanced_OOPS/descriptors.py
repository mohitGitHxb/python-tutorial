class ValidatedField:
    """
    A descriptor that validates values before setting them.
    Descriptors are the mechanism behind properties and other attribute access customization.
    """
    def __init__(self, name, validation_func, error_message):
        self.name = "_" + name             # Private attribute name
        self.validation_func = validation_func
        self.error_message = error_message
    
    def __get__(self, instance, owner):
        if instance is None:
            return self                    # Class access returns the descriptor itself
        return getattr(instance, self.name, None)
    
    def __set__(self, instance, value):
        if not self.validation_func(value):
            raise ValueError(f"{value} {self.error_message}")
        setattr(instance, self.name, value)

class Person:
    """
    A class that uses descriptors for field validation.
    Demonstrates how descriptors can create reusable validation logic.
    """
    # Define validation rules as descriptors
    name = ValidatedField(
        "name", 
        lambda x: isinstance(x, str) and len(x) > 0,
        "is not a valid name. Name must be a non-empty string."
    )
    
    age = ValidatedField(
        "age", 
        lambda x: isinstance(x, int) and 0 <= x <= 150,
        "is not a valid age. Age must be an integer between 0 and 150."
    )
    
    email = ValidatedField(
        "email", 
        lambda x: isinstance(x, str) and "@" in x,
        "is not a valid email. Email must contain @."
    )
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Create a person with valid data
person = Person("Alice", 30, "alice@example.com")
print(f"Person: {person.name}, {person.age}, {person.email}")

# Try setting invalid values
try:
    person.age = 200  # Outside valid range
except ValueError as e:
    print(f"Age validation: {e}")

try:
    person.email = "invalid-email"  # Missing @
except ValueError as e:
    print(f"Email validation: {e}")

# Property - another way to implement attribute access control
class Temperature:
    """
    A class that uses properties for attribute access control.
    Properties are a more concise way to implement getters and setters.
    """
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get the temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set the temperature in Celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get the temperature in Fahrenheit (calculated from Celsius)."""
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set the temperature in Fahrenheit (converts to Celsius)."""
        self.celsius = (value - 32) * 5/9

# Create a temperature object
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

# Change temperature
temp.fahrenheit = 68
print(f"New temperature: {temp.celsius}°C = {temp.fahrenheit}°F")

# Try setting an impossible temperature
try:
    temp.celsius = -300  # Below absolute zero
except ValueError as e:
    print(f"Temperature validation: {e}")