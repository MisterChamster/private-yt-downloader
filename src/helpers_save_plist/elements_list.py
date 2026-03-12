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


    def __init__(self,
                 urls_list: list[str],
                 names_list: list[str],
                 numbering: bool,
                 numbering_has_zeros: bool
    ) -> None:
        if len(urls_list) != len(names_list):
            raise ValueError("Lists not of the same length")

        self.og_urls_list    = urls_list
        self.og_names_list   = names_list
        self.og_len          = len(urls_list)
        self.new_urls_list   = urls_list
        self.new_names_list  = names_list
        self.new_index_in_og = [i for i in range(len(urls_list))]
        self.new_len         = len(urls_list)
        self.numbering       = numbering
        self.numbering_has_zeros = numbering_has_zeros

        self.calc_numbering_list()


    def calc_numbering_list(self) -> None:
        if not self.numbering:
            self.new_numbers_list = ['' for el in range(self.new_len)]
            return

        if not self.numbering_has_zeros:
            self.new_numbers_list = [el for el in range(self.new_len)]
            return

        if self.numbering_has_zeros:
            self.new_numbers_list = [
                Plist_Utils.zeros_at_beginning(el, self.new_len)
                for el in range(self.new_len)]


    def set_new_to_og(self):
        self.new_urls_list    = self.og_urls_list
        self.new_names_list   = self.og_names_list
        self.new_index_in_og  = [i for i in range(len(self.og_urls_list))]
        self.new_len = len(self.og_urls_list)


    def update_newlen(self) -> None:
        self.new_len = len(self.new_urls_list)


    def pop_new(self, index) -> None:
        self.new_urls_list.pop[index]
        self.new_names_list.pop[index]
        self.new_numbers_list.pop[index]
        self.new_index_in_og.pop[index]
        self.update_newlen()
