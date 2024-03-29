# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tetrisboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(6, 2, 391, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Output.sizePolicy().hasHeightForWidth())
        self.Output.setSizePolicy(sizePolicy)
        self.Output.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Output.setFont(font)
        self.Output.setLineWidth(1)
        self.Output.setTextFormat(QtCore.Qt.AutoText)
        self.Output.setScaledContents(False)
        self.Output.setAlignment(QtCore.Qt.AlignCenter)
        self.Output.setWordWrap(False)
        self.Output.setObjectName("Output")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Output.setText(_translate("MainWindow", "░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ▓▓ ▓▓ ▓▓ ▓▓ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n"
"▓▓ ▓▓ ▓▓ ▓▓ ░░ ░░ ░░ ░░ ░░ ░░"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
