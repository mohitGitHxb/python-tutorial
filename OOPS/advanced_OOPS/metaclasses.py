class ValidationMeta(type):
    """
    A metaclass that adds validation to class attributes.
    This is the "class of a class" - it creates and configures classes.
    """
    def __new__(mcs, name, bases, attrs):
        # Add validation to all methods that start with 'set_'
        for attr_name, attr_value in attrs.items():
            if attr_name.startswith('set_') and callable(attr_value):
                attrs[attr_name] = ValidationMeta.add_validation(attr_value)
        
        # Create and return the new class
        return super().__new__(mcs, name, bases, attrs)
    
    @staticmethod
    def add_validation(method):
        """Wrap methods with validation logic."""
        def wrapper(self, value):
            if value is None:
                raise ValueError(f"None is not allowed for {method.__name__}")
            return method(self, value)
        return wrapper

class ModelWithValidation(metaclass=ValidationMeta):
    """
    A model class that uses the ValidationMeta metaclass.
    All setter methods will automatically validate against None values.
    """
    def __init__(self, name=None, value=None):
        self._name = name
        self._value = value
    
    def set_name(self, name):
        self._name = name
    
    def set_value(self, value):
        self._value = value
    
    def get_name(self):
        return self._name
    
    def get_value(self):
        return self._value

# Create a model and test the validation
model = ModelWithValidation("test", 42)
print(f"Initial state: name={model.get_name()}, value={model.get_value()}")

# This works fine
model.set_name("new_name")
print(f"After setting name: name={model.get_name()}")

# This should raise a ValueError
try:
    model.set_value(None)
except ValueError as e:
    print(f"Caught expected error: {e}")

# Let's create a class dynamically using type
DynamicModel = type(
    'DynamicModel',                          # Class name
    (ModelWithValidation,),                  # Base classes (tuple)
    {                                        # Class attributes dictionary
        'special_method': lambda self: "This method was added dynamically",
        'CONSTANT': 42
    }
)

# Create an instance of our dynamically created class
dynamic_instance = DynamicModel("dynamic", 100)
print(f"Dynamic instance: name={dynamic_instance.get_name()}, constant={dynamic_instance.CONSTANT}")
print(f"Special method result: {dynamic_instance.special_method()}")