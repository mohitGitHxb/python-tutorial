# 1. Basic Class Definition
class Person:
    """
    Simple class representing a person
    """
    # Class variable
    species = "Homo Sapiens"
    
    # Constructor
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old"
    
    # Class method
    @classmethod
    def get_species(cls):
        return cls.species
    
    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

# Usage
person1 = Person("Alice", 30)
print(person1.introduce())
print(Person.get_species())
print(Person.is_adult(20))

# 2. Inheritance Example
class Student(Person):
    """
    Student class inheriting from Person
    """
    def __init__(self, name, age, student_id):
        # Call parent class constructor
        super().__init__(name, age)
        self.student_id = student_id
    
    # Method overriding
    def introduce(self):
        return f"{super().introduce()}, Student ID: {self.student_id}"
    
    # Additional method
    def study(self):
        return f"{self.name} is studying"

# Usage
student1 = Student("Bob", 22, "S12345")
print(student1.introduce())
print(student1.study())

# 3. Advanced Inheritance and Polymorphism
class Shape:
    """
    Abstract base class for shapes
    """
    def __init__(self, color):
        self.color = color
    
    def area(self):
        """
        Abstract method to be implemented by subclasses
        """
        raise NotImplementedError("Subclass must implement abstract method")
    
    def describe(self):
        return f"A {self.color} shape"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def describe(self):
        return f"{super().describe()} rectangle"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def describe(self):
        return f"{super().describe()} circle"

# Usage of polymorphism
shapes = [
    Rectangle("red", 5, 3),
    Circle("blue", 4)
]

for shape in shapes:
    print(shape.describe())
    print(f"Area: {shape.area()}")

# 4. Composition and Aggregation
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        # Composition: Car owns the Engine
        self.engine = engine
    
    def start_car(self):
        return f"{self.make} {self.model} - {self.engine.start()}"

# Usage
my_engine = Engine(200)
my_car = Car("Toyota", "Camry", my_engine)
print(my_car.start_car())

# 5. Multiple Inheritance
class WorkerMixin:
    def work(self):
        return "Working hard"

class SalaryMixin:
    def get_salary(self):
        return 50000

class Employee(Person, WorkerMixin, SalaryMixin):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title
    
    def introduce(self):
        return f"{super().introduce()}, Job: {self.job_title}"

# Usage
employee1 = Employee("Charlie", 35, "Software Engineer")
print(employee1.introduce())
print(employee1.work())
print(employee1.get_salary())

# 6. Property Decorators and Encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self._owner = owner  # Protected attribute
        self._balance = balance  # Protected attribute
    
    # Getter
    @property
    def balance(self):
        return self._balance
    
    # Setter with validation
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
    # Deleter
    @balance.deleter
    def balance(self):
        print("Deleting balance")
        del self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

# Usage
account = BankAccount("David", 1000)
print(account.balance)
account.deposit(500)
print(account.balance)

# 7. Metaclass Example
class SingletonMeta(type):
    """
    Metaclass to create singleton classes
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected"
    
    def get_connection(self):
        return self.connection

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - Same instance

# 8. Context Manager with Classes
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage
with FileManager('example.txt', 'w') as f:
    f.write('Hello, World!')

# 9. Advanced Descriptor
class ValidatedAttribute:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name} must be a number")
        
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"{self.name} must be at least {self.min_value}")
        
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.name} must be at most {self.max_value}")
        
        instance.__dict__[self.name] = value

class Person:
    age = ValidatedAttribute(min_value=0, max_value=120)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age