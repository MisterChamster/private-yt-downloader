from typing  import Literal
from pathlib import Path
from os      import chdir, mkdir, path, listdir

from src.common.askers import Askers
from src.common.utils  import Utils
from src.common.download_opts import Download_Opts
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

    opts = Download_Opts()
    save_numbering           = Utils.get_val_from_settings("PLIST_NUMBERING")
    save_numbering_has_zeros = Utils.get_val_from_settings("PLIST_NUMBERING_HAS_ZEROS")
    del_duplicates           = Utils.get_val_from_settings("PLIST_DEL_DUPLICATES")
    duplis_flag = Plist_Utils.has_duplicates(plist_urls)
    yt_list     = Elements_List(
        plist_title,
        plist_urls,
        plist_el_titles,
        save_numbering,
        save_numbering_has_zeros,
        del_duplicates)

    while True:
        if yt_list.new_len == 0:
            print("There are no elements left in the playlist!\n\n")
            return

        numbering_string = ("None"
                            if not yt_list.numbering else
                            "Yes, with zeros"
                            if yt_list.numbering_has_zeros else
                            "Yes, without zeros")

        Utils.print_list(yt_list.new_names_list)
        print()
        print(f"Playlist:  {yt_list.new_plist_title}")
        print(f"Format:    {opts.save_format}")
        print(f"Save path: {opts.save_path}")
        print(f"Numbering: {numbering_string}")
        if duplis_flag:
            duplis_del_msg = f"Duplicates deleting: {del_duplicates}\n"
            print(duplis_del_msg, end="")
        print()
        asker_menu = Plist_Askers.ask_plist_menu(duplis_flag)
        print("\n")

        if asker_menu == "handle_duplicates" and duplis_flag:
            if not del_duplicates:
                asker = Plist_Askers.ask_delete_duplis()
                print("\n")
                if not asker:
                    continue
                del_duplicates = not del_duplicates
                Utils.save_value_to_settings(
                    "PLIST_DEL_DUPLICATES",
                    del_duplicates)
                yt_list.delete_duplicates()

            elif del_duplicates:
                asker = Plist_Askers.ask_restore_duplis()
                print("\n")
                if not asker:
                    continue
                del_duplicates = not del_duplicates
                Utils.save_value_to_settings(
                    "PLIST_DEL_DUPLICATES",
                    del_duplicates)
                yt_list.restore_elements_to_og()

        elif asker_menu == "change_format":
            asker = Askers.ask_save_ext()
            print("\n")
            if asker in (opts.save_format, "return"):
                continue

            opts.set_save_format(asker)
            opts.reset_ydl()

        elif asker_menu == "remove_elements":
            while True:
                if yt_list.new_len == 0:
                    print("There are no elements left in the playlist!\n\n")
                    return

                print("Current elements in playlist:")
                Utils.print_list(yt_list.new_names_list, True)
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

        elif asker_menu == "edit_captions":
            while True:
                asker = Plist_Askers.ask_edit_captions()
                print("\n")

                if asker == 'trim_names':
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
                                yt_list.new_names_list[trim_index] = old_name[:-trim_len]

                        elif action == "trim_range":
                            start_el_index: int = Plist_Askers.ask_first_index(
                                yt_list.new_len,
                                'trim')
                            print("\n")
                            if start_el_index is None:
                                continue

                            ending_el_index = Plist_Askers.ask_second_index(
                                yt_list.new_len,
                                'trim',
                                start_el_index)
                            print("\n")
                            if ending_el_index is None:
                                continue

                            trim_front_back = Plist_Askers.ask_trim_front_back()
                            print("\n")
                            if trim_front_back == 'return':
                                continue

                            trim_len = Plist_Askers.ask_trim_length()
                            print("\n")
                            if not trim_len:
                                continue

                            for i in range(len(yt_list.new_names_list)):
                                if i < start_el_index or i > ending_el_index:
                                    continue

                                name = yt_list.new_names_list[i]
                                if trim_front_back == 'start':
                                    yt_list.new_names_list[i] = name[trim_len:]
                                elif trim_front_back == 'end':
                                    yt_list.new_names_list[i] = name[:-trim_len]

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
                                    yt_list.new_names_list[i] = name[:-trim_len]

                        elif action == "original_names":
                            yt_list.restore_names_to_og()

                        elif action == "return":
                            break

                elif asker == 'edit_numbering':
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
                            Utils.save_value_to_settings(
                                'PLIST_NUMBERING',
                                yt_list.numbering)
                        elif asker == "change_zeros":
                            yt_list.numbering_has_zeros = not yt_list.numbering_has_zeros
                            Utils.save_value_to_settings(
                                'PLIST_NUMBERING_HAS_ZEROS',
                                yt_list.numbering_has_zeros)
                        elif asker == "return":
                            break

                elif asker == 'edit_plist_name':
                    new_plist_name = Plist_Askers.ask_plist_name()
                    print("\n")
                    if new_plist_name == 'r':
                        continue
                    if new_plist_name == 'o':
                        yt_list.new_plist_title = yt_list.og_plist_title
                    else:
                        yt_list.new_plist_title = new_plist_name

                elif asker == 'return':
                    break

        elif asker_menu == "change_save_path":
            asker = Askers.ask_save_path()
            print("\n")
            if asker == "":
                print("Empty path was chosen.\n\n")
                continue
            if not path.exists(asker):
                print("Invalid path.\n\n")
                continue

            opts.set_save_path(asker)

        elif asker_menu == "change_link":
            return "repeat"

        elif asker_menu == "rev_to_original":
            yt_list.reset_new_to_og()

        elif asker_menu == "download":
            if not path.exists(opts.save_path):
                print("Save path does not exist on your device.")
                continue

            # Get dir name and create it
            chdir(opts.save_path)
            dir_name = Utils.illegal_char_remover(yt_list.new_plist_title)
            while True:
                dirpath = Path(opts.save_path) / dir_name
                if not (dirpath).exists():
                    break
                dir_name += "_d"
            mkdir(dir_name)
            chdir(dir_name)
            opts.mutate_ydl("paths", {"home": str(dirpath)})

            total_errors = 0
            print(f"Downloading {yt_list.new_plist_title}")

            for index in range(yt_list.new_len):
                filename = yt_list.get_filename_for_download(index)
                filename = Utils.illegal_char_remover(filename)
                while filename in listdir():
                    filename += "_d"
                opts.mutate_ydl("outtmpl", filename)

                url = yt_list.new_urls_list[index]

                download_flag = ydl_support.download_fromyt(opts.ydl_opts, url)
                if download_flag:
                    print(filename)
                else:
                    total_errors += 1
                    print(f"Downloading {filename} failed. Link: {url}")

            print()
            if not total_errors:
                print(f"{yt_list.new_plist_title} playlist has been successfully downloaded.\n\n")
            elif total_errors == 1:
                print(f"Downloading {yt_list.new_plist_title} didn't go smooth. There has been 1 exception.\n\n")
            else:
                print(f"Downloading {yt_list.new_plist_title} didn't go smooth. There have been {total_errors} exceptions.\n\n")

        elif asker_menu == "exit":
            return "exit"
