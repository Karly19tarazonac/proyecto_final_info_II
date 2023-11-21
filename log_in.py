# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from imagenes import imagenes


class Ui_inicio_de_sesion(object):
    def setupUi(self, inicio_de_sesion):
        inicio_de_sesion.setObjectName("inicio_de_sesion")
        inicio_de_sesion.resize(402, 488)
        inicio_de_sesion.setStyleSheet("border-radius:20px;\n"
"border-color: rgb(85, 170, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(inicio_de_sesion)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 391, 471))
        self.widget.setStyleSheet("alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:20px;")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 351, 431))
        self.label_2.setStyleSheet("background-color: rgb(0,0,0,100);\n"
"border-radius:15px;\n"
"border-image: url(:/new_imagen/descarga.jpg);\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(100, 50, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 371, 451))
        self.label_4.setStyleSheet("border-image: url(:/imagenes/cropped-Neurologia.jpg);\n"
"border-radius:20px;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.campo_password = QtWidgets.QLineEdit(self.widget)
        self.campo_password.setGeometry(QtCore.QRect(20, 370, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.campo_password.setFont(font)
        self.campo_password.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(105,118,132,255);\n"
"color:rgb(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.campo_password.setText("")
        self.campo_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.campo_password.setObjectName("campo_password")
        self.campo_usuario = QtWidgets.QLineEdit(self.widget)
        self.campo_usuario.setGeometry(QtCore.QRect(20, 330, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.campo_usuario.setFont(font)
        self.campo_usuario.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgb(105,118,132,255);\n"
"color:rgb(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.campo_usuario.setText("")
        self.campo_usuario.setObjectName("campo_usuario")
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(150, 410, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet("QPushBottom#pushBottom{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(20, 47, 78, 219), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"    color:rgb(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushBottom#pushBottom:hover{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QPushBottom#pushBottom:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:(105,118,132,200);\n"
"}\n"
"\n"
"")
        self.login.setObjectName("login")
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.login.raise_()
        self.campo_usuario.raise_()
        self.campo_password.raise_()
        inicio_de_sesion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(inicio_de_sesion)
        self.statusbar.setObjectName("statusbar")
        inicio_de_sesion.setStatusBar(self.statusbar)

        self.retranslateUi(inicio_de_sesion)
        QtCore.QMetaObject.connectSlotsByName(inicio_de_sesion)

    def retranslateUi(self, inicio_de_sesion):
        _translate = QtCore.QCoreApplication.translate
        inicio_de_sesion.setWindowTitle(_translate("inicio_de_sesion", "MainWindow"))
        self.label_3.setText(_translate("inicio_de_sesion", "LOG IN :"))
        self.campo_password.setPlaceholderText(_translate("inicio_de_sesion", "Password: "))
        self.campo_usuario.setPlaceholderText(_translate("inicio_de_sesion", "User Name: "))
        self.login.setText(_translate("inicio_de_sesion", "L O G  I N"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inicio_de_sesion = QtWidgets.QMainWindow()
    ui = Ui_inicio_de_sesion()
    ui.setupUi(inicio_de_sesion)
    inicio_de_sesion.show()
    sys.exit(app.exec_())
