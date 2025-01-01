import stat
import os
import time
import platform
'''
print(os.name)
print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.basename(os.path.abspath(__file__)))
print(os.path.split(os.path.abspath(__file__)))
print(os.path.splitext(os.path.abspath(__file__)))

'''
# 1. os.getcwd() - Get Current Working Directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# Advanced usage: Safe directory navigation
def safe_change_directory(target_dir):
    try:
        original_dir = os.getcwd()
        os.chdir(target_dir)
        return original_dir
    except FileNotFoundError:
        print(f"Directory {target_dir} not found")
        return None

# 2. os.mkdir() - Create a Single Directory
os.mkdir('new_directory')

# Advanced usage: Create directory with error handling
def create_project_directory(project_name):
    try:
        os.mkdir(project_name)
        print(f"Project directory '{project_name}' created successfully")
    except FileExistsError:
        print(f"Directory '{project_name}' already exists")

# 3. os.makedirs() - Create Nested Directories
os.makedirs('path/to/nested/directories', exist_ok=True)

# Advanced usage: Create project structure
def setup_project_structure(base_path):
    directories = [
        'src', 
        'tests', 
        'docs', 
        'config'
    ]
    for dir_name in directories:
        full_path = os.path.join(base_path, dir_name)
        os.makedirs(full_path, exist_ok=True)
    print("Project structure created")

# 4. os.listdir() - List Directory Contents
dir_contents = os.listdir('.')
print("Directory Contents:", dir_contents)

# Advanced usage: Filter files by extension
def list_python_files(directory='.'):
    return [f for f in os.listdir(directory) if f.endswith('.py')]

# 5. os.remove() - Delete a File
os.remove('file_to_delete.txt')

# Advanced usage: Safe file deletion
def safe_delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully")
    except FileNotFoundError:
        print(f"File {file_path} not found")
    except PermissionError:
        print(f"Permission denied to delete {file_path}")

# 6. os.rename() - Rename File or Directory
os.rename('old_name', 'new_name')

# Advanced usage: Batch renaming
def batch_rename_files(directory, old_prefix, new_prefix):
    for filename in os.listdir(directory):
        if filename.startswith(old_prefix):
            new_filename = filename.replace(old_prefix, new_prefix)
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, new_filename)
            )

# 7. os.path.exists() - Check Path Existence
path_exists = os.path.exists('/path/to/file_or_directory')

# Advanced usage: Comprehensive path validation
def validate_path(path):
    checks = {
        'exists': os.path.exists(path),
        'is_file': os.path.isfile(path),
        'is_directory': os.path.isdir(path),
        'is_readable': os.access(path, os.R_OK),
        'is_writable': os.access(path, os.W_OK)
    }
    return checks

# 8. os.getenv() - Get Environment Variable
python_path = os.getenv('PYTHONPATH')

# Advanced usage: Configuration management
def load_config():
    config = {
        'database_url': os.getenv('DB_URL', 'default_url'),
        'debug_mode': os.getenv('DEBUG', 'False').lower() == 'true',
        'log_level': os.getenv('LOG_LEVEL', 'INFO')
    }
    return config

# 9. os.walk() - Traverse Directory Tree
def find_large_files(directory, size_threshold=1024*1024):
    large_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > size_threshold:
                large_files.append(file_path)
    return large_files

# 10. os.system() - Execute System Command
os.system('ls -l')

# Advanced usage: Secure command execution
def run_safe_command(command):
    try:
        exit_code = os.system(command)
        if exit_code == 0:
            print("Command executed successfully")
        else:
            print(f"Command failed with exit code {exit_code}")
    except Exception as e:
        print(f"Error executing command: {e}")




# 11. os.rmdir() - Remove Empty Directory
os.rmdir('empty_directory')

# Advanced usage: Safe directory removal
def remove_empty_directories(base_path):
    for root, dirs, files in os.walk(base_path, topdown=False):
        for dir_name in dirs:
            full_path = os.path.join(root, dir_name)
            try:
                os.rmdir(full_path)
                print(f"Removed empty directory: {full_path}")
            except OSError:
                # Directory not empty or permission issues
                pass

