import dearpygui.dearpygui as dpg
import os
from hltbgui import HLTBGUI

# vars
VIEWPORT_HEIGHT = 1000
VIEWPORT_WIDTH = 1000
GAME_IMG_DIR = "resources/game_imgs"

def create_win():
    # dpg viewport
    dpg.setup_viewport()
    dpg.set_viewport_title("(DearPyGUI) HowLongToBeat GUI")
    dpg.set_viewport_height(VIEWPORT_HEIGHT)
    dpg.set_viewport_width(VIEWPORT_WIDTH)

    # create themes
    create_dpg_themes()

    # create the main gui
    HLTBGUI(dpg)

    dpg.start_dearpygui()


def create_dpg_themes():
    with dpg.theme(default_theme=True):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (156, 209, 28), category=dpg.mvThemeCat_Core)


def cleanup_game_folder():
    # delete all of the images from the game_imgs folder
    for file in os.listdir(GAME_IMG_DIR):
        os.remove(os.path.join(GAME_IMG_DIR, file))


if __name__ == '__main__':
    # dpg.show_style_editor()
    create_win()
    cleanup_game_folder()