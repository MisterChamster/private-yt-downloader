def zeros_at_beginning(
    number: int,
    max_element_number: int
) -> str:
    """
    Determines a number in name of element present in a playlist.

    Depending on number of max element, function will put an adequate number of 0's
    before the index.

    Examples:
        (plist_len = 4):        01, 02, 03, 04
        (plist_len = 64):    ...08, 09, 10, 11,...
        (plist_len = 128):   ...008, 009, 010, 011,..., 098, 099, 100, 101,...

    Args:
        number (int):               number of element in playlist.
        max_element_number (int):   max number that'll be used.

    Returns:
        str: zeros determined by function + number + ". "
    """
    return ((max_element_number < 10) * f"0{number}. ") + ((max_element_number >= 10) * (f"{(len(str(max_element_number)) - len(str(number))) * '0'}{number}. ")) # I'm really sorry. The same code is written below, but it's readable
    if max_element_number < 10:
        return f"0{number}."
    else:
        digits_of_biggest_number = len(str(max_element_number))
        digits_of_number         = len(str(number))
        gg                       = digits_of_biggest_number - digits_of_number
        return f"{gg * '0'}{number}."


def get_indexes_of_searched_item(
    list_of_items: list,
    searched_item: int | str
) -> list:
    indexes_list = []
    i = 0
    while i < len(list_of_items):
        if list_of_items[i] == searched_item:
            indexes_list.append(i)
        i += 1
    return indexes_list


def are_duplicates(list_of_items: list) -> bool:
    i = 0
    while i+1 < len(list_of_items):
        item_appearances = get_indexes_of_searched_item(list_of_items, list_of_items[i])
        if len(item_appearances) > 1:
            return True
        i += 1
    return False


def get_indexes_of_duplicates(list_of_items: list) -> list:
    list_of_appearances = []
    list_of_lists_of_appearances = []
    i = 0
    while i+1 < len(list_of_items):
        item_appearances = get_indexes_of_searched_item(list_of_items, list_of_items[i])
        if len(item_appearances) > 1:
            list_of_lists_of_appearances.append(item_appearances[1:])
        i += 1
    
    for item1 in list_of_lists_of_appearances:
        for item2 in item1:
            list_of_appearances.append(item2)
            list_of_appearances = list(set(list_of_appearances))
    return list_of_appearances


def del_indexes(list_of_items: list, indexes_list: list) -> list:
    indexes_list.sort()
    indexes_list.reverse()
    for i in indexes_list:
        list_of_items.pop(i)
    return list_of_items


def list_vids(plist_list: list) -> None:
    # print("Hello! I list videos. You're pretty.")
    for i in range(0, len(plist_list)):
        print(f"{plist_list[i][0]}. {plist_list[i][1]}")


def del_by_number(plist_list: list, number: int) -> list:
    i = 0
    while i < len(plist_list):
        if plist_list[i][0] == number:
            plist_list.pop(i)
            return plist_list
        i += 1


def del_by_range(plist_list: list, start_el: int, end_el: int) -> list:
    for i in range(start_el, end_el+1):
        del_by_number(plist_list, i)
    return plist_list


def list_vid_names(plist_numbers: list, plist_vid_titles: list) -> None:
    for i in range(0, len(plist_vid_titles)):
        print(f"{plist_numbers[i]}. {plist_vid_titles[i]}")
