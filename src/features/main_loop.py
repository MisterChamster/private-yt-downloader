from typing import Literal
from pathlib import Path

from src.common.askers import Askers
from src.common.utils import Utils
from .save_single import save_single
from .save_plist import save_plist



src_path = Path(__file__).resolve().parent.parent
downloads_path = str(src_path.parent / "downloads")
Askers.downloads_path = downloads_path
settings_path = str(src_path / "settings.json")

def main_loop() -> None:
    print()
    while True:
        print("=============================================================\n"
              "=======================  Welcome to   =======================\n"
              "======================= YT Downloader =======================\n"
              "=============================================================\n")
        # Get url from user and clean it
        url = Askers.ask_url()
        if not url:
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
            print("Invalid URL.\n")

        # Single stuff
        elif url_type == "single":
            print()
            save_single(url)

        # Playlist stuff
        elif url_type == 'plist':
            print()
            save_plist(url)
