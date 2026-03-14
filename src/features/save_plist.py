from yt_dlp import YoutubeDL
from typing import Literal
from os     import chdir, mkdir, path, listdir

from src.common.askers import Askers
from src.common.utils  import Utils
from src.helpers_save_plist.plist_askers  import Plist_Askers
from src.helpers_save_plist.plist_utils   import Plist_Utils
from src.helpers_save_plist.elements_list import Elements_List
import src.common.ydl_support as ydl_support



def save_plist(plist_url: list) -> Literal["repeat", "exit"]:
    # Get playlist dictionary
    plist_dict = ydl_support.get_plist_dict(plist_url)
    if not plist_dict:
        return

    # Get playlist title and lists with videos data
    plist_title = plist_dict['title']
    plist_urls      = [el['url']   for el in plist_dict['entries']]
    plist_el_titles = [el['title'] for el in plist_dict['entries']]
    del(plist_dict)

    setts_format = Utils.get_val_from_settings("PLIST_SAVE_FORMAT")
    setts_path   = Utils.get_val_from_settings("SAVE_PATH")
    setts_numbering           = Utils.get_val_from_settings("PLIST_NUMBERING")
    setts_numbering_has_zeros = Utils.get_val_from_settings("PLIST_NUMBERING_HAS_ZEROS")
    setts_del_duplicates      = Utils.get_val_from_settings("PLIST_DEL_DUPLICATES")
    ydl_opts = Utils.get_ydl_options(setts_format)
    duplis_flag = Plist_Utils.has_duplicates(plist_urls)
    yt_list = Elements_List(plist_urls,
                            plist_el_titles,
                            setts_numbering,
                            setts_numbering_has_zeros,
                            setts_del_duplicates)

    while True:
        if yt_list.new_len == 0:
            print("There are no elements left in the playlist!\n\n")
            return

        numbering_string = ("None"
                            if not setts_numbering else
                            "Yes, with zeros"
                            if setts_numbering_has_zeros else
                            "Yes, without zeros")

        Utils.print_list(yt_list.new_names_list)
        print()
        print(f"Playlist:  {plist_title}")
        print(f"Format:    {setts_format}")
        print(f"Save path: {setts_path}")
        print(f"Numbering: {numbering_string}")
        if duplis_flag:
            duplis_del_msg = f"Duplicates deleting: {setts_del_duplicates}\n"
            print(duplis_del_msg, end="")
        print()
        asker = Plist_Askers.ask_plist_menu(duplis_flag)
        print("\n")

        if asker == "handle_duplicates" and duplis_flag:
            if not setts_del_duplicates:
                asker = Plist_Askers.ask_delete_duplis()
                print("\n")
                if not asker:
                    continue
                setts_del_duplicates = not setts_del_duplicates
                Utils.save_value_to_settings(
                    "PLIST_DEL_DUPLICATES",
                    setts_del_duplicates)
                yt_list.delete_duplicates()

            elif setts_del_duplicates:
                asker = Plist_Askers.ask_restore_duplis()
                print("\n")
                if not asker:
                    continue
                setts_del_duplicates = not setts_del_duplicates
                Utils.save_value_to_settings(
                    "PLIST_DEL_DUPLICATES",
                    setts_del_duplicates)
                yt_list.restore_elements_to_og()

        elif asker == "change_format":
            extension = Askers.ask_save_ext()
            print()
            if extension in (setts_format, "return"):
                print()
                continue

            ydl_opts = Utils.get_ydl_options(extension)
            setts_format = extension
            Utils.save_value_to_settings("PLIST_SAVE_FORMAT", extension)

        elif asker == "remove_elements":
            while True:
                if yt_list.new_len == 0:
                    print("There are no elements left in the playlist!\n\n")
                    return

                print("Current elements in playlist:")
                Utils.print_list(yt_list.new_names_list)
                print()
                action = Plist_Askers.ask_el_removal_menu()
                print("\n")

                if action == 'remove_single':
                    print()
                    while True:
                        if yt_list.new_len == 0:
                            print("There are no elements left in the playlist!\n\n")
                            return

                        Utils.print_list(yt_list.new_names_list, True)
                        print()
                        remove_number = Plist_Askers.ask_single_index(yt_list.new_len, 'remove')
                        print("\n")
                        if not remove_number:
                            break

                        remove_index = remove_number-1
                        yt_list.pop_new(remove_index)

                elif action == 'remove_range':
                    start_el_index: int = Plist_Askers.ask_first_index(
                        yt_list.new_len,
                        'remove')
                    print("\n")
                    if not start_el_index:
                        continue

                    ending_el_index = Plist_Askers.ask_second_index(
                        yt_list.new_len,
                        'remove',
                        start_el_index)
                    print("\n")
                    if not ending_el_index:
                        continue

                    yt_list.pop_new_range(start_el_index, ending_el_index)
                    if yt_list.new_len == 0:
                        print("There are no elements left in the playlist!\n\n")
                        return

                elif action == 'return':
                    break

        elif asker == "trim_names":
            while True:
                print("Current names:")
                Utils.print_list(yt_list.new_names_list)
                print()

                action = Plist_Askers.ask_trim_names_option()
                print("\n")
                print("Current names:")
                Utils.print_list(yt_list.new_names_list, True)
                print()

                if action == "trim_single":
                    trim_index = Plist_Askers.ask_single_index(yt_list.new_len, 'trim')
                    print("\n")
                    if not isinstance(trim_index, int):
                        continue

                    trim_front_back = Plist_Askers.ask_trim_front_back()
                    print("\n")
                    if trim_front_back == 'return':
                        continue

                    trim_len = Plist_Askers.ask_trim_length()
                    print("\n")
                    if not trim_len:
                        continue

                    old_name = yt_list.new_names_list[trim_index]
                    if trim_front_back == 'start':
                        yt_list.new_names_list[trim_index] = old_name[trim_len:]
                    elif trim_front_back == 'end':
                        yt_list.new_names_list[trim_index] = old_name[:trim_len]

                elif action == "trim_range":
                    start_el_index: int = Plist_Askers.ask_first_index(
                        yt_list.new_len,
                        'trim')
                    print("\n")
                    if not start_el_index:
                        continue

                    ending_el_index = Plist_Askers.ask_second_index(
                        yt_list.new_len,
                        'trim',
                        start_el_index)
                    print("\n")
                    if not ending_el_index:
                        continue

                    trim_front_back = Plist_Askers.ask_trim_front_back()
                    print("\n")
                    if trim_front_back == 'return':
                        continue

                    trim_len = Plist_Askers.ask_trim_length()
                    print("\n")
                    if not trim_len:
                        continue

                    for i, name in enumerate(
                    yt_list.new_names_list[start_el_index:ending_el_index+1]):
                        if trim_front_back == 'start':
                            yt_list.new_names_list[i] = name[trim_len:]
                        elif trim_front_back == 'end':
                            yt_list.new_names_list[i] = name[:trim_len]

                elif action == "trim_all_names":
                    trim_front_back = Plist_Askers.ask_trim_front_back()
                    print("\n")
                    if trim_front_back == 'return':
                        continue

                    trim_len = Plist_Askers.ask_trim_length()
                    print("\n")
                    if not trim_len:
                        continue

                    for i, name in enumerate(yt_list.new_names_list):
                        if trim_front_back == 'start':
                            yt_list.new_names_list[i] = name[trim_len:]
                        elif trim_front_back == 'end':
                            yt_list.new_names_list[i] = name[:trim_len]

                elif action == "original_names":
                    yt_list.restore_names_to_og()

                elif action == "return":
                    break

        elif asker == "change_numbering":
            while True:
                print("Current numbering:")
                yt_list.print_newnames_numbering()
                print()

                asker = Plist_Askers.ask_numbering_menu(
                    yt_list.numbering,
                    yt_list.numbering_has_zeros)
                print("\n")

                if asker == "change_numbering":
                    yt_list.numbering = not yt_list.numbering
                elif asker == "change_zeros":
                    yt_list.numbering_has_zeros = not yt_list.numbering_has_zeros
                elif asker == "return":
                    break

        elif asker == "change_save_path":
            save_path = Askers.ask_save_path()
            print()
            if save_path == "":
                print("Empty path was chosen.\n\n")
                continue
            if not path.exists(save_path):
                print("Invalid path.\n\n")
                continue
            Utils.save_value_to_settings("SAVE_PATH", save_path)

        elif asker == "change_link":
            return "repeat"

        elif asker == "rev_to_original":
            yt_list = Elements_List(
                plist_urls,
                plist_el_titles,
                setts_numbering,
                setts_numbering_has_zeros,
                setts_del_duplicates)

        elif asker == "download":
            if not path.exists(setts_path):
                print("Save path does not exist on your device.")
                continue
            pass

        elif asker == "exit":
            return "exit"


    # Get dir name and create it
    chdir(save_path)
    dir_name = Utils.illegal_char_remover(plist_title)
    while path.exists(save_path + "/" + dir_name):
        dir_name += "_d"
    mkdir(dir_name)
    chdir(dir_name)
    ydl_opts["paths"] = {"home": save_path + "/" + dir_name}

    total_errors = 0
    print(f"Downloading {plist_title}...")

    for index in range(0, len(plist_urls)):
        final_filename = (
            plist_el_titles_legal[index]
            if not is_numbered
            else plist_indexes_zeros[index] + plist_el_titles_legal[index])

        while final_filename in listdir():
            final_filename += "_d"
        ydl_opts["outtmpl"] = final_filename

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([plist_urls[index]])
            print(final_filename)
        except:
            if not Utils.is_internet_available():
                print("Internet connection failed.\n\n")
                return
            else:
                total_errors += 1
                print(f"{final_filename} could not be downloaded. Here's link to this video: {plist_urls[index]}")

    print()
    if total_errors == 0:
        print(f"{plist_title} playlist has been successfully downloaded.\n\n")
    elif total_errors == 1:
        print(f"Downloading {plist_title} didn't go smooth. There has been 1 exception.\n\n")
    else:
        print(f"Downloading {plist_title} didn't go smooth. There have been {total_errors} exceptions.\n\n")


    # Now we have:
    # - plist_title
    # - dir_name
    # - extension
    # - ydl_opts
    # - plist_list
    # - og_names

    # - plist_urls
    # - plist_el_titles (for metadata later)
    # - plist_el_titles_legal
    # - plist_indexes (for metadata later)
    # - plist_indexes_zeros
