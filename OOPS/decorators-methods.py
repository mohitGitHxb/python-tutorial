# 1. Basic Function Decorator
def simple_decorator(func):
    """
    Basic decorator that wraps a function
    """
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f"Hello, {name}")

greet("Alice")

# 2. Function Timing Decorator
import time
import functools

def timer_decorator(func):
    """
    Decorator to measure function execution time
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Slow function completed")

slow_function()

# 3. Logging Decorator
import logging

def log_decorator(func):
    """
    Decorator to log function calls and arguments
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} returned {result}")
            return result
        except Exception as e:
            logging.error(f"Exception in {func.__name__}: {e}")
            raise
    return wrapper

@log_decorator
def divide(a, b):
    return a / b

divide(10, 2)

# 4. Authentication Decorator
def authenticate(func):
    """
    Decorator to check user authentication
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Simulated authentication check
        user = kwargs.get('user')
        if not user or not user.get('is_authenticated'):
            raise PermissionError("User not authenticated")
        return func(*args, **kwargs)
    return wrapper

class User:
    def __init__(self, is_authenticated=False):
        self.is_authenticated = is_authenticated

@authenticate
def sensitive_operation(user=None, data=None):
    print("Performing sensitive operation")

# Usage
authenticated_user = User(is_authenticated=True)
sensitive_operation(user=authenticated_user, data="secret")

# 5. Retry Decorator
def retry(max_attempts=3, delay=1):
    """
    Decorator to retry a function multiple times
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=1)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

# 6. Caching Decorator
def memoize(func):
    """
    Decorator to cache function results
    """
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a hashable key from arguments
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 7. Parameter Validation Decorator
def validate_types(*types, **type_kwargs):
    """
    Decorator to validate function argument types
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Validate positional arguments
            for (arg, expected_type) in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument must be {expected_type}")
            
            # Validate keyword arguments
            for (name, expected_type) in type_kwargs.items():
                if name in kwargs and not isinstance(kwargs[name], expected_type):
                    raise TypeError(f"{name} must be {expected_type}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int, result=str)
def multiply_and_convert(a, b, result=None):
    return str(a * b) if result else a * b

# 8. Context Manager Decorator
def context_manager_decorator(func):
    """
    Decorator that acts like a context manager
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Setup
            print("Entering context")
            result = func(*args, **kwargs)
            return result
        finally:
            # Cleanup
            print("Exiting context")
    return wrapper

@context_manager_decorator
def database_operation():
    print("Performing database operation")

# 9. Rate Limiting Decorator
import time

def rate_limit(max_calls, time_frame):
    """
    Decorator to limit function calls
    """
    calls = []
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            # Remove old calls
            calls[:] = [call for call in calls if current_time - call < time_frame]
            
            if len(calls) >= max_calls:
                raise RuntimeError("Rate limit exceeded")
            
            calls.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, time_frame=60)
def api_call():
    print("API called")

# 10. Class Decorator
def singleton(cls):
    """
    Decorator to create a singleton class
    """
    _instance = {}
    def get_instance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected"

# 11. Async Decorator
import asyncio

def async_retry(max_attempts=3):
    """
    Decorator for retrying async functions
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    await asyncio.sleep(1)
        return wrapper
    return decorator

# Example usage demonstrations
if __name__ == "__main__":
    # Demonstrate various decorators
    
    # Simple decorator
    @simple_decorator
    def example_func():
        print("Function body")
    
    example_func()
    
    # Timing decorator
    @timer_decorator
    def long_running_task():
        time.sleep(1)
        print("Task completed")
    
    long_running_task()
    
    # Parameter validation
    try:
        multiply_and_convert(5, 3, result="string")
    except TypeError as e:
        print(f"Validation error: {e}")


# 12. Dependency Injection Decorator
class DependencyContainer:
    """
    Dependency injection container
    """
    _dependencies = {}
    
    @classmethod
    def register(cls, interface, implementation):
        cls._dependencies[interface] = implementation
    
    @classmethod
    def resolve(cls, interface):
        return cls._dependencies.get(interface)

def inject(*dependencies):
    """
    Decorator for dependency injection
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Resolve dependencies
            resolved_deps = []
            for dep in dependencies:
                implementation = DependencyContainer.resolve(dep)
                if implementation is None:
                    raise ValueError(f"No implementation found for {dep}")
                resolved_deps.append(implementation())
            
            # Merge resolved dependencies with existing arguments
            new_args = list(args) + resolved_deps
            return func(*new_args, **kwargs)
        return wrapper
    return decorator

