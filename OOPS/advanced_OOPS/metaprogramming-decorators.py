import functools
import time
import inspect
from typing import Any, Callable, TypeVar, cast

# Type hint for function
F = TypeVar('F', bound=Callable[..., Any])

def debug(func: F) -> F:
    """
    A decorator that logs function calls and their arguments.
    Shows basic decorator usage with functools.wraps to preserve metadata.
    """
    @functools.wraps(func)  # Preserves function metadata (name, docstring, etc.)
    def wrapper(*args, **kwargs):
        # Get function signature
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        # Format arguments for printing
        args_str = ", ".join(f"{k}={v!r}" for k, v in bound_args.arguments.items())
        
        print(f"Calling {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    
    return cast(F, wrapper)  # Type hint to help static analyzers

def retry(attempts: int = 3, delay: float = 1.0, backoff: float = 2.0) -> Callable[[F], F]:
    """
    A parametrized decorator that retries a function on exception.
    Shows how to create decorators that take parameters.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            local_attempts, local_delay = attempts, delay
            while local_attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    local_attempts -= 1
                    if local_attempts <= 0:
                        raise
                    print(f"Exception in {func.__name__}: {e}. Retrying in {local_delay:.2f}s...")
                    time.sleep(local_delay)
                    local_delay *= backoff  # Exponential backoff
            return None  # Should never reach here
        return cast(F, wrapper)
    return decorator

def enforce_types(func: F) -> F:
    """
    A decorator that enforces type annotations at runtime.
    Shows how to use function introspection for validation.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        
        # Check types
        for param_name, param in sig.parameters.items():
            if param.annotation != inspect.Parameter.empty:
                value = bound_args.arguments.get(param_name)
                if value is not None and not isinstance(value, param.annotation):
                    raise TypeError(
                        f"Parameter '{param_name}' expected {param.annotation.__name__}, "
                        f"got {type(value).__name__}"
                    )
        
        # Check return type
        result = func(*args, **kwargs)
        return_annotation = sig.return_annotation
        
        if (return_annotation != inspect.Signature.empty and 
            result is not None and 
            not isinstance(result, return_annotation)):
            raise TypeError(
                f"Return value expected {return_annotation.__name__}, "
                f"got {type(result).__name__}"
            )
        
        return result
    
    return cast(F, wrapper)

class Cache:
    """
    A class-based decorator for memoization.
    Shows how to create stateful decorators using classes.
    """
    def __init__(self, func: Callable):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)  # Update wrapper attributes
    
    def __call__(self, *args, **kwargs):
        # Create a hashable key from the arguments
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kwargs)
            print(f"Cache miss for {self.func.__name__}{args}")
        else:
            print(f"Cache hit for {self.func.__name__}{args}")
        
        return self.cache[key]
    
    def clear_cache(self):
        """Clear the cache."""
        self.cache.clear()

# Demonstration of the decorators
@debug
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

@retry(attempts=2, delay=0.5)
def unstable_operation(success_on_attempt: int) -> str:
    """A function that fails occasionally."""
    static_var = getattr(unstable_operation, '_attempt', 0) + 1
    unstable_operation._attempt = static_var
    
    if static_var < success_on_attempt:
        raise ValueError(f"Failed on attempt {static_var}")
    return "Operation successful!"

@enforce_types
def add(a: int, b: int) -> int:
    """Add two numbers with type checking."""
    return a + b

@Cache
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number with memoization."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Using the decorated functions
print(greet("Alice"))

try:
    print(unstable_operation(2))  # Will succeed on the 2nd attempt
    
    # Reset the static variable for another test
    unstable_operation._attempt = 0
    print(unstable_operation(4))  # Will fail as we only retry once
except ValueError as e:
    print(f"Expected error: {e}")

print(add(5, 3))

try:
    print(add("5", 3))  # Type error
except TypeError as e:
    print(f"Expected type error: {e}")

# Test the memoization
print(f"Fibonacci of 8: {fibonacci(8)}")
print(f"Fibonacci of 8 (cached): {fibonacci(8)}")