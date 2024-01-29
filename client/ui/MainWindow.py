# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import socket
import threading
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 841)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(10, 0, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Buttons = QtWidgets.QHBoxLayout()
        self.Buttons.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Buttons.setSpacing(6)
        self.Buttons.setObjectName("Buttons")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Buttons.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Buttons.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Buttons.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.Buttons.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.Buttons)
        self.Content = QtWidgets.QHBoxLayout()
        self.Content.setObjectName("Content")
        self.Files = QtWidgets.QVBoxLayout()
        self.Files.setObjectName("Files")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.Files.addWidget(self.label)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(True)
        self.Files.addWidget(self.treeWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.Files.addLayout(self.horizontalLayout_2)
        self.Content.addLayout(self.Files)
        self.Users = QtWidgets.QVBoxLayout()
        self.Users.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Users.setObjectName("Users")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.Users.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/earth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/web-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        self.listWidget.addItem(item)
        self.Users.addWidget(self.listWidget)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.Users.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.Users.addLayout(self.horizontalLayout)
        self.Users.setStretch(1, 4)
        self.Users.setStretch(3, 1)
        self.Content.addLayout(self.Users)
        self.Content.setStretch(0, 3)
        self.Content.setStretch(1, 2)
        self.verticalLayout.addLayout(self.Content)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 150))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1033, 334))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.widget_6)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.progressBar_6 = QtWidgets.QProgressBar(self.widget_6)
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setObjectName("progressBar_6")
        self.horizontalLayout_8.addWidget(self.progressBar_6)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.progressBar_3 = QtWidgets.QProgressBar(self.widget_3)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_5.addWidget(self.progressBar_3)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.progressBar_4 = QtWidgets.QProgressBar(self.widget_4)
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.horizontalLayout_6.addWidget(self.progressBar_4)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.verticalLayout_5.addWidget(self.widget, 0, QtCore.Qt.AlignTop)
        self.widget_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.progressBar_5 = QtWidgets.QProgressBar(self.widget_5)
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.horizontalLayout_7.addWidget(self.progressBar_5)
        self.verticalLayout_5.addWidget(self.widget_5)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.progressBar_2 = QtWidgets.QProgressBar(self.widget_2)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_4.addWidget(self.progressBar_2)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_7.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.widget_7)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.progressBar_7 = QtWidgets.QProgressBar(self.widget_7)
        self.progressBar_7.setProperty("value", 24)
        self.progressBar_7.setObjectName("progressBar_7")
        self.horizontalLayout_9.addWidget(self.progressBar_7)
        self.verticalLayout_5.addWidget(self.widget_7, 0, QtCore.Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.main()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Drizzle"))
        self.label_3.setText(_translate("MainWindow", "Drizzle / Sender"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Files"))
        self.pushButton.setText(_translate("MainWindow", "Settings"))
        self.label.setText(_translate("MainWindow", "Browse Files"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "RichardRoe12"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "photoshop.iso"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Movies/"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "The Matrix.mov"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Forrest Gump.mp4"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Django.mp4"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "msoffice.zip"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Games/"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "NFS/"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "nfsmostwanted.zip"))
        self.treeWidget.topLevelItem(3).child(2).setText(0, _translate("MainWindow", "TLauncher.zip"))
        self.treeWidget.topLevelItem(3).child(3).setText(0, _translate("MainWindow", "GTA-V.iso"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "Study Material/"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "Selected File/Folder: msoffice.zip"))
        self.pushButton_5.setText(_translate("MainWindow", "Info"))
        self.pushButton_4.setText(_translate("MainWindow", "Download"))
        self.label_2.setText(_translate("MainWindow", "Users"))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "RichardRoe12"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "ronaldw"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "harrypotter (last active: 11:45 am)"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "anonymous_lol"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600; color:#e5a50a;\">12:03</span><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600;\"> RichardRoe12: </span><span style=\" font-family:\'Noto Sans\'; font-size:10pt;\">Hello</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600; color:#1a5fb4;\">12:03</span><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600;\"> You: </span><span style=\" font-family:\'Noto Sans\'; font-size:10pt;\">Hii</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600; color:#e5a50a;\">12:03</span><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600;\"> RichardRoe12: </span><span style=\" font-family:\'Noto Sans\'; font-size:10pt;\">Got any games?</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600; color:#1a5fb4;\">12:03</span><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600;\"> You: </span><span style=\" font-family:\'Noto Sans\'; font-size:10pt;\">Probably</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600; color:#1a5fb4;\">12:03</span><span style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:600;\"> You: </span><span style=\" font-family:\'Noto Sans\'; font-size:10pt;\">Wait ill upload something...</span></p></body></html>"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "Enter message"))
        self.pushButton_3.setText(_translate("MainWindow", "Send Message"))
        self.pushButton_6.setText(_translate("MainWindow", "Send File"))
        self.label_12.setText(_translate("MainWindow", "Downloading:"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))

    
    def list_files_and_empty_folders(self, folder_path):
        file_list = []

        for root, dirs, files in os.walk(folder_path):
            # Add files to list
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append(str(file_path))
            
            # Check if folder is empty
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                # if not os.listdir(folder_path):
                file_list.append(str(folder_path))

        Files = ''
        for file_path in file_list:
            Files += file_path + '\n'
        
        return Files

    def thread(self, chat_socket): 
        t1 = threading.Thread(target=self.receive_chat, args=(chat_socket,))
        t1.start()

    def receive_chat(self,client_socket):
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                self.textEdit.append("Sender: " + message)
        except Exception as e:
            print(f"Error receiving chat message: {e}")

    # def receive_chat(self, client_socket):
    #     try:
    #         while True:
    #             response = client_socket.recv(1024).decode('utf-8')
    #             print(f"Received message: {response}")
    #             if not response:
    #                 break

    #             response = response.split('@')
    #             if response[0] == 'message':
    #                 message = response[1]
    #                 print(f"Received message: {message}")
    #             elif response[0] == 'request':
    #                 request = response[1]
    #                 if request == 'list_files':
    #                     print("Received request for list of files")
    #                     files = list_files_and_empty_folders('./public')
    #                     client_socket.send(files.encode('utf-8'))
                    
    #             elif response[0] == 'download':
    #                 file_path = response[1]
    #                 send_file(file_path)
                    
    #     except Exception as e:
    #         print(f"Error receiving chat message: {e}")

    def send_chat(self, client_socket):
        try:
            message = self.plainTextEdit.toPlainText()
            client_socket.send(message.encode('utf-8'))
            self.textEdit.append("You: " + message)
            self.plainTextEdit.clear()
        except Exception as e:
            print(f"Error sending chat message: {e}")

    def receive_file(self, client_socket, download_path):
        try:
            file_name = client_socket.recv(1024).decode('utf-8')
            file_path = os.path.join(download_path, file_name)
            with open(file_path, 'wb') as file:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    file.write(data)
            print(f"File received and saved at: {file_path}")
        except Exception as e:
            print(f"Error receiving file: {e}")
        

    def send_file(self, file_path):
        global host
        port_file = 5556

        file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        file_socket.bind((host, port_file))
        file_socket.listen()

        print(f"File server listening on {host}:{port_file}")

        file_client, file_addr = file_socket.accept()
        print(f"File connection established with {file_addr}")
        try:
            file_name = os.path.basename(file_path)
            file_client.send(file_name.encode('utf-8'))
            print("Sending file...")
            with open(file_path, 'rb') as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    file_client.send(data)
            print("File sent")
        except Exception as e:
            print(f"Error sending file: {e}")
        

    def main(self):
        global host
        host = '192.168.68.241'
        port_chat = 5555
        # port_file = 5556

        chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        chat_socket.bind((host, port_chat))
        chat_socket.listen()

        print(f"Chat server listening on {host}:{port_chat}")

        # file_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # file_socket.bind((host, port_file))
        # file_socket.listen()

        # print(f"File server listening on {host}:{port_file}")

        chat_client, chat_addr = chat_socket.accept()
        # file_client, file_addr = file_socket.accept()

        print(f"Chat connection established with {chat_addr}")
        # print(f"File connection established with {file_addr}")

        # chat_receive_thread = threading.Thread(target=self.receive_chat, args=(chat_client,))
        # chat_send_thread = threading.Thread(target=self.send_chat, args=(chat_client,))
        # file_receive_thread = threading.Thread(target=receive_file, args=(file_client, 'downloads'))
        # file_send_thread = threading.Thread(target=send_file, args=(file_client, './public/hello.txt'))

        # chat_receive_thread.start()
        # chat_send_thread.start()
        # file_receive_thread.start()
        # file_send_thread.start()

        # Wait for threads to finish
        # chat_receive_thread.join()
        # chat_send_thread.join()
        # file_receive_thread.join()
        # file_send_thread.join()

        self.textEdit.clear()
        
        self.pushButton_3.clicked.connect(lambda: self.send_chat(chat_client))
        self.pushButton_6.clicked.connect(lambda: self.thread(chat_client))
        # self.pushButton_6.clicked.connect(self.send_file('./public/Resume.pdf'))

        # while True:
        #     self.receive_chat(chat_socket)

        # Close sockets
        # chat_socket.close()
        # file_socket.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())