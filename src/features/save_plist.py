from yt_dlp import YoutubeDL
from os import chdir, mkdir, path, listdir
from src.common.askers import Askers
from src.common.utils import (illegal_char_remover,
                              is_internet_available,
                              get_ydl_options)
from src.helpers_save_plist.askers_plist import Askers_Plist
from src.helpers_save_plist.utils import (zeros_at_beginning,
                                          get_indexes_of_duplicates,
                                          are_duplicates,
                                          del_indexes)
from src.common.ydl_support import get_plist_dict
from src.helpers_save_plist.loops.trim_elements import trim_elements_loop
from src.helpers_save_plist.loops.numbering import numbering_loop
from src.helpers_save_plist.loops.trim_names import trim_names_loop



def save_plist(plist_url: list) -> None:
    # Get playlist dictionary
    plist_dict = get_plist_dict(plist_url)
    if not plist_dict:
        return

    # Get playlist title
    plist_title = plist_dict['title']
    print(f"Playlist: {plist_title}")
    print()

    # Get lists with videos data
    plist_urls = [el['url'] for el in plist_dict['entries']]
    plist_el_titles = [el['title'] for el in plist_dict['entries']]
    del(plist_dict)

    # Check and handle duplicates
    if are_duplicates(plist_urls):
        del_duplicates_choice = Askers_Plist.ask_del_duplicates()
        if del_duplicates_choice:
            dupli_indexes = get_indexes_of_duplicates(plist_urls)

            plist_urls = del_indexes(plist_urls, dupli_indexes)
            plist_el_titles = del_indexes(plist_el_titles, dupli_indexes)
        print()
    # I don't care about indexing b4 deleting duplicates and neither should you

    # Get save extension from user and correct ydl options
    extension = Askers.ask_save_ext()
    print()
    ydl_opts = get_ydl_options(extension)

    # Make user specify which elements to download
    plist_list = [[i+1, plist_el_titles[i], plist_urls[i]] for i in range(0, len(plist_urls))]
    plist_list = trim_elements_loop(plist_list)
    print()
    if not plist_list:
        return
    plist_urls = [el[2] for el in plist_list]

    # Ask user to trim elements names
    # List with illegals (for metadata later)
    plist_el_titles = trim_names_loop([el[0] for el in plist_list], [el[1] for el in plist_list])
    print()
    # List with legals   (for file names)
    plist_el_titles_legal = [illegal_char_remover(el) for el in plist_el_titles]

    # Get indexing style from user
    # Without zeros (for metadata later)
    plist_indexes = numbering_loop([el[0] for el in plist_list], plist_el_titles)
    # With zeros    (for file naming)
    plist_indexes_zeros = [zeros_at_beginning(el, max(plist_indexes)) for el in plist_indexes]
    is_numbered: bool = True if plist_indexes else False
    print()

    # Get save path from user
    save_path = Askers.ask_save_path()
    if save_path == "":
        print("Empty path was chosen.")
        return
    chdir(save_path)

    # Get dir name and create it
    dir_name = illegal_char_remover(plist_title)
    while path.exists(save_path + "/" + dir_name):
        dir_name += "_d"
    mkdir(dir_name)
    chdir(dir_name)
    ydl_opts["paths"] = {"home": save_path + "/" + dir_name}

    total_errors = 0
    print(f"Downloading {plist_title}...")

    for index in range(0, len(plist_urls)):
        final_filename = (plist_el_titles_legal[index]
                          if not is_numbered
                          else plist_indexes_zeros[index] + final_filename)

        while final_filename in listdir():
            final_filename += "_d"
        ydl_opts["outtmpl"] = final_filename

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([plist_urls[index]])
            print(final_filename)
        except:
            if not is_internet_available():
                print("Internet connection failed.\n\n")
                return
            else:
                total_errors += 1
                print(f"{final_filename} could not be downloaded. Here's link to this video: {plist_urls[index]}")

    if total_errors == 0:
        print("\n" + plist_title + " playlist has been successfully downloaded.\n\n")
    elif total_errors == 1:
        print("\n" + "Downloading " + plist_title + " didn't go smooth. There has been 1 exception.\n\n")
    else:
        print("\n" + "Downloading " + plist_title + " didn't go smooth. There have been " + str(total_errors) + " exceptions.\n\n")


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
