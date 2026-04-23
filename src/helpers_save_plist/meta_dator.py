class Meta_Dator():
    md_titles:       list[str]
    md_tracknumbers: list[str]
    md_artist:       str
    md_date:         str
    md_album:        str


    def __init__(
            self,
            single:                bool,
            md_titles:        list[str],
            md_tracknumbers:  list[str] = [None],
            md_album:        str | None = None,
            md_artist:       str | None = None,
            md_date:         str | None = None):

        self.md_titles  = md_titles
        self.md_album   = md_album
        self.md_artist  = md_artist
        self.md_date    = md_date

        if md_tracknumbers == [None] and not single:
            self.recalc_tracknums()
        else:
            self.md_tracknumbers = md_tracknumbers


    def recalc_tracknums(self) -> None:
        self.md_tracknumbers = [
            str(num+1)
            for num
            in range(len(self.md_titles))]


    def pop_md_lists(self, index: int) -> None:
        self.md_titles.pop(index)
        # self.md_tracknumbers.pop(index)
        self.recalc_tracknums()


    def pop_md_list_range(self, index_s: int, index_e: int) -> None:
        del(self.md_titles[index_s:index_e])
        # del(self.md_tracknumbers[index_s:index_e])
        self.recalc_tracknums()
