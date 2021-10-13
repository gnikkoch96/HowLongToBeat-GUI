import dearpygui.dearpygui as dpg
from hltbgui import HLTBGUI

# static
VIEWPORT_HEIGHT = 1000
VIEWPORT_WIDTH = 1000


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

if __name__ == '__main__':
    # dpg.show_style_editor()
    create_win()

    # delete the game_imgs folder
    
