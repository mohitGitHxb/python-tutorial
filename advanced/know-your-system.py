import os
import platform
import getpass
import socket
import sys
import locale
import uuid
import json
import datetime
import time
import subprocess

def get_comprehensive_system_details():
    system_details = {}

    # 1. Basic OS Information
    system_details['os_info'] = {
        'os_name': os.name,
        'platform': platform.system(),
        'platform_release': platform.release(),
        'platform_version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'architecture': platform.architecture(),
        'node_name': platform.node(),
        'python_version': platform.python_version(),
    }

    # 2. User and Environment Details
    try:
        system_details['user_info'] = {
            'current_user': getpass.getuser(),
            'home_directory': os.path.expanduser('~'),
            'current_working_directory': os.getcwd(),
            'username': os.getlogin() if hasattr(os, 'getlogin') else 'Unknown',
            'user_id': os.getuid() if hasattr(os, 'getuid') else 'Not Available',
            'group_id': os.getgid() if hasattr(os, 'getgid') else 'Not Available',
        }
    except Exception as e:
        system_details['user_info'] = {'error': str(e)}

    # 3. System Locale and Language
    system_details['locale_info'] = {
        'default_encoding': sys.getdefaultencoding(),
        'filesystem_encoding': sys.getfilesystemencoding(),
        'preferred_encoding': locale.getpreferredencoding(),
        'system_locale': locale.getlocale(),
        'language': locale.getdefaultlocale()[0],
    }

    # 4. CPU Details
    try:
        system_details['cpu_info'] = {
            'cores': os.cpu_count(),
            'cpu_architecture': platform.processor(),
            'cpu_frequency': os.sysconf('SC_CLK_TCK'),
        }
    except Exception as e:
        system_details['cpu_info'] = {'error': str(e)}

    # 5. Environment Variables
    system_details['environment_variables'] = dict(os.environ)

    # 6. Network Information
    try:
        system_details['network_info'] = {
            'hostname': socket.gethostname(),
            'fqdn': socket.getfqdn(),
            'ip_address': socket.gethostbyname(socket.gethostname())
        }
    except Exception as e:
        system_details['network_info'] = {'error': str(e)}

    # 7. System Time and Date
    system_details['time_info'] = {
        'current_time': datetime.datetime.now().isoformat(),
        'timezone': time.tzname,
        'utc_offset': time.timezone,
        'is_daylight_saving': time.daylight
    }

    # 8. Unique Machine Identifier
    system_details['machine_id'] = {
        'uuid': str(uuid.uuid4()),
    }

    # 9. Additional System Information via subprocess (cross-platform attempts)
    def run_command(command):
        try:
            return subprocess.check_output(command, shell=True, universal_newlines=True).strip()
        except:
            return 'Not Available'

    # Platform-specific commands
    if platform.system() == 'Windows':
        system_details['additional_system_info'] = {
            'windows_version': run_command('ver'),
            'system_info': run_command('systeminfo | findstr /B /C:"OS Name" /C:"OS Version"')
        }
    elif platform.system() == 'Darwin':
        system_details['additional_system_info'] = {
            'mac_version': run_command('sw_vers'),
            'system_profile': run_command('system_profiler SPSoftwareDataType')
        }
    elif platform.system() == 'Linux':
        system_details['additional_system_info'] = {
            'linux_version': run_command('cat /etc/os-release'),
            'kernel_version': run_command('uname -r')
        }

    # 10. Python Paths and Executable Info
    system_details['python_info'] = {
        'executable_path': sys.executable,
        'python_path': sys.path,
        'version_info': {
            'major': sys.version_info.major,
            'minor': sys.version_info.minor,
            'micro': sys.version_info.micro,
            'release_level': sys.version_info.releaselevel
        }
    }

    return system_details

def print_system_details():
    details = get_comprehensive_system_details()
    print(json.dumps(details, indent=2))

def save_system_details_to_file(filename='system_details.json'):
    details = get_comprehensive_system_details()
    with open(filename, 'w') as f:
        json.dump(details, f, indent=2)

# Run the functions
if __name__ == '__main__':
    print_system_details()
    save_system_details_to_file()