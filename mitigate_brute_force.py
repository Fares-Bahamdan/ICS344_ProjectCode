import re
import subprocess
from collections import defaultdict
from time import time

# Configuration
LOG_FILE_PATH = "/var/log/vsftpd.log"  # Path to FTP log file
THRESHOLD_ATTEMPTS = 5               # Max failed attempts allowed
TIME_WINDOW = 120                     # Time window in seconds

# Track failed login attempts
failed_attempts = defaultdict(list)

def block_ip(ip):
    """Block the IP using iptables."""
    print(f"Blocking IP: {ip}")
    subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    print(f"IP {ip} blocked successfully.")

try:
    with open(LOG_FILE_PATH, 'r') as log_file:
        log_file.seek(0, 2)  # Move to the end of the file
        print("Monitoring vsftpd log file...")
        while True:
            line = log_file.readline()
            if not line:
                continue

            # Detect failed login attempts
            match = re.search(r"FAIL LOGIN.*?(\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                current_time = time()
                failed_attempts[ip].append(current_time)

                # Remove outdated attempts
                failed_attempts[ip] = [
                    t for t in failed_attempts[ip] if current_time - t < TIME_WINDOW
                ]

                # Check if threshold is exceeded
                if len(failed_attempts[ip]) >= THRESHOLD_ATTEMPTS:
                    block_ip(ip)
                    del failed_attempts[ip]  # Clear the record for this IP
except FileNotFoundError:
    print(f"Log file not found: {LOG_FILE_PATH}")
except KeyboardInterrupt:
    print("Script stopped by user.")
