# Brute Force Simulation and Mitigation

This repository contains two Python scripts designed for educational purposes in the domain of cybersecurity. 

1. **`brute_force.py`**: Demonstrates how brute force attacks can target a victim system, with and without a honeypot.
2. **`mitigate_brute_force.py`**: Implements a defensive strategy to protect the victim system from brute force attacks.

## Getting Started

### Prerequisites
- Python 3.6 or later
- Basic understanding of networking and brute force attacks

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/brute-force-mitigation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd brute-force-mitigation
   ```

## Files in the Repository

### 1. brute_force.py
This script simulates a brute force attack targeting a victim's service. It reads a list of passwords and attempts to log in to an FTP server using a known username. 

#### Usage:
```bash
python brute_force.py
```

#### Features:
- Uses the `ftplib` library to simulate an FTP brute force attack.
- Tracks the number of attempts and the time taken for the attack.
- Handles exceptions like failed login and file not found.

---

### 2. mitigate_brute_force.py
This script implements defensive strategies to protect the victim system from brute force attacks. It monitors the FTP log file for failed login attempts and dynamically blocks IP addresses that exceed a defined threshold.

#### Features:
- Monitors real-time logs for failed login attempts.
- Blocks suspicious IPs exceeding the threshold using `iptables`.
- Supports customizable thresholds and time windows.

#### Usage:
```bash
python mitigate_brute_force.py
```

#### Example:
```bash
python mitigate_brute_force.py
```

---

## Project Structure
```
.
├── brute_force.py             # Script to perform brute force attacks
├── mitigate_brute_force.py    # Script to defend against brute force attacks
├── README.md                  # Documentation
```

## Legal Disclaimer
This project is intended for educational purposes only. The scripts should be used only in controlled environments with the permission of system owners. Misuse of these tools is illegal and unethical.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or comments, feel free to open an issue in the repository or contact the repository owner.
