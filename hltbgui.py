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


# vars
TABLE_COL = 4
TBL_HEADER_GAME = 0
TBL_HEADER_MAIN = 1
TBL_HEADER_MAINX = 2
TBL_HEADER_COMP = 3


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
            # 1st Row
            # Search Bar
            self.dpg.add_input_text(id=SEARCH_INPUT_ID,
                                    width=self.dpg.get_viewport_width() * 0.75)

            # Search Button
            self.dpg.add_same_line()
            self.dpg.add_button(label="Search",
                                id=SEARCH_BTN_ID,
                                width=self.dpg.get_viewport_width() * 0.15,
                                callback=self.search_callback)

            # 2nd Row
            # Result Container
            with self.dpg.child(id=RESULT_CONTAINER_ID,
                                height=self.dpg.get_viewport_height() * 0.60,
                                width=self.dpg.get_viewport_width() * 0.85):
                # Results Text
                self.dpg.add_text(RESULT_LABEL)

    def search_callback(self):
        # delete the table so that a new table can be made
        if self.isSearched:
            self.dpg.delete_item(TABLE_ID)

        # Grab the string from the input field
        search_query = self.dpg.get_value(SEARCH_INPUT_ID)

        # Check if it is blank or not (using the Tools)
        if not Tools.isBlank(search_query):
            self.isSearched = True

            # reset input field
            self.dpg.set_value(SEARCH_INPUT_ID, "")

            # use API to search
            results = HowLongToBeat().search(search_query)
            print(len(results))
            if results is not None and len(results) == 1:
                best_result = max(results, key=lambda element: element.similarity)
                self.add_game(best_result)

            else:
                # print out the other results
                for i in range(len(results)):
                    self.add_game(results)

    def add_game(self, result):
        # Results Table
        with self.dpg.table(id=TABLE_ID,
                            parent=RESULT_CONTAINER_ID,
                            header_row=True):
            # column headers
            self.dpg.add_table_column(label=GAME_LABEL)
            self.dpg.add_table_column(label=MAIN_TIME_LABEL)
            self.dpg.add_table_column(label=MAINX_TIME_LABEL)
            self.dpg.add_table_column(label=COMPLETE_TIME_LABEL)

            for i in range(len(result)):
                game = result[i]
                # Game Name + Cover
                self.dpg.add_text(game.game_name)
                self.dpg.add_table_next_column()

                # Main Time
                if game.gameplay_main_unit is not None:
                    main_t = game.gameplay_main + " " + game.gameplay_main_unit
                else:
                    main_t = 'N/A'
                self.dpg.add_text(main_t)
                self.dpg.add_table_next_column()

                # Main + Extra Time
                if game.gameplay_main_extra_unit is not None:
                    mainx_t = game.gameplay_main_extra + " " + game.gameplay_main_extra_unit
                else:
                    mainx_t = 'N/A'
                self.dpg.add_text(mainx_t)
                self.dpg.add_table_next_column()

                # Completionist Time
                if game.gameplay_completionist_unit is not None:
                    comp_t = game.gameplay_completionist + " " + game.gameplay_completionist_unit
                else:
                    comp_t = 'N/A'
                self.dpg.add_text(comp_t)
                self.dpg.add_table_next_column()

