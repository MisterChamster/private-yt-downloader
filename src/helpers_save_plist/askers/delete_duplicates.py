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
