import time
import contextlib
from datetime import datetime

class Timer:
    """
    A context manager that times code execution.
    Demonstrates the context manager protocol (__enter__, __exit__).
    """
    def __init__(self, name=None):
        self.name = name or "Timer"
    
    def __enter__(self):
        """Called when entering the 'with' block."""
        self.start_time = time.time()
        print(f"{self.name} started at {datetime.now().strftime('%H:%M:%S')}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exiting the 'with' block.
        Parameters allow handling exceptions that occurred in the block.
        """
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time
        print(f"{self.name} ended, took {self.elapsed:.4f} seconds")
        
        # Returning True would suppress any exception
        return False

# Using the context manager with the 'with' statement
with Timer("Sleep operation"):
    # Code inside the 'with' block is timed
    time.sleep(1)
    print("Slept for 1 second")

# Creating a context manager with @contextmanager decorator
@contextlib.contextmanager
def managed_resource(name):
    """
    A generator-based context manager.
    Demonstrates how to create context managers with the @contextmanager decorator.
    """
    print(f"Acquiring {name}...")
    resource = {"name": name, "value": 42}  # Simulate resource acquisition
    
    try:
        yield resource  # Provide the resource to the with block
    except Exception as e:
        # Handle exceptions if needed
        print(f"Exception occurred while using {name}: {e}")
        raise  # Re-raise the exception
    finally:
        # Clean up code that always runs
        print(f"Releasing {name}...")

# Use the generator-based context manager
with managed_resource("database connection") as db:
    print(f"Using {db['name']}, value: {db['value']}")
    # Simulate some work
    time.sleep(0.5)

# Nested context managers and exception handling
try:
    with Timer("Outer operation"):
        with Timer("Inner operation"):
            print("Doing some work...")
            time.sleep(0.3)
            
        with managed_resource("temporary file") as temp:
            print(f"Working with {temp['name']}...")
            time.sleep(0.2)
            
            # Uncomment to see exception handling
            # raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"Caught exception: {e}")