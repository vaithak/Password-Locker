# Password-Locker

This script is for you if you forget your passwords frequently.

A command line password locker made in python. When you run this script from terminal and passing  
your account stored or related tags as a command line argument, then the script copies the account's  
password to your clipboard.The passwords are stored encrypted by 256-bit AES in data.ini file.

**Requirements**
Make sure you have python3 installed then run this command in terminal :-
```
pip install pyperclip,configparser,pycrypto,getpass,hashlib
```

**Usage: -**  

Run this command for first time
```
$ python3 pass_lock.py
```

To add new accounts
```
$ python3 pass_lock.py --add [account_name]
```

To copy password of account stored
```
$ python3 pass_lock.py --get [account_name]
```

To list all accounts stored
```
$ python3 pass_lock.py -l
```

For help menu
```
$ python3 pass_lock.py -h
```


*****Add security to the script*****
1. Run ```chmod 700 data.ini``` so that only the owner can access the data file.

*****Accessing your passwords*****
1. Example run for example accounts and password given.

![Example Image](https://raw.githubusercontent.com/vaithak/Password-Locker/master/example.png)
