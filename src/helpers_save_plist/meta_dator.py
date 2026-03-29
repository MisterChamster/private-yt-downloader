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
