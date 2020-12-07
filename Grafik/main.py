import sys
import matplotlib
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QMainWindow , QApplication,QDialog,QAction
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matematik,anasayfa
from math import sin,cos,tan,pi
import fonkEkleyiciDiyalog
import numpy as np

matplotlib.use('Qt5Agg')
plt.style.use("dark_background")

class fonkEklePencere(QDialog):

    def __init__(self):
        super(fonkEklePencere, self).__init__()
        self.ui = fonkEkleyiciDiyalog.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonTamam.clicked.connect(self.tamam)
        self.donecekFonk = None

    def tamam(self):
        self.bas = self.ui.spinBoxBas.value()
        self.son = self.ui.spinBoxSon.value()
        self.alinanStringFonksiyon = self.ui.lineEditFonksiyon.text()
        try:
            matematik.Fonksiyon(*eval(self.alinanStringFonksiyon)).degerAl(0)
        except:
            self.reject()
        else:
            self.donecekFonk = matematik.Fonksiyon(*eval(self.alinanStringFonksiyon))
            self.accept()

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=6, height=5.70, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class anaSayfa(QMainWindow):

    def __init__(self):
        super(anaSayfa, self).__init__()
        self.fonksiyonlar = []
        self.ui = anasayfa.Ui_MainWindow()
        self.ui.setupUi(self)
        self.n = MplCanvas()
        self.n.setParent(self.ui.widgetCizdirici)
        self.ui.actionFonksiyon_Ekle.triggered.connect(self.fonkEkle)
        self.ui.actionFonksiyon_Sil.triggered.connect(self.fonkSil)
        self.setMaximumSize(self.width(),self.height())

    def fonkSil(self):
        pass # buraya ekle

    def fonkEkle(self):
        pencere = fonkEklePencere()
        pencere.exec_()
        if pencere.donecekFonk:
            self.ui.listWidgetGrafik.addItem(pencere.alinanStringFonksiyon)
            xdegeleri = np.linspace(pencere.bas,pencere.son,10000)
            ydegerleri = [pencere.donecekFonk.degerAl(i) for i in xdegeleri]
            self.n.ax.plot(xdegeleri,ydegerleri)
            self.n.draw()

uyg = QApplication(sys.argv)
p = anaSayfa()
p.show()
uyg.exec_()