#!/usr/bin/env python3
# [ Third party modules ]
from threading import Thread
from sched import scheduler

# [ CloudBird modules ]
from .backend import manager

'''
CloudBird's clock for background sessions.
'''

# [ Code ]
class Instance:
	def __init__(self, info: dict) -> object:
		self.session = manager.Session(info)
		self.info    = info

		self.thread  = Thread(target = self.session.execute)

class Clock:
	def __init__(self) -> object:
		self.sched = scheduler()
		self.sessions = {}

	def updateSessions(self) -> None:
		metadata = manager.loadSessionsMetaData()

		for data in metadata:
			if data not in self.sessions:
				self.sessions[data] = Instance(metadata[data])
				self.sessions[data].thread.start()
			else:
				self.sessions[data].session.config = metadata[data]
				self.sessions[data].info = metadata[data]
		
		del metadata
	
	def exec(self, ignore: bool = False) -> None:
		if not ignore:
			self.sched.enter(0, 0, self.exec, (True,))
			self.sched.run()

		self.sched.enter(10, 0, self.exec, (True,))
		self.updateSessions()

clock = Clock()
clock.exec()