from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Callable
from functools import partial
import copy
import time

# SINGLETON PATTERN
class Singleton:
    """
    A metaclass that creates singleton classes.
    Ensures only one instance of a class exists.
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=Singleton):
    """A database connection class that uses the Singleton pattern."""
    def __init__(self, host="localhost", port=5432):
        print(f"Creating new connection to {host}:{port}")
        self.host = host
        self.port = port
        self.connected = False
    
    def connect(self):
        """Connect to the database."""
        if not self.connected:
            print(f"Connecting to {self.host}:{self.port}")
            self.connected = True
        return self
    
    def query(self, sql):
        """Execute a query."""
        if not self.connected:
            raise RuntimeError("Not connected to database")
        print(f"Executing query: {sql}")
        return [{"result": "data"}]  # Dummy response

# FACTORY METHOD PATTERN
class Document(ABC):
    """Abstract document base class."""
    @abstractmethod
    def create(self) -> None:
        """Create the document."""
        pass

class PDFDocument(Document):
    """PDF document implementation."""
    def create(self) -> None:
        return "Creating PDF document"

class WordDocument(Document):
    """Word document implementation."""
    def create(self) -> None:
        return "Creating Word document"

class DocumentFactory:
    """Factory for creating documents of different types."""
    @staticmethod
    def create_document(doc_type: str) -> Document:
        """Create a document of the specified type."""
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        else:
            raise ValueError(f"Unknown document type: {doc_type}")

# OBSERVER PATTERN
class Subject:
    """
    Subject in the Observer pattern.
    Maintains a list of observers and notifies them of state changes.
    """
    def __init__(self):
        self._observers: List[Observer] = []
        self._state = None
    
    def attach(self, observer: 'Observer') -> None:
        """Attach an observer to the subject."""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: 'Observer') -> None:
        """Detach an observer from the subject."""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self) -> None:
        """Notify all observers of state change."""
        for observer in self._observers:
            observer.update(self)
    
    @property
    def state(self) -> Any:
        """Get the subject's state."""
        return self._state
    
    @state.setter
    def state(self, state: Any) -> None:
        """Set the subject's state and notify observers."""
        self._state = state
        self.notify()

class Observer(ABC):
    """Abstract observer base class."""
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """Update the observer, usually called by the subject."""
        pass

class ConcreteObserverA(Observer):
    """Concrete observer implementation A."""
    def update(self, subject: Subject) -> None:
        if subject.state < 3:
            print(f"ConcreteObserverA: Reacted to the event. State is {subject.state}")

class ConcreteObserverB(Observer):
    """Concrete observer implementation B."""
    def update(self, subject: Subject) -> None:
        if subject.state >= 3:
            print(f"ConcreteObserverB: Reacted to the event. State is {subject.state}")

# STRATEGY PATTERN
class Strategy(ABC):
    """Strategy interface."""
    @abstractmethod
    def execute(self, data: List[int]) -> List[int]:
        """Execute the strategy."""
        pass

class BubbleSortStrategy(Strategy):
    """Bubble sort implementation of the strategy."""
    def execute(self, data: List[int]) -> List[int]:
        """Sort using bubble sort."""
        print("Sorting using bubble sort")
        result = data.copy()
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
        return result

