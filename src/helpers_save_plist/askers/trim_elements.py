def ask_trimming_main_menu() -> str:
    returns_dict = {"c":  "custom",
                    "ls": "list",
                    "":   "all"}

    while True:
        print("Choose which elements to download:\n"
              "c     - Custom settings...\n"
              "ls    - List all current elements\n"
              "Enter - Save current list of elements\n>> ", end="")
        asker = input()

        if asker in returns_dict:
            return returns_dict[asker]
        else:
            print("Incorrect input.\n")


def ask_custom_trim() -> str:
    returns_dict = {"te": "trim_element",
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


def ask_el_trim(plist_numbers: list) -> int:
    while True:
        print("Input number of the element to trim:\n"
              "(to exit input 'exit')\n>> ", end="")
        asker = input()

        if asker == "exit":
            return None
        elif not asker.isdigit():
            print("Incorrect input.\n")
            continue
        el_number = int(asker)
        if el_number not in plist_numbers:
            print("Number is not an element on videos list.\n")
        else:
            return el_number


def ask_multiple_trim(plist_numbers: list) -> int:
    while True:
        print("Input number of the first element to trim:\n"
              "(to exit input 'exit')\n>> ", end="")
        asker = input()

        if asker == "exit":
            return None
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
              "(to exit input 'exit')\n>> ", end="")
        asker2 = input()

        if asker2 == "exit":
            return None
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
