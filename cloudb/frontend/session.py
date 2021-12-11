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

		#self.ui.CenterLine.setVisible(False)
		self.ui.SessionW.hide()

		self.currentSession = {}
		self.sessions = []
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

	def createObject(self, name: str, state: str = "Online", id: str = manager.generateID()) -> None:
		item = QTreeWidgetItem([name, state, id])
		self.setStatus(item, state)
		self.ui.Sessions.addTopLevelItems([item])
		self.sessions.append(item)
	
	def setStatus(self, item: QTreeWidgetItem, state: str) -> QTreeWidgetItem:
		if state.capitalize() not in self.icons['states']: raise IndexError(f'Invalid state "{state}"')
		item.setIcon(0, QIcon(QPixmap(f':/icons/{self.icons["states"][state.capitalize()]}.svg')))
		item.setText(1, state.capitalize())
		return item
	
	def select(self, item: QTreeWidgetItem) -> None:
		sessions = manager.loadSessionsMetaData()
		self.updateStreams()
		self.ui.SessionW.show()

		session = False if item.text(2) not in sessions else sessions[item.text(2)]

		print(session, sessions)

		self.currentSession = {} if not session else session
		if self.currentSession != {}:
			self.forceChanges()
		self.updateSession()
	
	def updateSession(self) -> None:
		self.currentSession['stream'] = self.ui.Stream.currentText()
		self.currentSession['priority'] = self.ui.Priority.value()
		self.currentSession['time'] = self.ui.Time.value()
		self.currentSession['name'] = self.ui.Name.text()
		self.currentSession['path'] = self.ui.Path.text()
		self.currentSession['url'] = self.ui.Url.text()
		self.currentSession['id'] = self.ui.ID.text()

	def forceChanges(self) -> None:
		self.updateStreams()
		self.ui.Stream.setCurrentIndex(self.ui.Stream.findText(manager.displayNames.fancyName(self.currentSession['stream'])))
		self.ui.Priority.setValue(self.currentSession['priority'])
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
	
if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec())
