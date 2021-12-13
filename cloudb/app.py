#!/usr/bin/env python3
import appdirs as _apd
from os import mkdir

'''
Just common information for general use.
'''

appname = 'CloudBird'
class appdir:
	config = _apd.user_config_dir(appname)
	state = _apd.user_state_dir(appname)
	cache = _apd.user_cache_dir(appname)
	data = _apd.user_data_dir(appname)
	log = _apd.user_log_dir(appname)

for path in dir(appdir):
	if '_' in path: continue
	try:    mkdir(eval('appdir.'+path))
	except Exception as err: print(f'Skiping creating appdir\t{path}\tbecause\t{err}.') 
