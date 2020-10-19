from PyQt5.QtCore import QDir, QFileInfo, QTimer
from PyQt5 import QtGui
import requests
from lxml import etree
import xml.etree.ElementTree as ET

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit,
    QFileDialog, QInputDialog, QMessageBox
)
from .ui.MainWindowUi import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self._showHideApi()
        self._initSignals()


    def _initSignals(self):
        self.sendBtn.clicked.connect(self.sendWorklog)
        self.logoutBtn.clicked.connect(self.close)


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




 # Отправка запросов

    def sendWorklog(self, data=None):
        """Отправляет рабочий журнал и возвращает ответ от сервера"""
        r = requests.post(f'https://sd.korusconsulting.ru/sdpapi/request/{self.getRequestNumber()}/worklogs',
                          params={'OPERATION_NAME': 'ADD_WORKLOG',
                                  'TECHNICIAN_KEY': '25F65F32-4E36-4F2A-B832-A08B8EBDAB6D',
                                  'INPUT_DATA': self.parseWorklogXml('gui/worklog.xml')
                                  },
                        )
        status = self.checkData(r.text)[0]
        message = self.checkData(r.text)[1]
        print(r.text)
        self.statusEdit.insert('')
        self.statusEdit.insert(f'Status - {str(status)} \n Message - {message}')



    def _showHideApi(self):
        """Скрывает и показывает виджет apiEdit"""
        not_resize = self.apiEdit.sizePolicy()
        not_resize.setRetainSizeWhenHidden(True)
        self.apiEdit.setSizePolicy(not_resize)
        self.apiEdit.setVisible(False)
