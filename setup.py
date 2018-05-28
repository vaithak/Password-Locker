import getpass
import hashlib
import inspect
import os

from common import encrypt, config


def setup():
    filename = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    config.read(filename + '/data.ini')
    if int(config['SETUP']['first_time']) == 1:
        print('Running the manager for first time')
        print('Please enter your password for encrypting and verification ( you will prompted for the password '
              'every time you run the main script)')

        # 256 bit key
        hashed_pw = hashlib.sha256(getpass.getpass(prompt='Password for script: ').encode('ascii').strip()).digest()
        check_pwd = hashlib.sha256(getpass.getpass(prompt='ReType the password: ').encode('ascii').strip()).digest()

        if check_pwd == hashed_pw:

            config['SETUP']['first_time'] = '0'
            config['SETUP']['check'] = str(encrypt(config['SETUP']['check'], hashed_pw), 'utf-8')

            # writing the changes back into the file
            filename = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
            with open(filename + '/data.ini', 'w') as configfile:  # save
                config.write(configfile)

            # succesful status
            print("Setup complete! Now you can use the script normally")
        else:
            print("Passwords do not match!")
            print("Aborting...")

    else:
        print("Setup already done")
        print("exiting...")