# Usage example
class DatabaseInterface:
    def connect(self):
        pass

class PostgresDatabase(DatabaseInterface):
    def connect(self):
        print("Connecting to PostgreSQL")

# Register dependency
DependencyContainer.register(DatabaseInterface, PostgresDatabase)

@inject(DatabaseInterface)
def perform_database_operation(db):
    db.connect()

# 13. Profiling Decorator
import cProfile
import pstats
import io

def profile(output=False):
    """
    Advanced profiling decorator
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            
            # Execute the function
            result = func(*args, **kwargs)
            
            pr.disable()
            
            # Capture profiling output
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
            ps.print_stats()
            
            if output:
                print(s.getvalue())
            
            return result
        return wrapper
    return decorator

@profile(output=True)
def complex_calculation():
    return sum(i**2 for i in range(10000))

# 14. Circuit Breaker Decorator
import time
from functools import wraps

class CircuitBreakerException(Exception):
    """Custom exception for circuit breaker"""
    pass

def circuit_breaker(
    failure_threshold=3, 
    recovery_timeout=30
):
    """
    Circuit breaker decorator to prevent repeated failures
    """
    def decorator(func):
        func.failures = 0
        func.last_failure_time = 0
        func.state = "CLOSED"
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            # Check if in open state and recovery time has passed
            if (func.state == "OPEN" and 
                current_time - func.last_failure_time > recovery_timeout):
                func.state = "HALF_OPEN"
            
            # If circuit is open, raise exception
            if func.state == "OPEN":
                raise CircuitBreakerException("Circuit is OPEN")
            
            try:
                result = func(*args, **kwargs)
                
                # Reset failures if successful
                if func.state == "HALF_OPEN":
                    func.state = "CLOSED"
                func.failures = 0
                
                return result
            
            except Exception as e:
                # Track failures
                func.failures += 1
                func.last_failure_time = current_time
                
                # Open circuit if threshold reached
                if func.failures >= failure_threshold:
                    func.state = "OPEN"
                
                raise
        
        return wrapper
    return decorator

# 15. Throttle Decorator
def throttle(max_calls, time_period):
    """
    Decorator to limit function calls within a time period
    """
    def decorator(func):
        calls = []
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            # Remove calls outside the time window
            calls[:] = [
                call_time for call_time in calls 
                if current_time - call_time < time_period
            ]
            
            # Check if max calls exceeded
            if len(calls) >= max_calls:
                raise RuntimeError("Throttle limit exceeded")
            
            # Record current call
            calls.append(current_time)
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

# 16. Transactional Decorator
class TransactionManager:
    def __init__(self):
        self.transactions = []
    
    def begin(self):
        transaction = {}
        self.transactions.append(transaction)
        return transaction
    
    def commit(self):
        if self.transactions:
            self.transactions.pop()
    
    def rollback(self):
        if self.transactions:
            self.transactions.pop()

def transactional(func):
    """
    Decorator to manage database-like transactions
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        transaction_manager = TransactionManager()
        try:
            # Begin transaction
            transaction = transaction_manager.begin()
            
            # Execute function
            result = func(*args, **kwargs)
            
            # Commit transaction
            transaction_manager.commit()
            
            return result
        except Exception as e:
            # Rollback on error
            transaction_manager.rollback()
            raise
    return wrapper

# Example usage
@transactional
def update_user_data(user_id, data):
    # Simulated database operation
    print(f"Updating user {user_id} with {data}")
    # Simulate potential failure
    if not data:
        raise ValueError("Invalid data")

# Demonstration of decorators
def demonstrate_decorators():
    # Dependency Injection
    perform_database_operation()
    
    # Profiling
    complex_calculation()
    
    # Circuit Breaker
    @circuit_breaker(failure_threshold=2)
    def unreliable_function():
        import random
        if random.random() < 0.5:
            raise Exception("Random failure")
        return "Success"
    
    # Throttle
    @throttle(max_calls=3, time_period=10)
    def rate_limited_function():
        print("Function called")
    
    # Transactional
    update_user_data(1, {"name": "John"})

# Run demonstrations
demonstrate_decorators()