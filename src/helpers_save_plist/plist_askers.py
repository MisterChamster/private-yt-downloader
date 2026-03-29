from typing import Literal



class Plist_Askers():
    # ==========================================================================
    # =============================== PLIST MENU ===============================
    # ==========================================================================
    @staticmethod
    def ask_plist_menu(
            duplicates_problem: bool = False,
            download_md: bool = False,
            md_possible: bool = True) -> str:
        returns_dict = {
            "f": "change_format",
            "r": "remove_elements",
            "e": "edit_captions",
            "p": "change_save_path",
            "m": "metadata_settings",
            "l": "change_link",
            "o": "rev_to_original",
            "d": "download",
            "x": "exit"}
        if duplicates_problem:
            returns_dict["c"] = "handle_duplicates"
        if md_possible:
            returns_dict["m"] = "metadata_settings"

        download_string = ("(with metadata)"
                           if download_md
                           else "(no metadata)"
                           if md_possible
                           else "")
        while True:
            if duplicates_problem:
                print("c - Handle duplicates")
            print("f - Change saving format\n"
                  "r - Remove elements to download\n"
                  "e - Edit captions...\n"
                  "p - Change save path")
            if md_possible:
                print("m - Metadata settings")
            print("l - Change link\n"
                  "o - Revert to original playlist\n"
                 f"d - Download {download_string}\n"
                  "x - Exit program\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n\n")


    # ==========================================================================
    # =============================== DUPLICATES ===============================
    # ==========================================================================
    @staticmethod
    def ask_delete_duplis() -> bool:
        returns_dict = {
            "d": True,
            "r": False}

        while True:
            print("Duplicates detected.\n"
                  "d - Delete duplicates\n"
                  "r - Return\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n\n")


    @staticmethod
    def ask_restore_duplis() -> bool:
        returns_dict = {
            "s": True,
            "r": False}

        while True:
            print("Duplicates have been detected and deleted.\n"
                  "s - Restore duplicates\n"
                  "r - Return\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n\n")


    # ==========================================================================
    # ================================== EDIT ==================================
    # ==========================================================================
    @staticmethod
    def ask_edit_captions() -> Literal[
        'trim_names',
        'edit_numbering',
        'edit_plist_name',
        'return']:
        returns_dict = {
            'n': 'trim_names',
            'e': 'edit_names',
            'b': 'edit_numbering',
            'p': 'edit_plist_name',
            'r': 'return'}

        while True:
            print("Choose action:")
            print("n - Trim elements' names\n"
                  "e - Edit elements' names\n"
                  "b - Edit elements' numbering\n"
                  "p - Edit playlist name\n"
                  "r - Return\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n\n")


    @staticmethod
    def ask_edit_names(max_num: int) -> str:
        returns_dict = {'r': 'return'}

        while True:
            print("Input a file's number to manually change title ('r' to return)\n>> ", end="")
            asker = input().strip()

            if asker in returns_dict:
                return returns_dict[asker]

            elif asker.isdigit():
                if (int(asker) < 1 or
                    int(asker) > max_num):
                    print("Incorrect input\n\n")
                else:
                    return asker
            else:
                print("Incorrect input\n\n")


    @staticmethod
    def ask_new_title(old_title: str) -> str:
        print(old_title)
        print("Input new title\n>> ", end="")
        asker = input()
        return asker


    @staticmethod
    def ask_plist_name() -> str:
        while True:
            print("Input new playlist name\n"
                  "('r' to return, 'o' to original):\n>> ", end="")
            asker = input()

            if not asker:
                print("Input can't be empty.\n\n")
                continue
            if asker in ('r', 'o'):
                return asker
            return asker


    # ============================ ELEMENT REMOVAL ============================
    @staticmethod
    def ask_el_removal_menu() -> Literal[
        'remove_single',
        'remove_range',
        'return']:
        returns_dict = {
            "s": "remove_single",
            "g": "remove_range",
            "r": "return"}

        while True:
            print("Choose element removal option:\n"
                  "s - Remove single element...\n"
                  "g - Remove a range of elements...\n"
                  "r - Return\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n")


    # ============================= NAME TRIMMING =============================
    @staticmethod
    def ask_trim_names_option() -> Literal[
        "trim_single",
        "trim_range",
        "trim_all_names",
        "original_names",
        "return"]:
        returns_dict = {
            "s": "trim_single",
            "g": "trim_range",
            "a": "trim_all_names",
            "o": "original_names",
            "r": "return"}

        while True:
            print("Choose element name trimming option:\n"
                  "s - Trim name of a single element...\n"
                  "g - Trim name of elements in range...\n"
                  "a - Trim all names...\n"
                  "o - Return all elements to original names\n"
                  "r - Return\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n\n")


    @staticmethod
    def ask_trim_front_back() -> Literal['start', 'end', 'return']:
        returns_dict = {
            "s": "start",
            "e": "end",
            "r": "return"}

        while True:
            print("Cut characters from:\n"
                  "s - Start\n"
                  "e - End\n"
                  "r - Return\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n\n")


    @staticmethod
    def ask_trim_length() -> int | None:
        len_type = Plist_Askers.ask_length_type()
        print("\n")

        if len_type == 'input_integer':
            trim_len = Plist_Askers.ask_length_int()
            print("\n")
            return trim_len
        elif len_type == 'input_string':
            trim_len = Plist_Askers.ask_length_str()
            print("\n")
            return trim_len
        elif len_type == 'return':
            return


    @staticmethod
    def ask_length_type() -> Literal['input_integer', 'input_string', 'return']:
        returns_dict = {
            "v": "input_integer",
            "s": "input_string",
            "r": "return"}

        while True:
            print("Choose trim length value type:\n"
                  "v - Input integer value\n"
                  "s - Input string to get its length\n"
                  "r - Return\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n\n")


    @staticmethod
    def ask_length_int() -> int | None:
        while True:
            print("Input a number of characters to trim:\n"
                  "(input 'r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker in ['r', '0']:
                return
            elif not asker.isdigit():
                print("Incorrect input.\n\n")

            asker_int = int(asker)
            return asker_int


    @staticmethod
    def ask_length_str() -> int | None:
        while True:
            print("Input string to cut (will count its characters):\n"
                  "(input 'r' to return)\n>> ", end="")
            asker = input()

            if asker in ['r', '']:
                return
            return len(asker)


    # =============================== NUMBERING ===============================
    @staticmethod
    def ask_numbering_menu(
        numbering_enabled: bool,
        zeros_enabled: bool
    ) -> str:
        returns_dict = {
            "n": "change_numbering",
            "z": "change_zeros",
            "r": "return"}
        numbering_msg = ("Disable"
                         if numbering_enabled else
                         "Enable")
        zeros_msg = ("Disable"
                     if zeros_enabled else
                     "Enable")

        while True:
            print("Choose numbering option:\n"
                 f"n - {numbering_msg} element numbering\n"
                 f"z - {zeros_msg} zeros before numbers\n"
                  "r - Return\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input\n\n")


    # ================================ GENERIC ================================
    @staticmethod
    def ask_single_index(
        plist_len: int,
        action: Literal['remove', 'trim']
    ) -> int | None:
        string = ('trim its name'
                  if action == 'trim' else
                  'remove it')
        while True:
            print(f"Input number of the element to {string}:\n"
                   "('r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker == "r":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n\n")
                continue

            el_number = int(asker)
            if el_number > plist_len or el_number <= 0:
                print("Number is not an element on videos list.\n")
            else:
                el_index = el_number-1
                return el_index


    @staticmethod
    def ask_first_index(
        plist_len: int,
        action: Literal['remove', 'trim']
    ) -> int | None:
        while True:
            print(f"Input number of the first element to {action}:\n"
                   "(input 'r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker == "r":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
                continue

            start_el = int(asker)
            if start_el >= plist_len-1 or start_el <= 0:
                print("Number is unavailable.\n")
            else:
                start_index = start_el - 1
                return start_index


    @staticmethod
    def ask_second_index(
        plist_len: int,
        action: Literal['remove', 'trim'],
        start_el_index: int
    ) -> int | None:
        while True:
            print(f"Input number of the first element to {action}:\n"
                   "(input 'l' to select last element of the playlist)\n"
                   "(input 'r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker == "r":
                return
            elif asker in ["l", "-1"]:
                return plist_len
            elif not asker.isdigit():
                print("Incorrect input.\n")
                continue

            ending_el = int(asker)
            if (ending_el <= start_el_index+1 or
                ending_el > plist_len):
                print("Number is unavailable.\n")
            else:
                if ending_el == plist_len:
                    return plist_len
                end_index = ending_el - 1
                return end_index


    # ==========================================================================
    # ================================ METADATA ================================
    # ==========================================================================
    @staticmethod
    def ask_metadata_menu(md_included:   bool,
                          md_to_emb:     dict[Literal["album", "artist", "date", "title", "tracknumber"]:bool],
                          md_album_set:  bool,
                          md_artist_set: bool,
                          md_date_set:   bool
                ) -> Literal[
                "change_appending",
                "which_md_embedded",
                "set_album",
                "set_artist",
                "set_date",
                "set_title",
                "set_tracknumber",
                "return",
                "exit"]:
        returns_dict = {
            "a":  "change_appending",
            "e":  "which_md_embedded",
            "sl": "set_album",
            "sa": "set_artist",
            "sd": "set_date",
            "sn": "set_title",
            "st": "set_tracknumber",
            "r":  "return",
            "x":  "exit"}

        able_msg = ("Disable metadata appending"
                    if md_included
                    else "Enable metadata appending")
        md_album_set_msg       = str(md_to_emb["album"]      ).replace("True", "True ")
        md_artist_set_msg      = str(md_to_emb["artist"]     ).replace("True", "True ")
        md_date_set_msg        = str(md_to_emb["date"]       ).replace("True", "True ")
        md_title_set_msg       = str(md_to_emb["title"]      ).replace("True", "True ")
        md_tracknumber_set_msg = str(md_to_emb["tracknumber"]).replace("True", "True ")

        while True:
            print(f"a  - {able_msg}\n"
                   "e  - Specify which metadata will be embedded\n"
                  f"sl - Set album        (Embed: {md_album_set_msg   }) (Is set: {md_album_set})\n"
                  f"sa - Set artist       (Embed: {md_artist_set_msg  }) (Is set: {md_artist_set})\n"
                  f"sd - Set date         (Embed: {md_date_set_msg    }) (Is set: {md_date_set})\n"
                  f"sn - Set titles       (Embed: {md_title_set_msg    }) (Is set: True)\n" #Troll!
                  f"st - Set tracknumbers (Embed: {md_tracknumber_set_msg}) (Is set: True)\n" #Troll!
                   "r  - Return\n"
                   "x  - Exit program\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n\n")


    @staticmethod
    def ask_which_md_embed(
        md_to_emb: dict[Literal[
        "album",
        "artist",
        "date",
        "title",
        "tracknumber"]:bool],
        md_album_set:  bool,
        md_artist_set: bool,
        md_date_set:   bool) -> Literal[
            "all_legal",
            "change_set_album",
            "change_set_artist",
            "change_set_date",
            "change_set_title",
            "change_set_tracknumber",
            "return",
            "exit"]:

        returns_dict = {
            "e": "all_legal",
            "l": "change_set_album",
            "a": "change_set_artist",
            "d": "change_set_date",
            "n": "change_set_title",
            "t": "change_set_tracknumber",
            "r": "return",
            "x": "exit"}

        # I know I'm lazy
        md_album_set_msg_1       = str(md_to_emb["album"]      ).replace("True", "Disable").replace("False", "Enable ")
        md_artist_set_msg_1      = str(md_to_emb["artist"]     ).replace("True", "Disable").replace("False", "Enable ")
        md_date_set_msg_1        = str(md_to_emb["date"]       ).replace("True", "Disable").replace("False", "Enable ")
        md_title_set_msg_1       = str(md_to_emb["title"]      ).replace("True", "Disable").replace("False", "Enable ")
        md_tracknumber_set_msg_1 = str(md_to_emb["tracknumber"]).replace("True", "Disable").replace("False", "Enable ")

        # I'm sure You'd do it better <3
        md_album_set_msg_2       = md_album_set_msg_1.replace(   "Disable", "enabled").replace("Enable ", "disabled")
        md_artist_set_msg_2      = md_artist_set_msg_1.replace(  "Disable", "enabled").replace("Enable ", "disabled")
        md_date_set_msg_2        = md_date_set_msg_1.replace(    "Disable", "enabled").replace("Enable ", "disabled")
        md_title_set_msg_2       = md_title_set_msg_1.replace(    "Disable", "enabled").replace("Enable ", "disabled")
        md_tracknumber_set_msg_2 = md_tracknumber_set_msg_1.replace("Disable", "enabled").replace("Enable ", "disabled")

        legality_to_set = {
            "l": md_album_set,
            "a": md_artist_set,
            "d": md_date_set}

        while True:
            print("Choose metadata to be embedded:\n"
                  "e - Embed all metadata with value\n"
                 f"l - {md_album_set_msg_1      } embedding album metadata       (currently {md_album_set_msg_2})\n"
                 f"a - {md_artist_set_msg_1     } embedding artist metadata      (currently {md_artist_set_msg_2})\n"
                 f"d - {md_date_set_msg_1       } embedding date metadata        (currently {md_date_set_msg_2})\n"
                 f"n - {md_title_set_msg_1      } embedding title metadata       (currently {md_title_set_msg_2})\n"
                 f"t - {md_tracknumber_set_msg_1} embedding tracknumber metadata (currently {md_tracknumber_set_msg_2})\n"
                  "r - Return\n"
                  "x - Exit\n"
                  ">> ", end='')
            asker = input().strip().lower()

            if asker in legality_to_set:
                if legality_to_set[asker] is False:
                    print("Can't enable embedding; value has to be set first\n\n")
                    continue

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Invalid input\n\n")


    @staticmethod
    def ask_set_album(current_album: str | None) -> str:
        if current_album == None:
            current_album = "Not set"

        print(f"Current album: {current_album}\n"
                "Input new album (leave empty to return):\n>> ", end='')
        asker = input()
        return asker


    @staticmethod
    def ask_set_artist(current_artist: str | None) -> str:
        if current_artist == None:
            current_artist = "Not set"

        print(f"Current artist: {current_artist}\n"
                "Input new artist (leave empty to return):\n>> ", end='')
        asker = input()
        return asker


    @staticmethod
    def ask_set_date(current_date: str | None) -> str:
        if current_date == None:
            current_date = "Not set"

        while True:
            print(f"Current date: {current_date}\n"
                   "Input new date (leave empty to return):\n>> ", end='')
            asker = input().strip()

            if (asker.isdigit() and
                len(asker) == 4):
                return asker
            else:
                print("Invalid input\n\n")


    @staticmethod
    def ask_set_titles_num(titles_count: int) -> int | None:
        while True:
            print("Input number of the title to change:\n"
                  "(leave empty to return)\n"
                  "(input 0 to revert to files titles)\n>> ", end='')
            asker = input().strip()

            if asker == "":
                return

            if (asker.isdigit() and
                int(asker) <= titles_count):
                return int(asker)
            else:
                print("Invalid input\n\n")


    @staticmethod
    def ask_set_tracknumbers_num(tnums_count: int) -> int | None:
        while True:
            print("Input number of the tracknumber to change:\n"
                  "(leave empty to return)\n"
                  "(input 0 to revert to file numbering)\n>> ", end='')
            asker = input().strip()

            if asker == "":
                return

            if (asker.isdigit() and
                int(asker) <= tnums_count):
                return int(asker)
            else:
                print("Invalid input\n\n")


    @staticmethod
    def ask_md_title_string(curr_title: str) -> str:
        while True:
            print(curr_title)
            print(f"Input new title metadata:\n>> ", end='')
            asker = input()

            return asker


    @staticmethod
    def ask_md_tracknumber_string(curr_tracknumber: str) -> str:
        while True:
            print(f"Current number: {curr_tracknumber}")
            print(f"Input new tracknumber metadata:\n>> ", end='')
            asker = input()

            if not asker.isdigit():
                print("Invalid input\n\n")
                continue

            return asker
