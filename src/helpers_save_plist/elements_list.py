class Elements_List():
    # immutable
    og_urls_list:    list[str]
    og_names_list:   list[str]
    og_numbers_list: list[str]
    og_len: int

    #mutable
    new_urls_list:    list[str]
    new_names_list:   list[str]
    new_numbers_list: list[str]
    new_index_in_og:  list[int]
    new_len: int


    def __init__(self,
                 urls_list: list[str],
                 names_list: list[str],
                 numbers_list: list[str]
    ) -> None:
        if (len(urls_list) != len(names_list) or
            len(urls_list) != len(numbers_list)):
            raise ValueError("Lists not of the same length")

        self.og_urls_list     = urls_list
        self.og_names_list    = names_list
        self.og_numbers_list  = numbers_list
        self.og_len = len(urls_list)
        self.new_urls_list    = urls_list
        self.new_names_list   = names_list
        self.new_numbers_list = numbers_list
        self.new_index_in_og  = [i for i in range(len(urls_list))]
        self.new_len = len(urls_list)


    def new_to_og(self):
        self.new_urls_list    = self.og_urls_list
        self.new_names_list   = self.og_names_list
        self.new_numbers_list = self.og_numbers_list
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
