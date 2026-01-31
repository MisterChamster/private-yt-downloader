class Plist_Askers():
    # =============================== DUPLICATES ===============================
    @staticmethod
    def ask_del_duplicates() -> bool:
        returns_dict = {
            "d": True,
            "l": False}

        while True:
            print("Duplicates detected. Choose handling option:\n"
                  "d - Delete duplicates\n"
                  "l - Leave duplicates\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n\n")


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
    def ask_first_number() -> int|None:
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
    def ask_last_number(plist_len: int) -> int|None:
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


    # ============================ ELEMENT TRIMMING ============================
    @staticmethod
    def ask_trimming_main_menu() -> str:
        returns_dict = {
            "c":  "custom",
            "ls": "list",
            "":   "all"}

        while True:
            print("Choose which elements to download:\n"
                "c     - Custom settings...\n"
                "ls    - List all current elements\n"
                "Enter - Save current list of elements\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_custom_trim() -> str:
        returns_dict = {
            "te": "trim_element",
            "tr": "trim_range",
            "rt": "return"}

        while True:
            print("Choose custom trimming option:\n"
                "te - Trim one element...\n"
                "tr - Trim a range of elements...\n"
                "rt - Return\n>> ", end="")
            asker = input()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_el_trim(plist_numbers: list) -> int|None:
        while True:
            print("Input number of the element to trim:\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker = input()

            if asker == "exit":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
                continue
            el_number = int(asker)
            if el_number not in plist_numbers:
                print("Number is not an element on videos list.\n")
            else:
                return el_number


    @staticmethod
    def ask_multiple_trim(plist_numbers: list) -> int|None:
        while True:
            print("Input number of the first element to trim:\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker = input().strip()

            if asker == "exit":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
                continue

            start_el = int(asker)
            if start_el not in plist_numbers:
                print("Number is not an element on videos list.\n")
            else:
                break

        print()

        while True:
            print("Input number of the last element to trim:\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker2 = input()

            if asker2 == "exit":
                return
            elif not asker2.isdigit():
                print("Incorrect input.\n")
                continue

            end_el = int(asker2)
            if end_el not in plist_numbers:
                print("Number is not an element on videos list.\n")
            elif end_el < start_el:
                print("End number can't be smaller than the start number.\n")
            else:
                return [start_el, end_el]


    # ============================= NAME TRIMMING =============================
    @staticmethod
    def ask_trim_names_main_menu() -> str:
        returns_dict = {
            "tan": "trim_all_elements",
            "ts":  "trim_specific",
            "tr":  "trim_range",
            "og":  "original_names",
            "":    "save"}

        while True:
            print("Choose element name trimming option:\n"
                "tan   - Trim all names...\n"
                "ts    - Trim name of a specific element...\n"
                "tr    - Trim name of elements in range... \n"
                "og    - Return all elements to original names\n"
                "Enter - Save current names\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_length_type() -> str:
        returns_dict = {
            "i":  "input_integer",
            "s":  "input_string",
            "rt": "return"}

        while True:
            print("Choose trim length value type:\n"
                "i  - Input integer value...\n"
                "s  - Input string and calculate it's length...\n"
                "rt - Return\n>> ", end="")
            asker = input().strip().lower()

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_length_int() -> int|None:
        while True:
            print("Input a number of characters to cut:\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker = input().strip()

            if asker == "exit":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
            asker_int = int(asker)
            if asker_int == 0:
                return
            else:
                return int(asker)


    @staticmethod
    def ask_length_str() -> int|None:
        while True:
            print("Input string to cut (will count its characters):\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker = input()

            if asker == "exit" or asker == "":
                return
            return len(asker)


    @staticmethod
    def ask_trim_front_back() -> str|None:
        returns_dict = {
            "s": "start",
            "e": "end"}

        while True:
            print("Cut characters from (input 'exit' to exit):\n"
                "s - start\n" \
                "e - end\n>> ", end="")
            asker = input().strip().lower()

            if asker == "exit":
                return
            elif asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_el_name_trim(plist_numbers: list) -> int|None:
        while True:
            print("Input number of the element to trim name:\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker = input().strip()

            if asker == "exit":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
                continue
            el_number = int(asker)
            if el_number not in plist_numbers:
                print("Number is not an element on videos list.\n")
            else:
                return el_number


    @staticmethod
    def ask_multiple_name_trim(plist_numbers: list) -> list[int,int]|None:
        while True:
            print("Input number of the first element to trim name:\n"
                "(input 'exit' to exit)\n>> ", end="")
            asker = input().strip()

            if asker == "exit":
                return
            elif not asker.isdigit():
                print("Incorrect input.\n")
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
                print("Incorrect input.\n")
                continue

            end_el = int(asker2)
            if end_el not in plist_numbers:
                print("Number is not an element on videos list.\n")
            elif end_el < start_el:
                print("End number can't be smaller than the start number.\n")
            else:
                return [start_el, end_el]
