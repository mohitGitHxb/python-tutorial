import logging
import sys
import os
from typing import Any, Callable
from functools import wraps
from contextlib import contextmanager

# Advanced Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app_errors.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Custom Exception Hierarchy
class BaseApplicationError(Exception):
    """Base application-level exception"""
    def __init__(self, message, error_code=None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

class DatabaseConnectionError(BaseApplicationError):
    """Specific exception for database connection issues"""
    pass

class ValidationError(BaseApplicationError):
    """Exception for data validation failures"""
    pass

# Decorator for Exception Handling and Logging
def exception_handler(
    log_level=logging.ERROR, 
    reraise=False, 
    default_return=None
):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.log(log_level, f"Exception in {func.__name__}: {e}", exc_info=True)
                
                if isinstance(e, (DatabaseConnectionError, ValidationError)):
                    # Special handling for specific exceptions
                    logger.critical(f"Critical Error: {e}")
                
                if reraise:
                    raise
                return default_return
        return wrapper
    return decorator

# Context Manager for Resource Management
@contextmanager
def managed_resource(resource_factory, cleanup_func):
    resource = None
    try:
        resource = resource_factory()
        yield resource
    except Exception as e:
        logger.error(f"Resource management error: {e}")
        raise
    finally:
        if resource:
            cleanup_func(resource)

# Advanced Error Handling Class
class ErrorManager:
    @staticmethod
    def validate_input(value: Any, validators: list) -> bool:
        """
        Validate input against multiple validation rules
        
        Args:
            value: Input to validate
            validators: List of validation functions
        
        Raises:
            ValidationError if validation fails
        """
        try:
            for validator in validators:
                if not validator(value):
                    raise ValidationError(f"Validation failed for {value}")
            return True
        except Exception as e:
            logger.error(f"Validation error: {e}")
            raise

    @staticmethod
    def retry_operation(
        operation: Callable, 
        max_retries: int = 3, 
        delay: float = 1.0
    ):
        """
        Retry an operation with exponential backoff
        
        Args:
            operation: Function to retry
            max_retries: Maximum number of retry attempts
            delay: Initial delay between retries
        """
        import time
        
        for attempt in range(max_retries):
            try:
                return operation()
            except Exception as e:
                if attempt == max_retries - 1:
                    logger.error(f"Operation failed after {max_retries} attempts")
                    raise
                
                wait_time = delay * (2 ** attempt)
                logger.warning(f"Attempt {attempt + 1} failed. Retrying in {wait_time} seconds")
                time.sleep(wait_time)

# Comprehensive Example with Multiple Error Handling Techniques
class DataProcessor:
    @exception_handler(reraise=False, default_return=[])
    def process_data(self, data: list) -> list:
        """
        Process data with comprehensive error handling
        
        Args:
            data: Input data list
        
        Returns:
            Processed data or empty list on error
        """
        # Input validation
        ErrorManager.validate_input(data, [
            lambda x: isinstance(x, list),
            lambda x: len(x) > 0
        ])
        
        # Simulated complex processing with potential errors
        processed_data = []
        for item in data:
            try:
                # Simulate complex transformation
                processed_item = self._transform_item(item)
                processed_data.append(processed_item)
            except ValueError as ve:
                logger.warning(f"Skipping invalid item: {item}")
        
        return processed_data
    
    def _transform_item(self, item):
        # Simulate item transformation with potential errors
        if not isinstance(item, (int, float)):
            raise ValueError(f"Invalid item type: {type(item)}")
        return item * 2

# Global Exception Handler
def global_exception_handler(exc_type, exc_value, exc_traceback):
    """
    Global unhandled exception handler
    
    Args:
        exc_type: Exception type
        exc_value: Exception value
        exc_traceback: Traceback object
    """
    logger.critical(
        "Uncaught exception",
        exc_info=(exc_type, exc_value, exc_traceback)
    )
    # Optional: Send error report, trigger monitoring alert
    sys.__excepthook__(exc_type, exc_value, exc_traceback)

sys.excepthook = global_exception_handler

# Main Execution
def main():
    try:
        # Simulated database connection with retry
        def connect_to_database():
            raise DatabaseConnectionError("Connection failed")
        
        ErrorManager.retry_operation(
            connect_to_database, 
            max_retries=3
        )
        
        # Resource management
        with managed_resource(
            resource_factory=lambda: open('temp.txt', 'w'),
            cleanup_func=lambda f: f.close()
        ) as file:
            file.write("Hello, Error Handling!")
        
        # Data processing
        processor = DataProcessor()
        result = processor.process_data([1, 2, 'invalid', 3, 4])
        print(f"Processed data: {result}")
    
    except BaseApplicationError as bae:
        logger.error(f"Application Error: {bae.message}")
    except Exception as e:
        logger.exception("Unexpected error occurred",e)

if __name__ == "__main__":
    main()