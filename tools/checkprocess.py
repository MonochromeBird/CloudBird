#!/usr/bin/env python
from appdirs import user_cache_dir
from datetime import datetime
from pickle import dump
from time import sleep
from git import Repo
from check import *

cache = user_cache_dir('CloudBird')
try: mkdir(cache)
except: pass

def start(repo: Repo, time: int = 60*5) -> None:
	with open(cache+'/time','wb') as cachefile:
		dump(datetime.now(), cachefile)

	while True:
		print(compare(repo.path))
		# repo.commit('Time elapsed (hh:mm:ss.ms) {}'.format(datetime.now()))
		# repo.push()
		sleep(time)

start(Repo('k','~/playground/'), 5)
