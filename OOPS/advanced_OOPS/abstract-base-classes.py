from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """
    Abstract base class defining the interface for data processors.
    Any concrete implementation must provide these methods.
    """
    
    @abstractmethod
    def process(self, data):
        """Process the given data and return the result."""
        pass
    
    @abstractmethod
    def validate(self, data):
        """Validate the data before processing."""
        pass
    
    def run(self, data):
        """
        Template method pattern: defines the skeleton of an algorithm
        but lets subclasses override specific steps.
        """
        if self.validate(data):
            return self.process(data)
        else:
            raise ValueError("Invalid data provided")

class NumericProcessor(DataProcessor):
    """Concrete implementation for processing numeric data."""
    
    def validate(self, data):
        return all(isinstance(item, (int, float)) for item in data)
    
    def process(self, data):
        return sum(data) / len(data) if data else 0

class TextProcessor(DataProcessor):
    """Concrete implementation for processing text data."""
    
    def validate(self, data):
        return all(isinstance(item, str) for item in data)
    
    def process(self, data):
        return " ".join(data)

# Try to instantiate the abstract class (will fail)
try:
    processor = DataProcessor()
except TypeError as e:
    print(f"Error: {e}")

# Create concrete implementations
numeric_processor = NumericProcessor()
text_processor = TextProcessor()

# Use the processors
print(f"Numeric result: {numeric_processor.run([1, 2, 3, 4, 5])}")
print(f"Text result: {text_processor.run(['Hello', 'advanced', 'OOP', 'world'])}")