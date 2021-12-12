#!/usr/bin/env python3
# -*- enconding:utf-8 -*-

# [ 3th party Libraries ]
from random import randint
from hashlib import md5
import os as _os
import sys

# [ The uic (graphical user interface) ]
from .gui.home import *

# [ Backend ]
from ..backend import manager
from .. import app as _app
from ..utils import *


# [ Qt class ]
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.showSessionsDetails(0)
		self.ui.ErrorZone.hide()
		self.ui.InfoZone.hide()

		self.sessions = {}
		self.currentSession = {}

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
		self.ui.GetPath.pressed.connect(self.setPath)
		self.ui.Add.pressed.connect(self.newSession)
		self.initSessions()

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

	def info(self, message: str, infoType: str = 'error') -> None:
		self.ui.InfoZone.show()
		self.ui.InfoMessage.setText(f'{infoType}: {message}')

	def newSession(self) -> None:
		self.createObject('<no name>', 'waiting')

	def createObject(self, name: str, state: str = "Online", id: str = manager.generateID()) -> None:
		item = QTreeWidgetItem([name, state, id])
		self.setStatus(item, state)
		self.ui.Sessions.addTopLevelItems([item])
		self.sessions[id] = item
	
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
		self.ui.SessionName.setText(item.text(0))

		self.currentSession = {} if not session else session
		if self.currentSession != {}:
			self.forceChanges()
		self.updateSession(item.text(2))
	
	def updateSession(self, id: bool = False) -> None:
		if id: self.ui.ID.setText(id)
		valid =  self.validateInput()
		if valid:
			new = load(_app.appdir.data+_os.sep+'sessions.json', [])
			
			for session in range(len(new)):
			
				if new[session]['id'] == (id if id else self.currentSession['id']):
					del new[session]
					break

			self.currentSession['stream'] = self.ui.Stream.currentText()
			self.currentSession['priority'] = self.ui.Priority.value()	
			self.currentSession['time'] = self.ui.Time.value()
			self.currentSession['name'] = self.ui.Name.text()
			self.currentSession['path'] = self.ui.Path.text()
			self.currentSession['url'] = self.ui.Url.text()
			self.currentSession['id'] = self.ui.ID.text()
			self.currentSession['state'] = 'Online' if self.ui.Toggle.toggled else 'Offline'
			
			if self.currentSession['stream']: new.append(self.currentSession)
			dump(_app.appdir.data+_os.sep+'sessions.json', new)
			del new
			
			self.forceChanges()
			self.initSessions()
		else:
			self.error(valid[0], valid[1], valid[2])
		del valid

	def forceChanges(self) -> None:
		self.updateStreams()
		self.ui.Stream.setCurrentIndex(self.ui.Stream.findText(manager.displayNames.fancyName(self.currentSession['stream'])))
		self.ui.Priority.setValue(self.currentSession['priority'])
		self.ui.SessionName.setText(self.currentSession['name'])
		self.ui.Time.setValue(self.currentSession['time'])
		self.ui.Name.setText(self.currentSession['name'])
		self.ui.Path.setText(self.currentSession['path'])
		self.ui.Url.setText(self.currentSession['url'])
		self.ui.ID.setText(self.currentSession['id'])


	def toggleActive(self, toggle: bool) -> None:
		self.currentSession['active'] = toggle
		self.ui.Toggle.setIcon(QIcon(QPixmap(':/icons/'+self.icons['power'][('On' if toggle else 'Off')]+'.svg')))

	def updateStreams(self) -> None:
		self.ui.Stream.clear()
		self.ui.Stream.addItems(list(map(lambda x: manager.displayNames.fancyName(x), manager.displayNames.getStreams())))
	
	def initSessions(self, metadatamode: bool = False) -> None:
		# TODO: MAKE THE NON-METADATA MODE.
		self.ui.Sessions.clear()
		if not _os.path.exists(_app.appdir.data+_os.sep+'sessions.json'):
			dump(_app.appdir.data+_os.sep+'sessions.json', [])
		
		if len(read(_app.appdir.data+_os.sep+'sessions.json').decode()) == 0:
			return
		
		sessions = manager.loadSessionsMetaData()
		for session in sessions:
			try: self.createObject(sessions[session]['name'], sessions[session]['state'], sessions[session]['id'])
			except Exception as error: self.error(f'There are unknow sessions that may are corrupted. [{error}]', 'Session load error', 500)
		
		if not metadatamode:
			try: self.sessions = manager.loadSessions()
			except Exception as error:
				tb = sys.exc_info()[2]
				self.error(error.__class__.__name__+': '+str(error.with_traceback(tb)), 'Failed to initialize sessions', 501)
				print(error.__class__.__name__+': '+str(error.with_traceback(tb)))


	def validateInput(self) -> bool:
		return True

if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec())