# 12. os.chmod() - Change File Permissions
os.chmod('filename.txt', 0o755)  # Read, write, execute for owner

# Advanced usage: Secure file permission management
def secure_sensitive_file(file_path):
    # Set read/write for owner only
    os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)
    
    # Verify permissions
    file_stats = os.stat(file_path)
    print("File Permissions:", oct(file_stats.st_mode & 0o777))

# 13. os.path.join() - Path Construction
full_path = os.path.join('directory', 'subdirectory', 'file.txt')

# Advanced usage: Cross-platform path builder
def create_safe_path(*path_components):
    # Normalize and sanitize path components
    cleaned_components = [
        component.strip().replace(' ', '_') 
        for component in path_components
    ]
    return os.path.normpath(os.path.join(*cleaned_components))

# 14. os.path.splitext() - Split Filename and Extension
filename, extension = os.path.splitext('document.txt')

# Advanced usage: Batch file extension processing
def process_files_by_extension(directory, target_extension):
    processed_files = []
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() == target_extension:
            full_path = os.path.join(directory, filename)
            # Perform processing
            processed_files.append(full_path)
    return processed_files

# 15. os.urandom() - Generate Cryptographically Strong Random Bytes
random_bytes = os.urandom(16)

# Advanced usage: Generate secure tokens
def generate_secure_token(length=16):
    return os.urandom(length).hex()

# 16. os.path.expanduser() - Expand User Home Directory
home_config = os.path.expanduser('~/.config')

# Advanced usage: Cross-platform config path
def get_config_path(app_name):
    return os.path.join(
        os.path.expanduser('~'),
        '.config',
        app_name
    )

