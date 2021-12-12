# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeHiTNwB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 464)
        self.Main = QWidget(MainWindow)
        self.Main.setObjectName(u"Main")
        self.gridLayout = QGridLayout(self.Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Header = QHBoxLayout()
        self.Header.setObjectName(u"Header")
        self.frame = QFrame(self.Main)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 35))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Add = QPushButton(self.frame)
        self.Add.setObjectName(u"Add")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(QFont.Weight(75))
        self.Add.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/list-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Add.setIcon(icon)
        self.Add.setIconSize(QSize(16, 16))
        self.Add.setCheckable(False)
        self.Add.setAutoExclusive(False)
        self.Add.setAutoDefault(False)
        self.Add.setFlat(True)

        self.horizontalLayout_3.addWidget(self.Add)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.Remove = QPushButton(self.frame)
        self.Remove.setObjectName(u"Remove")
        icon1 = QIcon()
        icon1.addFile(u":/icons/list-remove.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Remove.setIcon(icon1)
        self.Remove.setCheckable(False)
        self.Remove.setAutoDefault(False)
        self.Remove.setFlat(True)

        self.horizontalLayout_3.addWidget(self.Remove)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.Save = QPushButton(self.frame)
        self.Save.setObjectName(u"Save")
        self.Save.setTabletTracking(False)
        self.Save.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/document-save-as.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Save.setIcon(icon2)
        self.Save.setCheckable(False)
        self.Save.setAutoDefault(False)
        self.Save.setFlat(True)

        self.horizontalLayout_3.addWidget(self.Save)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.Open = QPushButton(self.frame)
        self.Open.setObjectName(u"Open")
        icon3 = QIcon()
        icon3.addFile(u":/icons/document-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Open.setIcon(icon3)
        self.Open.setCheckable(False)
        self.Open.setAutoDefault(False)
        self.Open.setFlat(True)

        self.horizontalLayout_3.addWidget(self.Open)

        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)

        self.Help = QPushButton(self.frame)
        self.Help.setObjectName(u"Help")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(QFont.Weight(75))
        self.Help.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/help.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Help.setIcon(icon4)
        self.Help.setFlat(True)

        self.horizontalLayout_3.addWidget(self.Help)


        self.Header.addWidget(self.frame)


        self.gridLayout.addLayout(self.Header, 0, 0, 1, 1)

        self.ErrorZone = QWidget(self.Main)
        self.ErrorZone.setObjectName(u"ErrorZone")
        self.horizontalLayout = QHBoxLayout(self.ErrorZone)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ErrorFrame = QFrame(self.ErrorZone)
        self.ErrorFrame.setObjectName(u"ErrorFrame")
        self.ErrorFrame.setStyleSheet(u"background-color: rgb(170, 0, 0);\n"
"color: rgb(255,  255, 255);\n"
"")
        self.ErrorFrame.setFrameShape(QFrame.StyledPanel)
        self.ErrorFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ErrorFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ErrorMessage = QLabel(self.ErrorFrame)
        self.ErrorMessage.setObjectName(u"ErrorMessage")

        self.gridLayout_3.addWidget(self.ErrorMessage, 0, 0, 1, 1)

        self.CloseError = QPushButton(self.ErrorFrame)
        self.CloseError.setObjectName(u"CloseError")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseError.sizePolicy().hasHeightForWidth())
        self.CloseError.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addFile(u":/icons/red-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseError.setIcon(icon5)
        self.CloseError.setIconSize(QSize(25, 25))
        self.CloseError.setFlat(True)

        self.gridLayout_3.addWidget(self.CloseError, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.ErrorFrame)


        self.gridLayout.addWidget(self.ErrorZone, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Sessions = QTreeWidget(self.Main)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignLeading|Qt.AlignVCenter);
        self.Sessions.setHeaderItem(__qtreewidgetitem)
        self.Sessions.setObjectName(u"Sessions")
        self.Sessions.setAutoScroll(True)
        self.Sessions.setTextElideMode(Qt.ElideLeft)
        self.Sessions.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.Sessions.setIndentation(0)
        self.Sessions.setUniformRowHeights(False)
        self.Sessions.setItemsExpandable(True)
        self.Sessions.setAllColumnsShowFocus(False)
        self.Sessions.setWordWrap(False)
        self.Sessions.setHeaderHidden(False)
        self.Sessions.setExpandsOnDoubleClick(True)
        self.Sessions.header().setVisible(True)
        self.Sessions.header().setDefaultSectionSize(195)
        self.Sessions.header().setHighlightSections(True)

        self.horizontalLayout_2.addWidget(self.Sessions)

        self.CenterLine = QFrame(self.Main)
        self.CenterLine.setObjectName(u"CenterLine")
        self.CenterLine.setFrameShape(QFrame.VLine)
        self.CenterLine.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.CenterLine)

        self.SessionW = QWidget(self.Main)
        self.SessionW.setObjectName(u"SessionW")
        self.Session = QVBoxLayout(self.SessionW)
        self.Session.setObjectName(u"Session")
        self.scrollArea = QScrollArea(self.SessionW)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 334, 472))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lName = QLabel(self.scrollAreaWidgetContents)
        self.lName.setObjectName(u"lName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lName)

        self.lID = QLabel(self.scrollAreaWidgetContents)
        self.lID.setObjectName(u"lID")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lID)

        self.ID = QLineEdit(self.scrollAreaWidgetContents)
        self.ID.setObjectName(u"ID")
        self.ID.setEnabled(False)
        self.ID.setFrame(True)
        self.ID.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ID)

        self.lPath = QLabel(self.scrollAreaWidgetContents)
        self.lPath.setObjectName(u"lPath")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lPath)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Path = QLineEdit(self.scrollAreaWidgetContents)
        self.Path.setObjectName(u"Path")

        self.horizontalLayout_5.addWidget(self.Path)

        self.GetPath = QPushButton(self.scrollAreaWidgetContents)
        self.GetPath.setObjectName(u"GetPath")
        icon6 = QIcon()
        icon6.addFile(u":/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.GetPath.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.GetPath)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.lUrl = QLabel(self.scrollAreaWidgetContents)
        self.lUrl.setObjectName(u"lUrl")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lUrl)

        self.Url = QLineEdit(self.scrollAreaWidgetContents)
        self.Url.setObjectName(u"Url")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Url)

        self.lTime = QLabel(self.scrollAreaWidgetContents)
        self.lTime.setObjectName(u"lTime")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lTime)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Time = QSpinBox(self.scrollAreaWidgetContents)
        self.Time.setObjectName(u"Time")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Time.sizePolicy().hasHeightForWidth())
        self.Time.setSizePolicy(sizePolicy1)
        self.Time.setMaximum(1000000000)
        self.Time.setSingleStep(60)
        self.Time.setValue(1800)

        self.horizontalLayout_4.addWidget(self.Time)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.lPriority = QLabel(self.scrollAreaWidgetContents)
        self.lPriority.setObjectName(u"lPriority")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.lPriority)

        self.Priority = QSpinBox(self.scrollAreaWidgetContents)
        self.Priority.setObjectName(u"Priority")
        sizePolicy1.setHeightForWidth(self.Priority.sizePolicy().hasHeightForWidth())
        self.Priority.setSizePolicy(sizePolicy1)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.Priority)


        self.horizontalLayout_4.addLayout(self.formLayout_6)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.lStream = QLabel(self.scrollAreaWidgetContents)
        self.lStream.setObjectName(u"lStream")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lStream)

        self.Stream = QComboBox(self.scrollAreaWidgetContents)
        self.Stream.setObjectName(u"Stream")
        sizePolicy1.setHeightForWidth(self.Stream.sizePolicy().hasHeightForWidth())
        self.Stream.setSizePolicy(sizePolicy1)
        self.Stream.setMinimumSize(QSize(0, 0))
        self.Stream.setMaxVisibleItems(10)
        self.Stream.setMinimumContentsLength(0)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.Stream)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Name = QLineEdit(self.scrollAreaWidgetContents)
        self.Name.setObjectName(u"Name")

        self.horizontalLayout_6.addWidget(self.Name)

        self.Toggle = QPushButton(self.scrollAreaWidgetContents)
        self.Toggle.setObjectName(u"Toggle")
        icon7 = QIcon()
        icon7.addFile(u":/icons/turnon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Toggle.setIcon(icon7)
        self.Toggle.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.Toggle)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_6)


        self.gridLayout_2.addLayout(self.formLayout, 2, 0, 1, 1)

        self.Apply = QPushButton(self.scrollAreaWidgetContents)
        self.Apply.setObjectName(u"Apply")

        self.gridLayout_2.addWidget(self.Apply, 4, 0, 1, 1)

        self.Output = QTextEdit(self.scrollAreaWidgetContents)
        self.Output.setObjectName(u"Output")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Output.sizePolicy().hasHeightForWidth())
        self.Output.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.Output, 5, 0, 1, 1)

        self.Addons = QPushButton(self.scrollAreaWidgetContents)
        self.Addons.setObjectName(u"Addons")

        self.gridLayout_2.addWidget(self.Addons, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.SessionName = QLabel(self.scrollAreaWidgetContents)
        self.SessionName.setObjectName(u"SessionName")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(QFont.Weight(75))
        self.SessionName.setFont(font2)

        self.horizontalLayout_7.addWidget(self.SessionName)

        self.CloseTab = QPushButton(self.scrollAreaWidgetContents)
        self.CloseTab.setObjectName(u"CloseTab")
        sizePolicy.setHeightForWidth(self.CloseTab.sizePolicy().hasHeightForWidth())
        self.CloseTab.setSizePolicy(sizePolicy)
        self.CloseTab.setIcon(icon5)
        self.CloseTab.setIconSize(QSize(25, 25))
        self.CloseTab.setFlat(True)

        self.horizontalLayout_7.addWidget(self.CloseTab)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.Session.addWidget(self.scrollArea)


        self.horizontalLayout_2.addWidget(self.SessionW)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.HeaderLine = QFrame(self.Main)
        self.HeaderLine.setObjectName(u"HeaderLine")
        self.HeaderLine.setFrameShape(QFrame.HLine)
        self.HeaderLine.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.HeaderLine, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)
        self.CloseTab.pressed.connect(self.SessionW.hide)
        self.CloseTab.pressed.connect(self.CenterLine.hide)
        self.CloseError.pressed.connect(self.ErrorZone.close)

        self.Add.setDefault(False)
        self.Remove.setDefault(False)
        self.Save.setDefault(False)
        self.Open.setDefault(False)
        self.CloseError.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CloudBird", None))
        self.Add.setText("")
