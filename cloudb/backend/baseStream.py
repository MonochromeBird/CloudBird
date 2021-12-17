#!/usr/bin/env python3
# [ 3th party / builtins modules ]
from importlib import import_module as _imp
from datetime import datetime as _datetime
from threading import Thread as _Thread
from random import randint as _randint
from shutil import rmtree as _rmtree
import logging as _
import os as _os

# [ CloudBird modules ]
from .services import addons as _addons
from . import manager
from ..utils import *
from .. import app

# [ The class ]
class BaseStream:
	'''Wrapper from an API to be used on CloudBird.'''
	def __init__(self, session: dict, addons: list = []) -> object:
		assure(session['path'], f'A path is required. Error on session {session["id"]} "{session["name"]}"', TypeError)
		_.basicConfig(filename = app.appdir.log + _os.sep + f'{session["id"]}.log', encoding='utf-8', level=_.INFO, format = '[%(levelname)s]: %(message)s')
		try:    _os.mkdir(session['path'])
		except: pass

		self.session = session
		self.repo    = None

		self.addons = [eval(f'_addons.{addon}') for addon in addons]
		self.loadingThread = _Thread(target = self.init)
		self.loadingThread.start()


	def init(self) -> None:
		try:
			if self.hasMetadata():
				_.info(f'Downloading at {_datetime.now()}.')
				manager.changeState('downloading', self.session)
				cache = app.appdir.cache+_os.sep+str(_randint(100000,999999))
				
				self.getFromCloud(cache)

				for thing in _os.listdir(cache):
					try:    _copy(cache+_os.sep+thing, self.session['path'])
					except: pass
				_rmtree(cache)
				_.info(f'Done downloading at {_datetime.now()}.')
				
		except Exception as error:
			# I could handle this for the case that the path doesn't exists but this is supposed to raise a error anyway :shrugy:
			_rmtree(cache)
			_.error(f'Failed downloading at {_datetime.now()}. Details:\n{error}')
			manager.changeState('error', self.session)
			raise error
		
		self.initializeStream()
		manager.changeState(self.session['backstage'], self.session)
		exit()

	def bake(self) -> None:
		'''Prepares the upload.'''
		if self.repo == None: return
		date = _datetime.now()
		_.info(f'Baking at {_datetime.now()}.')
		manager.changeState('baking', self.session)

		# [ Runs baking addons ]
		if self.addons:
			for addon in self.addons:
				addon.bake(self)

		# [ Bakes and handles errors that can potentially happen ]
		try: self.bakingProtocol(self.session['message'].format(date = date))
		except Exception as err:
			_.error(f'Error while baking at {_datetime.now()}. Details:\n{err}')
			return manager.changeState('error', self.session)
		
		manager.changeState(self.session['backstage'], self.session)
		_.info('Done baking.')
	
	def upload(self) -> None:
		'''Commit changes to cloud.'''
		if self.repo == None: return
		_.info(f'Uploading at {_datetime.now()}.')
		manager.changeState('uploading', self.session)

		# [ Runs uploading addons ]
		if self.addons:
			for addon in self.addons:
				addon.upload(self)
		
		# [ Uploads and handles errors that can potentially happen ]
		try: self.uploadProtocol()
		except Exception as err:
			_.error(f'Error while uploading at {_datetime.now()}. Details:\n{err}')
			return manager.changeState('error', self.session)

		manager.changeState(self.session['backstage'], self.session)
		_.info(f'Done uploading at {_datetime.now()}.')
	
	def download(self, pull: bool = False) -> None:
		'''Download changes from cloud.'''
		if self.repo == None: return
		_.info(f'Downloading at {_datetime.now()}.')
		manager.changeState('downloading', self.session)


		# [ Runs downloading addons ]
		if self.addons:
			for addon in self.addons:
				addon.download(self)

		# [ Downloads and handles errors that can potentially happen ]
		try: self.downloadProtocol()
		except Exception as err:
			_.error(f'Error while downloading at {_datetime.now()}. Details:\n{err}')
			return manager.changeState('error', self.session)
		
		manager.changeState(self.session['backstage'], self.session)
		_.info(f'Done downloading at {_datetime.now()}.')
