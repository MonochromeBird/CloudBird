#!/usr/bin/env python3
from os.path import dirname as _dirname, exists as _exists, isfile as _isfile, isdir as _isdir
from os import walk as _walk, mkdir as _mkdir, remove as _remove, sep as _sep
from json.decoder import JSONDecodeError as _JSONDecodeError
from json import load as _load, dump as _dump
from types import GeneratorType as _generator
from functools import lru_cache as _cache
from functools import reduce as _reduce
from shutil import rmtree as _rmtree
'''
CloudBird utils
'''

def assure(condition: any, message: str, error: Exception = AssertionError) -> None:
	'''Assertion but with different error types.'''
	if not bool(condition): raise error(message)

def fileFromDir(path: str) -> str:
	'''Being honest I don't remember why the fudge I did this but ok.'''
	return path.replace(_dirname(path)+'/', '')

def load(path: str, assureIfNotExists: any = []) -> dict:
	'''Fast loading for data notation.'''
	try:
		with open(path) as file:
			return _load(file)
	except FileNotFoundError:
		dump(path, assureIfNotExists)
		return load(path)

def dump(path: str, value: dict) -> int:
	'''Fast dumping for data notation.'''
	with open(path, 'w') as file:
		_dump(value, file)

def buildTree(root: str) -> dict:
	'''Build a tree of a path. Thanks to Andrew Clark.'''
	dir = {}
	root = root.rstrip(_sep)
	start = root.rfind(_sep) + 1
	for path, dirs, files in _walk(root):
		folders = path[start:].split(_sep)
		subdir = dict.fromkeys(files)
		parent = _reduce(dict.get, folders[:-1], dir)
		parent[folders[-1]] = subdir
	return dir

def read(path: str) -> bytes:
	'''Fast reader for file.'''
	try:
		with open(path, 'rb') as file:
			return file.read()
	except: return ''.encode()

def write(path: str, content: bytes) -> int:
	'''Fast writer for file.'''
	with open(path, 'wb') as file:
		return file.write(content)