# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'general_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_General(object):
    def setupUi(self, General):
        General.setObjectName("General")
        General.resize(736, 522)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/viewer.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        General.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(General)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.general_info = QtWidgets.QTreeWidget(General)
        self.general_info.setMinimumSize(QtCore.QSize(600, 500))
        self.general_info.setObjectName("general_info")
        self.general_info.headerItem().setText(0, "1")
        self.general_info.header().setVisible(False)
        self.horizontalLayout.addWidget(self.general_info)
        self.GPS = QtWidgets.QPushButton(General)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GPS.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/map.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.GPS.setIcon(icon1)
        self.GPS.setObjectName("GPS")
        self.horizontalLayout.addWidget(self.GPS)

        self.retranslateUi(General)
        QtCore.QMetaObject.connectSlotsByName(General)

    def retranslateUi(self, General):
        _translate = QtCore.QCoreApplication.translate
        General.setWindowTitle(_translate("General", "General"))
        self.GPS.setText(_translate("General", "Show GPS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    General = QtWidgets.QWidget()
    ui = Ui_General()
    ui.setupUi(General)
    General.show()
    sys.exit(app.exec_())

