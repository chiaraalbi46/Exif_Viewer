# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metadata_view_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Metadata(object):
    def setupUi(self, Metadata):
        Metadata.setObjectName("Metadata")
        Metadata.resize(787, 454)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Metadata)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Metadata)
        self.tabWidget.setObjectName("tabWidget")
        self.Gen = QtWidgets.QWidget()
        self.Gen.setObjectName("Gen")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Gen)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget.addTab(self.Gen, "")
        self.Exif = QtWidgets.QWidget()
        self.Exif.setObjectName("Exif")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Exif)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget.addTab(self.Exif, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Metadata)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Metadata)

    def retranslateUi(self, Metadata):
        _translate = QtCore.QCoreApplication.translate
        Metadata.setWindowTitle(_translate("Metadata", "Metadata"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gen), _translate("Metadata", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Exif), _translate("Metadata", "Tab 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Metadata = QtWidgets.QWidget()
    ui = Ui_Metadata()
    ui.setupUi(Metadata)
    Metadata.show()
    sys.exit(app.exec_())

