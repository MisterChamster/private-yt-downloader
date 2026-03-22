from pathlib import Path

from src.common.utils import Utils



class Download_Opts():
    save_format: str
    save_path:   Path
    ydl_opts:    dict

    def __init__(self) -> None:
        self.save_format = Utils.get_val_from_settings("SAVE_FORMAT")
        self.save_path   = Utils.get_val_from_settings("SAVE_PATH")
        self.save_path   = Path(self.save_path)
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
