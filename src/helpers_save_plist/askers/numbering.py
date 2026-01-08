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


def ask_first_number() -> int|None:
    while True:
        print("Input the number of the first element:\n"
              "(to exit input 'exit')\n>> ", end="")
        asker = input().strip()

        if asker == "exit":
            return
        elif not asker.isdigit():
            print("Incorrect input.\n")
        else:
            first_el_num = int(asker)
            return first_el_num


def ask_last_number(plist_len: int) -> int|None:
    lowest_possible = plist_len - 1
    while True:
        print(f"Input the number of the last element ({lowest_possible} or higher):\n"
              "(to exit input 'exit')\n>> ", end="")
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
