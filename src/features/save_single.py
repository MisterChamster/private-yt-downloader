from src.common.askers import Askers
from src.common.utils  import Utils
from src.common.download_opts import Download_Opts
from src.helpers_save_plist.meta_dator import Meta_Dator
from src.helpers_save_plist.plist_askers import Plist_Askers
import src.common.ydl_support as ydl_support



def save_single(url: str) -> bool:
    opts = Download_Opts()
    video_title = ydl_support.get_video_title(url)
    metadator = Meta_Dator([video_title], single=True)

    while True:
        print()
        print(f"Video:     {video_title}")
        print(f"Format:    {opts.save_format}")
        print(f"Save path: {opts.save_path}")
        print()
        download_md = opts.is_md_saved()
        asker_single = Askers.ask_single_menu(
            opts.save_format in ("mp3", "ogg", "flac"),
            download_md)
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
            while True:
                asker = Askers.ask_single_md(
                    opts.include_md,
                    opts.md_to_emb)

                if asker == "change_appending":
                    opts.change_include_md()

                elif asker == "set_album":
                    asker = Plist_Askers.ask_set_album(
                        metadator.md_album)
                    print("\n")
                    if asker == "":
                        continue
                    opts.set_md_to_embed("album", True)
                    metadator.md_album = asker

                elif asker == "set_artist":
                    asker = Plist_Askers.ask_set_artist(
                        metadator.md_artist)
                    print("\n")
                    if asker == "":
                        continue
                    opts.set_md_to_embed("artist", True)
                    metadator.md_artist = asker

                elif asker == "set_date":
                    asker = Plist_Askers.ask_set_date(
                        metadator.md_date)
                    print("\n")
                    if asker == "":
                        continue
                    opts.set_md_to_embed("date", True)
                    metadator.md_date = asker

                elif asker == "set_title":
                    asker = Plist_Askers.ask_md_title_string(
                        metadator.md_titles[0])
                    print("\n")
                    if asker == "":
                        continue
                    opts.set_md_to_embed("title", True)
                    metadator.md_titles[0] = asker

                elif asker == "set_tracknumber":
                    asker = Plist_Askers.ask_md_tracknumber_string(
                        metadator.md_tracknumbers[0])
                    print("\n")
                    if asker == "":
                        continue
                    opts.set_md_to_embed("tracknumber", True)
                    metadator.md_tracknumbers[0] = asker

                elif asker == "return":
                    break

                elif asker == "exit":
                    return True

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
