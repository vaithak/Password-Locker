# configuration settings
import base64
import configparser

from Crypto.Cipher import AES

config = configparser.ConfigParser()


# padding for encrypting
def pad(s):
    return s + '?' * (int(config['SETUP']['BLOCK_SIZE']) - len(s) % int(config['SETUP']['BLOCK_SIZE']))


# unpadding for outputting
def unpad(s):
    s.replace('?', '')


def encrypt(raw, private_key):
    raw = pad(raw)
    cipher = AES.new(private_key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(raw))


def decrypt(enc, private_key):
    cipher = AES.new(private_key, AES.MODE_ECB)
    enc = base64.b64decode(enc)
    return cipher.decrypt(enc)
