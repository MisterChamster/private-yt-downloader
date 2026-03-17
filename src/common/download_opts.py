from src.common.utils import Utils



class Download_Opts():
    save_format: str  #= Utils.get_val_from_settings("PLIST_SAVE_FORMAT")
    save_path:   str  #= Utils.get_val_from_settings("SAVE_PATH")
    ydl_opts:    dict #= Utils.get_ydl_options(save_format)

    def __init__(self) -> None:
        self.save_format = Utils.get_val_from_settings("PLIST_SAVE_FORMAT")
        self.save_path   = Utils.get_val_from_settings("SAVE_PATH")
        self.reset_ydl()


    def mutate_ydl(self, ydl_key: str, ydl_val) -> None:
        self.ydl_opts[ydl_key] = ydl_val

    def reset_ydl(self) -> None:
        self.ydl_opts = Utils.get_ydl_options(self.save_format)
