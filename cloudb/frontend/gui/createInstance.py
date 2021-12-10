# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SessionCreator.ui'
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
        Dialog.resize(505, 310)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(505, 310))
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Title = QLabel(Dialog)
        self.Title.setObjectName(u"Title")
        self.Title.setMaximumSize(QSize(16777215, 48))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.Title)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lName = QLabel(Dialog)
        self.lName.setObjectName(u"lName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lName)

        self.Name = QLineEdit(Dialog)
        self.Name.setObjectName(u"Name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Name)

        self.lStream = QLabel(Dialog)
        self.lStream.setObjectName(u"lStream")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lStream)

        self.Stream = QComboBox(Dialog)
        self.Stream.setObjectName(u"Stream")
        self.Stream.setMinimumSize(QSize(0, 0))
        self.Stream.setMaxVisibleItems(10)
        self.Stream.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.Stream.setMinimumContentsLength(50)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Stream)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.Path = QLineEdit(Dialog)
        self.Path.setObjectName(u"Path")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.Path)

        self.lPath = QLabel(Dialog)
        self.lPath.setObjectName(u"lPath")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lPath)

        self.Url = QLineEdit(Dialog)
        self.Url.setObjectName(u"Url")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.Url)

        self.lUrl = QLabel(Dialog)
        self.lUrl.setObjectName(u"lUrl")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lUrl)


        self.verticalLayout_3.addLayout(self.formLayout_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_3)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lTime = QLabel(Dialog)
        self.lTime.setObjectName(u"lTime")

        self.horizontalLayout_4.addWidget(self.lTime)

        self.Time = QSpinBox(Dialog)
        self.Time.setObjectName(u"Time")
        self.Time.setMaximum(1000000000)
        self.Time.setSingleStep(60)
        self.Time.setValue(1800)

        self.horizontalLayout_4.addWidget(self.Time)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lPriority = QLabel(Dialog)
        self.lPriority.setObjectName(u"lPriority")

        self.horizontalLayout_6.addWidget(self.lPriority)

        self.Priority = QSpinBox(Dialog)
        self.Priority.setObjectName(u"Priority")

        self.horizontalLayout_6.addWidget(self.Priority)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ChoosePath = QPushButton(Dialog)
        self.ChoosePath.setObjectName(u"ChoosePath")
        self.ChoosePath.setAcceptDrops(True)

        self.horizontalLayout_5.addWidget(self.ChoosePath)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.exit = QDialogButtonBox(Dialog)
        self.exit.setObjectName(u"exit")
        self.exit.setOrientation(Qt.Horizontal)
        self.exit.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.exit)


        self.retranslateUi(Dialog)
        self.exit.accepted.connect(Dialog.accept)
        self.exit.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create an instance", None))
        self.Title.setText(QCoreApplication.translate("Dialog", u"Create an instance", None))
        self.lName.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.Name.setPlaceholderText(QCoreApplication.translate("Dialog", u"Cool name", None))
        self.lStream.setText(QCoreApplication.translate("Dialog", u"Stream", None))
        self.Stream.setCurrentText("")
        self.Stream.setPlaceholderText(QCoreApplication.translate("Dialog", u"Stream", None))
        self.Path.setPlaceholderText(QCoreApplication.translate("Dialog", u"/path/to/your/folder", None))
        self.lPath.setText(QCoreApplication.translate("Dialog", u"Path", None))
        self.Url.setPlaceholderText(QCoreApplication.translate("Dialog", u"https://service.tld/mylink", None))
        self.lUrl.setText(QCoreApplication.translate("Dialog", u"Url", None))
        self.lTime.setText(QCoreApplication.translate("Dialog", u"Time", None))
        self.Time.setSuffix(QCoreApplication.translate("Dialog", u"s", None))
        self.Time.setPrefix("")
        self.lPriority.setText(QCoreApplication.translate("Dialog", u"Priority", None))
        self.ChoosePath.setText(QCoreApplication.translate("Dialog", u"Choose folder", None))
    # retranslateUi

