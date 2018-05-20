import getpass
import hashlib
import configparser
import base64
import re
from Crypto.Cipher import AES

# configuration settings
config = configparser.ConfigParser()

# padding for encrypting
pad = lambda s : s + '?'*(int(config['SETUP']['BLOCK_SIZE']) - len(s)%int(config['SETUP']['BLOCK_SIZE']))

# unpadding for outputting
unpad = lambda s : s.replace('?','')

def encrypt(raw, private_key):
    raw = pad(raw)
    cipher = AES.new(private_key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(raw))

def decrypt(enc, private_key):
    cipher = AES.new(private_key, AES.MODE_ECB)
    enc = base64.b64decode(enc)
    return cipher.decrypt(enc)

def main():
    print("Setup will be done in pass_lock file only")

def setup():
    config.read('data.ini')
    if int(config['SETUP']['first_time']) == 1:
        print('Running the manager for first time')
        print('Please enter your password for encrypting and verification ( you will prompted for the password every time you run the main script)')

        # 256 bit key
        hashed_pw = hashlib.sha256(getpass.getpass(prompt='Password for script: ').encode('ascii').strip()).digest()
        check_pwd = hashlib.sha256(getpass.getpass(prompt='ReType the password: ').encode('ascii').strip()).digest()

        if(check_pwd == hashed_pw):

            config['SETUP']['first_time']='0'
            config['SETUP']['check'] = str(encrypt(config['SETUP']['check'],hashed_pw),'utf-8')

            # writing the changes back into the file
            with open('data.ini', 'w') as configfile:    # save
                config.write(configfile)

            # succesful status
            print("Setup complete! Now you can use the script normally")
        else:
            print("Passwords do not match!")
            print("Aborting...")

    else:
        print("Setup already done")
        print("exiting...")

if __name__ == '__main__':
    main()