# 17. os.makedirs() with exist_ok - Robust Directory Creation
def ensure_directory_exists(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Ensured directory exists: {directory_path}")
    except PermissionError:
        print(f"Permission denied to create {directory_path}")

# 18. os.path.getsize() - Get File Size
def get_file_size_info(file_path):
    try:
        size = os.path.getsize(file_path)
        # Convert to human-readable format
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
    except FileNotFoundError:
        return "File not found"

# 19. os.scandir() - Efficient Directory Iteration
def advanced_directory_scan(directory):
    with os.scandir(directory) as entries:
        file_info = []
        for entry in entries:
            info = {
                'name': entry.name,
                'is_file': entry.is_file(),
                'is_dir': entry.is_dir(),
                'size': entry.stat().st_size if entry.is_file() else None
            }
            file_info.append(info)
    return file_info

# 20. os.path.commonpath() - Find Common Path Prefix
def find_common_project_root(paths):
    try:
        common_path = os.path.commonpath(paths)
        return common_path
    except ValueError:
        # Paths on different drives or inconsistent
        return None

# Bonus: Comprehensive Path Utility Function
def path_analyzer(file_or_directory_path):
    """
    Comprehensive path analysis utility
    """
    analysis = {
        'absolute_path': os.path.abspath(file_or_directory_path),
        'exists': os.path.exists(file_or_directory_path),
        'is_file': os.path.isfile(file_or_directory_path),
        'is_directory': os.path.isdir(file_or_directory_path),
        'size': os.path.getsize(file_or_directory_path) if os.path.exists(file_or_directory_path) else None,
        'permissions': oct(os.stat(file_or_directory_path).st_mode & 0o777) if os.path.exists(file_or_directory_path) else None,
        'creation_time': os.path.getctime(file_or_directory_path) if os.path.exists(file_or_directory_path) else None,
        'modification_time': os.path.getmtime(file_or_directory_path) if os.path.exists(file_or_directory_path) else None
    }
    return analysis





# 21. os.path.realpath() - Resolve Symbolic Links
def resolve_symlink(link_path):
    try:
        real_path = os.path.realpath(link_path)
        return {
            'original_link': link_path,
            'resolved_path': real_path,
            'is_symlink': os.path.islink(link_path)
        }
    except Exception as e:
        return f"Error resolving symlink: {e}"

# 22. os.access() - Check File Permissions
def check_file_access(file_path):
    access_checks = {
        'exists': os.path.exists(file_path),
        'readable': os.access(file_path, os.R_OK),
        'writable': os.access(file_path, os.W_OK),
        'executable': os.access(file_path, os.X_OK)
    }
    return access_checks

# 23. os.times() - Get Process Time Information
def measure_process_time():
    times = os.times()
    return {
        'user_time': times.user,
        'system_time': times.system,
        'children_user_time': times.children_user,
        'children_system_time': times.children_system,
        'elapsed_time': times.elapsed
    }

# 24. os.pipe() - Create Pipe for Inter-Process Communication
def create_communication_pipe():
    try:
        read_fd, write_fd = os.pipe()
        return {
            'read_descriptor': read_fd,
            'write_descriptor': write_fd
        }
    except Exception as e:
        return f"Pipe creation error: {e}"

# 25. os.get_terminal_size() - Get Terminal Dimensions
def get_terminal_info():
    try:
        terminal_size = os.get_terminal_size()
        return {
            'columns': terminal_size.columns,
            'lines': terminal_size.lines
        }
    except Exception as e:
        return f"Unable to get terminal size: {e}"

# 26. os.sendfile() - Efficient File Copying
def efficient_file_copy(source, destination):
    try:
        with open(source, 'rb') as src, open(destination, 'wb') as dst:
            # Get source file stats
            source_stat = os.fstat(src.fileno())
            
            # Use sendfile for efficient copying
            os.sendfile(dst.fileno(), src.fileno(), 0, source_stat.st_size)
        
        return {
            'status': 'success',
            'source': source,
            'destination': destination,
            'file_size': source_stat.st_size
        }
    except Exception as e:
        return f"File copy error: {e}"

# 27. os.set_blocking() - Set File Descriptor Blocking Mode
def configure_file_descriptor_blocking(fd, blocking=True):
    try:
        os.set_blocking(fd, blocking)
        return {
            'file_descriptor': fd,
            'blocking_mode': blocking
        }
    except Exception as e:
        return f"Blocking configuration error: {e}"

# 28. os.get_blocking() - Check File Descriptor Blocking Mode
def check_descriptor_blocking(fd):
    try:
        is_blocking = os.get_blocking(fd)
        return {
            'file_descriptor': fd,
            'is_blocking': is_blocking
        }
    except Exception as e:
        return f"Blocking check error: {e}"

# 29. os.path.commonprefix() - Find Common Path Prefix
def find_common_project_paths(paths):
    try:
        common_prefix = os.path.commonprefix(paths)
        return {
            'common_prefix': common_prefix,
            'input_paths': paths
        }
    except Exception as e:
        return f"Common prefix error: {e}"

# 30. Platform-Specific Information Gathering
def system_information():
    return {
        'os_name': os.name,
        'platform': platform.system(),
        'platform_release': platform.release(),
        'platform_version': platform.version(),
        'machine_type': platform.machine(),
        'processor': platform.processor(),
        'cpu_count': os.cpu_count(),
        'current_user': os.getlogin() if hasattr(os, 'getlogin') else 'Unknown'
    }

# Comprehensive Path and File Validation Utility
def advanced_path_validator(path, 
                             min_size=0, 
                             max_size=float('inf'), 
                             allowed_extensions=None):
    """
    Advanced path validation with multiple checks
    """
    if not os.path.exists(path):
        return {'valid': False, 'reason': 'Path does not exist'}
    
    file_stats = os.stat(path)
    
    # Size validation
    if not (min_size <= file_stats.st_size <= max_size):
        return {
            'valid': False, 
            'reason': f'File size out of allowed range: {file_stats.st_size}'
        }
    
    # Extension validation
    if allowed_extensions:
        _, ext = os.path.splitext(path)
        if ext.lower() not in allowed_extensions:
            return {
                'valid': False, 
                'reason': f'Disallowed file extension: {ext}'
            }
    
    return {
        'valid': True,
        'path': path,
        'size': file_stats.st_size,
        'permissions': oct(file_stats.st_mode & 0o777),
        'created': time.ctime(file_stats.st_ctime),
        'modified': time.ctime(file_stats.st_mtime)
    }