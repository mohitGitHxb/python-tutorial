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
import re

def run_command(command):
    try:
        result = subprocess.check_output(
            command, 
            shell=True, 
            universal_newlines=True, 
            stderr=subprocess.STDOUT,
            timeout=10
        )
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Command failed (RC={e.returncode}): {e.output.strip()}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_system_details():
    system_details = {}

    # 1. Core System Identification
    uname = platform.uname()
    system_details['core_system'] = {
        'platform': {
            'system': uname.system,
            'node': uname.node,
            'release': uname.release,
            'version': uname.version,
            'machine': uname.machine,
            'processor': uname.processor
        },
        'os_name': os.name,
        'python_build': platform.python_build(),
        'python_compiler': platform.python_compiler(),
        'python_implementation': platform.python_implementation(),
        'byte_order': sys.byteorder
    }

    # 2. Hardware Deep Dive
    system_details['hardware'] = {}
    try:
        # CPU Details
        cpu_info = {}
        if platform.system() == 'Linux':
            with open('/proc/cpuinfo', 'r') as f:
                cpu_info = [line.strip() for line in f if 'model name' in line or 'cpu MHz' in line]
        elif platform.system() == 'Darwin':
            cpu_info = run_command('sysctl -n machdep.cpu.brand_string')
        elif platform.system() == 'Windows':
            cpu_info = run_command('wmic cpu get name,NumberOfCores,NumberOfLogicalProcessors /format:list')
        
        # Memory Details
        mem_info = {}
        if platform.system() == 'Linux':
            with open('/proc/meminfo', 'r') as f:
                mem_info = {line.split(':')[0]: line.split(':')[1].strip() for line in f}
        elif platform.system() == 'Darwin':
            mem_info = run_command('sysctl hw.memsize')
        elif platform.system() == 'Windows':
            mem_info = run_command('wmic memorychip get Capacity,PartNumber,Speed /format:list')
        
        # Storage Details
        storage_info = {}
        if platform.system() == 'Linux':
            storage_info['block_devices'] = run_command('lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,UUID')
            storage_info['smartctl'] = run_command('sudo smartctl --scan').split('\n')
        elif platform.system() == 'Darwin':
            storage_info = run_command('diskutil list')
        elif platform.system() == 'Windows':
            storage_info = run_command('wmic diskdrive get Model,Size,Partitions /format:list')
        
        system_details['hardware'].update({
            'cpu_details': cpu_info,
            'memory_details': mem_info,
            'storage_details': storage_info,
            'usb_devices': run_command('lsusb').split('\n') if platform.system() == 'Linux' else 'N/A',
            'pci_devices': run_command('lspci -vvv').split('\n') if platform.system() == 'Linux' else 'N/A',
            'bios_info': run_command('dmidecode -t bios') if platform.system() == 'Linux' else run_command('wmic bios get /format:list')
        })

    except Exception as e:
        system_details['hardware']['error'] = str(e)

    # 3. Kernel & System Architecture
    system_details['kernel'] = {}
    try:
        kernel_info = {}
        if platform.system() == 'Linux':
            kernel_info['modules'] = run_command('lsmod').split('\n')
            kernel_info['parameters'] = {param.split('=')[0]: param.split('=')[1] 
                                       for param in run_command('cat /proc/cmdline').split() 
                                       if '=' in param}
            kernel_info['interrupts'] = run_command('cat /proc/interrupts').split('\n')[:20]
        elif platform.system() == 'Darwin':
            kernel_info = run_command('sysctl -a')
        elif platform.system() == 'Windows':
            kernel_info = {
                'kernel_version': platform.version(),
                'build_number': run_command('ver')
            }
        
        system_details['kernel'].update(kernel_info)
    except Exception as e:
        system_details['kernel']['error'] = str(e)

    # 4. System Resources & Utilization
    system_details['resources'] = {}
    try:
        # Process Details
        processes = []
        if platform.system() == 'Linux':
            ps_output = run_command('ps -eo pid,ppid,user,%cpu,%mem,cmd --sort=-%cpu')
            processes = [line.split(None, 5) for line in ps_output.split('\n')[1:21]]
        elif platform.system() == 'Darwin':
            ps_output = run_command('ps aux')
            processes = [line.split(None, 10) for line in ps_output.split('\n')[1:21]]
        elif platform.system() == 'Windows':
            tasklist = run_command('tasklist /FO CSV /NH')
            processes = [line.split('","') for line in tasklist.split('\n')[:20]]
        
        # Network Statistics
        net_info = {}
        if platform.system() == 'Linux':
            net_info['connections'] = run_command('ss -tulpn').split('\n')
            net_info['interface_stats'] = run_command('ip -s link').split('\n')
        elif platform.system() == 'Darwin':
            net_info = run_command('netstat -atn')
        elif platform.system() == 'Windows':
            net_info = run_command('netstat -ano')
        
        system_details['resources'].update({
            'top_processes': processes,
            'load_average': os.getloadavg() if hasattr(os, 'getloadavg') else 'N/A',
            'memory_usage': {
                'virtual': shutil.disk_usage('/'),
                'swap': run_command('free -m | grep Swap') if platform.system() == 'Linux' else 'N/A'
            },
            'network': net_info,
            'open_files': {
                'lsof': run_command('lsof').split('\n') if platform.system() != 'Windows' else 'N/A',
                'handle_count': run_command('ls /proc/*/fd | wc -l') if platform.system() == 'Linux' else 'N/A'
            }
        })
    except Exception as e:
        system_details['resources']['error'] = str(e)

    # 5. Security Configuration
    system_details['security'] = {}
    try:
        security_info = {}
        if platform.system() == 'Linux':
            security_info.update({
                'selinux': run_command('sestatus'),
                'apparmor': run_command('aa-status'),
                ' firewall': run_command('sudo iptables -L -n') 
            })
        elif platform.system() == 'Windows':
            security_info.update({
                'firewall': run_command('netsh advfirewall show allprofiles'),
                'antivirus': run_command('wmic /namespace:\\\\root\\securitycenter2 path AntiVirusProduct get displayName')
            })
        elif platform.system() == 'Darwin':
            security_info['firewall'] = run_command('defaults read /Library/Preferences/com.apple.alf globalstate')
        
        system_details['security'].update(security_info)
    except Exception as e:
        system_details['security']['error'] = str(e)

    # 6. User Accounts and Groups
    system_details['user_accounts'] = {}
    try:
        if platform.system() == 'Linux':
            users = run_command('cat /etc/passwd').split('\n')
            groups = run_command('cat /etc/group').split('\n')
            system_details['user_accounts']['users'] = [user.split(':')[0] for user in users if user]
            system_details['user_accounts']['groups'] = [group.split(':')[0] for group in groups if group]
        elif platform.system() == 'Windows':
            users = run_command('net user').split('\n')[4:]
            system_details['user_accounts']['users'] = [user.strip() for user in users if user.strip()]
        elif platform.system() == 'Darwin':
            users = run_command('dscl . list /Users').split('\n')
            system_details['user_accounts']['users'] = [user for user in users if user]
    except Exception as e:
        system_details['user_accounts']['error'] = str(e)

    # 7. System Time and Locale
    system_details['time_locale'] = {
        'current_time': datetime.datetime.now().isoformat(),
        'timezone': time.tzname,
        'locale': locale.getlocale()
    }

    # 8. Python Environment
    system_details['python_env'] = {
        'version': sys.version,
        'executable': sys.executable,
        'path': sys.path,
        'packages': run_command('pip freeze') if hasattr(sys, 'real_prefix') else 'N/A'
    }

    return system_details

def print_system_details():
    details = get_system_details()
    print(json.dumps(details, indent=2))

def save_system_details_to_file(filename='full_system_details.json'):
    details = get_system_details()
    with open(filename, 'w') as f:
        json.dump(details, f, indent=2)

# Run the functions
if __name__ == '__main__':
    # print_system_details()
    save_system_details_to_file()