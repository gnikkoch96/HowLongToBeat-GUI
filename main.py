import dearpygui.dearpygui as dpg
from hltbgui import HLTBGUI

# static
VIEWPORT_HEIGHT = 700
VIEWPORT_WIDTH = 1000


def create_win():
    # dpg viewport
    dpg.setup_viewport()
    dpg.set_viewport_title("(DearPyGUI) HowLongToBeat GUI")
    dpg.set_viewport_height(VIEWPORT_HEIGHT)
    dpg.set_viewport_width(VIEWPORT_WIDTH)

    # create the main gui
    HLTBGUI(dpg)

    dpg.start_dearpygui()


if __name__ == '__main__':
    create_win()
