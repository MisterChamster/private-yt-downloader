from src.common.askers import Askers
from src.common.utils import determine_url_type, clean_url
from .save_single import save_single
from .save_plist import save_plist
from typing import Literal
from pathlib import Path



src_path = Path(__file__).resolve().parent.parent
downloads_path = str(src_path.parent / "downloads")
Askers.downloads_path = downloads_path

def main_loop() -> None:
    print()
    while True:
        print("=============================================================\n"
              "=======================  Welcome to   =======================\n"
              "======================= YT Downloader =======================\n"
              "=============================================================\n")
        url = Askers.ask_url()
        if not url:
            return
        cleaned_url = clean_url(url)
        if cleaned_url != url:
            url = cleaned_url
            print("Your link has been cleaned of fluff.")
        url_type: Literal['plist', 'single', 'invalid'] = determine_url_type(url)

        if not url_type:
            print("Invalid URL.\n")
        elif url_type == 'plist':
            print()
            save_plist(url)
        elif url_type == "single":
            print()
            save_single(url)
