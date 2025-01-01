import datetime
import os
import shutil

# 1. shutil.copy() - Copy File
def copy_file(source, destination):
    """
    Copy a single file with metadata preservation
    """
    try:
        copied_file = shutil.copy(source, destination)
        return {
            'status': 'success',
            'source': source,
            'destination': copied_file,
            'timestamp': datetime.datetime.now()
        }
    except Exception as e:
        return f"File copy error: {e}"

# 2. shutil.copy2() - Copy File with Metadata
def copy_file_with_metadata(source, destination):
    """
    Copy file preserving all metadata (permissions, timestamps)
    """
    try:
        copied_file = shutil.copy2(source, destination)
        return {
            'status': 'success',
            'source': source,
            'destination': copied_file,
            'metadata_preserved': True
        }
    except Exception as e:
        return f"Metadata copy error: {e}"

# 3. shutil.copytree() - Recursive Directory Copy
def copy_directory_tree(source, destination, symlinks=False):
    """
    Recursively copy entire directory structure
    """
    try:
        copied_tree = shutil.copytree(source, destination, symlinks=symlinks)
        return {
            'status': 'success',
            'source': source,
            'destination': copied_tree,
            'symlinks_preserved': symlinks
        }
    except Exception as e:
        return f"Directory copy error: {e}"

# 4. shutil.move() - Move/Rename Files and Directories
def move_file_or_directory(source, destination):
    """
    Move or rename files/directories across filesystems
    """
    try:
        moved_path = shutil.move(source, destination)
        return {
            'status': 'success',
            'source': source,
            'destination': moved_path
        }
    except Exception as e:
        return f"Move operation error: {e}"

# 5. shutil.rmtree() - Recursive Directory Deletion
def safe_directory_removal(directory):
    """
    Safely remove directory and all its contents
    """
    try:
        shutil.rmtree(directory)
        return {
            'status': 'success',
            'removed_directory': directory,
            'timestamp': datetime.datetime.now()
        }
    except Exception as e:
        return f"Directory removal error: {e}"

# 6. shutil.disk_usage() - Get Disk Space Information
def get_disk_space_info(path):
    """
    Retrieve comprehensive disk usage statistics
    """
    try:
        usage = shutil.disk_usage(path)
        return {
            'total': usage.total / (1024 ** 3),  # GB
            'used': usage.used / (1024 ** 3),    # GB
            'free': usage.free / (1024 ** 3),    # GB
            'percentage_used': (usage.used / usage.total) * 100
        }
    except Exception as e:
        return f"Disk usage error: {e}"

# 7. shutil.which() - Find Executable Path
def find_executable(executable_name):
    """
    Locate executable in system PATH
    """
    executable_path = shutil.which(executable_name)
    return {
        'executable': executable_name,
        'path': executable_path,
        'exists': executable_path is not None
    }

# 8. Advanced Archiving Functions
def create_zip_archive(source_dir, output_filename):
    """
    Create compressed ZIP archive with advanced options
    """
    try:
        shutil.make_archive(
            output_filename, 
            'zip', 
            source_dir, 
            base_dir=os.path.basename(source_dir)
        )
        return {
            'status': 'success',
            'source': source_dir,
            'archive': f"{output_filename}.zip",
            'timestamp': datetime.datetime.now()
        }
    except Exception as e:
        return f"Zip archive creation error: {e}"

# 9. Unpack Archives
def extract_archive(archive_path, extract_path):
    """
    Smart archive extraction supporting multiple formats
    """
    try:
        shutil.unpack_archive(archive_path, extract_path)
        return {
            'status': 'success',
            'archive': archive_path,
            'destination': extract_path
        }
    except Exception as e:
        return f"Archive extraction error: {e}"

# 10. Comprehensive File Management Utility
def advanced_file_management(source, destination, operation='copy'):
    """
    Unified file management utility with multiple operations
    """
    operations = {
        'copy': shutil.copy2,
        'move': shutil.move,
        'copytree': shutil.copytree,
        'rmtree': shutil.rmtree
    }

    try:
        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")

        if operation == 'copytree':
            result = operations[operation](source, destination)
        elif operation == 'rmtree':
            result = operations[operation](source)
        else:
            result = operations[operation](source, destination)

        return {
            'status': 'success',
            'operation': operation,
            'source': source,
            'destination': destination if operation != 'rmtree' else None
        }
    except Exception as e:
        return f"{operation.capitalize()} operation error: {e}"

