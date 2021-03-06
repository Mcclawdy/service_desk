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
        MainWindow.resize(793, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.showAPIBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showAPIBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.showAPIBtn.setText("")
        self.showAPIBtn.setObjectName("showAPIBtn")
        self.gridLayout.addWidget(self.showAPIBtn, 0, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout_3.setHorizontalSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_3.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.logoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logoutBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.logoutBtn.setMaximumSize(QtCore.QSize(250, 50))
        self.logoutBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logoutBtn.setObjectName("logoutBtn")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.logoutBtn)
        self.gridLayout.addLayout(self.formLayout_3, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.employeeNameLable = QtWidgets.QLabel(self.centralwidget)
        self.employeeNameLable.setObjectName("employeeNameLable")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.employeeNameLable)
        self.employeeNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.employeeNameEdit.setObjectName("employeeNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.employeeNameEdit)
        self.requestNumberLable = QtWidgets.QLabel(self.centralwidget)
        self.requestNumberLable.setObjectName("requestNumberLable")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.requestNumberLable)
        self.requestDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.requestDoubleSpinBox.setDecimals(0)
        self.requestDoubleSpinBox.setMinimum(0.0)
        self.requestDoubleSpinBox.setMaximum(999999999999999.0)
        self.requestDoubleSpinBox.setObjectName("requestDoubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.requestDoubleSpinBox)
        self.timesheetsLable = QtWidgets.QLabel(self.centralwidget)
        self.timesheetsLable.setObjectName("timesheetsLable")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.timesheetsLable)
        self.timesheetsDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.timesheetsDoubleSpinBox.setDecimals(0)
        self.timesheetsDoubleSpinBox.setMaximum(999999999999999.0)
        self.timesheetsDoubleSpinBox.setObjectName("timesheetsDoubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.timesheetsDoubleSpinBox)
        self.commentLable = QtWidgets.QLabel(self.centralwidget)
        self.commentLable.setObjectName("commentLable")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.commentLable)
        self.commentEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.commentEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.commentEdit.setObjectName("commentEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.commentEdit)
        self.statusLable = QtWidgets.QLabel(self.centralwidget)
        self.statusLable.setObjectName("statusLable")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.statusLable)
        self.statusEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.statusEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.statusEdit.setReadOnly(True)
        self.statusEdit.setObjectName("statusEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.statusEdit)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn.setMinimumSize(QtCore.QSize(150, 0))
        self.sendBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sendBtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.sendBtn.setObjectName("sendBtn")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sendBtn)
        self.gridLayout.addLayout(self.formLayout_2, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.APIAppendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.APIAppendBtn.setObjectName("APIAppendBtn")
        self.gridLayout_2.addWidget(self.APIAppendBtn, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.apiEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.apiEdit.setMinimumSize(QtCore.QSize(307, 0))
        self.apiEdit.setObjectName("apiEdit")
        self.gridLayout_2.addWidget(self.apiEdit, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 793, 21))
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
        self.actionSecret_Function = QtWidgets.QAction(MainWindow)
        self.actionSecret_Function.setObjectName("actionSecret_Function")
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
        self.employeeNameLable.setText(_translate("MainWindow", "Имя сотрудника"))
        self.requestNumberLable.setText(_translate("MainWindow", "Номер заявки"))
        self.timesheetsLable.setText(_translate("MainWindow", "Трудозатраты"))
        self.commentLable.setText(_translate("MainWindow", "Комментарий"))
        self.statusLable.setText(_translate("MainWindow", "Статус"))
        self.sendBtn.setText(_translate("MainWindow", "Отправить"))
        self.APIAppendBtn.setText(_translate("MainWindow", "OK"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuVirw.setTitle(_translate("MainWindow", "Virw"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionSecret_Function.setText(_translate("MainWindow", "Secret Function"))
