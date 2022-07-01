# ╔═╗ ╔═╗ ╔═╗ ╔   ╔═╗
# ╠═╣ ║   ╠═╣ ║   ║
# ╩ ╩ ╚═╝ ╩ ╩ ╚══ ╚═╝ ©
# by Mefiboshet

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 455)
        Form.setMaximumSize(QtCore.QSize(500, 455))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        Form.setFont(font)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setStyleSheet("background-image: url(:/Github/back.jpg);\n"
"background-repeat: no-repeat; \n"
"background-position: center;")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 370, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.494, y1:1, x2:0.528, y2:0.0113182, stop:0 rgba(2, 157, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-image: url(:/0.png);\n"
"border: 1px solid black;")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(120, 110, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.lcdNumber.setFont(font)
        self.lcdNumber.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lcdNumber.setStyleSheet("background-color: rgb(162, 255, 221);\n"
"border: 3px solid black;\n"
"background-image: url(:/0.png);")
        self.lcdNumber.setDigitCount(20)
        self.lcdNumber.setObjectName("lcdNumber")
        self.TextEdit = QtWidgets.QPlainTextEdit(Form)
        self.TextEdit.setGeometry(QtCore.QRect(30, 300, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.TextEdit.setFont(font)
        self.TextEdit.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(255, 255, 255);\n"
"background-image: url(:/0.png);")
        self.TextEdit.setFrameShape(QtWidgets.QFrame.Panel)
        self.TextEdit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TextEdit.setPlainText("")
        self.TextEdit.setObjectName("plainTextEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 240, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("border-radius:5px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 188, 17, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-image: url(:/0.png);")
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-radius:5px;\n"
"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);\n"
"image: url(:/Github/github2.png);\n"
"background-image: url(:/0.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.raise_()
        self.TextEdit.raise_()
        self.textBrowser_2.raise_()
        self.pushButton_2.raise_()
        self.lcdNumber.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.show_line)
        self.pushButton_2.clicked.connect(lambda: webbrowser.open('https://github.com/Fajowskowy'))

    def show_line(self):
        try:
            my_list = []
            for i in self.TextEdit.toPlainText().split(',') or self.TextEdit.toPlainText().split(', ') or self.TextEdit.toPlainText().split(' ,'):
                my_list.append(float(i))
                avg = (sum(my_list)/len(my_list))
                self.lcdNumber.display(str(round(avg, 2)))
        except:
            self.lcdNumber.display("Error")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("ACALC", "ACALC"))
        self.pushButton.setText(_translate("Form", "="))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\">Enter the following </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; color:#000000;\">decimal numbers</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600;\"> to calculate their arithmetic mean:</span></p></body></html>"))

import icons

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

