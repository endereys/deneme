from math import sin,cos,tan,pi
import re
import numpy

class Fonksiyon:

    def __init__(self,*args):#gelen veri [şart,fonksiyon şeklinde gelecek] ornek: args = [["x","x^2"]]
        self.gelenVeriler = args
        self.parcaliSozluk = {}
        self.sartlar = [i[0] for i in args]
        self.fonksiyonGosterimleri = [i[1] for i in args]
        for a in args:
            self.parcaliSozluk[a[0]] = a[1]

    def degerAl(self,x):
        for sart in self.sartlar:
            if not x and sart == "x":
                return eval(self.parcaliSozluk[sart].replace("^","**").replace("x","("+str(x)+")"))
            if eval(sart.replace("x",str(x))):
                return eval(self.parcaliSozluk[sart].replace("^","**").replace("x","("+str(x)+")"))
        return None