# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/viewer.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.main_layout.setObjectName("main_layout")
        self.listFrame = QtWidgets.QFrame(self.centralwidget)
        self.listFrame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.listFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listFrame.setObjectName("listFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.listFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = ImageListView(self.listFrame)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.listWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.layoutButtons = QtWidgets.QVBoxLayout()
        self.layoutButtons.setObjectName("layoutButtons")
        self.deleteItem = QtWidgets.QPushButton(self.listFrame)
        self.deleteItem.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.deleteItem.setFont(font)
        self.deleteItem.setObjectName("deleteItem")
        self.layoutButtons.addWidget(self.deleteItem)
        self.clearList = QtWidgets.QPushButton(self.listFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clearList.setFont(font)
        self.clearList.setObjectName("clearList")
        self.layoutButtons.addWidget(self.clearList)
        self.horizontalLayout.addLayout(self.layoutButtons)
        self.main_layout.addWidget(self.listFrame)
        self.label = ImageView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAcceptDrops(True)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.main_layout.addWidget(self.label)
        self.buttons = QtWidgets.QHBoxLayout()
        self.buttons.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.buttons.setObjectName("buttons")
        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.open.setFont(font)
        self.open.setToolTipDuration(-1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.open.setIcon(icon1)
        self.open.setObjectName("open")
        self.buttons.addWidget(self.open)
        self.exif = QtWidgets.QPushButton(self.centralwidget)
        self.exif.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exif.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/investigation.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exif.setIcon(icon2)
        self.exif.setObjectName("exif")
        self.buttons.addWidget(self.exif)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.buttons.addItem(spacerItem)
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.left.setFont(font)
        self.left.setToolTipDuration(-1)
        self.left.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/rotating_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.left.setIcon(icon3)
        self.left.setObjectName("left")
        self.buttons.addWidget(self.left)
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.right.setFont(font)
        self.right.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/rotating_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.right.setIcon(icon4)
        self.right.setObjectName("right")
        self.buttons.addWidget(self.right)
        self.main_layout.addLayout(self.buttons)
        self.verticalLayout.addLayout(self.main_layout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actioncao = QtWidgets.QAction(MainWindow)
        self.actioncao.setObjectName("actioncao")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image and Exif Viewer"))
        self.deleteItem.setText(_translate("MainWindow", "Delete image"))
        self.clearList.setText(_translate("MainWindow", "Clear all"))
        self.label.setText(_translate("MainWindow", "Drag and drop"))
        self.open.setToolTip(_translate("MainWindow", "Open a new image [Ctrl+O]"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.exif.setToolTip(_translate("MainWindow", "Show metadata [Ctrl+E]"))
        self.exif.setText(_translate("MainWindow", "Exif "))
        self.left.setToolTip(_translate("MainWindow", "Rotate 90 degrees counter-clockwise [Ctrl+L]"))
        self.right.setToolTip(_translate("MainWindow", "Rotate 90 degrees clockwise [Ctrl+R]"))
        self.actioncao.setText(_translate("MainWindow", "cao"))

from custom_widgets import ImageListView, ImageView

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

