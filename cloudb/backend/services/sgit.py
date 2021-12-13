#!/usr/bin/env python3
# [ 3th party / builtins modules ]
from shutil import rmtree as _rmtree, move as _move
from importlib import import_module as _imp
from threading import Thread as _Thread
from random import randint as _randint
from git import Repo as _Repo
import os as _os

# [ CloudBird modules ]
from . import addons as _addons
from .. import manager
from ...utils import *
from ... import app

name = 'git'

'''
Git support for CloudBird.
'''

class Stream:
	'''Wrapper from an API to be used on CloudBird.'''
	def __init__(self, path: str, url: str, session: dict, addons: list = []) -> object:
		assure(path, f'A path is required. Error on session {session["id"]} "{session["name"]}"', TypeError)
		try: _os.mkdir(path)
		except: pass

		self.session = session
		self.repo = None
		self.name = name
		self.path = path
		self.name = 'git'
		self.url  = url

		self.addons = [eval(f'_addons.{addon}') for addon in addons]

		self.session['state'] = 'waiting'
		manager.editSession(self.session['id'], self.session)
		self.loadingThread = _Thread(target = self.init)
		self.loadingThread.start()


	def init(self) -> None:
		try:
			if self.url and not _os.path.exists(self.path+_os.sep+'.git'):
				cache = app.appdir.cache+_os.sep+str(_randint(100000,999999))
				_Repo.clone_from(self.url, cache)

				for thing in _os.listdir(cache):
					try:    _move(cache+_os.sep+thing, self.path)
					except: pass
				_rmtree(cache)
				
		except Exception as error:
			# I could handle this for the case that the path doesn't exists but this is supposed to raise a error anyway :shrugy:
			_rmtree(cache)
			raise error
		
		self.repo = _Repo(self.path)
		self.session['state'] = 'online'
		manager.editSession(self.session['id'], self.session)
		exit()

	def bake(self, commit: str) -> None:
		'''Prepares the upload.'''
		if self.repo == None: return

		# [ Runs baking addons ]
		if self.addons:
			for addon in self.addons:
				addon.bake(self)

		self.repo.git.add('*')
		self.repo.git.commit('-m', commit)
	
	def upload(self) -> None:
		'''Commit changes to cloud.'''
		if self.repo == None: return

		# [ Runs uploading addons ]
		if self.addons:
			for addon in self.addons:
				addon.upload(self)
		
		self.repo.git.push()
	
	def download(self) -> None:
		'''Download changes from cloud.'''
		if self.repo == None: return

		# [ Runs downloading addons ]
		if self.addons:
			for addon in self.addons:
				addon.download(self)

		self.repo.git.pull()
