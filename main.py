""" Main function """

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence
import sys
from main_window import Ui_MainWindow
from model import Model
from custom_widgets import CustomTab


class MainWindow(QMainWindow):
    """ This is the Main window """

    def __init__(self, model):
        super().__init__()

        # print("super: ", super().parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # assegno a questa main window la ui creata

        self.model = model

        # list viewer
        self.ui.listFrame.setVisible(False)
        self.list_viewer = self.ui.listFrame  # contains list widget e the button which act on it
        self.list_widget = self.ui.listWidget  # list widget
        self.ui.deleteItem.setEnabled(False)

        # viewer
        self.viewer = self.ui.label
        self.viewer.parent = self.ui  # set the correct parent (default is centralwidget)

        self.viewer.set_model(self.model)
        self.viewer.set_viewer_list(self.list_widget)

        self.list_widget.parent = self.ui
        self.list_widget.set_action_list_buttons()  # connect delete button to delete action

        # model
        self.list_widget.set_model(self.model)
        self.list_widget.set_viewer(self.viewer)

        # widget metadata
        self.metadata_tab = None  # QWidget()

        # connect slot to buttons
        self.ui.open.clicked.connect(self.open_image)
        self.ui.left.clicked.connect(self.left_rotate)
        self.ui.right.clicked.connect(self.right_rotate)
        self.ui.exif.clicked.connect(self.open_info)

        # hotkeys
        self.right_rot_shortcut = QShortcut(QKeySequence('Ctrl+R'), self)
        self.right_rot_shortcut.activated.connect(self.right_rotate)
        self.left_rot_shortcut = QShortcut(QKeySequence('Ctrl+L'), self)
        self.left_rot_shortcut.activated.connect(self.left_rotate)
        self.exif_shortcut = QShortcut(QKeySequence('Ctrl+E'), self)
        self.exif_shortcut.activated.connect(self.open_info)
        self.open_shortcut = QShortcut(QKeySequence('Ctrl+O'), self)
        self.open_shortcut.activated.connect(self.open_image)

        self.setMinimumSize(120, 140)

    def open_image(self):
        """ Open an image from folder system """

        fname = QFileDialog.getOpenFileName(self, caption='Open an image',
                                            filter='Image files (*.jpg *.jpeg *.png *.JPG *.PNG)')

        # consider the possibility to add support for raw and dicoms images

        if fname:
            # enable buttons for actions on the image
            self.ui.left.setEnabled(True)
            self.ui.right.setEnabled(True)
            self.ui.exif.setEnabled(True)
            self.list_viewer.setVisible(True)

            self.right_rot_shortcut.setEnabled(True)
            self.left_rot_shortcut.setEnabled(True)

            # update model and viewer
            self.model.update(fname[0])
            self.model.fill_list(fname[0])
            if self.viewer.rotation:
                self.viewer.rotation = False
            self.viewer.set_model(self.model)
            self.list_widget.populate()
        else:
            QMessageBox.about(self, "File Name Error", "No file name selected")

    def resizeEvent(self, ev):
        """ Slot for window resize event (Override)"""

        self.viewer.update()
        super().resizeEvent(ev)

    def left_rotate(self):
        """ Left rotation """

        self.viewer.left_rotate()

    def right_rotate(self):
        """ Right rotation """

        self.viewer.right_rotate()

    def open_info(self):
        """ Tab for General info and Exif metadata of the current image """

        self.model.extract_general_info(self.model.current_image)
        # print("info: ", self.model.info)
        self.model.extract_exif_data(self.model.current_image)

        self.metadata_tab = CustomTab(self.model)
        self.metadata_tab.open_dict()

    def closeEvent(self, event):
        """ Closing of the MainWindow """

        if self.metadata_tab:
            print("metadata tab is visible - close it")
            self.metadata_tab.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    model = Model()

    UIWindow = MainWindow(model)
    UIWindow.setMinimumSize(800, 700)

    UIWindow.show()

    app.exec_()
