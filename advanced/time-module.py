# 1. time.time() - Returns current timestamp in seconds since epoch
import time

current_timestamp = time.time()
print(current_timestamp)  # Output: 1621234567.890123

# Advanced usage: Measuring execution time
start_time = time.time()
# Some time-consuming operation
for _ in range(1000000):
    pass
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")

# 2. time.sleep() - Pauses program execution

time.sleep(2)  # Pause for 2 seconds

# Advanced usage: Implementing retry mechanism
max_retries = 3
for attempt in range(max_retries):
    try:
        # result = perform_risky_operation()
        break
    except Exception:
        print(f"Attempt {attempt + 1} failed. Retrying...")
        time.sleep(2)  # Wait before retry

# Basic usage
current_time = time.localtime()
print(current_time)  # Struct_time object

# Extracting specific time components
print(f"Year: {current_time.tm_year}")
print(f"Month: {current_time.tm_mon}")
print(f"Day: {current_time.tm_mday}")

# Advanced formatting
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(formatted_time)


# Various time format examples
current_time = time.localtime()

# Different date formats
print(time.strftime("%Y/%m/%d", current_time))  # 2023/05/18
print(time.strftime("%d-%b-%Y", current_time))  # 18-May-2023
print(time.strftime("%I:%M %p", current_time))  # 10:30 AM

# Logging with timestamps
def log_event(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

log_event("Application started")
log_event("Processing data")


# Parsing date strings
date_string = "21 June, 2023"
parsed_time = time.strptime(date_string, "%d %B, %Y")
print(parsed_time)

# Converting between formats
input_date = "2023-06-21"
parsed_time = time.strptime(input_date, "%Y-%m-%d")
formatted_date = time.strftime("%d/%m/%Y", parsed_time)
print(formatted_date)  # 21/06/2023



# Precise performance measurement
def expensive_function():
    return sum(range(1000000))

start = time.perf_counter()
result = expensive_function()
end = time.perf_counter()

print(f"Function execution time: {end - start:.6f} seconds")

# Benchmarking multiple implementations
def method1():
    return sum(range(1000000))

def method2():
    return sum(x for x in range(1000000))

def benchmark(func, iterations=10):
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / iterations

print(f"Method 1 avg time: {benchmark(method1)}")
print(f"Method 2 avg time: {benchmark(method2)}")






class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            self.calls = [call for call in self.calls if current_time - call < self.period]
            
            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (current_time - self.calls[0])
                time.sleep(sleep_time)
            
            result = func(*args, **kwargs)
            self.calls.append(time.time())
            return result
        return wrapper

@RateLimiter(max_calls=3, period=5)
def api_call():
    print("API called")

# This will respect the rate limit
for _ in range(10):
    api_call()