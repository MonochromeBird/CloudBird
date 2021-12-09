#!/usr/bin/env python3
from . import addons as _addons
from git import Repo

name = 'git'

'''
Git support for CloudBird.
'''

class Stream:
	'''Wrapper from an API to be used on CloudBird.'''
	def __init__(self, path: str, url: str, addons: list = []) -> object:
		assure(path, 'A path is required.', TypeError)
		if url: self.repo = Repo.clone_from(url, path)
		else:   self.repo = Repo(path)
		self.name = name
		self.path = path
		self.url  = url
		self.name = 'git'

		self.addons = [eval(f'_addons.{addon}') for addon in addons]

	
	def bake(self, commit: str) -> None:
		'''Prepares the upload.'''
		# [ Runs baking addons ]
		if self.addons:
			for addon in self.addons:
				addon.bake(self)

		self.repo.git.add('*')
		self.repo.git.commit('-m', commit)
	
	def upload(self) -> None:
		'''Commit changes to cloud.'''
		# [ Runs uploading addons ]
		if self.addons:
			for addon in self.addons:
				addon.upload(self)
		
		self.repo.git.push()
	
	def download(self) -> None:
		'''Download changes from cloud.'''
		# [ Runs downloading addons ]
		if self.addons:
			for addon in self.addons:
				addon.download(serm lf)

		self.repo.git.pull()
	