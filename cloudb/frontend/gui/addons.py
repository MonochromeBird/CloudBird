# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SessionAddons.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(606, 280)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AddonsRepo = QTreeWidget(Dialog)
        self.AddonsRepo.setObjectName(u"AddonsRepo")
        self.AddonsRepo.setAlternatingRowColors(True)
        self.AddonsRepo.setIndentation(0)

        self.horizontalLayout.addWidget(self.AddonsRepo)

        self.AddonsUsed = QTreeWidget(Dialog)
        self.AddonsUsed.setObjectName(u"AddonsUsed")
        self.AddonsUsed.setAlternatingRowColors(True)
        self.AddonsUsed.setIndentation(0)

        self.horizontalLayout.addWidget(self.AddonsUsed)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Remove = QPushButton(Dialog)
        self.Remove.setObjectName(u"Remove")
        icon = QIcon()
        iconThemeName = u"arrow-left"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.Remove.setIcon(icon)

        self.verticalLayout.addWidget(self.Remove)

        self.Add = QPushButton(Dialog)
        self.Add.setObjectName(u"Add")
        icon1 = QIcon()
        iconThemeName = u"arrow-right"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.Add.setIcon(icon1)

        self.verticalLayout.addWidget(self.Add)

        self.AddAll = QPushButton(Dialog)
        self.AddAll.setObjectName(u"AddAll")

        self.verticalLayout.addWidget(self.AddAll)

        self.RemoveAll = QPushButton(Dialog)
        self.RemoveAll.setObjectName(u"RemoveAll")

        self.verticalLayout.addWidget(self.RemoveAll)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.exit = QDialogButtonBox(Dialog)
        self.exit.setObjectName(u"exit")
        self.exit.setOrientation(Qt.Horizontal)
        self.exit.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.exit, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.exit.accepted.connect(Dialog.accept)
        self.exit.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Addons", None))
        ___qtreewidgetitem = self.AddonsRepo.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"Unused addons", None));
        ___qtreewidgetitem1 = self.AddonsUsed.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Dialog", u"Addons that are being used", None));
        self.Remove.setText("")
        self.Add.setText("")
        self.AddAll.setText(QCoreApplication.translate("Dialog", u"Add All", None))
        self.RemoveAll.setText(QCoreApplication.translate("Dialog", u"Remove All", None))
    # retranslateUi

