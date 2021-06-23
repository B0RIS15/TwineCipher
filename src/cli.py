import argparse
import sys
from .twine import Twine


def main():
    twine = Twine(key_size=128)
    tmp = input("Write string: ")
    print(tmp)
    print(f'Encryption Key: "{twine.key}"', flush=True)
    enc = twine.encrypt(tmp)
    print(enc)
    print(f'Decryption Key: "{twine.key}"', flush=True)
    print(twine.decrypt(enc))
