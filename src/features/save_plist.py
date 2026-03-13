from yt_dlp import YoutubeDL
from os import chdir, mkdir, path, listdir
from typing import Literal

from src.common.askers import Askers
from src.common.utils  import Utils
from src.helpers_save_plist.plist_askers  import Plist_Askers
from src.helpers_save_plist.plist_utils   import Plist_Utils
from src.helpers_save_plist.elements_list import Elements_List
import src.common.ydl_support as ydl_support
import src.helpers_save_plist.loops.trim_elements as trim_elements
import src.helpers_save_plist.loops.numbering     as numbering
import src.helpers_save_plist.loops.trim_names    as trim_names



def save_plist(plist_url: list) -> Literal["repeat", "exit"]:
    # Get playlist dictionary
    plist_dict = ydl_support.get_plist_dict(plist_url)
    if not plist_dict:
        return

    # Get playlist title
    plist_title = plist_dict['title']

    setts_format = Utils.get_val_from_settings("PLIST_SAVE_FORMAT")
    setts_path   = Utils.get_val_from_settings("SAVE_PATH")
    setts_numbering           = Utils.get_val_from_settings("PLIST_NUMBERING")
    setts_numbering_has_zeros = Utils.get_val_from_settings("PLIST_NUMBERING_HAS_ZEROS")
    setts_del_duplicates      = Utils.get_val_from_settings("PLIST_DEL_DUPLICATES")
    ydl_opts = Utils.get_ydl_options(setts_format)

    # Get lists with videos data
    plist_urls      = [el['url'] for el in plist_dict['entries']]
    plist_el_titles = [el['title'] for el in plist_dict['entries']]
    del(plist_dict)
    duplis_flag = Plist_Utils.has_duplicates(plist_urls)
    yt_list = Elements_List(plist_urls,
                            plist_el_titles,
                            setts_numbering,
                            setts_numbering_has_zeros,
                            setts_del_duplicates)

    while True:
        numbering_string = ("None"
                            if not setts_numbering else
                            "Yes, with zeros"
                            if setts_numbering_has_zeros else
                            "Yes, without zeros")
        print(f"Playlist: {plist_title}\n")
        print(f"Format:    {setts_format}")
        print(f"Save path: {setts_path}")
        print(f"Numbering: {numbering_string}")
        if duplis_flag:
            del_msg = f"Duplicates deleting: {setts_del_duplicates}\n"
            print(del_msg, end="")
        print()
        asker = Plist_Askers.ask_plist_menu(duplis_flag)
        print()

        if asker == "handle_duplicates" and duplis_flag:
            if not setts_del_duplicates:
                asker = Plist_Askers.ask_delete_duplis()
                if not asker:
                    continue
                setts_del_duplicates = not setts_del_duplicates
                Utils.save_value_to_settings(
                    "PLIST_DEL_DUPLICATES",
                    setts_del_duplicates)
                yt_list.delete_duplicates()

            elif setts_del_duplicates:
                asker = Plist_Askers.ask_restore_duplis()
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
            if extension == setts_format:
                continue

            ydl_opts = Utils.get_ydl_options(extension)
            setts_format = extension
            Utils.save_value_to_settings("PLIST_SAVE_FORMAT", extension)

        elif asker == "remove_elements":
            while True:
                print("Current elements in playlist:")
                for el in yt_list.new_names_list:
                    print(el)
                print()

                action = Plist_Askers.ask_trimming_main_menu()
                print()
                break
            pass

        elif asker == "change_names":
            pass

        elif asker == "change_numbering":
            pass

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

        elif asker == "download":
            if not path.exists(setts_path):
                print("Save path does not exist on your device.")
                continue
            pass

        elif asker == "exit":
            return "exit"



    # Make user specify which elements to download
    plist_list = [[i+1, plist_el_titles[i], plist_urls[i]] for i in range(0, len(plist_urls))]
    plist_list = trim_elements.trim_elements_loop(plist_list)
    print()
    if not plist_list:
        return
    plist_urls = [el[2] for el in plist_list]

    # Ask user to trim elements names
    # List with illegals (for metadata later)
    plist_el_titles = trim_names.trim_names_loop(
        [el[0] for el in plist_list], [el[1] for el in plist_list])
    print()
    # List with legals   (for file names)
    plist_el_titles_legal = [
        Utils.illegal_char_remover(el) for el in plist_el_titles]

    # Get indexing style from user
    # Without zeros (for metadata later)
    plist_indexes = numbering.numbering_loop(
        [el[0] for el in plist_list], plist_el_titles)
    # With zeros    (for file naming)
    plist_indexes_zeros = [Plist_Utils.zeros_at_beginning(el, max(plist_indexes)) for el in plist_indexes]
    is_numbered: bool = True if plist_indexes else False
    print()

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
