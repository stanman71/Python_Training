# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Python/Python Bootcamp/QT/CSV_Import/ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 496)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.studentsTable = QtWidgets.QTableWidget(self.centralWidget)
        self.studentsTable.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.studentsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.studentsTable.setObjectName("studentsTable")
        self.studentsTable.setColumnCount(3)
        self.studentsTable.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.studentsTable.setItem(1, 2, item)
        self.studentsTable.horizontalHeader().setVisible(True)
        self.studentsTable.horizontalHeader().setDefaultSectionSize(110)
        self.studentsTable.horizontalHeader().setStretchLastSection(True)
        self.studentsTable.verticalHeader().setVisible(False)
        self.studentsTable.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_2.addWidget(self.studentsTable, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newEntryButton = QtWidgets.QPushButton(self.centralWidget)
        self.newEntryButton.setObjectName("newEntryButton")
        self.horizontalLayout_2.addWidget(self.newEntryButton)
        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 8, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 371, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuDatei = QtWidgets.QMenu(self.menuBar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuDatei.addAction(self.actionSave)
        self.menuBar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.studentsTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.studentsTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.studentsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Vorname"))
        item = self.studentsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nachname"))
        item = self.studentsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Studienfach"))
        __sortingEnabled = self.studentsTable.isSortingEnabled()
        self.studentsTable.setSortingEnabled(False)
        item = self.studentsTable.item(0, 0)
        item.setText(_translate("MainWindow", "Max"))
        item = self.studentsTable.item(0, 1)
        item.setText(_translate("MainWindow", "Mustermann"))
        item = self.studentsTable.item(0, 2)
        item.setText(_translate("MainWindow", "Informatik"))
        item = self.studentsTable.item(1, 0)
        item.setText(_translate("MainWindow", "Erika"))
        item = self.studentsTable.item(1, 1)
        item.setText(_translate("MainWindow", "Mustermann"))
        item = self.studentsTable.item(1, 2)
        item.setText(_translate("MainWindow", "Mathematik"))
        self.studentsTable.setSortingEnabled(__sortingEnabled)
        self.newEntryButton.setText(_translate("MainWindow", "Neuen Eintrag"))
        self.saveButton.setText(_translate("MainWindow", "Speichern"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionSpeichern.setText(_translate("MainWindow", "Speichern"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Speichern"))

