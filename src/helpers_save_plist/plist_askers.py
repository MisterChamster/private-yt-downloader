from typing import Literal



class Plist_Askers():
    # =============================== PLIST MENU ===============================
    def ask_plist_menu(duplicates_problem: bool = False) -> str:
        returns_dict = {
            "f": "change_format",
            "r": "remove_elements",
            "e": "edit_captions",
            "p": "change_save_path",
            "l": "change_link",
            "o": "rev_to_original",
            "d": "download",
            "x": "exit"}
        if duplicates_problem:
            returns_dict["c"] = "handle_duplicates"

        while True:
            if duplicates_problem:
                print("c - Handle duplicates")
            print("f - Change saving format\n"
                  "r - Remove elements to download\n"
                  "e - Edit captions...\n"
                  "p - Change save path\n"
                  "l - Change link\n"
                  "o - Revert to original playlist\n"
                  "d - Download\n"
                  "x - Exit program\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n\n")


    # =============================== DUPLICATES ===============================
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
            'b': 'edit_numbering',
            'p': 'edit_plist_name',
            'r': 'return'}

        while True:
            print("n - Trim elements' names\n"
                  "b - Edit elements' numbering\n"
                  "p - Edit playlist name"
                  "r - Return\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n\n")


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
