from yt_dlp import  YoutubeDL
from pathlib import Path

from os import path
from src.common.askers import Askers
from src.common.utils  import Utils
from src.common.ydl_support import get_video_title



def save_single(url: str) -> str:
    save_format = Utils.get_val_from_settings("PLIST_SAVE_FORMAT")
    save_path   = Utils.get_val_from_settings("SAVE_PATH")
    ydl_opts    = Utils.get_ydl_options(save_format)
    video_title = get_video_title(url)

    while True:
        print()
        print(f"Video:     {video_title}")
        print(f"Format:    {save_format}")
        print(f"Save path: {save_path}")
        print()
        asker = Askers.ask_single_menu()
        print("\n")

        if asker == "change_format":
            extension = Askers.ask_save_ext()
            print("\n")
            if extension in (save_format, "return"):
                continue

            ydl_opts = Utils.get_ydl_options(extension)
            save_format = extension
            Utils.save_value_to_settings("PLIST_SAVE_FORMAT", extension)

        elif asker == "change_save_path":
            save_path = Askers.ask_save_path()
            print("\n")

            if save_path == "":
                print("Empty path was chosen.\n\n")
                continue
            if not path.exists(save_path):
                print("Invalid path.\n\n")
                continue

            Utils.save_value_to_settings("SAVE_PATH", save_path)

        elif asker == "change_link":
            return "repeat"

        elif asker == "download":
            pass

        elif asker == "exit":
            return "exit"

    pass



    if save_path == "":
        print("Empty path was chosen.")
        return
    ydl_opts["paths"] = {"home": save_path}

    finalname = Utils.illegal_char_remover(video_title)
    i = 1
    while path.exists(str(Path(save_path) / finalname)):
        finalname += "_d"*i
        i += 1
    ydl_opts["outtmpl"] = finalname

    print("Downloading...")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"{finalname} has been successfully downloaded.\n\n")
    except:
        if not Utils.is_internet_available():
            print("Internet connection failed.\n\n")
        else:
            print("Something went wrong.\n\n")
        return
