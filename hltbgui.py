import os
from tools import Tools
from howlongtobeatpy import HowLongToBeat

# ids
HLTB_WINDOW_ID = "How Long to Beat Window"
SEARCH_INPUT_ID = "Search Bar"
SEARCH_BTN_ID = "Search Button"
TABLE_ID = "Table"
RESULT_CONTAINER_ID = "Results Container"

# labels
RESULT_LABEL = "Results"
GAME_LABEL = "Game"
MAIN_TIME_LABEL = "Main Time"
MAINX_TIME_LABEL = "Main + Extra Time"
COMPLETE_TIME_LABEL = "Completionist Time"
SEARCH_BTN_LABEL = "Search"

# vars
HLTB_URL = 'https://howlongtobeat.com'
BANNER_IMG_PATH = "resources/img/banner.png"
GAME_IMG_DIR = "resources/game_imgs"
GAME_NAME_WRAP_CNT = 200
IMG_SCALE_FACTOR = 0.25

class HLTBGUI:
    def __init__(self, dpg):
        self.dpg = dpg
        self.create_win()
        self.isSearched = False  # flag used to delete the table if a search was already done
        self.dpg.set_primary_window(HLTB_WINDOW_ID, True)

    def create_win(self):
        with self.dpg.window(id=HLTB_WINDOW_ID,
                             height=self.dpg.get_viewport_height(),
                             width=self.dpg.get_viewport_width()):
            # Banner
            Tools.add_padding(self.dpg, 75, 15, True)
            Tools.add_and_load_image(self.dpg, BANNER_IMG_PATH, HLTB_WINDOW_ID)

            # Search Bar
            Tools.add_padding(self.dpg, 25, 10, True)
            self.dpg.add_input_text(id=SEARCH_INPUT_ID,
                                    width=self.dpg.get_viewport_width() * 0.75)

            # Search Button
            self.dpg.add_same_line()
            self.dpg.add_button(label=SEARCH_BTN_LABEL,
                                id=SEARCH_BTN_ID,
                                width=self.dpg.get_viewport_width() * 0.15,
                                callback=self.search_callback)

            # Padding for the Results Container
            Tools.add_padding(self.dpg, 25, 10, True)

    def search_callback(self):
        # Grab the string from the input field
        search_query = self.dpg.get_value(SEARCH_INPUT_ID)

        # Check if it is blank or not (using the Tools)
        if not Tools.isBlank(search_query):
            # delete the table so that a new table can be made
            if self.isSearched:
                self.dpg.delete_item(RESULT_CONTAINER_ID)

            self.isSearched = True

            # reset input field
            self.dpg.set_value(SEARCH_INPUT_ID, "")

            # use API to search
            results = HowLongToBeat().search(search_query)

            # Result Container
            with self.dpg.child(id=RESULT_CONTAINER_ID,
                                parent=HLTB_WINDOW_ID,
                                height=self.dpg.get_viewport_height() * 0.65,
                                width=self.dpg.get_viewport_width() * 0.908):

                # Results Label Text
                self.dpg.add_text(RESULT_LABEL)

                # Results Table
                with self.dpg.table(id=TABLE_ID,
                                    parent=RESULT_CONTAINER_ID,
                                    header_row=True):
                    # column headers
                    self.dpg.add_table_column(label=GAME_LABEL)
                    self.dpg.add_table_column(label=MAIN_TIME_LABEL)
                    self.dpg.add_table_column(label=MAINX_TIME_LABEL)
                    self.dpg.add_table_column(label=COMPLETE_TIME_LABEL)

            if results is not None and len(results) == 1:
                best_result = max(results, key=lambda element: element.similarity)
                self.add_game(best_result)

            else:
                # print out the other results
                for i in range(len(results)):
                    game = results[i]
                    self.add_game(game)

            self.cleanup_game_folder()

    def add_game(self, game):
        # Game Name + Cover
        self.dpg.add_text(game.game_name,
                          parent=TABLE_ID,
                          wrap=GAME_NAME_WRAP_CNT)

        # 7 b/c /games/ is constant for all image urls
        game_file_name = game.game_image_url[7 : game.game_image_url.index('.')]
        img_path = Tools.load_img_url(HLTB_URL + game.game_image_url, game_file_name, IMG_SCALE_FACTOR)

        if img_path is not None:
            Tools.add_and_load_image(self.dpg, img_path, parent=TABLE_ID)
        self.dpg.add_table_next_column(parent=TABLE_ID)

        # Main Time
        if game.gameplay_main_unit is not None:
            main_t = game.gameplay_main + " " + game.gameplay_main_unit
        else:
            main_t = 'N/A'
        self.dpg.add_text(main_t,
                          parent=TABLE_ID)
        self.dpg.add_table_next_column(parent=TABLE_ID)

        # Main + Extra Time
        if game.gameplay_main_extra_unit is not None:
            mainx_t = game.gameplay_main_extra + " " + game.gameplay_main_extra_unit
        else:
            mainx_t = 'N/A'
        self.dpg.add_text(mainx_t,
                          parent=TABLE_ID)
        self.dpg.add_table_next_column(parent=TABLE_ID)

        # Completionist Time
        if game.gameplay_completionist_unit is not None:
            comp_t = game.gameplay_completionist + " " + game.gameplay_completionist_unit
        else:
            comp_t = 'N/A'
        self.dpg.add_text(comp_t,
                          parent=TABLE_ID)
        self.dpg.add_table_next_column(parent=TABLE_ID)


    def cleanup_game_folder(self):
        # delete all of the images from the game_imgs folder
        for file in os.listdir(GAME_IMG_DIR):
            os.remove(os.path.join(GAME_IMG_DIR, file))
