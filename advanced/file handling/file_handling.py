# 1. open() - Basic File Opening
"""
Basic syntax: open(file_path, mode)
Modes:
- 'r': Read (default)
- 'w': Write (creates/overwrites)
- 'a': Append
- 'x': Exclusive creation
- 'b': Binary mode
- '+': Read and Write
"""
# Basic usage
file = open('example.txt', 'r')
content = file.read()
file.close()

# Advanced usage with context manager
with open('example.txt', 'r') as file:
    content = file.read()
    # File automatically closes after block

# 2. read() - Reading File Contents
"""
Methods to read file contents:
- read(): Read entire file
- readline(): Read single line
- readlines(): Read all lines as list
"""
# Basic reading
with open('example.txt', 'r') as file:
    # Read entire file
    full_content = file.read()
    
    # Read specific number of characters
    partial_content = file.read(50)
    
    # Read line by line
    file.seek(0)  # Reset file pointer
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# 3. write() - Writing to Files
"""
Writing methods:
- write(): Write string
- writelines(): Write list of strings
"""
# Basic writing
with open('output.txt', 'w') as file:
    file.write("Hello, World!")
    
    # Writing multiple lines
    lines = ['First line\n', 'Second line\n']
    file.writelines(lines)

# 4. append() - Adding to Existing Files
"""
Appending to files without overwriting
"""
with open('log.txt', 'a') as file:
    file.write("New log entry\n")

# 5. tell() - Get Current File Position
"""
Returns current position in file
"""
with open('example.txt', 'r') as file:
    current_position = file.tell()
    print(f"Current position: {current_position}")

# 6. seek() - Move File Pointer
"""
Move file pointer to specific position
"""
with open('example.txt', 'r') as file:
    # Move to 10th byte
    file.seek(10)
    content = file.read()

# 7. os Module for File Handling
import os

# Check file existence
if os.path.exists('example.txt'):
    print("File exists")

# Get file size
file_size = os.path.getsize('example.txt')

# Delete file
os.remove('example.txt')

# 8. Advanced File Reading with Encoding
"""
Handling different character encodings
"""
with open('international.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 9. CSV File Handling
import csv

# Reading CSV
with open('data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)

# Writing CSV
with open('output.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerows([
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'San Francisco']
    ])

# 10. JSON File Handling
import json

# Writing JSON
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Reading JSON
with open('data.json', 'r') as jsonfile:
    loaded_data = json.load(jsonfile)
    print(loaded_data)

# 11. Binary File Handling
"""
Reading and writing binary files
"""
# Writing binary
with open('image.bin', 'wb') as binfile:
    binfile.write(b'\x00\x01\x02\x03')

# Reading binary
with open('image.bin', 'rb') as binfile:
    binary_data = binfile.read()

# 12. File Permissions and Info
import os

# Get file permissions
file_stats = os.stat('example.txt')
print(f"File size: {file_stats.st_size}")
print(f"File permissions: {oct(file_stats.st_mode)}")

# 13. Temporary File Handling
import tempfile

# Create temporary file
with tempfile.TemporaryFile() as temp:
    temp.write(b'Some temporary data')
    temp.seek(0)
    print(temp.read())

# 14. Buffered I/O Operations
"""
Buffered file reading and writing for improved performance
"""
# Buffered reading
with open('large_file.txt', 'r', buffering=1024*1024) as file:
    # 1MB buffer
    content = file.read()

# 15. Fileinput Module for Multiple File Processing
import fileinput

# Process multiple input files
with fileinput.input(files=('file1.txt', 'file2.txt')) as f:
    for line in f:
        print(f"File {f.filename()}, Line {f.lineno()}: {line.strip()}")

# 16. Pathlib - Modern Path Handling
from pathlib import Path

# Create path object
file_path = Path('documents/example.txt')

# Check file properties
print(file_path.exists())
print(file_path.is_file())
print(file_path.suffix)  # .txt
print(file_path.stem)    # example

# Read file using Path
content = file_path.read_text()

# Write file using Path
file_path.write_text("New content")

# 17. Mmap - Memory-Mapped File Handling
import mmap

# Memory-mapped file reading (efficient for large files)
with open('large_file.bin', 'rb') as file:
    # Map entire file to memory
    mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
    
    # Read specific section
    specific_section = mmapped_file[100:200]
    
    # Close mapping
    mmapped_file.close()

# 18. Pickle - Serialization of Python Objects
import pickle

# Serialize object to file
data = {'name': 'John', 'age': 30}
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize from file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

# 19. Comprehensive File Locking
import fcntl

# File locking for concurrent access
def write_with_lock(filename, content):
    with open(filename, 'a') as file:
        try:
            # Acquire an exclusive lock
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
            file.write(content + '\n')
        finally:
            # Release the lock
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)

# 20. Advanced File Searching
import glob

# Find files with pattern
txt_files = glob.glob('*.txt')
python_files = glob.glob('**/*.py', recursive=True)

# 21. File Compression Handling
import gzip
import shutil

# Compress file
with open('large_file.txt', 'rb') as f_in:
    with gzip.open('large_file.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# Decompress file
with gzip.open('large_file.txt.gz', 'rb') as f_in:
    with open('decompressed_file.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# 22. Async File I/O (Python 3.7+)
import aiofiles

async def async_file_read():
    async with aiofiles.open('example.txt', mode='r') as file:
        content = await file.read()
        return content

# 23. File Diff and Patch
import difflib

# Compare two files
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    diff = list(difflib.unified_diff(
        file1.readlines(), 
        file2.readlines(), 
        fromfile='file1.txt', 
        tofile='file2.txt'
    ))
    
    # Print differences
    print(''.join(diff))

# 24. Robust File Reading with Error Handling
def safe_file_read(filename, encoding='utf-8', errors='replace'):
    """
    Safely read file with error handling
    
    Args:
        filename (str): Path to the file
        encoding (str): File encoding
        errors (str): Error handling strategy
    
    Returns:
        str: File content or None if error occurs
    """
    try:
        with open(filename, 'r', encoding=encoding, errors=errors) as file:
            return file.read()
    except (IOError, PermissionError) as e:
        print(f"Error reading file: {e}")
        return None

# 25. File Rotation and Logging
import logging
from logging.handlers import RotatingFileHandler

# Create a rotating file handler
logger = logging.getLogger('MyLogger')
handler = RotatingFileHandler(
    'app.log', 
    maxBytes=1024*1024,  # 1 MB
    backupCount=3
)
logger.addHandler(handler)