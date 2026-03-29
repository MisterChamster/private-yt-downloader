class Meta_Dator():
    md_names:     list[str]
    md_tracknums: list[str]
    md_artist:    str
    md_date:      str
    md_album:     str


    def __init__(
            self,
            md_names:     list[str],
            md_tracknums: list[str] = None,
            md_album:    str | None = None,
            md_artist:   str | None = None,
            md_date:     str | None = None):

        self.md_names  = md_names
        self.md_album  = md_album
        self.md_artist = md_artist
        self.md_date   = md_date

        if md_tracknums == None:
            self.md_tracknums = [
                num+1
                for num
                in range(len(md_names))]
        else:
            self.md_tracknums = md_tracknums


    def pop_md_lists(self, index: int) -> None:
        self.md_names.pop(index)
        self.md_tracknums.pop(index)


    def pop_md_list_range(self, index_s: int, index_e: int) -> None:
        del(self.md_names[index_s:index_e])
        del(self.md_tracknums[index_s:index_e])
