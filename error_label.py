# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_label.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error_label(object):
    def setupUi(self, Error_label):
        Error_label.setObjectName("Error_label")
        Error_label.resize(367, 289)
        self.verticalLayout = QtWidgets.QVBoxLayout(Error_label)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message = QtWidgets.QLabel(Error_label)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        self.message.setFont(font)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)

        self.retranslateUi(Error_label)
        QtCore.QMetaObject.connectSlotsByName(Error_label)

    def retranslateUi(self, Error_label):
        _translate = QtCore.QCoreApplication.translate
        Error_label.setWindowTitle(_translate("Error_label", "Error_label"))
        self.message.setText(_translate("Error_label", "No Info available for this file :("))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error_label = QtWidgets.QWidget()
    ui = Ui_Error_label()
    ui.setupUi(Error_label)
    Error_label.show()
    sys.exit(app.exec_())

