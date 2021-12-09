#!/usr/bin/env python3
# [ 3th party / builtins modules ]
from datetime import datetime as _datetime
from sched import scheduler as _scheduler
from threading import Thread as _Thread
import os as _os

# [ CloudBird modules ]
from .compare import compare
from . import services
from ..utils import *
from .. import app

'''
The core of CloudBird.
'''

class Session:
	'''A sync task managed by CloudBird.'''
	def __init__(self, config: dict) -> object:
		self.streamType = eval(f'''_services.{config['stream']}''')
		self.stream = self.streamType(config['path'], config['url'])
		self.config = config
		
		self.sched = _scheduler()
	
	def execute(self) -> None:
		date = _datetime.now()
		self.stream.download()
		if compare(self.stream.path):
			self.stream.bake(self.config['commit'].format(date = date))
			self.stream.upload()
		self.sched.enter(self.config['time'], self.config['priority'], self.execute)
		self.sched.run()
		
def loadSessions() -> dict:
	'''Instanciate sessions'''
	return {session['id']:Session(session) for session in load(app.appdirs.data + _os.sep + 'sessions.yaml')}

def createSession(info: dict) -> int:
	if not exists(app.appdirs.data + _os.sep + 'sessions.yaml'):
		return dump(app.appdirs.data + _os.sep + 'sessions.yaml', [info])
	return dump(app.appdirs.data + _os.sep + 'sessions.yaml', load(app.appdirs.data + _os.sep + 'sessions.yaml') + [info])

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


