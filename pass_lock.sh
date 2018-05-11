#! /Library/Frameworks//Python.framework/Versions/3.6/bin/python3

import re,sys,pyperclip

passwords = {"account1_tag1 account1_tag2": "password1",
            "account2_tag1 account2_tag2": "password2",
            "account3_tag1 account3_tag2": "password3"}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

flag = 0
account = sys.argv[1]

for check in passwords:
    search = re.search('\\b' + account + '\\b',check)
    if search:
        pyperclip.copy(passwords[check])
        print('Password for ' + check + ' copied to clipboard.')
        flag = 1

if flag == 0:
    print("Account not found!")
    count = 0
    for find in passwords:
        search = re.search(account,find)
        if search:
            if count == 0:
                print("Did you mean?")
            print("=> " + find)
            count = count + 1
