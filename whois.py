import os
import sys
from time import sleep

### Logic to Check for the arguments:
if len(sys.argv) != 2:
    print(f'Invalid amount of arguments')
    print(f'Usage:')
    print(f'\tpython3 whois.py <TEXT_FILE>')
    sys.exit(1)
elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print(f'Usage:')
    print(f'\tpython3 whois.py <TEXT_FILE>')
    sys.exit(0)
else:
    fname = sys.argv[1]

divider = '=' * 20

def whois():
    with open(fname, 'r') as file:
        for line in file:
            line = line.strip()
            print(f'{divider} [IP Address: {line}] {divider}')
                        
            arguments = f'grep -ie "orgname" -ie "address" -ie "organization" -ie "netrange" -ie "cidr"'
            # command = f'ping -c1 {line} | {arguments}'
            command = f'whois {line} | {arguments}'
            try:
                os.system(f'/usr/bin/bash -c "{command}"')

            except ConnectionError:
                print(f'Could not connect to {line}')
                continue

whois()
