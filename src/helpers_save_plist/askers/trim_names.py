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


def ask_length_int() -> int|None:
    while True:
        print("Input a number of characters to cut:\n"
              "(to exit input 'exit')\n>> ", end="")
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


def ask_length_str() -> int|None:
    while True:
        print("Input string to cut (will count its characters):\n"
              "(to exit input 'exit')\n>> ", end="")
        asker = input()

        if asker == "exit" or asker == "":
            return
        return len(asker)


def ask_trim_front_back() -> str|None:
    returns_dict = {
        "s": "start",
        "e": "end"}

    while True:
        print("Cut characters from (to exit input 'exit'):\n"
              "s - start\n" \
              "e - end\n>> ", end="")
        asker = input().strip().lower()

        if asker == "exit":
            return
        elif asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n")


def ask_el_name_trim(plist_numbers: list) -> int|None:
    while True:
        print("Input number of the element to trim name:\n"
              "(to exit input 'exit')\n>> ", end="")
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


def ask_multiple_name_trim(plist_numbers: list) -> list[int,int]|None:
    while True:
        print("Input number of the first element to trim name:\n"
              "(to exit input 'exit')\n>> ", end="")
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
              "(to exit input 'exit')\n>> ", end="")
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