class QuickSortStrategy(Strategy):
    """Quick sort implementation of the strategy."""
    def execute(self, data: List[int]) -> List[int]:
        """Sort using quick sort."""
        print("Sorting using quick sort")
        result = data.copy()
        if len(result) <= 1:
            return result
        
        pivot = result[len(result) // 2]
        left = [x for x in result if x < pivot]
        middle = [x for x in result if x == pivot]
        right = [x for x in result if x > pivot]
        
        return self.execute(left) + middle + self.execute(right)

class Sorter:
    """Context class that uses a strategy."""
    def __init__(self, strategy: Strategy = None):
        self._strategy = strategy
    
    @property
    def strategy(self) -> Strategy:
        """Get the current strategy."""
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Set the strategy."""
        self._strategy = strategy
    
    def sort(self, data: List[int]) -> List[int]:
        """Sort the data using the selected strategy."""
        if self._strategy is None:
            raise RuntimeError("Strategy not set")
        return self._strategy.execute(data)

# DECORATOR PATTERN
class Component(ABC):
    """Component interface."""
    @abstractmethod
    def operation(self) -> str:
        """Basic operation."""
        pass

class ConcreteComponent(Component):
    """Concrete component implementation."""
    def operation(self) -> str:
        return "ConcreteComponent"

class Decorator(Component, ABC):
    """Base decorator class."""
    def __init__(self, component: Component):
        self._component = component
    
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteDecoratorA(Decorator):
    """Concrete decorator A implementation."""
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    """Concrete decorator B implementation."""
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self._component.operation()})"

# COMMAND PATTERN
class Command(ABC):
    """Command interface."""
    @abstractmethod
    def execute(self) -> None:
        """Execute the command."""
        pass
    
    @abstractmethod
    def undo(self) -> None:
        """Undo the command."""
        pass

class TextEditor:
    """Receiver class."""
    def __init__(self):
        self.text = ""
    
    def insert_text(self, text: str) -> None:
        """Insert text at the end."""
        self.text += text
    
    def delete_text(self, length: int) -> str:
        """Delete text from the end."""
        if length <= 0:
            return ""
        
        deleted = self.text[-length:]
        self.text = self.text[:-length]
        return deleted

class InsertTextCommand(Command):
    """Command to insert text."""
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text
    
    def execute(self) -> None:
        """Insert the text."""
        self.editor.insert_text(self.text)
    
    def undo(self) -> None:
        """Undo the text insertion."""
        self.editor.delete_text(len(self.text))

class DeleteTextCommand(Command):
    """Command to delete text."""
    def __init__(self, editor: TextEditor, length: int):
        self.editor = editor
        self.length = length
        self.deleted_text = ""
    
    def execute(self) -> None:
        """Delete the text."""
        self.deleted_text = self.editor.delete_text(self.length)
    
    def undo(self) -> None:
        """Undo the text deletion."""
        self.editor.insert_text(self.deleted_text)

class CommandHistory:
    """Command history for undo/redo."""
    def __init__(self):
        self.history: List[Command] = []
        self.current = -1
    
    def execute(self, command: Command) -> None:
        """Execute a command and add it to history."""
        # Remove any undone commands
        if self.current < len(self.history) - 1:
            self.history = self.history[:self.current + 1]
        
        command.execute()
        self.history.append(command)
        self.current += 1
    
    def undo(self) -> bool:
        """Undo the last command."""
        if self.current >= 0:
            self.history[self.current].undo()
            self.current -= 1
            return True
        return False
    
    def redo(self) -> bool:
        """Redo the last undone command."""
        if self.current < len(self.history) - 1:
            self.current += 1
            self.history[self.current].execute()
            return True
        return False

# COMPOSITE PATTERN
class FileSystemComponent(ABC):
    """Component interface for file system items."""
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component."""
        pass
    
    @abstractmethod
    def print_details(self, indent: str = "") -> None:
        """Print details of the component."""
        pass

class File(FileSystemComponent):
    """Leaf component representing a file."""
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size
    
    def get_size(self) -> int:
        """Get the file size."""
        return self.size
    
    def print_details(self, indent: str = "") -> None:
        """Print file details."""
        print(f"{indent}File: {self.name} ({self.size} bytes)")

class Directory(FileSystemComponent):
    """Composite component representing a directory."""
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []
    
    def add(self, component: FileSystemComponent) -> None:
        """Add a component to the directory."""
        self.children.append(component)
    
    def remove(self, component: FileSystemComponent) -> None:
        """Remove a component from the directory."""
        self.children.remove(component)
    
    def get_size(self) -> int:
        """Get the total size of the directory."""
        return sum(child.get_size() for child in self.children)
    
    def print_details(self, indent: str = "") -> None:
        """Print directory details."""
        print(f"{indent}Directory: {self.name} ({self.get_size()} bytes)")
        for child in self.children:
            child.print_details(indent + "  ")

# Demonstration of the design patterns
print("\n---- SINGLETON PATTERN ----")
# First connection
db1 = DatabaseConnection().connect()
db1.query("SELECT * FROM users")

# Second connection should be the same instance
db2 = DatabaseConnection()
print(f"Are db1 and db2 the same object? {db1 is db2}")

print("\n---- FACTORY METHOD PATTERN ----")
factory = DocumentFactory()
pdf = factory.create_document("pdf")
word = factory.create_document("word")
print(pdf.create())
print(word.create())

print("\n---- OBSERVER PATTERN ----")
subject = Subject()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject.state = 2  # Should notify observer A
subject.state = 5  # Should notify observer B

subject.detach(observer_a)
subject.state = 1  # Should not notify observer A

print("\n---- STRATEGY PATTERN ----")
sorter = Sorter()

# Use bubble sort
sorter.strategy = BubbleSortStrategy()
result1 = sorter.sort([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Bubble sort result: {result1}")

# Switch to quick sort
sorter.strategy = QuickSortStrategy()
result2 = sorter.sort([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Quick sort result: {result2}")

print("\n---- DECORATOR PATTERN ----")
simple = ConcreteComponent()
print(f"Simple component: {simple.operation()}")

decorator1 = ConcreteDecoratorA(simple)
print(f"Decorated once: {decorator1.operation()}")

decorator2 = ConcreteDecoratorB(decorator1)
print(f"Decorated twice: {decorator2.operation()}")

print("\n---- COMMAND PATTERN ----")
editor = TextEditor()
history = CommandHistory()