# Bonus: Comprehensive Backup Utility
def create_system_backup(source_dirs, backup_dir):
    """
    Create timestamped backup of multiple directories
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    full_backup_path = os.path.join(backup_dir, backup_name)

    try:
        # Create backup directory
        os.makedirs(full_backup_path, exist_ok=True)

        # Backup each source directory
        backup_details = {}
        for source in source_dirs:
            dir_name = os.path.basename(source)
            destination = os.path.join(full_backup_path, dir_name)
            
            shutil.copytree(source, destination)
            backup_details[dir_name] = {
                'source': source,
                'destination': destination,
                'timestamp': timestamp
            }

        return {
            'status': 'success',
            'backup_name': backup_name,
            'backup_location': full_backup_path,
            'backed_up_directories': backup_details
        }
    except Exception as e:
        return f"Backup creation error: {e}"
    



import datetime
import hashlib
import os
import shutil
import stat
import tempfile


# 11. shutil.chown() - Change File Owner
def change_file_ownership(path, user=None, group=None):
    """
    Change file/directory ownership with comprehensive error handling
    """
    try:
        shutil.chown(path, user, group)
        return {
            'status': 'success',
            'path': path,
            'new_user': user,
            'new_group': group,
            'timestamp': datetime.datetime.now()
        }
    except Exception as e:
        return f"Ownership change error: {e}"

# 12. shutil.get_terminal_size() - Get Terminal Dimensions
def get_terminal_dimensions():
    """
    Retrieve terminal size with additional information
    """
    try:
        terminal_size = shutil.get_terminal_size()
        return {
            'columns': terminal_size.columns,
            'lines': terminal_size.lines,
            'width_in_characters': terminal_size.columns,
            'height_in_lines': terminal_size.lines
        }
    except Exception as e:
        return f"Terminal size retrieval error: {e}"

# 13. Advanced File Comparison Utility
def compare_files(file1, file2, compare_content=True):
    """
    Comprehensive file comparison utility
    """
    def calculate_hash(filepath):
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    try:
        # Basic metadata comparison
        stat1 = os.stat(file1)
        stat2 = os.stat(file2)

        comparison_result = {
            'metadata': {
                'size_match': stat1.st_size == stat2.st_size,
                'file1_size': stat1.st_size,
                'file2_size': stat2.st_size,
                'modification_time_match': stat1.st_mtime == stat2.st_mtime
            }
        }

        # Optional content comparison
        if compare_content:
            comparison_result['content'] = {
                'hash_match': calculate_hash(file1) == calculate_hash(file2)
            }

        return comparison_result

    except Exception as e:
        return f"File comparison error: {e}"

# 14. Intelligent File Synchronization
def synchronize_directories(source, destination, 
                             ignore_patterns=None, 
                             dry_run=False):
    """
    Advanced directory synchronization with multiple options
    """
    try:
        # Create default ignore patterns if not provided
        if ignore_patterns is None:
            ignore_patterns = shutil.ignore_patterns('*.pyc', '.git', '__pycache__')

        # Perform dry run or actual sync
        if dry_run:
            # Simulate sync and return potential changes
            changes = []
            for root, dirs, files in os.walk(source):
                for file in files:
                    source_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_path, source)
                    dest_path = os.path.join(destination, relative_path)
                    
                    if not os.path.exists(dest_path):
                        changes.append({
                            'type': 'new_file',
                            'source': source_path,
                            'destination': dest_path
                        })
            
            return changes
        else:
            # Actual synchronization
            shutil.copytree(
                source, 
                destination, 
                ignore=ignore_patterns, 
                dirs_exist_ok=True
            )
            
            return {
                'status': 'success',
                'source': source,
                'destination': destination,
                'timestamp': datetime.datetime.now()
            }

    except Exception as e:
        return f"Directory synchronization error: {e}"

# 15. Secure Temporary File Management
def secure_temp_file_handler(content=None, mode='w'):
    """
    Create secure temporary file with advanced options
    """
    try:
        # Create temporary file with restricted permissions
        with tempfile.NamedTemporaryFile(
            mode=mode, 
            delete=False, 
            prefix='secure_', 
            suffix='.tmp'
        ) as temp_file:
            # Set restrictive permissions (read/write for owner only)
            os.chmod(temp_file.name, stat.S_IRUSR | stat.S_IWUSR)
            
            # Write content if provided
            if content:
                temp_file.write(content)
            
            temp_file_path = temp_file.name

        return {
            'file_path': temp_file_path,
            'created_at': datetime.datetime.now(),
            'permissions': oct(os.stat(temp_file_path).st_mode & 0o777)
        }
    except Exception as e:
        return f"Temporary file creation error: {e}"

# 16. Comprehensive File System Walker
def advanced_file_system_walker(
    root_path, 
    max_depth=None, 
    file_filter=None, 
    size_threshold=None
):
    """
    Advanced file system traversal with multiple filtering options
    """
    def walk_directory(current_path, current_depth=0):
        try:
            results = []
            
            # Depth check
            if max_depth is not None and current_depth > max_depth:
                return results

            for entry in os.scandir(current_path):
                try:
                    # Apply file filter if provided
                    if file_filter and not file_filter(entry):
                        continue

                    # Size threshold check
                    if size_threshold and entry.is_file():
                        file_size = entry.stat().st_size
                        if file_size > size_threshold:
                            continue

                    file_info = {
                        'path': entry.path,
                        'name': entry.name,
                        'is_file': entry.is_file(),
                        'is_dir': entry.is_dir(),
                        'size': entry.stat().st_size if entry.is_file() else None,
                        'depth': current_depth
                    }
                    results.append(file_info)

                    # Recursive directory traversal
                    if entry.is_dir():
                        results.extend(
                            walk_directory(
                                entry.path, 
                                current_depth + 1
                            )
                        )

                except Exception as e:
                    print(f"Error processing {entry.path}: {e}")

            return results

        except Exception as e:
            print(f"Directory walk error for {current_path}: {e}")
            return []

    return walk_directory(root_path)

# Example usage of advanced file system walker
def example_usage():
    # Custom file filter
    def large_python_files(entry):
        return (entry.is_file() and 
                entry.name.endswith('.py') and 
                entry.stat().st_size > 1024 * 100)  # 100KB

    results = advanced_file_system_walker(
        '/path/to/directory',
        max_depth=3,
        file_filter=large_python_files,
        size_threshold=1024 * 1024  # 1MB
    )
    
    return results