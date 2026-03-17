from src.common.utils import Utils



class Download_Opts():
    save_format: str  #= Utils.get_val_from_settings("PLIST_SAVE_FORMAT")
    save_path:   str  #= Utils.get_val_from_settings("SAVE_PATH")
    ydl_opts:    dict #= Utils.get_ydl_options(save_format)

    def __init__(self):
        self.save_format = Utils.get_val_from_settings("PLIST_SAVE_FORMAT")
        self.save_path   = Utils.get_val_from_settings("SAVE_PATH")
        self.ydl_opts    = Utils.get_ydl_options(self.save_format)
