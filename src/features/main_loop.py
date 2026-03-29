from typing  import Literal
from pathlib import Path

from src.common.askers import Askers
from src.common.utils  import Utils
import src.features.save_single as save_single
import src.features.save_plist  as save_plist



proj_path = Path(__file__).resolve().parent.parent.parent
settings_path = Path(proj_path) / "settings.json"
Utils.settings_path = settings_path

downloads_path = Path(proj_path) / "downloads"
Askers.downloads_path = downloads_path
path_in_setts = Utils.get_val_from_settings("SAVE_PATH")
if path_in_setts == "None":
    Utils.save_value_to_settings("SAVE_PATH", downloads_path)


def main_loop() -> None:
    print()
    while True:
        print("=============================================================\n"
              "=======================  Welcome to   =======================\n"
              "======================= YT Downloader =======================\n"
              "=============================================================\n")
        # Get url from user and clean it
        url = Askers.ask_url()
        if url == "e":
            return
        cleaned_url = Utils.clean_url(url)
        if cleaned_url != url:
            url = cleaned_url
            print("Your link has been cleaned of fluff.")

        url_type: Literal[
            'plist',
            'single',
            'invalid'] = Utils.determine_url_type(url)

        if not url_type:
            print("Invalid URL.\n\n")
            continue

        print()
        # Single stuff
        if url_type == "single":
            print()
            exit_flag = save_single.save_single(url)
            if exit_flag:
                return
            else:
                continue

        # Playlist stuff
        elif url_type == 'plist':
            print()
            exit_flag = save_plist.save_plist(url)
            if exit_flag:
                return
            else:
                continue
