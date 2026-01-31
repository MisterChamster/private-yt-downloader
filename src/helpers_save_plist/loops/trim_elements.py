from src.helpers_save_plist.plist_utils import Plist_Utils
from src.helpers_save_plist.plist_askers import Plist_Askers



def trim_elements_loop(plist_list: list) -> list|None:
    while True:
        print("Current elements in playlist:")
        Plist_Utils.list_vids(plist_list)
        print()

        action = Plist_Askers.ask_trimming_main_menu()
        print()

        if action == "all":
            return plist_list

        elif action == "custom":
            plist_list = custom_trim_loop(plist_list)
            if plist_list == None:
                return

        elif action == "list":
            Plist_Utils.list_vids(plist_list)
            print()


def custom_trim_loop(plist_list: list) -> list:
    while True:
        if not plist_list:
            print("All elements have been removed.\n\n")
            return None

        print("Current elements in playlist:")
        Plist_Utils.list_vids(plist_list)
        print()

        action = Plist_Askers.ask_custom_trim()
        print()

        if action == "trim_element":
            plist_numbers = [i[0] for i in plist_list]
            number_to_trim = Plist_Askers.ask_el_trim(plist_numbers)
            print()
            if number_to_trim is None:
                continue
            plist_list = Plist_Utils.del_by_number(plist_list, number_to_trim)
            return plist_list

        elif action == "trim_range":
            plist_numbers = [i[0] for i in plist_list]
            trim_range = Plist_Askers.ask_multiple_trim(plist_numbers)
            print()
            if trim_range is None:
                continue
            plist_list = Plist_Utils.del_by_range(plist_list, trim_range[0], trim_range[1])
            return plist_list

        elif action == "return":
            return plist_list
