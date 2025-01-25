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
import shutil

def run_command(command):
    try:
        return subprocess.check_output(command, shell=True, universal_newlines=True, stderr=subprocess.STDOUT).strip()
    except Exception as e:
        return f'Error: {str(e)}'

def get_comprehensive_system_details():
    system_details = {}

    # 1. Expanded OS Information
    uname = platform.uname()
    system_details['os_info'] = {
        'os_name': os.name,
        'system': uname.system,
        'node': uname.node,
        'release': uname.release,
        'version': uname.version,
        'machine': uname.machine,
        'processor': uname.processor,
        'python_version': platform.python_version(),
        'byte_order': sys.byteorder,
    }

    # 2. User and Environment Details with Effective IDs
    try:
        system_details['user_info'] = {
            'current_user': getpass.getuser(),
            'home_directory': os.path.expanduser('~'),
            'current_working_directory': os.getcwd(),
            'username': os.getlogin() if hasattr(os, 'getlogin') else 'Unknown',
            'user_id': os.getuid() if hasattr(os, 'getuid') else 'Not Available',
            'group_id': os.getgid() if hasattr(os, 'getgid') else 'Not Available',
            'effective_user_id': os.geteuid() if hasattr(os, 'geteuid') else 'Not Available',
            'effective_group_id': os.getegid() if hasattr(os, 'getegid') else 'Not Available',
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

    # 4. Enhanced CPU and Memory Information
    try:
        mem_info = {}
        if platform.system() == 'Linux':
            mem_stats = run_command('free -b').split('\n')
            if 'Error' not in mem_stats[1]:
                mem_info = dict(zip(['total', 'used', 'free', 'shared', 'buff_cache', 'available'],
                                    [int(x) for x in mem_stats[1].split()[1:]]))
        elif platform.system() == 'Darwin':
            vm_stats = run_command('vm_stat').split('\n')
            mem_info = {line.split(':')[0].strip(): int(line.split(':')[1].strip().rstrip('.')) * 4096 
                        for line in vm_stats if ':' in line}
        elif platform.system() == 'Windows':
            mem_output = run_command('wmic ComputerSystem get TotalPhysicalMemory')
            mem_info['total'] = int(mem_output.split()[-1]) if 'TotalPhysicalMemory' in mem_output else 0

        system_details['cpu_mem_info'] = {
            'logical_cores': os.cpu_count(),
            'cpu_architecture': platform.processor(),
            'memory_info': mem_info,
            'load_average': os.getloadavg() if hasattr(os, 'getloadavg') else 'Not Available'
        }
    except Exception as e:
        system_details['cpu_mem_info'] = {'error': str(e)}

    # 5. Enhanced Disk Information
    try:
        disk_info = []
        if platform.system() == 'Windows':
            disks = run_command('wmic logicaldisk get caption,freespace,size,volumename')
            for line in disks.split('\n')[1:]:
                if line.strip():
                    parts = line.split()
                    disk_info.append({
                        'device': parts[0],
                        'free': int(parts[1]),
                        'total': int(parts[2]),
                        'name': ' '.join(parts[3:])
                    })
        else:
            disks = run_command('df -B1').split('\n')[1:]
            for line in disks:
                if line.strip():
                    parts = line.split()
                    disk_info.append({
                        'device': parts[0],
                        'total': int(parts[1]),
                        'used': int(parts[2]),
                        'free': int(parts[3]),
                        'mount_point': parts[5]
                    })
        system_details['disk_info'] = disk_info
    except Exception as e:
        system_details['disk_info'] = {'error': str(e)}

    # 6. Process Information with Resource Usage
    try:
        processes = []
        if platform.system() == 'Windows':
            tasklist = run_command('tasklist /FO CSV /NH').split('\n')
            for task in tasklist:
                if task.strip():
                    parts = task.split('","')
                    processes.append({
                        'name': parts[0].strip('"'),
                        'pid': parts[1].strip('"'),
                        'mem_usage': parts[4].strip('"'),
                        'status': parts[5].strip('"')
                    })
        else:
            ps_output = run_command('ps aux').split('\n')[1:]
            for process in ps_output:
                if process.strip():
                    parts = process.split()
                    processes.append({
                        'user': parts[0],
                        'pid': parts[1],
                        'cpu': parts[2],
                        'mem': parts[3],
                        'vsz': parts[4],
                        'rss': parts[5],
                        'tty': parts[6],
                        'stat': parts[7],
                        'start': parts[8],
                        'time': parts[9],
                        'command': ' '.join(parts[10:])
                    })
        system_details['processes'] = processes
    except Exception as e:
        system_details['processes'] = {'error': str(e)}

    # 7. Network Information and Connections
    try:
        netstat = []
        if platform.system() == 'Windows':
            connections = run_command('netstat -ano').split('\n')
        else:
            connections = run_command('netstat -tulpn').split('\n')
        system_details['network_connections'] = connections[2:]
    except Exception as e:
        system_details['network_connections'] = {'error': str(e)}

    # 8. System Hardware Details
    try:
        hw_info = {}
        if platform.system() == 'Linux':
            hw_info['usb_devices'] = run_command('lsusb').split('\n')
            hw_info['pci_devices'] = run_command('lspci').split('\n')
        elif platform.system() == 'Darwin':
            hw_info['system_profiler'] = run_command('system_profiler SPHardwareDataType').split('\n')
        elif platform.system() == 'Windows':
            hw_info['system_info'] = run_command('systeminfo').split('\n')
        system_details['hardware_info'] = hw_info
    except Exception as e:
        system_details['hardware_info'] = {'error': str(e)}

    # 9. System Time and Boot Information
    system_details['time_info'] = {
        'current_time': datetime.datetime.now().isoformat(),
        'timezone': time.tzname,
        'utc_offset': time.timezone,
        'is_daylight_saving': time.daylight
    }

    # 10. Machine Identifier
    system_details['machine_id'] = {}
    try:
        if platform.system() == 'Linux':
            with open('/etc/machine-id', 'r') as f:
                system_details['machine_id']['linux_machine_id'] = f.read().strip()
        elif platform.system() == 'Darwin':
            cmd_output = run_command('ioreg -rd1 -c IOPlatformExpertDevice | grep IOPlatformUUID')
            system_details['machine_id']['macos_platform_uuid'] = cmd_output
        elif platform.system() == 'Windows':
            cmd_output = run_command('reg query HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Cryptography /v MachineGuid')
            guid = cmd_output.split()[-1] if 'REG_SZ' in cmd_output else cmd_output
            system_details['machine_id']['windows_machine_guid'] = guid
    except Exception as e:
        system_details['machine_id']['error'] = str(e)
    system_details['machine_id']['random_uuid'] = str(uuid.uuid4())

    # 11. Python Paths and Executable Info
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