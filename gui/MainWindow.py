import os
import requests
import xml.etree.ElementTree as ET

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit,
    QFileDialog, QInputDialog, QMessageBox
)
from .ui.MainWindowUi import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        self.clickedCount = 0
        self._apiKey = ''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self._showHideApi()
        self._initSignals()
        self.setWindowIcon(QtGui.QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'ico.png'))



    def _initSignals(self):
        self.sendBtn.clicked.connect(self.sendWorklog)
        self.logoutBtn.clicked.connect(self.close)
        self.showAPIBtn.clicked.connect(self.onClick)
        self.APIAppendBtn.clicked.connect(self.setApiKey)


    def getApiKey(self):
        if self._apiKey:
            apiKey = self._apiKey
            return apiKey

    def getEmployeeFullame(self):
        """Задает полное имя сотрудника"""
        if self.employeeNameEdit:
            fullname = self.employeeNameEdit.text()
            return fullname


    def getRequestNumber(self):
        """Задает номер заявки"""
        if self.requestDoubleSpinBox:
            request_number = int(self.requestDoubleSpinBox.value())
            return request_number


    def getTimesheets(self):
        """Задает потраченное время (в минутах)"""
        if self.timesheetsDoubleSpinBox:
            timesheets = int(self.timesheetsDoubleSpinBox.value())
            return timesheets


    def getComment(self):
        """Задает комментарий"""
        if self.commentEdit:
            comment = self.commentEdit.toPlainText()
            return comment

# работа с XML


    def parseWorklogXml(self, file):
        """Возвращает словарь данных для записи в xml"""
        data = [self.getComment(), self.getEmployeeFullame(), 0, self.getTimesheets(), 0]
        with open(file, 'r') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            xmlstr = ET.tostring(root, encoding='utf8', method='xml')
            xml_file = ET.fromstring(xmlstr)
            for index, value in enumerate(xml_file.iter('value')):
                value.text = str(data[index])
            return ET.tostring(xml_file, encoding='unicode', method='xml')




    def checkData(self, request_answer):
        """Прооверяет статус выполнения запроса"""
        xml_sting = ET.fromstring(request_answer)
        status = [status.text for status in  xml_sting.iter('status')]
        message = [message.text for message in xml_sting.iter('message')]
        if status[0] != 'Failed':
            self.employeeNameEdit.clear()
            self.requestDoubleSpinBox.clear()
            self.timesheetsDoubleSpinBox.clear()
            self.commentEdit.clear()
        return [status[0], message[0]]


 # Запись API ключа

    def setApiKey(self):
        if self.apiEdit.text():
            self._apiKey = self.apiEdit.text().strip()
            self.APIAppendBtn.setVisible(False)
            self.apiEdit.setVisible(False)
        else:
            self.statusEdit.insert('')
            self.statusEdit.insert('API ключ не введен, или введен неверно')


    def onClick(self):
        self.clickedCount += 1
        if self.clickedCount == 5:
            self.apiEdit.setVisible(1)
            self.APIAppendBtn.setVisible(1)
            self.clickedCount = 0


    def _showHideApi(self):
        """Скрывает и показывает виджет apiEdit"""
        self.showAPIBtn.setFlat(True)
        notResizeEdit = self.apiEdit.sizePolicy()
        notResizeEdit.setRetainSizeWhenHidden(True)
        notResizeBtn = self.APIAppendBtn.sizePolicy()
        notResizeBtn.setRetainSizeWhenHidden(True)
        self.apiEdit.setSizePolicy(notResizeEdit)
        self.APIAppendBtn.setSizePolicy(notResizeEdit)
        self.apiEdit.setVisible(0)
        self.APIAppendBtn.setVisible(0)





 # Отправка запросов

    def sendWorklog(self, data=None):
        """Отправляет рабочий журнал и возвращает ответ от сервера"""
        r = requests.post(f'https://sd.korusconsulting.ru/sdpapi/request/{self.getRequestNumber()}/worklogs',
                          params={'OPERATION_NAME': 'ADD_WORKLOG',
                                  'TECHNICIAN_KEY': f'{self.getApiKey()}',
                                  'INPUT_DATA': self.parseWorklogXml('gui/worklog.xml')
                                  },
                        )
        status = self.checkData(r.text)[0]
        message = self.checkData(r.text)[1]
        print(r.text)
        self.statusEdit.insert('')
        self.statusEdit.insert(f'Status - {str(status)}')
        self.statusEdit.insert(f'Message - {message}')