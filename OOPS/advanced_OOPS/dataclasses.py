from dataclasses import dataclass, field, asdict
from typing import List, Optional, ClassVar, Dict, Any
import sys

@dataclass
class Point:
    """
    A simple dataclass representing a point.
    Dataclasses automatically generate __init__, __repr__, __eq__, etc.
    """
    x: float
    y: float
    
    def distance_to_origin(self) -> float:
        """Calculate distance to origin (0, 0)."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

@dataclass(frozen=True)
class ImmutablePoint:
    """
    An immutable dataclass representing a point.
    The frozen parameter makes instances immutable.
    """
    x: float
    y: float
    
    # Even with frozen=True, we can use __post_init__ for validation
    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            # This uses object.__setattr__ to bypass the frozen restriction
            # during initialization. Cannot be used after initialization.
            object.__setattr__(self, "_quadrant", "special")
        else:
            object.__setattr__(self, "_quadrant", "standard")

@dataclass
class User:
    """
    A more complex dataclass with default values, factories, and metadata.
    Shows advanced dataclass features.
    """
    name: str
    email: str
    active: bool = True
    login_count: int = 0
    
    # Private field (not included in repr)
    _last_login: Optional[str] = field(default=None, repr=False)
    
    # Using default_factory for mutable defaults
    roles: List[str] = field(default_factory=list)
    
    # Class variable (not an instance field)
    MAX_ROLES: ClassVar[int] = 5
    
    # Metadata for serialization
    metadata: Dict[str, Any] = field(default_factory=dict, metadata={"serialize": False})
    
    def __post_init__(self):
        """Runs after __init__ to perform validation or post-processing."""
        # Normalize email
        self.email = self.email.lower()
        
        # Validate roles
        if len(self.roles) > self.MAX_ROLES:
            raise ValueError(f"User cannot have more than {self.MAX_ROLES} roles")
    
    def login(self, timestamp: str) -> None:
        """Record a login."""
        self.login_count += 1
        self._last_login = timestamp
    
    @property
    def last_login(self) -> Optional[str]:
        """Get the last login time."""
        return self._last_login

# Comparing memory usage with slots
class RegularPerson:
    """A regular class with dictionary-based attributes."""
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class SlotsPerson:
    """A class that uses __slots__ to optimize memory usage."""
    __slots__ = ['name', 'age', 'email']
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

@dataclass
class DataclassPerson:
    """A dataclass version of the person."""
    name: str
    age: int
    email: str

@dataclass
class DataclassSlotsPerson:
    """A dataclass with slots for memory optimization."""
    name: str
    age: int
    email: str
    
    # Define __slots__ for dataclass
    __slots__ = ['name', 'age', 'email']

# Memory usage comparison
def measure_size(obj):
    """Measure the approximate memory size of an object."""
    return sys.getsizeof(obj)

# Using the different classes
print("\n---- Dataclass Basics ----")
point = Point(3, 4)
print(f"Point: {point}")
print(f"Distance to origin: {point.distance_to_origin()}")

immutable_point = ImmutablePoint(5, 12)
print(f"Immutable point: {immutable_point}")
print(f"Quadrant: {immutable_point._quadrant}")

try:
    # This will fail because the point is immutable
    immutable_point.x = 10
except AttributeError as e:
    print(f"Expected error: {e}")

print("\n---- Advanced Dataclass Features ----")
admin = User(
    name="Admin",
    email="ADMIN@example.com",  # Will be normalized to lowercase
    roles=["admin", "moderator"]
)
admin.login("2023-05-15 14:30:00")

print(f"User: {admin}")
print(f"Last login: {admin.last_login}")

# Convert dataclass to dictionary
admin_dict = asdict(admin)
print(f"As dictionary: {admin_dict}")

print("\n---- Memory Usage Comparison ----")
# Create instances of each class
regular = RegularPerson("John", 30, "john@example.com")
slots = SlotsPerson("John", 30, "john@example.com")
dataclass_obj = DataclassPerson("John", 30, "john@example.com")
dataclass_slots = DataclassSlotsPerson("John", 30, "john@example.com")

# Compare memory usage
print(f"RegularPerson size: {measure_size(regular)} bytes")
print(f"SlotsPerson size: {measure_size(slots)} bytes")
print(f"DataclassPerson size: {measure_size(dataclass_obj)} bytes")
print(f"DataclassSlotsPerson size: {measure_size(dataclass_slots)} bytes")

# Compare dictionary overhead
try:
    print(f"RegularPerson __dict__ size: {measure_size(regular.__dict__)} bytes")
except AttributeError:
    print("SlotsPerson has no __dict__")

try:
    print(f"SlotsPerson __dict__ size: {measure_size(slots.__dict__)} bytes")
except AttributeError:
    print("SlotsPerson has no __dict__")

try:
    print(f"DataclassPerson __dict__ size: {measure_size(dataclass_obj.__dict__)} bytes")
except AttributeError:
    print("DataclassSlotsPerson has no __dict__")

try:
    print(f"DataclassSlotsPerson __dict__ size: {measure_size(dataclass_slots.__dict__)} bytes")
except AttributeError:
    print("DataclassSlotsPerson has no __dict__")