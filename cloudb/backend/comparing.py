#!/usr/bin/env python3
from os.path import abspath as _abspath, dirname as _dirname
from os import walk as _walk, sep as _sep, mkdir as _mkdir
from hashlib import sha3_256 as _sha
from .. import app as _app
from ..utils import *

'''
Comparing module for CloudBird!
'''

def hashTree(path: str) -> dict:
	'''Makes a hash of every single file it founds on the tree'''
	path = _abspath(path)
	return {p+_sep+file:_sha(read(p+_sep+file)).hexdigest() for p, d, files in _walk(path) for file in files}

def hashText(tree: dict, remove: str = '') -> str:
	'''Turns the hashTree into str.'''
	return '\n'.join([f'{item if not remove else item.replace(remove, "")}: \t {tree[item]}' for item in tree])

def compare(path: str) -> bool:
	'''Compares a folder with its previous version.'''
	hashFile 	= f'{_app.appdir.data+_sep}hashs{_sep+path.replace(_sep,".")}'
	currentHash = hashText(hashTree(path))
	pastHash 	= None

	if not exists(hashFile):
		if not exists(_dirname(hashFile)):
			_mkdir(_dirname(hashFile))
		else:
			write(hashFile, currentHash.encode())
		return False
	else:
		pastHash = read(hashFile).decode()
	
	if pastHash != currentHash:
		write(hashFile, currentHash.encode())
		return True
	
	return False