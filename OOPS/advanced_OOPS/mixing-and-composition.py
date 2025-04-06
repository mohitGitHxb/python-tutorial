import time
class SerializableMixin:
    """
    A mixin class that adds serialization capabilities.
    Mixins provide functionality without establishing an "is-a" relationship.
    """
    def to_dict(self):
        """Convert object attributes to a dictionary."""
        return {
            key: value for key, value in self.__dict__.items()
            if not key.startswith('_') and not callable(value)
        }
    
    def to_json(self):
        """Convert object to JSON string."""
        import json
        return json.dumps(self.to_dict())

class LoggableMixin:
    """
    A mixin that adds logging capabilities.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call parent's __init__
        self._log = []
    
    def log(self, message):
        """Add a message to the log."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self._log.append(f"[{timestamp}] {message}")
    
    def get_log(self):
        """Return the log entries."""
        return self._log

class ComparableMixin:
    """
    A mixin that adds comparison capabilities.
    Implements all comparison methods based on a single _compare method.
    """
    def _compare(self, other, method):
        """
        Compare this object with another.
        Subclasses should override this to implement the actual comparison.
        """
        raise NotImplementedError("Subclasses must implement _compare")
    
    def __lt__(self, other):
        return self._compare(other, lambda s, o: s < o)
    
    def __le__(self, other):
        return self._compare(other, lambda s, o: s <= o)
    
    def __eq__(self, other):
        return self._compare(other, lambda s, o: s == o)
    
    def __ge__(self, other):
        return self._compare(other, lambda s, o: s >= o)
    
    def __gt__(self, other):
        return self._compare(other, lambda s, o: s > o)
    
    def __ne__(self, other):
        return self._compare(other, lambda s, o: s != o)

# Product class using both mixins through multiple inheritance
class Product(SerializableMixin, LoggableMixin, ComparableMixin):
    """
    A product class that uses mixins for serialization, logging, and comparison.
    Demonstrates how mixins can be used to add functionality without deep inheritance.
    """
    def __init__(self, name, price):
        super().__init__()  # Call parent's __init__ (in this case, LoggableMixin)
        self.name = name
        self.price = price
        self.log(f"Created product: {name} at ${price}")
    
    def _compare(self, other, method):
        """Implement comparison based on price."""
        if not isinstance(other, Product):
            return NotImplemented
        return method(self.price, other.price)
    
    def apply_discount(self, percentage):
        """Apply a discount to the product."""
        old_price = self.price
        self.price = self.price * (1 - percentage / 100)
        self.log(f"Applied {percentage}% discount. Price changed from ${old_price} to ${self.price}")

# Create products
laptop = Product("Laptop", 1200)
phone = Product("Phone", 800)

# Use mixin functionality
laptop.apply_discount(10)
print(f"Laptop data: {laptop.to_dict()}")
print(f"Laptop JSON: {laptop.to_json()}")
print(f"Laptop log: {laptop.get_log()}")

# Compare products using ComparableMixin
print(f"Is laptop more expensive than phone? {laptop > phone}")
print(f"Is laptop equal to phone? {laptop == phone}")

# Creating functionality through composition instead of inheritance
class Logger:
    """A simple logger class for composition."""
    def __init__(self):
        self.messages = []
    
    def log(self, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.messages.append(f"[{timestamp}] {message}")
    
    def get_log(self):
        return self.messages

class ShoppingCart:
    """
    A shopping cart class that uses composition instead of inheritance.
    Demonstrates how to use composition to combine functionality.
    """
    def __init__(self):
        # Create and store instances of other classes
        self.logger = Logger()
        self.items = []
        self.logger.log("Created new shopping cart")
    
    def add_item(self, product, quantity=1):
        """Add a product to the cart."""
        self.items.append({"product": product, "quantity": quantity})
        self.logger.log(f"Added {quantity} x {product.name} to cart")
    
    def total(self):
        """Calculate the total price."""
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        self.logger.log(f"Calculated total: ${total}")
        return total
    
    def get_log(self):
        """Delegate to the logger."""
        return self.logger.get_log()
    
    def to_dict(self):
        """Convert to dictionary."""
        return {
            "items": [
                {
                    "product": item["product"].to_dict(),
                    "quantity": item["quantity"]
                }
                for item in self.items
            ],
            "total": self.total()
        }

# Use the shopping cart
cart = ShoppingCart()
cart.add_item(laptop)
cart.add_item(phone, 2)

print(f"Cart total: ${cart.total()}")
print(f"Cart log: {cart.get_log()}")
print(f"Cart data: {cart.to_dict()}")