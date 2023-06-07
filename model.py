from PIL import Image
import os
import os.path
import time
from hurry.filesize import size
import exifread


class Model:
    """ This class contains the program state (The Model).
    It provides methods to get, set, modify and evolve the state """

    def __init__(self, name=None):

        self.current_image = name
        self.images = []
        self.has_gps = False

    def update(self, name):
        """ Update the Model """

        self.current_image = name

    def extract_exif_data(self, image):
        """ Extract exif data of image """

        self.exif = {}
        f = open(image, 'rb')
        tags = exifread.process_file(f)
        if len(tags) == 0:
            print("No exif data are available for this image")
        else:
            print("Start parsing")

            for tag in tags.keys():
                if tag == 'Image GPSInfo':
                    print("GPS data available")
                    self.has_gps = True

                self.exif[tag] = tags[tag]

    def get_exif(self):
        """ Return exif data """

        return self.exif

    def extract_general_info(self, image):
        """ Extract general info from image """

        self.info = {}
        try:
            img = Image.open(image)
            self.info['File name'] = os.path.basename(img.filename)
            self.info['Document type'] = img.format
            self.info['File size'] = size(os.stat(img.filename).st_size) + " (%5d bytes)" % os.stat(
                img.filename).st_size
            self.info['Creation date'] = time.ctime(os.path.getctime(img.filename))
            self.info['Modification date'] = time.ctime(os.path.getmtime(img.filename))
            self.info['Image size'] = img.size
            self.info['Color model'] = img.mode
        except AttributeError:
            print('Error with image')

    def get_general_info(self):
        """ Return general info of image """

        return self.info

    def get_tag_if_exist(self, tag):
        """ Check the presence of a specific tag """

        if tag in self.exif:
            return self.exif[tag]
        return None

    def to_degrees(self, value):
        """ Convert dms coordinates in degrees """

        # minute = 1/60th of a degree
        # second = 1/60th of a minute = 1/3600th of a degree
        return round(float(value[0]) + (float(value[1]) / 60.0) + (float(value[2]) / 3600.0), 6)

    def get_gps_coordinates(self):
        """ Get latitude and longitude from GPS tags """

        # Latitude specifies the angular distance from the equator, which can be either north or sud.
        # The 'GPS GPSLatitudeRef' property indicates this direction, which is either N or S.
        # Longitude specifies the angular distance from the meridian, which can be either east or west.
        # The 'GPS GPSLongitudeRef' property indicates this direction, which is either E or W.

        lat = None
        lon = None
        gps_lat = self.get_tag_if_exist('GPS GPSLatitude')  # degrees, minutes, seconds
        gps_lat_ref = self.get_tag_if_exist('GPS GPSLatitudeRef')
        gps_lon = self.get_tag_if_exist('GPS GPSLongitude')
        gps_lon_ref = self.get_tag_if_exist('GPS GPSLongitudeRef')

        if gps_lat and gps_lat_ref and gps_lon and gps_lon:
            lat = self.to_degrees(gps_lat.values)
            if gps_lat_ref.values != 'N':
                lat = - lat
            lon = self.to_degrees(gps_lon.values)
            if gps_lon_ref.values != 'E':
                lon = - lon

        return lat, lon

    def fill_list(self, image):
        """ Insert image in list """

        for i in self.images:
            if i == image:
                return
        self.images.append(image)

    def get_element(self, position):
        """ Returns element of list at certain position """

        current_element = self.images[position]
        self.update(current_element)

    def empty_list(self):
        """ Empty the list """

        del self.images[:]

    def delete_element(self, position):
        """ Delete image from list at certain position. If image deleted is main image update the model """

        if self.images[position] == self.current_image:
            self.update("")
        self.images = [v for i, v in enumerate(self.images) if i != position]

    def get_list(self):
        """ Return the list of images """

        return self.images