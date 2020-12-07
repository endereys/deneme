# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fonkEkleyiciDiyalog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(328, 149)
        self.lineEditFonksiyon = QtWidgets.QLineEdit(Dialog)
        self.lineEditFonksiyon.setGeometry(QtCore.QRect(10, 10, 311, 41))
        self.lineEditFonksiyon.setObjectName("lineEditFonksiyon")
        self.pushButtonTamam = QtWidgets.QPushButton(Dialog)
        self.pushButtonTamam.setGeometry(QtCore.QRect(210, 110, 111, 31))
        self.pushButtonTamam.setObjectName("pushButtonTamam")
        self.spinBoxBas = QtWidgets.QSpinBox(Dialog)
        self.spinBoxBas.setGeometry(QtCore.QRect(10, 60, 151, 24))
        self.spinBoxBas.setMinimum(-999999999)
        self.spinBoxBas.setMaximum(999999999)
        self.spinBoxBas.setObjectName("spinBoxBas")
        self.spinBoxSon = QtWidgets.QSpinBox(Dialog)
        self.spinBoxSon.setGeometry(QtCore.QRect(170, 60, 151, 24))
        self.spinBoxSon.setMinimum(-999999999)
        self.spinBoxSon.setMaximum(999999999)
        self.spinBoxSon.setObjectName("spinBoxSon")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonTamam.setText(_translate("Dialog", "Tamam"))

