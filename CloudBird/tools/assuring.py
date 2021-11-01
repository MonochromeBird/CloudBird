#!/usr/bin/env python3
from os import mkdir

def assure_path(paths: list) -> None
	for path in paths:
		try: mkdir(path)
		except: pass