from PyQt5.QtCore import QDir, QFileInfo
from PyQt5 import QtGui
import requests
from lxml import etree
import xml.etree.ElementTree as ET
import urllib
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit,
    QFileDialog, QInputDialog, QMessageBox
)
from .ui.MainWindowUi import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self._initSignals()


    def _initSignals(self):
        self.sendBtn.clicked.connect(self.sendWorklog)


    def printError(self, data):
        """Выдает сообщение об ошибке, если какие то данные не верны"""
        ret = QMessageBox.warning(
            self, f'Ошибка', f'Параметр {data} неверен'
        )


    def getEmployeeFullame(self):
        """Задает полное имя сотрудника"""
        if self.employeeNameEdit:
            fullname = self.employeeNameEdit.text()
            return fullname
        else:
            return f'Неверные данные в поле {self.employeeNameLable}'


    def getRequestNumber(self):
        """Задает номер заявки"""
        if self.requestDoubleSpinBox:
            request_number = int(self.requestDoubleSpinBox.value())
            return request_number
        else:
            print("request error")


    def getTimesheets(self):
        """Задает потраченное время (в минутах)"""
        if self.timesheetsDoubleSpinBox:
            timesheets = int(self.timesheetsDoubleSpinBox.value())
            return timesheets
        else:
            print("request error")

    def getComment(self):
        """Задает комментарий"""
        if self.commentEdit:
            comment = self.commentEdit.toPlainText()
            return comment
        else:
            print("request error")

    def parseXML(self):
        xml_str = f"""
        <Operation>
            <Details>
                <Worklogs>
                    <Worklog>
                        <parameter>
                            <name>description</name>
                            <value>{self.getComment()}</value>
                        </parameter>
                        <parameter>
                            <name>technician</name>
                            <value>{self.getEmployeeFullame()}</value>
                        </parameter>
                        <parameter>
                            <name>cost</name>
                            <value>0</value>
                        </parameter>
                        <parameter>
                            <name>workMinutes</name>
                            <value>{self.getTimesheets()}</value>
                        </parameter>
                        <parameter>
                            <name>workHours</name>
                            <value>0</value>
                        </parameter>
                    </Worklog>
                </Worklogs>
            </Details>
        </Operation>
"""

        parser = etree.XMLParser(remove_blank_text=True)
        elem = etree.XML(xml_str, parser = parser)
        print(type(etree.tostring(elem).decode("utf-8")))
        return etree.tostring(elem)


    def sendWorklog(self, data=None):
        """Отправляет рабочий журнал, если все данные верны"""
        print(self.parseXML())
        headers = {'Content-Type': 'application/xml'}
        r = requests.post(f'https://sd.korusconsulting.ru/sdpapi/request/{self.getRequestNumber()}/worklogs',
                          params={'OPERATION_NAME': 'ADD_WORKLOG', 'TECHNICIAN_KEY': '25F65F32-4E36-4F2A-B832-A08B8EBDAB6D', 'INPUT_DATA': self.parseXML()},
)
        print(r.url)
        print(r.text)


    def checkData(self, request_number, employee_fullname):
        """Прооверяет статус заявки и наличие сотрудника"""
        pass

    def closeApp(self):
        """Выходит из приложения"""
        pass



