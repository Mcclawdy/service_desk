# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.statusBar = QtWidgets.QLineEdit(self.centralwidget)
        self.statusBar.setMaximumSize(QtCore.QSize(88, 16777215))
        self.statusBar.setObjectName("statusBar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.statusBar)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setHorizontalSpacing(100)
        self.formLayout_3.setObjectName("formLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_3.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.logoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logoutBtn.setObjectName("logoutBtn")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.logoutBtn)
        self.gridLayout_2.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.commentEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.commentEdit.setObjectName("commentEdit")
        self.gridLayout.addWidget(self.commentEdit, 3, 2, 1, 1)
        self.timesheetsLable = QtWidgets.QLabel(self.centralwidget)
        self.timesheetsLable.setObjectName("timesheetsLable")
        self.gridLayout.addWidget(self.timesheetsLable, 2, 0, 1, 1)
        self.employeeNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.employeeNameEdit.setObjectName("employeeNameEdit")
        self.gridLayout.addWidget(self.employeeNameEdit, 0, 2, 1, 1)
        self.employeeNameLable = QtWidgets.QLabel(self.centralwidget)
        self.employeeNameLable.setObjectName("employeeNameLable")
        self.gridLayout.addWidget(self.employeeNameLable, 0, 0, 1, 1)
        self.timesheetsDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.timesheetsDoubleSpinBox.setDecimals(0)
        self.timesheetsDoubleSpinBox.setMaximum(999999999999999.0)
        self.timesheetsDoubleSpinBox.setObjectName("timesheetsDoubleSpinBox")
        self.gridLayout.addWidget(self.timesheetsDoubleSpinBox, 2, 2, 1, 1)
        self.requestDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.requestDoubleSpinBox.setDecimals(0)
        self.requestDoubleSpinBox.setMinimum(0.0)
        self.requestDoubleSpinBox.setMaximum(999999999999999.0)
        self.requestDoubleSpinBox.setObjectName("requestDoubleSpinBox")
        self.gridLayout.addWidget(self.requestDoubleSpinBox, 1, 2, 1, 1)
        self.requestNumberLable = QtWidgets.QLabel(self.centralwidget)
        self.requestNumberLable.setObjectName("requestNumberLable")
        self.gridLayout.addWidget(self.requestNumberLable, 1, 0, 1, 1)
        self.commentLable = QtWidgets.QLabel(self.centralwidget)
        self.commentLable.setObjectName("commentLable")
        self.gridLayout.addWidget(self.commentLable, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setHorizontalSpacing(100)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn.setObjectName("sendBtn")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sendBtn)
        self.gridLayout_2.addLayout(self.formLayout_2, 2, 1, 1, 1)
        self.apiEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.apiEdit.setObjectName("apiEdit")
        self.gridLayout_2.addWidget(self.apiEdit, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuVirw = QtWidgets.QMenu(self.menuBar)
        self.menuVirw.setObjectName("menuVirw")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuVirw.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Service Desk Worklog"))
        self.logoutBtn.setText(_translate("MainWindow", "Выйти"))
        self.timesheetsLable.setText(_translate("MainWindow", "Трудозатраты"))
        self.employeeNameLable.setText(_translate("MainWindow", "Имя сотрудника"))
        self.requestNumberLable.setText(_translate("MainWindow", "Номер заявки"))
        self.commentLable.setText(_translate("MainWindow", "Комментарий"))
        self.sendBtn.setText(_translate("MainWindow", "Отправить"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuVirw.setTitle(_translate("MainWindow", "Virw"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
