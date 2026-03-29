from typing  import Literal
from pathlib import Path

from src.common.utils import Utils



class Download_Opts():
    save_format: str
    save_path:   Path
    include_md:  bool
    md_to_emb:   dict[str: bool]
    ydl_opts:    dict

    def __init__(self) -> None:
        self.save_format = Utils.get_val_from_settings("SAVE_FORMAT")
        self.save_path   = Utils.get_val_from_settings("SAVE_PATH")
        self.include_md  = Utils.get_val_from_settings("INCLUDE_METADATA")
        self.save_path   = Path(self.save_path)
        self.md_to_emb   = {"album":       False,
                            "artist":      False,
                            "date":        False,
                            #These will be True bc I want to nye hye hye
                            "title":       True,
                            "tracknumber": True}
        self.reset_ydl()


    def mutate_ydl(self, ydl_key: str, ydl_val) -> None:
        self.ydl_opts[ydl_key] = ydl_val

    def reset_ydl(self) -> None:
        self.ydl_opts = Utils.get_ydl_options(self.save_format)

    def set_save_format(self, new_format: str) -> None:
        self.save_format = new_format
        Utils.save_value_to_settings("SAVE_FORMAT", new_format)

    def set_save_path(self, new_path: Path) -> None:
        self.save_path = new_path
        Utils.save_value_to_settings("SAVE_PATH", str(new_path))

    def change_include_md(self) -> None:
        self.include_md = not self.include_md
        Utils.save_value_to_settings("INCLUDE_METADATA", self.include_md)

    def is_md_saved(self) -> bool:
        if not self.include_md:
            return False

        audio_formats = ("mp3", "ogg", "flac")
        if not self.save_format in audio_formats:
            return False
        return True

    def change_md_to_embed(self, md_key: Literal[
            "album",
            "artist",
            "date",
            "title",
            "tracknumber"]) -> None:
        current_val = self.md_to_emb[md_key]
        self.md_to_emb[md_key] = not current_val

    def set_md_to_embed(self,
            md_key: Literal[
            "album",
            "artist",
            "date",
            "title",
            "tracknumber"],
            set_val: bool) -> None:
        self.md_to_emb[md_key] = set_val

