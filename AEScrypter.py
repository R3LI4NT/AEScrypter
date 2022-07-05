#!/usr/bind/env python
#_*_ coding: utf8 _*_

from pyfiglet import Figlet
from termcolor import colored
import pyAesCrypt
import argparse
import os
import time

RED_NORMAL = '\033[0;31m'
END = '\033[0m'

parse = argparse.ArgumentParser()
########## ENCRYPT FILE
parse.add_argument("-e",'--encrypt',help="Encrypt file")
########## DECRYPT FILE
parse.add_argument("-d",'--decrypt',help="Decrypt file")
######### BUFFERSIZE
parse.add_argument("-b",'--buffersize',help="Buffer size (128 / 192 / 256)")
######### PASSWORD
parse.add_argument("-p",'--password',help="Password to encrypt and decrypt file ")
parse = parse.parse_args()


def encryptFile():
	file = parse.encrypt
	bufferSize = round(int(parse.buffersize)) * 1024
	password = parse.password

	pyAesCrypt.encryptFile(f"{file}", f"{file}.aes", password, bufferSize)
	os.system(f'shred -n 10 -z -u {file}')
	f=Figlet(font='slant')
	print(colored(f.renderText(' File ENCRYPTED'),'red'))
	print(f"Before --> {file}")
	print(f"Now --> {f'{file}.aes'}")


def decryptFile():
	file = parse.decrypt
	bufferSize = round(int(parse.buffersize)) * 1024
	password = parse.password

	pyAesCrypt.decryptFile(f"{file}.aes", f"{file}", password, bufferSize)
	os.system(f"shred -u {f'{file}.aes'}")
	f=Figlet(font='slant')
	print(colored(f.renderText(' File DECRYPTED'),'green'))
	print(f"Before --> {f'{file}.aes'}")
	print(f"Now --> {file}")


def main():
	if parse.encrypt:
		encryptFile()

	elif parse.decrypt:
		decryptFile()

	else:
		print(f"\n{RED_NORMAL}[ERR0R]{END} Argument invalid\nRequest help : python3 AEScrypter.py --help\nExit the script...")
		time.sleep(2)
		exit(0)		


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()	
