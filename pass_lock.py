import re
import sys,os,inspect
import pyperclip
import hashlib
import getpass
import setup
import configparser
import base64
import argparse
from Crypto.Cipher import AES

# configurations
hashed_pwd = ''
config = configparser.ConfigParser()

# padding for encrypting
pad = lambda s : s + '?'*(int(config['SETUP']['BLOCK_SIZE']) - len(s)%int(config['SETUP']['BLOCK_SIZE']))

# unpadding for outputting
unpad = lambda s : s.replace('?','')


def encrypt(raw):
    private_key = hashed_pwd
    raw = pad(raw)
    cipher = AES.new(private_key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(raw))


def decrypt(enc):
    private_key = hashed_pwd
    cipher = AES.new(private_key, AES.MODE_ECB)
    enc = base64.b64decode(enc)
    return cipher.decrypt(enc)


def adduser(username):
    # adding a new user
    config['DATA'][username] = str(encrypt(getpass.getpass(prompt='Password for ' + username + ':')), 'utf-8')

    # writing the changes back into the file
    filename = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    with open(filename + '/data.ini', 'w') as configfile:    # save
        config.write(configfile)

    # Success message
    print("Account of " + username + " successfully added")


def retrieve(username):

    # to keep check of status
    flag = 0

    # finding the account
    for check in config['DATA'].keys():
        search = re.search('\\b' + username + '\\b',check)
        if search:
            pyperclip.copy(unpad(bytes.decode(decrypt(config['DATA'][check]))))
            print('Password for ' + check + ' copied to clipboard.')
            flag = 1

    # If account not found
    if flag == 0:
        print("Account not found!")
        count = 0
        for find in config['DATA'].keys():
            search = re.search(username,find)
            if search:
                if count == 0:
                    print("Did you mean?")
                print("=> " + find)
                count = count + 1


def listall():
    # list all users
    print("Currently added accounts:-")
    for check in config['DATA'].keys():
        print(check)


def hashed_pass(password):
    return hashlib.sha256(password.encode("utf-8")).digest()


def main():
    filename = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    config.read(filename + '/data.ini')

    if int(config['SETUP']['first_time']) == 1:
        setup.setup()
        exit()

    # authenticating the user
    global hashed_pwd
    hashed_pwd = hashed_pass(getpass.getpass(prompt='Password for script: '))
    if unpad(bytes.decode(decrypt(config['SETUP']['check']))) == "dictionary_check":

        # if less than one argument
        if len(sys.argv) <= 1:
            sys.argv.append('--help')

        # Main script
        parser = argparse.ArgumentParser(description='A Command line password manager')
        parser.set_defaults(func=lambda x: parser.print_usage())
        parser.add_argument('-a', '--add', nargs='?',action='store', help='Add a new account. Just provide the unique account-name along with it')
        parser.add_argument('-g', '--get', nargs='?',action='store', help='Copies the password of username passed as argument to your clipboard')
        parser.add_argument('-l', '--list',nargs='?',default='all',const='all', help='List usernames of accounts already added')
        args = parser.parse_args()

        # calling functions
        if args.add:
            adduser(args.add)
        elif args.get:
            retrieve(args.get)
        elif args.list:
            listall()

    else:
        print("Wrong password!!")


if __name__ == '__main__':
    main()
