from src.common.askers import Askers
from src.common.utils  import Utils
from src.common.download_opts import Download_Opts
from src.helpers_save_plist.meta_dator import Meta_Dator
import src.common.ydl_support as ydl_support



def save_single(url: str) -> bool:
    opts = Download_Opts()
    video_title = ydl_support.get_video_title(url)
    metadata = Meta_Dator([video_title])

    while True:
        print()
        print(f"Video:     {video_title}")
        print(f"Format:    {opts.save_format}")
        print(f"Save path: {opts.save_path}")
        print()
        asker_single = Askers.ask_single_menu(
            opts.save_format in ("mp3", "ogg", "flac"))
        print("\n")

        if asker_single == "change_format":
            asker = Askers.ask_save_ext()
            print("\n")
            if asker in (opts.save_format, "return"):
                continue

            opts.set_save_format(asker)
            opts.reset_ydl()

        elif asker_single == "change_save_path":
            asker = Askers.ask_save_path()
            if asker is None:
                print("Empty path was chosen.\n\n")
                continue
            if not asker.exists():
                print("Invalid path.\n\n")
                continue

            opts.set_save_path(asker)

        elif asker_single == "metadata_settings":
            print("MD SETTINGS HIII")
            pass

        elif asker_single == "change_link":
            return False

        elif asker_single == "download":
            save_path_string = str(opts.save_path)
            opts.mutate_ydl("paths", {"home": save_path_string})

            filename = Utils.illegal_char_remover(video_title)
            i = 1
            while True:
                file_name_and_ext = f"{filename}.{opts.save_format}"
                predicted_file_path = opts.save_path / file_name_and_ext
                if not predicted_file_path.exists():
                    break
                filename += "_d"*i
                i += 1
            opts.mutate_ydl("outtmpl", filename)

            print("Downloading...")
            download_flag = ydl_support.download_fromyt(opts.ydl_opts, url)
            if download_flag:
                print(f"{filename} has been successfully downloaded.\n\n")

        elif asker_single == "exit":
            return True
