from typing import Literal



class Plist_Askers():
    # =============================== PLIST MENU ===============================
    def ask_plist_menu(duplicates_problem: bool = False) -> str:
        returns_dict = {
            "f": "change_format",
            "r": "remove_elements",
            "n": "trim_names",
            "u": "change_numbering",
            "p": "change_save_path",
            "l": "change_link",
            "o": "rev_to_original",
            "d": "download",
            "e": "exit"}
        if duplicates_problem:
            returns_dict["c"] = "handle_duplicates"

        while True:
            if duplicates_problem:
                print("c - Handle duplicates")
            print("f - Change saving format\n"
                  "r - Remove elements to download\n"
                  "n - Trim elements' names\n"
                  "u - Edit elements' numbering\n"
                  "p - Change save path\n"
                  "l - Change link\n"
                  "o - Revert to original playlist\n"
                  "d - Download\n"
                  "e - Exit program\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n")


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


    @staticmethod
    def ask_single_index_remove(plist_len: int) -> int | None:
        while True:
            print("Input number of the element to remove:\n"
                  "('r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker == "r":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
                continue

            el_number = int(asker)
            if el_number > plist_len or el_number < 1:
                print("Number is not an element on videos list.\n")
                continue
            else:
                return el_number


    @staticmethod
    def ask_remove_first_index(plist_len: int) -> int | None:
        while True:
            print("Input number of the first element to trim:\n"
                  "(input 'r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker == "return":
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
    def ask_remove_second_index(plist_len: int, start_el_index: int) -> int | None:
        while True:
            print("Input number of the first element to trim:\n"
                  "(input 'l' to select last element of the playlist)\n"
                  "(input 'r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker == "r":
                return
            elif asker in ["l", "-1"]:
                return -1
            elif not asker.isdigit():
                print("Incorrect input.\n")
                continue

            ending_el = int(asker)
            if (ending_el <= start_el_index+1 or
                ending_el > plist_len):
                print("Number is unavailable.\n")
            else:
                if ending_el == plist_len:
                    return -1
                end_index = ending_el - 1
                return end_index


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
    def ask_trim_single_index(plist_len: int) -> int | None:
        while True:
            print("Input number of the element to trim name:\n"
                  "(input 'r' to return)\n>> ", end="")
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
                return el_number-1


    @staticmethod
    def ask_length_type() -> str:
        returns_dict = {
            "i": "input_integer",
            "s": "input_string",
            "r": "return"}

        while True:
            print("Choose trim length value type:\n"
                  "i - Input integer value...\n"
                  "s - Input string and calculate it's length...\n"
                  "r - Return\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n\n")


    @staticmethod
    def ask_length_int() -> int | None:
        while True:
            print("Input a number of characters to cut:\n"
                  "(input 'r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker == "r":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n\n")

            asker_int = int(asker)
            if asker_int == 0:
                return
            else:
                return int(asker)


    @staticmethod
    def ask_length_str() -> int | None:
        while True:
            print("Input string to cut (will count its characters):\n"
                  "(input 'r' to return)\n>> ", end="")
            asker = input()

            if asker == "r" or asker == "":
                return
            return len(asker)


    @staticmethod
    def ask_trim_front_back() -> str | None:
        returns_dict = {
            "s": "start",
            "e": "end",
            "r": "return"}

        while True:
            print("Cut characters from (input 'r' to return):\n"
                  "s - start\n"
                  "e - end\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n\n")


    @staticmethod
    def ask_multiple_name_trim(plist_numbers: list) -> list[int,int] | None:
        while True:
            print("Input number of the first element to trim name:\n"
                  "(input 'r' to return)\n>> ", end="")
            asker = input().strip().lower()

            if asker == "r":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n\n")
                continue

            start_el = int(asker)
            if start_el not in plist_numbers:
                print("Number is not an element on videos list.\n")
            else:
                break

        print()

        while True:
            print("Input number of the last element to trim name:\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker2 = input().strip()

            if asker2 == "exit":
                return
            elif not asker2.isdigit():
                print("Incorrect input.\n\n")
                continue

            end_el = int(asker2)
            if end_el not in plist_numbers:
                print("Number is not an element on videos list.\n")
            elif end_el < start_el:
                print("End number can't be smaller than the start number.\n")
            else:
                return [start_el, end_el]


    # =============================== NUMBERING ===============================
    @staticmethod
    def ask_numbering_main_menu() -> str:
        returns_dict = {
            "o":  "start_on_1",
            "n":  "no_numbering",
            "b":  "begin_on_integer",
            "e":  "end_on_integer",
            "r":  "reverse_numbering",
            "og": "original_numbering",
            "":   "save"}

        while True:
            print("Choose numbering option:\n"
                  "o     - Starting on 1\n"
                  "n     - No numbering\n"
                  "b     - Beginning on integer...\n"
                  "e     - Ending on integer...\n"
                  "r     - Reverse current numbering\n"
                  "og    - Original numbering\n"
                  "Enter - Save current style\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_first_number() -> int | None:
        while True:
            print("Input the number of the first element:\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker = input().strip()

            if asker == "exit":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
            else:
                first_el_num = int(asker)
                return first_el_num


    @staticmethod
    def ask_last_number(plist_len: int) -> int | None:
        lowest_possible = plist_len - 1
        while True:
            print(f"Input the number of the last element ({lowest_possible} or higher):\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker = input().strip()

            if asker == "exit":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
                continue

            last_el_num = int(asker)
            if last_el_num < lowest_possible:
                print("Given number is too small.\n")
            else:
                return last_el_num
