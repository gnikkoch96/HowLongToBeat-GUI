# importing modules
import os
import dearpygui.dearpygui as dpg
import urllib.request
import numpy as numpy
from PIL import Image

# retrieves the img through url and downloads to local folder
urllib.request.urlretrieve(
  'https://howlongtobeat.com/games/94075_Metroid_Dread.jpg',
   "metroid.png")

# gets the abs path (used to move the file to a specific folder)
pkg_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(pkg_dir, "../testing/metroid.png")

# moves the image to the correct folder
new_path = os.path.join(pkg_dir, "../resources/game_imgs/metroid.png")
os.replace(path, new_path)

image = Image.open(new_path)
image.putalpha(255)

# resize the image
img = cv2.imread(image)
# scale_percent = 0.50
# width = int(img.shape[1] * scale_percent)
# height = ing(img.shape[0] * scale_percent)
# dimension = (width, height)
#
# resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
# print(resized.shape)
# cv2.imshow('output', resized)
# cv2.imwrite('resized_photo.jpg', resized)
#
# dpg_image = numpy.frombuffer(image.tobytes(), dtype=numpy.uint8)/255.0
#
dpg.setup_viewport()

with dpg.window():
    print(dpg.load_image(new_path))
    width, height, channels, data = dpg.load_image(new_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    dpg.add_image(texture_id)


dpg.start_dearpygui()