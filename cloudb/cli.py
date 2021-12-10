#!/usr/bin/env python3
from argparse import ArgumentParser
from sys import argv

if __name__ != '__main__': exit()

def new(args: ArgumentParser) -> int:
	pass

def manage(args: ArgumentParser) -> int:
	pass

def config(args: ArgumentParser) -> int:
	pass

if len(argv) < 2:
	pass
else:
	try:
		choice = {
			'new':	  new,
			'manage': manage,
			'config': config,
		}[argv[1]]
	except: exit(f'{argv[1]} is not an option.')