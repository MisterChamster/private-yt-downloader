class Meta_Dator():
    md_artist:    str
    md_date:      str
    md_album:     str
    md_names:     list[str]
    md_tracknums: list[str]


    def __init__(
            self,
            md_artist:          str = "",
            md_date:            str = "",
            md_album:           str = "",
            md_names:     list[str] = [],
            md_tracknums: list[str] = []):

        self.md_artist = md_artist
        self.md_artist = md_date
        self.md_artist = md_album
        self.md_artist = md_names
        self.md_artist = md_tracknums
