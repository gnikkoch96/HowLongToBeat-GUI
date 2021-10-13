import urllib
import os
import cv2


class Tools:
    @staticmethod
    def add_padding(dpg, width_value=0, height_value=0, is_same_line=False):
        if height_value != 0:
            dpg.add_dummy(height=height_value)

        if width_value != 0:
            dpg.add_dummy(width=width_value)

        if is_same_line:
            dpg.add_same_line()

    @staticmethod
    def add_and_load_image(dpg, image_path, parent=None):
        width, height, channels, data = dpg.load_image(image_path)

        with dpg.texture_registry() as reg_id:
            texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

        if parent is None:
            return dpg.add_image(texture_id)
        else:
            return dpg.add_image(texture_id, parent=parent)

    @staticmethod
    # checks if a string is blank and that it is not None type
    def isBlank(myString):
        if myString and myString.strip():
            # myString is not None AND myString is not empty or blank
            return False
        # myString is None OR myString is empty or blank
        return True


    @staticmethod
    # loads the image through a url, and then scales it down
    # url - url of image
    # name - name the image
    # scale_factor - how small do you want the image to be (0.0 -> 1)
    def load_img_url(url, name, scale_factor):
        # retrieves the img through url and downloads to local folder

        urllib.request.urlretrieve(
            url,
            name + ".png"
        )

        path = name + ".png"

        # resize image
        img = cv2.imread(path)

        if img is None:
            print("Warning: Image was not loaded, please check url")
            return

        width = int(img.shape[1] * scale_factor)
        height = int(img.shape[0] * scale_factor)
        dimension = (width, height)

        resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)

        # new file contains the resized image and replaces old image
        cv2.imwrite(f'{name}.png', resized)

        # moves the image to the correct folder
        new_path = f"resources/game_imgs/{name}.png"
        os.replace(path, new_path)

        return new_path
