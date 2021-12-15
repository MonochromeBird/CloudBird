#!/usr/bin/env python3
from git import Repo as _Repo
from ..baseStream import *
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
	
	getFromCloud(self) -> None:
		Called when the path doesn't have a metadata.
	
	initializeStream(self) -> None:
		Called when localizated a metadata on the path.
	
	downloadProtocol(self) -> None:
		The process of downloading cloud content to the stream's path.
	
	bakingProtocol(self) -> None:
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

	def getFromCloud(self) -> None:
		'''Called when the path doesn't have a metadata.'''
		self.repo = _Repo.clone_from(self.session['url'], cache)
		
	def initializeStream(self) -> None:
		'''Called when localizated a metadata on the path.'''
		self.repo = _Repo(self.session['path'])
	
	def downloadProtocol(self) -> None:
		'''The process of downloading cloud content to the stream's path.'''
		try:
			self.repo.git.fetch('--all')
			self.repo.git.reset('--hard', 'master')
		except:
			self.repo.git.pull()
	
	def bakingProtocol(self) -> None:
		'''The process before the upload.'''
		self.repo.git.add('*')
		self.repo.git.commit('-m', commit)
	
	def uploadProtocol(self) -> None:
		'''The process of uploading stream's content to the cloud.'''
		self.repo.git.push('--force')
	
	

	

	
