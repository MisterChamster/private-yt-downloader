from src.helpers_save_plist.plist_utils import Plist_Utils
from src.helpers_save_plist.plist_askers import Plist_Askers



def numbering_loop(
    og_numbering:     list[int],
    plist_vid_titles: list
) -> list[int]|None:

    final_numbering = og_numbering
    while True:
        print("Current numbering:")
        Plist_Utils.list_vid_names(final_numbering, plist_vid_titles)
        print()

        action = Plist_Askers.ask_numbering_main_menu()
        print()

        if action == "start_on_1":
            final_numbering = [i+1 for i in range(0, len(og_numbering))]
            print()

        elif action == "no_numbering":
            final_numbering = None
            print()

        elif action == "begin_on_integer":
            first_el_num = Plist_Askers.ask_first_number()
            print()
            if first_el_num == None:
                continue
            final_numbering = [i for i in range(first_el_num, first_el_num+len(og_numbering))]

        elif action == "end_on_integer":
            last_el_num = Plist_Askers.ask_last_number(len(og_numbering))
            print()
            if last_el_num == None:
                continue
            final_numbering = [i for i in range(last_el_num-len(og_numbering)+1, last_el_num+2)]

        elif action == "reverse_numbering":
            final_numbering = final_numbering[::-1]
            print()

        elif action == "original_numbering":
            final_numbering = og_numbering
            print()

        elif action == "save":
            return final_numbering
