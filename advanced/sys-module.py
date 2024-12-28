import sys

# 1. Basic System Information
print("=" * 50)
print("COMPREHENSIVE SYS MODULE EXPLORATION")
print("=" * 50)

# Python Version Details
print("1. Python Version Information:")
print("Python Version:", sys.version)
print("Python Version Info:", sys.version_info)
print("Python Implementation:", sys.implementation)

# 2. System Path and Environment
print("\n2. System Paths and Environment:")
print("Python Executable Path:", sys.executable)
print("System Path (sys.path):")
for path in sys.path:
    print(f"  - {path}")

# 3. System Arguments
print("\n3. System Arguments:")
print("Script Name:", sys.argv[0])
print("Full Arguments:", sys.argv)

# 4. System Limits and Configurations
print("\n4. System Limits and Configurations:")
print("Maximum Integer:", sys.maxsize)
print("Float Info:", sys.float_info)
print("Platform:", sys.platform)
print("Byte Order:", sys.byteorder)

# 5. Module Search Paths
print("\n5. Module Search Paths:")
print("Module Search Paths:")
for path in sys.path:
    print(f"  - {path}")

# 6. Standard Input/Output/Error
print("\n6. Standard Streams:")
print("Standard Input:", sys.stdin)
print("Standard Output:", sys.stdout)
print("Standard Error:", sys.stderr)

# 7. System-Specific Parameters
print("\n7. System-Specific Parameters:")
print("API Version:", sys.api_version)
print("Recursion Limit:", sys.getrecursionlimit())
print("Default Encoding:", sys.getdefaultencoding())

# 8. Advanced System Exploration Function
def explore_sys_module():
    """
    Comprehensive exploration of sys module attributes
    """
    print("\n9. Advanced Sys Module Exploration:")
    
    # Get all attributes of sys module
    sys_attrs = [attr for attr in dir(sys) if not attr.startswith('__')]
    
    print("Available sys Module Attributes:")
    for attr in sys_attrs:
        try:
            value = getattr(sys, attr)
            print(f"{attr}: {value}")
        except Exception as e:
            print(f"{attr}: Unable to retrieve value - {e}")

# 9. Memory and Performance Info
print("\n10. Memory and Performance:")
try:
    import resource
    print("Maximum Memory Usage:", resource.getrlimit(resource.RLIMIT_AS))
except ImportError:
    print("Resource module not available on this platform")

# 11. Exception Handling Information
print("\n11. Exception Handling:")
print("Last Traceback:", sys.last_traceback)
print("Last Type:", sys.last_type)
print("Last Value:", sys.last_value)

# 12. Python Flags
print("\n12. Python Flags:")
print("Optimization Level:", sys.flags.optimize)
print("Debug Mode:", sys.flags.debug)
print("Ignore Environment:", sys.flags.ignore_environment)

# 13. Interactive Mode Check
print("\n13. Interpreter Mode:")
print("Interactive Mode:", sys.flags.interactive)

# 14. Detailed Exploration Function Call
explore_sys_module()

# 15. Safe Attribute Exploration
def safe_sys_explore():
    print("\n15. Safe Sys Module Exploration:")
    for attr in dir(sys):
        if not attr.startswith('__'):
            try:
                value = getattr(sys, attr)
                print(f"{attr}: {repr(value)}")
            except Exception as e:
                print(f"{attr}: Unable to retrieve - {e}")

# Call safe exploration
safe_sys_explore()