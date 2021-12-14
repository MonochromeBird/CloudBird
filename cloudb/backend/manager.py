#!/usr/bin/env python3
# [ 3th party / builtins modules ]
from importlib import import_module as _imp
from datetime import datetime as _datetime
from sched import scheduler as _scheduler
from threading import Thread as _Thread
from random import randint as _randint
from hashlib import md5 as _md5
import os as _os

# [ CloudBird modules ]
from .compare import compare as _compare
from .services import addons as _addons
from . import services as _services
from ..utils import *
from .. import app

'''
The core of CloudBird.
'''

baseSession = {
	'name':      '',
	'id':        '',
	'state':     'waiting',
	'path':      '', 
	'url':       '',
	'stream':    '',
	'time':      1800,
	'priority':  0,
	'addons':    [],
	'backstage': 'online'
}

class Session:
	'''A sync task managed by CloudBird.'''
	def __init__(self, config: dict) -> object:
		config['stream'] = displayNames.importName(config['stream'])
		_imp(f'''.services.{config['stream']}''', __package__)
		self.streamType = eval(f'''_services.{config['stream']}''').Stream
		self.stream = self.streamType(config['path'], config['url'], config)
		self.config = config
		
		self.sched = _scheduler()
	
	def execute(self) -> None:
		'''Main session execute.'''
		date = _datetime.now()
		self.stream.download()
		if _compare(self.stream.path):
			self.stream.bake(self.config['commit'].format(date = date))
			self.stream.upload()
		self.sched.enter(self.config['time'], self.config['priority'], self.execute)
		self.sched.run()
		
def loadSessions() -> dict:
	'''Instanciate sessions'''
	return {session['id']:Session(session) for session in load(app.appdir.data + _os.sep + 'sessions.json', [])}
		
def loadSessionsMetaData() -> dict:
	'''Instanciate sessions'''
	try: return {session['id']:session for session in load(app.appdir.data + _os.sep + 'sessions.json', [])}
	except: return {}

def createSession(info: dict) -> int:
	'''Creates a session on the main session database.'''
	if not _os.exists(app.appdir.data + _os.sep + 'sessions.json'):
		return dump(app.appdir.data + _os.sep + 'sessions.json', [info])
	return dump(app.appdir.data + _os.sep + 'sessions.json', load(app.appdir.data + _os.sep + 'sessions.json', []) + [info])

class Clock:
	'''The main clock of cloudb.'''
	def __init__(self) -> object:
		self.sessions = loadSessions()
		self.threads  = {}
		self.queryThreads(self.sessions)

	def startAll(self) -> None:
		'''Starts every thread.'''
		for thread in self.threads:
			self.threads[thread].start()
	
	def stopAll(self) -> None:
		'''Stops every thread.'''
		for thread in self.threads:
			self.threads[thread]._stop()
			del     self.threads[thread]
			self.queryThreads([self.sessions[thread]])
	
	def start(self, id: str) -> None:
		'''Starts a single session thread.'''
		self.threads[id].start()
	
	def stop(self, id: str) -> None:
		'''Stops a single session thread.'''
		self.threads[id]._stop()
		del     self.threads[id]
		self.queryThreads([self.sessions[id]])
	
	def queryThreads(self, sessions: list) -> None:
		'''Create threads for sessions.'''
		for session in sessions:
			self.threads[session.config['id']] = _Thread(target = session.execute)

class displayNames:
	def __init__(self) -> object:
		self.addons = {self.fancyName(addon):addon for addon in self.getAddons()}
		self.streams = {self.fancyName(stream):stream for stream in self.getStreams()}

	def fancyName(content: str, file = True) -> str:
		'''Takes a Python file name and returns a fancy and usable name :)'''
		result = content.replace('_', ' ').replace('-', ' ').capitalize()
		return '.'.join(result.split('.')[:-1:]) if '.' in result and file else result

	def importName(content: str, file = True) -> str:
		'''Takes a Python file name and returns a fancy and usable name :)'''
		return content.replace(' ','_').lower()

	def getStreams() -> list:
		'''Get all cloudb streams.'''
		return next(_os.walk(_services.__path__[0]), (None, None, []))[2]

	def getAddons() -> list:
		'''Get all cloudb addons.'''
		return next(_os.walk(_addons.__path__[0]), (None, None, []))[2]

def generateID() -> str:
	id = _md5(_randint(100000, 999999).to_bytes(6, 'little')).hexdigest()
	try:
		for session in load(app.appdir.data+_os.sep+'sessions.json', []):
			if session['id'] == id:
				del id
				del session
				return generateID()
	except: pass
	return id

def editSession(id: str, content: dict) -> None:
	new = load(app.appdir.data+_os.sep+'sessions.json', [])
	for session in range(len(new)):
		if new[session]['id'] == id:
			del new[session]
			break
	
	new.append(content)
	dump(app.appdir.data+_os.sep+'sessions.json', new)
	del new
	