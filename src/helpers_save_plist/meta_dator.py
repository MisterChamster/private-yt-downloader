class Meta_Dator():
    md_artist:    str
    md_date:      str
    md_album:     str
    md_names:     list[str]
    md_tracknums: list[str]


    def __init__(
            self,
            el_count: int,
            md_album:           str | None = None,
            md_artist:          str | None = None,
            md_date:            str | None = None,
            md_names:     list[str] | None = None,
            md_tracknums: list[str] | None = None):

        self.md_album = md_album
        self.md_artist = md_artist
        self.md_date = md_date
