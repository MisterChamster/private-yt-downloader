from src.helpers_save_plist.plist_utils import Plist_Utils



class Elements_List():
    # immutable
    og_urls_list:    list[str]
    og_names_list:   list[str]
    og_len: int

    #mutable
    new_urls_list:    list[str]
    new_names_list:   list[str]
    new_numbers_list: list[str]
    new_index_in_og:  list[int]
    new_len: int
    numbering: bool
    numbering_has_zeros: bool
    del_duplicates: bool


    def __init__(self,
                 urls_list: list[str],
                 names_list: list[str],
                 numbering: bool,
                 numbering_has_zeros: bool,
                 del_duplicates: bool
    ) -> None:
        if len(urls_list) != len(names_list):
            raise ValueError("Lists not of the same length")

        self.og_urls_list   = urls_list
        self.og_names_list  = names_list
        self.og_len         = len(urls_list)

        self.new_urls_list  = urls_list
        self.new_names_list = names_list
        self.new_len        = len(urls_list)
        self.numbering      = numbering
        self.numbering_has_zeros = numbering_has_zeros
        self.del_duplicates  = del_duplicates

        self.reset_new_index_in_og()
        self.calc_numbering_list()
        self.delete_duplicates_accordingly()


    def reset_new_index_in_og(self):
        self.new_index_in_og = [
            i for i in range(len(self.new_urls_list))]


    def calc_numbering_list(self) -> None:
        if not self.numbering:
            self.new_numbers_list = ['' for _ in range(self.new_len)]

        elif not self.numbering_has_zeros:
            self.new_numbers_list = [el for el in range(self.new_len)]

        elif self.numbering_has_zeros:
            self.new_numbers_list = [
                Plist_Utils.zeros_at_beginning(el, self.new_len)
                for el in range(self.new_len)]


    def _delete_duplicates(self) -> None:
        dupli_indexes = Plist_Utils.get_indexes_of_duplicates(self.new_urls_list)
        i = len(dupli_indexes) - 1
        while i >= 0:
            self.pop_new(dupli_indexes[i])
            i -= 1


    def delete_duplicates_accordingly(self) -> None:
        if not self.del_duplicates:
            return
        self._delete_duplicates()


    def restore_elements_to_og(self) -> None:
        self.new_urls_list = self.og_urls_list.copy()
        temp_names_list = self.og_names_list.copy()
        for index in range(self.new_index_in_og):
            changed_name = self.new_names_list[index]
            index_to_change = self.new_index_in_og[index]
            temp_names_list[index_to_change] = changed_name
        self.new_names_list = temp_names_list.copy()

        self.update_newlen()


    def set_new_to_og(self) -> None:
        self.new_urls_list   = self.og_urls_list
        self.new_names_list  = self.og_names_list
        self.new_index_in_og = [i for i in range(len(self.og_urls_list))]
        self.new_len = len(self.og_urls_list)
        self.calc_numbering_list()


    def update_newlen(self) -> None:
        self.new_len = len(self.new_urls_list)


    def pop_new(self, index) -> None:
        self.new_urls_list.pop[index]
        self.new_names_list.pop[index]
        self.new_numbers_list.pop[index]
        self.new_index_in_og.pop[index]
        self.update_newlen()