#if QT_CONFIG(shortcut)
        self.Add.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.Remove.setText("")
#if QT_CONFIG(shortcut)
        self.Remove.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.Save.setText("")
#if QT_CONFIG(shortcut)
        self.Save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Open.setText("")
#if QT_CONFIG(shortcut)
        self.Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.Help.setText("")
#if QT_CONFIG(shortcut)
        self.Help.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.ErrorMessage.setText(QCoreApplication.translate("MainWindow", u"Error: Error message.", None))
        self.CloseError.setText("")
#if QT_CONFIG(shortcut)
        self.CloseError.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Backspace", None))
#endif // QT_CONFIG(shortcut)
        ___qtreewidgetitem = self.Sessions.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
        self.lName.setText(QCoreApplication.translate("MainWindow", u"Name ", None))
        self.lID.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.ID.setText(QCoreApplication.translate("MainWindow", u"0xdeadbeef", None))
        self.lPath.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.Path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/path/to/folder", None))
        self.GetPath.setText("")
        self.lUrl.setText(QCoreApplication.translate("MainWindow", u"Url", None))
        self.Url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"https://service.tld/mylink", None))
        self.lTime.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.Time.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.lPriority.setText(QCoreApplication.translate("MainWindow", u"Priority", None))
        self.lStream.setText(QCoreApplication.translate("MainWindow", u"Stream", None))
        self.Stream.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Stream", None))
        self.Name.setText("")
        self.Name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.Toggle.setText("")
        self.Apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.Output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The output of this session will be shown here!", None))
        self.Addons.setText(QCoreApplication.translate("MainWindow", u"Manage plugins", None))
        self.SessionName.setText(QCoreApplication.translate("MainWindow", u"Name of the session", None))
        self.CloseTab.setText("")
    # retranslateUi

