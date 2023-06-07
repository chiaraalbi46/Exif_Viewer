""" Custom widgets """

from PyQt5.QtCore import Qt, QSize, QFileInfo
from PyQt5.QtWidgets import QLabel, QWidget, QTreeWidgetItem, QMessageBox, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap, QTransform, QIcon, QImage, QFont

from metadata_view import Ui_Metadata
from general_widget import Ui_General
from error_label import Ui_Error_label

import webbrowser
from PIL import Image


class ImageView(QLabel):
    """ Custom Widget to show image """

    def __init__(self, parent):

        super().__init__(parent)
        self.parent = parent  # reference to the parent

        self.angle = 0
        self.rotation = False

        self.qpix = QPixmap()
        self.setPixmap(self.qpix)

    def set_model(self, model):
        """ Set the reference to the model and update the view """

        self.model = model
        self.update()

    def set_viewer_list(self, viewer_list):
        """ Set the reference to list of images """

        self.viewer_list = viewer_list

    def update(self):
        """ Update the view of the current image """

        if self.model.current_image and not self.rotation:
            self.qpix = QPixmap(self.model.current_image)
            self.setPixmap(self.qpix.scaled(QSize(min(self.size().width(), 512), min(self.size().height(), 512)),
                                            Qt.KeepAspectRatio, Qt.FastTransformation))

        elif self.model.current_image and self.rotation:
            self.setPixmap(self.qpix.scaled(QSize(min(self.size().width(), 512), min(self.size().height(), 512)),
                                            Qt.KeepAspectRatio, Qt.FastTransformation))
        elif not self.model.current_image:
            self.qpix = QPixmap()
            self.setPixmap(self.qpix)
            self.parent.exif.setEnabled(False)
            self.parent.left.setEnabled(False)
            self.parent.right.setEnabled(False)
            self.setFont(QFont("Lucida Calligraphy", 18, True))
            self.setText("Drag and drop your images here !")

    def left_rotate(self):
        """ Rotate the main image of 90 degrees to the left and update the view """

        self.rotation = True
        self.angle -= 90

        transform = QTransform().rotate(self.angle)
        self.qpix = self.qpix.transformed(transform, Qt.SmoothTransformation)

        self.update()

        # reset
        self.angle = 0

    def right_rotate(self):

        """ Rotate the main image of 90 degrees to the right and update the view """

        self.rotation = True
        self.angle += 90

        transform = QTransform().rotate(self.angle)
        self.qpix = self.qpix.transformed(transform, Qt.SmoothTransformation)

        self.update()

        # reset
        self.angle = 0

    def dragEnterEvent(self, e):
        """ Drag files directly onto the widget """

        if len(e.mimeData().urls()) > 0 and e.mimeData().urls()[0].isLocalFile():
            qi = QFileInfo(e.mimeData().urls()[0].toLocalFile())
            ext = qi.suffix()
            if ext == 'jpg' or ext == 'jpeg' or ext == 'png' or ext == 'JPG' or ext == 'PNG':
                e.accept()
            else:
                e.ignore()
        else:
            e.ignore()

    def dropEvent(self, e):
        """ Drop files directly onto the widget. File locations are stored in fname, update the model,
        fill the list of images, enable some buttons and populate the list """

        if self.rotation:
            self.rotation = False
        if e.mimeData().hasUrls:
            e.setDropAction(Qt.CopyAction)
            e.accept()

            for url in e.mimeData().urls():
                fname = str(url.toLocalFile())
                self.model.fill_list(fname)

            self.model.update(fname)
            self.set_model(self.model)

            self.parent.exif.setEnabled(True)  # self.parent.ui.exif pensavo invece no
            self.parent.left.setEnabled(True)
            self.parent.right.setEnabled(True)
            self.parent.listFrame.setVisible(True)

            self.viewer_list.populate()
        else:
            e.ignore()


class GeneralView(QWidget):
    """ General info widget """

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.ui_gen = Ui_General()
        self.ui_gen.setupUi(self.parent)

        self.gen_info_tree_widg = self.ui_gen.general_info


class ExifView(QWidget):
    """ Exif metadata widget """

    def __init__(self, parent, model):
        super().__init__(parent)
        self.parent = parent
        self.model = model

        self.ui_gen = Ui_General()
        self.ui_gen.setupUi(self.parent)

        self.exif_info = self.ui_gen.general_info
        self.gps_button = self.ui_gen.GPS

        self.gps_button.clicked.connect(self.open_maps)

    def open_maps(self):
        """ Open Google Maps at the image location """

        print("GPS button clicked")
        if self.model.has_gps:
            lat, lon = self.model.get_gps_coordinates()
            webbrowser.open(
                f'https://www.google.com/maps/search/?api=1&query={lat},{lon}', 2)
        else:
            print("no gps data available")
            QMessageBox.about(self, "Error", "No GPS coordinates are available")


