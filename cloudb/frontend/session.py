#!/usr/bin/env python3
# -*- enconding:utf-8 -*-

# [ 3th party Libraries ]
from random import randint
from hashlib import md5
from os import remove
import sys

# [ The uic (graphical user interface) ]
from .gui.home import *

# [ Backend ]
from ..backend import manager


# [ Qt class ]
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#self.ui.CenterLine.setVisible(False)
		self.ui.SessionW.hide()

		self.sessions = []
		self.icons = {
			'states':{
				'Online':  'network',
				'Offline': 'network-offline',
				'Error':   'network-error',
				'Waiting': 'wait'}
		}

		self.createObject("Playground")
		self.ui.Sessions.itemActivated.connect(self.select)

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
		self.ui.SessionW.show()
	
	
if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec())
