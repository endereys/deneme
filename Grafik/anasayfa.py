# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 594)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidgetGrafik = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetGrafik.setGeometry(QtCore.QRect(10, 10, 311, 531))
        self.listWidgetGrafik.setObjectName("listWidgetGrafik")
        self.widgetCizdirici = QtWidgets.QWidget(self.centralwidget)
        self.widgetCizdirici.setGeometry(QtCore.QRect(330, 10, 571, 531))
        self.widgetCizdirici.setObjectName("widgetCizdirici")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 24))
        self.menubar.setObjectName("menubar")
        self.menuAra_lar = QtWidgets.QMenu(self.menubar)
        self.menuAra_lar.setObjectName("menuAra_lar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFonksiyon_Ekle = QtWidgets.QAction(MainWindow)
        self.actionFonksiyon_Ekle.setObjectName("actionFonksiyon_Ekle")
        self.actionFonksiyon_Sil = QtWidgets.QAction(MainWindow)
        self.actionFonksiyon_Sil.setObjectName("actionFonksiyon_Sil")
        self.menuAra_lar.addAction(self.actionFonksiyon_Ekle)
        self.menuAra_lar.addAction(self.actionFonksiyon_Sil)
        self.menubar.addAction(self.menuAra_lar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuAra_lar.setTitle(_translate("MainWindow", "Araçlar"))
        self.actionFonksiyon_Ekle.setText(_translate("MainWindow", "Fonksiyon Ekle"))
        self.actionFonksiyon_Sil.setText(_translate("MainWindow", "Fonksiyon Sil"))

