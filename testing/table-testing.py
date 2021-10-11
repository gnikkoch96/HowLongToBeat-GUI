import dearpygui.dearpygui as dpg

def create_rows():
    dpg.add_text(f"Row Column dsfadf",
                 parent="table")
    dpg.add_table_next_column(parent="table")

    dpg.add_text(f"Row Column dsfadf",
                 parent="table")
    dpg.add_table_next_column(parent="table")

    dpg.add_text(f"Row Column dsfadf",
                 parent="table")
    dpg.add_table_next_column(parent="table")

    dpg.add_text(f"Row Column dsfadf",
                 parent="table")

    # for i in range(0, 4):
    #         for j in range(0, 3):
    #             dpg.add_text(f"Row{i} Column{j} dsfadf",
    #                          parent="table")
    #             if not (i == 3 and j == 2):
    #                 dpg.add_table_next_column(parent="table")

with dpg.window(label="about"):

    with dpg.table(id="table",
                   header_row=True):

        # use add_table_column to add columns to the table,
        # table columns use slot 0
        dpg.add_table_column(label="Header 1")
        dpg.add_table_column(label="Header 2")
        dpg.add_table_column(label="Header 3")

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1

create_rows()
dpg.start_dearpygui()