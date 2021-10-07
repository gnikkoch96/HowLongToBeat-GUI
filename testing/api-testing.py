from howlongtobeatpy import HowLongToBeat

# returns the list of HowLongToBeat objs
results = HowLongToBeat().search("Tales of Arise")

if results is not None and len(results) > 0:
    # returns the most likely result
    best_element = max(results, key=lambda element: element.similarity)

# Base Game Details
print(best_element.game_id)
print(best_element.game_name)
print(best_element.game_image_url)  # need to provide https://howlongtobeat.com first
print(best_element.game_web_link)

# Gameplay Main
print(best_element.gameplay_main)
print(best_element.gameplay_main_unit)
print(best_element.gameplay_main_label)

# Gameplay Main + Extra
print(best_element.gameplay_main_extra)
print(best_element.gameplay_main_extra_unit)
print(best_element.gameplay_main_extra_label)

# Gameplay Completionist
print(best_element.gameplay_completionist)
print(best_element.gameplay_completionist_unit)
print(best_element.gameplay_completionist_label)
