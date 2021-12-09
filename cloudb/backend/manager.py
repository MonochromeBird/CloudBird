#!/usr/bin/env python3
# [ 3th party / builtins modules ]
from importlib import import_module as _imp
from datetime import datetime as _datetime
from sched import scheduler as _scheduler
from threading import Thread as _Thread
import os as _os

# [ CloudBird modules ]
from .compare import compare as _compare
from . import services as _services
from ..utils import *
from .. import app

'''
The core of CloudBird.
'''

class Session:
	'''A sync task managed by CloudBird.'''
	def __init__(self, config: dict) -> object:
		_imp(f'''.services.{config['stream']}''', __package__)
		self.streamType = eval(f'''_services.{config['stream']}''').Stream
		self.stream = self.streamType(config['path'], config['url'])
		self.config = config
		
		self.sched = _scheduler()
	
	def execute(self) -> None:
		date = _datetime.now()
		self.stream.download()
		if _compare(self.stream.path):
			self.stream.bake(self.config['commit'].format(date = date))
			self.stream.upload()
		self.sched.enter(self.config['time'], self.config['priority'], self.execute)
		self.sched.run()
		
def loadSessions() -> dict:
	'''Instanciate sessions'''
	return {session['id']:Session(session) for session in load(app.appdir.data + _os.sep + 'sessions.json')}

def createSession(info: dict) -> int:
	if not _os.exists(app.appdir.data + _os.sep + 'sessions.json'):
		return dump(app.appdir.data + _os.sep + 'sessions.json', [info])
	return dump(app.appdir.data + _os.sep + 'sessions.json', load(app.appdir.data + _os.sep + 'sessions.json') + [info])

class Clock:
	def __init__(self) -> object:
		self.sessions = loadSessions()
		self.threads  = {}
		self.queryThreads(self.sessions)

	def start(self) -> None:
		for thread in self.threads:
			self.threads[thread].start()
	
	def stop(self) -> None:
		for thread in self.threads:
			self.threads[thread]._stop()
			del     self.threads[thread]
			self.queryThreads([self.sessions[thread]])
	
	def queryThreads(self, sessions: list) -> None:
		for session in sessions:
			self.threads[session.config['id']] = _Thread(target = session.execute)


