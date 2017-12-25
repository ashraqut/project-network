# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wireshark.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from scapy.all import *
import time

counter = 0

def custom_action(packet):
    global counter
    counter += 1
    a = [time.ctime(), counter, packet[0][1].src, packet[0][1].dst, packet[0][1].len]
    ui.editTable(a)
    pkt_detail = str(packet.show)
    ui.edittableshow(pkt_detail)

    return a, pkt_detail


def capture():
    sniff(lfilter=None, prn=custom_action, store=0, count=10)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Capture = QtWidgets.QPushButton(self.centralwidget)
        self.Capture.setGeometry(QtCore.QRect(120, 20, 75, 23))
        self.Capture.setObjectName("Capture")
        self.Capture.clicked.connect(capture)
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(500, 20, 75, 23))
        self.Stop.setObjectName("Stop")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 270, 261, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 500, 71, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 90, 611, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 310, 611, 171))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(40, 520, 361, 161))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Capture.setText(_translate("MainWindow", "Capture"))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Packet List"))
        self.label_2.setText(_translate("MainWindow", "TCP/UDP and HTTP protocols details view "))
        self.label_3.setText(_translate("MainWindow", "Hexa view"))

    def editTable (self,a):
        horHeaders = ['Date&Time', 'Packet#', 'Source', 'Destination', 'Length']
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(a[0]))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(str(a[1])))
        self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(a[2]))
        self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(a[3]))
        self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(a[4])))

    def edittableshow(self,pkt_detail):
        headershow=['Packet Detail']
        self.tableWidget_2.setHorizontalHeaderLabels(headershow)
        rowPosition = self.tableWidget_2.rowCount()
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.insertRow(rowPosition)
        self.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(pkt_detail))

    def edittablehex(self,hex_p):
        headerhex=['Hex value']
        self.tableWidget_3.setHorizontalHeaderLabels(headerhex)
        rowPosition = self.tableWidget_3.rowCount()
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.insertRow(rowPosition)
        self.tableWidget_3.setItem(rowPosition, 0, QTableWidgetItem(hex_p))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

