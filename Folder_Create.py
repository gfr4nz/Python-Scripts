#!/usr/bin/python3

import os
import sys
from time import sleep

### Logic to Check for the arguments:
if len(sys.argv) != 2:
    print('Invalid number of arguments.\n')
    print('Usage:')
    print('\t./script.py <FOLDER_NAME>')
    exit()
elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print('Usage:')
    print('\t./script.py <FOLDER_NAME>')
    exit()
else:
    fname = sys.argv[1]
    # print(fname)

### Functions
def htb():
    # pass
    htb_path = '/home/kali/Desktop/CTF/HTB/Rooms/' # Change this if this is in other location.
    ## Creating Parent Folder
    os.mkdir(f'{htb_path}{fname}')
    print(f'[INFO]  Creating the folder {fname}.')
    sleep(1)
    
    # For Loop for creating subfolders
    for folder in ['enu', 'loot', 'payload', 'exploit', 'tools']:
        ## Creating Sub-folders
        print(f'[INFO]  Creating "{folder}" sub-folders in {fname}.')
        os.mkdir(f'{htb_path}{fname}/{folder}')
        sleep(1)

def thm():
    # pass
    
    thm_path = '/home/kali/Desktop/CTF/THM/ROOMS/' # Change this if this is in other location.
    ## Creating Parent Folder
    os.mkdir(f'{thm_path}{fname}')
    print(f'[INFO]  Creating the folder {fname}.')
    sleep(1)
    
    # For Loop for creating subfolders
    for folder in ['enu', 'loot', 'payload', 'exploit', 'tools']:
        ## Creating Sub-folders
        print(f'[INFO]  Creating "{folder}" sub-folders in {fname}.')
        os.mkdir(f'{thm_path}{fname}/{folder}')
        sleep(1)    
    
    
### User input to get the platform:
banner = '''
Select which platform you want to choose by entering the number:
1. HacktheBox
2. TryHackMe
3. Exit
'''
print(banner)
platform = input('Select the number: ')

### Logic for the choice provided.
if platform == '1':
    htb()
elif platform == '2':
    thm()
elif platform == '3':
    exit()
else:
    print('Not in the choices.')
    exit()
