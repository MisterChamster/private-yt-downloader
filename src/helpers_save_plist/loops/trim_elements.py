from src.helpers_save_plist.utils import (list_vids,
                                          del_by_number,
                                          del_by_range)
from src.helpers_save_plist.askers_plist import Askers_Plist



def trim_elements_loop(plist_list: list) -> list|None:
    while True:
        print("Current elements in playlist:")
        list_vids(plist_list)
        print()

        action = Askers_Plist.ask_trimming_main_menu()
        print()

        if action == "all":
            return plist_list

        elif action == "custom":
            plist_list = custom_trim_loop(plist_list)
            if plist_list == None:
                return

        elif action == "list":
            list_vids(plist_list)
            print()


def custom_trim_loop(plist_list: list) -> list:
    while True:
        if not plist_list:
            print("All elements have been removed.\n\n")
            return None

        print("Current elements in playlist:")
        list_vids(plist_list)
        print()

        action = Askers_Plist.ask_custom_trim()
        print()

        if action == "trim_element":
            plist_numbers = [i[0] for i in plist_list]
            number_to_trim = Askers_Plist.ask_el_trim(plist_numbers)
            print()
            if number_to_trim is None:
                continue
            plist_list = del_by_number(plist_list, number_to_trim)
            return plist_list

        elif action == "trim_range":
            plist_numbers = [i[0] for i in plist_list]
            trim_range = Askers_Plist.ask_multiple_trim(plist_numbers)
            print()
            if trim_range is None:
                continue
            plist_list = del_by_range(plist_list, trim_range[0], trim_range[1])
            return plist_list

        elif action == "return":
            return plist_list
