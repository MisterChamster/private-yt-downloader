from os import path

from src.common.askers import Askers
from src.common.utils  import Utils
from src.common.download_opts import Download_Opts
import src.common.ydl_support as ydl_support



def save_single(url: str) -> str:
    opts = Download_Opts()
    video_title = ydl_support.get_video_title(url)

    while True:
        print()
        print(f"Video:     {video_title}")
        print(f"Format:    {opts.save_format}")
        print(f"Save path: {opts.save_path}")
        print()
        asker = Askers.ask_single_menu()
        print("\n")

        if asker == "change_format":
            asker = Askers.ask_save_ext()
            print("\n")
            if asker in (opts.save_format, "return"):
                continue

            opts.save_format = asker
            opts.reset_ydl()
            Utils.save_value_to_settings("PLIST_SAVE_FORMAT", asker)

        elif asker == "change_save_path":
            opts.save_path = Askers.ask_save_path()
            print("\n")

            if opts.save_path == "":
                print("Empty path was chosen.\n\n")
                continue
            if not path.exists(opts.save_path):
                print("Invalid path.\n\n")
                continue

            Utils.save_value_to_settings("SAVE_PATH", opts.save_path)

        elif asker == "change_link":
            return "repeat"

        elif asker == "download":
            opts.mutate_ydl("paths", {"home": opts.save_path})

            filename = Utils.illegal_char_remover(video_title)
            i = 1
            while path.exists(filename + f".{opts.save_format}"):
                filename += "_d"*i
                i += 1
            opts.mutate_ydl("outtmpl", filename)

            print("Downloading...")
            download_flag = ydl_support.download_fromyt(opts.ydl_opts, url)
            if download_flag:
                print(f"{filename} has been successfully downloaded.\n\n")

        elif asker == "exit":
            return "exit"