class CustomTab(QWidget):
    """ Custom Widget to show info on image """

    def __init__(self, model):

        super(CustomTab, self).__init__()

        self.ui_widg = Ui_Metadata()
        self.ui_widg.setupUi(self)  # assign the ui at the passed widget
        self.tab_widget = self.ui_widg.tabWidget
        self.tab_info = self.ui_widg.Gen
        self.tab_exif = self.ui_widg.Exif

        self.ui_gen = Ui_General()

        self.tab_info_ui(model)
        self.tab_exif_ui(model)

    def tab_info_ui(self, model):
        """ Set the reference to model and set general info into widget """

        self.model = model
        general_info = self.model.get_general_info()

        layout = self.ui_widg.horizontalLayout_5

        if general_info:
            self.temp_widg = QWidget()
            self.ui_gen.setupUi(self.temp_widg)
            self.fill_widget(self.ui_gen.general_info, general_info)
        else:
            # if general info on current image is empty
            ui_error = Ui_Error_label()
            temp_label = QLabel()
            ui_error.setupUi(temp_label)
            self.ui_gen.general_info = ui_error.message  # temp_label

        layout.addWidget(self.ui_gen.general_info)

        self.tab_widget.setTabText(0, "General")
        self.tab_info.setLayout(layout)

    def tab_exif_ui(self, model):
        """ Set the reference to model and set exif data into widget """

        self.model = model
        exif = self.model.get_exif()

        layout = self.ui_widg.horizontalLayout_4

        if exif:
            self.temp_widg = QWidget()

            self.exif_view = ExifView(self.temp_widg, self.model)  # QWidget()
            self.fill_widget(self.exif_view.exif_info, exif)
            layout.addWidget(self.exif_view.exif_info)
            layout.addWidget(self.exif_view.gps_button)

        else:
            # if general info on current image is empty
            ui_error = Ui_Error_label()
            temp_label = QLabel()
            ui_error.setupUi(temp_label)

            self.ui_gen.general_info = ui_error.message
            layout.addWidget(self.ui_gen.general_info)

        self.tab_widget.setTabText(1, "Exif")
        self.tab_exif.setLayout(layout)

    def open_dict(self):
        """ Open tab widget to visualize info and exif on image """

        self.show()

    def fill_widget(self, widget, value):
        """ Fill the widget """

        self.widget = widget
        self.widget.clear()
        self.fill_item(self.widget.invisibleRootItem(), value)

    def fill_item(self, item, value):
        """ Fill the widget with value (info or exif) """

        item.setExpanded(True)
        if type(value) is dict:
            for key, val in value.items():
                child = QTreeWidgetItem()
                child.setText(0, str(key))
                item.addChild(child)
                self.fill_item(child, val)
        elif type(value) is list:
            for val in value:
                child = QTreeWidgetItem()
                item.addChild(child)
                if type(val) is dict:
                    child.setText(0, '[dict]')
                    self.fill_item(child, val)
                elif type(val) is list:
                    child.setText(0, '[list]')
                    self.fill_item(child, val)
                else:
                    child.setText(0, str(val))
                    child.setExpanded(True)
        else:
            child = QTreeWidgetItem()
            child.setText(0, str(value))
            item.addChild(child)


class ImageListView(QListWidget):
    """ Custom Widget to list of images """

    def __init__(self, parent=None):
        """ Set several parameters and reference to parent, model and viewer """

        QListWidget.__init__(self, parent)
        self.setIconSize(QSize(80, 80))

        self.parent = parent
        self.model = None
        self.viewer = None

        self.itemDoubleClicked.connect(self.upload_image)
        self.itemClicked.connect(self.enable_delete_button)

    def set_model(self, model):
        """ Set the model """

        self.model = model

    def set_viewer(self, viewer):
        """ Set the viewer """

        self.viewer = viewer

    def populate(self):
        """ Fill the list of images and set itself to viewer """

        # clear the list (case of repopulating)
        self.clear()

        # create a list item for each image file, setting the text and icon appropriately
        for image in self.model.get_list():
            picture = Image.open(image)
            picture.thumbnail((72, 72), Image.ANTIALIAS)
            icon = QIcon(QPixmap.fromImage(QImage(picture.filename)))
            item = QListWidgetItem(self)  # insert the image in list
            item.setToolTip(image)
            item.setIcon(icon)

        if not self.parent.clearList.isEnabled():
            self.parent.clearList.setEnabled(True)  # enable buttons to empty the list
        self.viewer.set_viewer_list(self)

    def upload_image(self):
        """ If double click on image in list the image will displayed in main viewer. Update the view """

        if self.viewer.rotation:
            self.viewer.rotation = False
        self.current_item = self.currentRow()
        self.model.get_element(self.current_item)  # Get image from model
        self.viewer.update()

        # enable buttons on current image
        if not self.parent.exif.isEnabled():
            self.parent.exif.setEnabled(True)
            self.parent.left.setEnabled(True)
            self.parent.right.setEnabled(True)

    def enable_delete_button(self):
        """ Activate button to remove an image from list and set the current image clicked in list """

        self.parent.deleteItem.setEnabled(True)
        self.current_item = self.currentRow()

    def set_action_list_buttons(self):
        """ Connect delete item and clear all buttons to their respective functions """

        self.parent.deleteItem.clicked.connect(self.delete_item)
        self.parent.clearList.clicked.connect(self.clear_list)

    def delete_item(self):
        """ Delete image from list and call model to delete image. Update the view """

        self.model.delete_element(self.current_item)
        self.takeItem(self.current_item)
        print("current item: ", self.current_item)

        if self.current_item == 0 and not self.model.images:
            self.model.update("")
            self.disable_list_buttons()

        elif self.current_item != 0:
            print("update")
            self.current_item = self.current_item - 1
            self.setCurrentRow(self.current_item)

        self.viewer.update()

    def clear_list(self):
        """ Empty the list and update model and view """

        self.model.empty_list()
        self.model.update("")
        self.clear()
        self.viewer.update()
        self.disable_list_buttons()

    def disable_list_buttons(self):
        """ Disable delete item and clear all buttons """

        self.parent.deleteItem.setEnabled(False)
        self.parent.clearList.setEnabled(False)
