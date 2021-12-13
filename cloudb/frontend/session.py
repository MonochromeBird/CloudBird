#!/usr/bin/env python3
# -*- enconding:utf-8 -*-

# [ 3th party Libraries ]
from datetime import datetime
from threading import Thread
from random import randint
from hashlib import md5
import os as _os
import sys
import re

# [ The uic (graphical user interface) ]
from .gui.home import *

# [ Backend ]
from ..backend import manager, validate
from .. import app as _app
from ..utils import *

updateDelay = 300

# [ Qt class ]
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.showSessionsDetails(0)
		self.ui.ErrorZone.hide()
		self.ui.InfoZone.hide()

		self.currentSession = {}
		self.currentInfo = 0
		self.sessions = {}

		self.icons = {
			'states':{
				'Online':  'network',
				'Offline': 'network-offline',
				'Error':   'network-error',
				'Waiting': 'wait'},
			
			'power':{
				'On': 'turnon',
				'Off': 'exit'
			}
		}

		self.ui.Sessions.itemActivated.connect(self.select)
		self.ui.Apply.pressed.connect(self.updateSession)
		self.ui.Toggle.toggled.connect(self.toggleActive)
		self.ui.Download.pressed.connect(self.download)
		self.ui.GetPath.pressed.connect(self.setPath)
		self.ui.Add.pressed.connect(self.newSession)
		self.ui.Upload.pressed.connect(self.upload)
		self.initSessions()

		self.updateTimer = QTimer()
		self.updateTimer.start(updateDelay)
		self.updateTimer.timeout.connect(self.updateSessionsState)

	def setPath(self) -> None:
		path = QFileDialog.getExistingDirectory(self, 'Choose the path to use in this session')
		self.ui.Path.setText(path)
	
	def showSessionsDetails(self, show: bool = True) -> None:
		if show:
			self.ui.SessionW.show()
			self.ui.CenterLine.show()
		else:
			self.ui.SessionW.hide()
			self.ui.CenterLine.hide()
		
	def error(self, message: str, errorType: str = 'error', errorNum: int = 0) -> None:
		self.ui.ErrorZone.show()
		self.ui.ErrorMessage.setText(f'{errorType} ({errorNum}): {message}')

	def info(self, message: str, infoType: str = 'error', infoNum: int = 0) -> None:
		self.ui.InfoZone.show()
		self.ui.InfoMessage.setText(f'{infoType}: {message}')
		self.currentInfo = infoNum
	
	def closeInfo(self, info: int) -> None:
		if info == self.currentInfo: self.ui.InfoZone.hide()

	def newSession(self) -> None:
		self.createObject('<no name>', 'waiting')

	def createObject(self, name: str, state: str = "Online", id: str = '') -> None:
		if not id: id = manager.generateID()
		
		shownSessions = self.getShownSessions()
		shownSessions = {s.text(2):s for s in shownSessions}
		if not (id in shownSessions):
			item = QTreeWidgetItem([name, state, id])
			self.setStatus(item, state)
			self.ui.Sessions.addTopLevelItems([item])
			self.sessions[id] = item
		else:
			self.setStatus(shownSessions[id], state)
			shownSessions[id].setText(0, name)
	
	def setStatus(self, item: QTreeWidgetItem, state: str) -> QTreeWidgetItem:
		if state.capitalize() not in self.icons['states']: raise IndexError(f'Invalid state "{state}"')
		item.setIcon(0, QIcon(QPixmap(f':/icons/{self.icons["states"][state.capitalize()]}.svg')))
		item.setText(1, state.capitalize())
		return item
	
	def select(self, item: QTreeWidgetItem) -> None:
		sessions = manager.loadSessionsMetaData()
		self.updateStreams()
		self.showSessionsDetails()

		session = False if item.text(2) not in sessions else sessions[item.text(2)]

		self.currentSession = manager.baseSession if not session else session
		self.forceChanges()
		self.updateSession(item.text(2), True)
	
	def updateSession(self, id: bool = False, ignoreValidation = False) -> None:
		if id: self.ui.ID.setText(id)
		if not ignoreValidation: valid = self.validateInput()
		else: valid = True
		if valid:
			self.currentSession['stream'] = self.ui.Stream.currentText()
			self.currentSession['priority'] = self.ui.Priority.value()	
			self.currentSession['time'] = self.ui.Time.value()
			self.currentSession['name'] = self.ui.Name.text()
			self.currentSession['path'] = self.ui.Path.text()
			self.currentSession['url'] = self.ui.Url.text()
			self.currentSession['id'] = self.ui.ID.text()
			self.currentSession['state'] = 'online' if self.ui.Toggle.toggled else 'offline'
			
			if not ignoreValidation: 
				new = load(_app.appdir.data+_os.sep+'sessions.json', [])
				for session in range(len(new)):	
					if new[session]['id'] == (id if id else self.currentSession['id']):
						del new[session]
						new.append(self.currentSession)
						break
				dump(_app.appdir.data+_os.sep+'sessions.json', new)
				del new
			
			self.forceChanges()
			self.initSessions()
		del valid

	def forceChanges(self) -> None:
		self.updateStreams()
		self.ui.Stream.setCurrentIndex(self.ui.Stream.findText(manager.displayNames.fancyName(self.currentSession['stream'])))
		self.ui.Priority.setValue(self.currentSession['priority'])
		self.ui.SessionName.setText(self.currentSession['name'] if self.currentSession['name'] else 'New Session')
		self.ui.Time.setValue(self.currentSession['time'])
		self.ui.Name.setText(self.currentSession['name'])
		self.ui.Path.setText(self.currentSession['path'])
		self.ui.Url.setText(self.currentSession['url'])
		self.ui.ID.setText(self.currentSession['id'])

	def toggleActive(self, toggle: bool) -> None:
		self.currentSession['state'] = 'Online' if toggle else 'Offline'
		self.ui.Toggle.setIcon(QIcon(QPixmap(':/icons/'+self.icons['power'][('On' if toggle else 'Off')]+'.svg')))

	def updateStreams(self) -> None:
		self.ui.Stream.clear()
		self.ui.Stream.addItems(list(map(lambda x: manager.displayNames.fancyName(x), manager.displayNames.getStreams())))

	def initSessions(self, metadatamode: bool = False) -> None:
		if not _os.path.exists(_app.appdir.data+_os.sep+'sessions.json'):
			dump(_app.appdir.data+_os.sep+'sessions.json', [])
		
		if len(read(_app.appdir.data+_os.sep+'sessions.json').decode()) == 0:
			return
		
		sessions = manager.loadSessionsMetaData()
		names = list(sessions.keys())
		names.sort()

		for session in names:
			try: self.createObject(sessions[session]['name'], sessions[session]['state'], sessions[session]['id'])
			except Exception as error: self.error(f'There are unknow sessions that may be corrupted. [{error}]', 'Session load error', 500)
		
		del names

		if not metadatamode:
			self.info('This can take some time.', 'Updating sessions', 500)
			try: self.sessions = manager.loadSessions()
			except Exception as error:
				tb = sys.exc_info()[2]
				self.error(error.__class__.__name__+': '+str(error.with_traceback(tb)), 'Failed to initialize sessions', 501)
				print(error.__class__.__name__+': '+str(error.with_traceback(tb)))
			self.closeInfo(500)
	
	def getShownSessions(self) -> list:
		root = self.ui.Sessions.invisibleRootItem()
		return [root.child(child) for child in range(root.childCount())]

	def validateInput(self) -> bool:
		if not validate.links(self.ui.Url.text()):
			self.error('That doesn\'t looks like a valid url.', 'Invalid url', 301)
			return False
		if not self.ui.Path.text():
			self.error('Please, insert a path.', 'Path required', 302)
			return False
		if not self.ui.Stream.currentText():
			self.error('Please, choose a stream for your session.', 'Stream required', 303)
			return False
		self.ui.ErrorZone.hide()
		return True
	
	def updateSessionsState(self) -> None:
		self.initSessions(True)
		self.updateTimer.start(updateDelay)
	
	def download(self) -> None:
		if self.currentSession['id'] not in self.sessions:
			return self.info('Canceling download because the selected session its not instanced.')
		session = self.sessions[self.currentSession['id']].stream
		session.download()

	def upload(self) -> None:
		if self.currentSession['id'] not in self.sessions:
			return self.info('Canceling upload because the selected session its not instanced.')
		session = self.sessions[self.currentSession['id']].stream
		session.bake(str(datetime.now()))
		session.upload()
	

if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec())
