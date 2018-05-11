# Password-Locker

This script is for you if you forget your passwords frequently.

A command line password locker made in python. When you run this script from terminal and passing  
your account stored or related tags as a command line argument, then the script copies the account's  
password to your clipboard.

**Requirements**
```
python3 with pyperclip module
```

**Usage: -**  

*****Adding your account and password*****
1. Open the script and edit the passwords dicctionary by replacing your accounts and password.
2. You can add space separated tags for each account as given inside the script as an example,  
   so that even if you type the related tag of your account then it copies the account's password.


*****Add security to the script*****
1. Run ```$chown root pass_block.sh``` on terminal so that root user becomes the owner of this script,  
   to protect your passwords. 
2. Run ```chmod 700 pass_block.sh``` so that only the owner=>root can access this script in any form.

*****Accessing your passwords*****
1. Example run for example accounts and password given. 
