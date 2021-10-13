import os
import dearpygui.dearpygui as dpg
import urllib.request
import cv2
from PIL import Image

# retrieves the img through url and downloads to local folder
urllib.request.urlretrieve(
  'https://howlongtobeat.com/games/79793_Kena_Bridge_of_Spirits.jpg',
   "kena.png")

# gets the abs path (used to move the file to a specific folder)
pkg_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(pkg_dir, "../testing/kena.png")

# moves the image to the correct folder
new_path = os.path.join(pkg_dir, "../resources/game_imgs/kena.png")
os.replace(path, new_path)

# resize the image
img = cv2.imread(new_path)
print(type(img))
scale_percent = 0.10
width = int(img.shape[1] * scale_percent)
height = int(img.shape[0] * scale_percent)
dimension = (width, height)

resized = cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)
# cv2.imshow('output', resized)
cv2.imwrite('resized_photo.jpg', resized)

dpg.setup_viewport()

with dpg.window():
    width, height, channels, data = dpg.load_image("resized_photo.jpg")

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    dpg.add_image(texture_id)


dpg.start_dearpygui()