from src.common.askers import Askers
from src.common.utils import determine_url_type
from .save_single import save_single
from .save_plist import save_plist
from typing import Literal



def main_loop() -> None:
    print()
    while True:
        print("=============================================================")
        print("=======================  Welcome to   =======================")
        print("======================= YT Downloader =======================")
        print("=============================================================\n")
        url = Askers.ask_url()
        if url == "exit":
            return
        url_type: Literal['plist', 'single', 'invalid'] = determine_url_type(url)

        if url_type == 'plist':
            print()
            save_plist(url)
        elif url_type == "single":
            print()
            save_single(url)
        elif url_type == "invalid":
            print("Invalid URL.\n")
