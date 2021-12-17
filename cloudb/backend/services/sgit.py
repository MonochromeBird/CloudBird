#!/usr/bin/env python3
from random import randint as _randint
from git import Repo as _Repo
from ..baseStream import *
import shutil as _sh
import os as _os

'''
Git support for CloudBird.
'''

class Stream(BaseStream):
	'''
	Git Stream: the CloudBird mainstream.
	You can use this stream as a template for the stream you wanna make!

	hasMetadata(self) -> bool:
		Called when the stream needs to know if it has to download the metadata from the url.
	
	getFromCloud(self, cache: str) -> None:
		Called when the path doesn't have a metadata.
	
	initializeStream(self) -> None:
		Called when localizated a metadata on the path.
	
	downloadProtocol(self) -> None:
		The process of downloading cloud content to the stream's path.
	
	bakingProtocol(self, message: str) -> None:
		The process before the upload.
	
	uploadProtocol(self) -> None:
		The process of uploading stream's content to the cloud.
	'''
	def __init__(self, session: dict, addons: tuple = ()) -> object:
		self.session = session
		BaseStream.__init__(self, self.session, addons)
	
	def hasMetadata(self) -> bool:
		'''Called when the stream needs to know if it has to download the metadata from the url.'''
		return not _os.path.exists(self.session['path']+_os.sep+'.git')

	def getFromCloud(self, cache: str) -> None:
		'''Called when the path doesn't have a metadata.'''
		self.repo = _Repo.clone_from(self.session['url'], cache)
		
	def initializeStream(self) -> None:
		'''Called when localizated a metadata on the path.'''
		self.repo = _Repo(self.session['path'])
	
	def downloadProtocol(self) -> None:
		'''The process of downloading cloud content to the stream's path.'''
		err = None
		cache = app.appdir.cache+_os.sep+str(_randint(100000,999999))

		if _os.path.exists(path+_os.sep+'.gitignore'):
			gitignore = list(map(lambda x: x if not x.endswith(_os.sep) else x[:-1:], read(path+_os.sep+'.gitignore').decode().split('\n')))
		else:
			gitignore = []

		_os.mkdir(cache)
		for thing in _os.listdir(self.session['path']):
			if thing in gitignore: continue
			try:    _sh.copy(self.session['path'] + _os.sep + thing, cache)
			except: pass
		
		try:
			try:
				self.repo.git.pull('--force')
			except:
				self.repo.git.fetch('--all')
				self.repo.git.reset('--hard', 'master')
		except Exception as error:
			err = error
		
		for thing in _os.listdir(self.session['path']):
			try:    _sh.copy(cache + _os.sep + thing, self.session['path'])
			except: pass
		
		_sh.rmtree(cache)
		
		if err: raise err
	
	def bakingProtocol(self, message: str) -> None:
		'''The process before the upload.'''
		self.repo.git.add('*')
		self.repo.git.commit('-m', message)
	
	def uploadProtocol(self) -> None:
		'''The process of uploading stream's content to the cloud.'''
		try: self.repo.git.push()
		except:
			raiseErr = False
			cache = app.appdir.cache+_os.sep+str(_randint(100000,999999))

			if _os.path.exists(path+_os.sep+'.gitignore'):
				gitignore = list(map(lambda x: x if not x.endswith(_os.sep) else x[:-1:], read(path+_os.sep+'.gitignore').decode().split('\n')))
			else:
				gitignore = []
			
			_os.mkdir(cache)
			for thing in _os.listdir(self.session['path']):
				if thing in gitignore: continue
				try:    _sh.copy(self.session['path'] + _os.sep + thing, cache)
				except: pass
			
			try: self.repo.git.pull('--force')
			except Exception as err: raiseErr = err

			for thing in _os.listdir(self.session['path']):
				try:    _sh.copy(cache + _os.sep + thing, self.session['path'])
				except: pass
			
			_sh.rmtree(cache)
			
			if not raiseErr:
				self.repo.git.push('--force')
			else: raise raiseErr
			
	
	

	

	
