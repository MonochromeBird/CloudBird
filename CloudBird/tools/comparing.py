#!/usr/bin/env python
from subprocess import PIPE, check_output
from os import mkdir, remove, getcwd
from os.path import exists, isfile
from appdirs import user_data_dir
from assuring import assure_path

tools = '/'.join(__file__.split('/')[:-1:])
data  = user_data_dir('CloudBird')
assure_path([data, f'{data}/sumfiles/'])

def sha256sum(path: str) -> str:
	return check_output(f'{tools}/sha256rec {path[:-1:] if path.endswith("/") else path}', shell = True).decode()

def save_state(path: str = getcwd()) -> str:
	sum = sha256sum(path)
	with open(f'{data}/sumfiles/{path.replace("/",".")}', 'w') as file:
		file.write(sum)
	return sum

def compare(path) -> bool:
	sum = sha256sum(path)
	with open(f'{data}/sumfiles/{path.replace("/",".")}') as file:
		if sum != file.read():
			save_state(path)
			return True
	return False

