from typing  import Literal
from pathlib import Path
from tkinter import filedialog
from os import chdir



class Askers():
    downloads_path: Path

    # =========================================================================
    # ================================ GENERIC ================================
    # =========================================================================
    @staticmethod
    def ask_url() -> str:
        print("Enter URL of YouTube video or playlist:\n"
              "(input 'e' to exit program)\n>> ", end="")
        asker = input().strip()
        return asker


    @staticmethod
    def ask_save_ext() -> str:
        returns_dict = {
            "4": "mp4",
            "o": "ogg",
            "3": "mp3",
            "f": "flac",
            "r": "return"}

        while True:
            print("Choose file format for saving:\n"
                  "4 - mp4\n"
                  "o - ogg\n"
                  "3 - mp3\n"
                  "f - flac\n"
                  "r - Return\n>> ", end="")
            asker = input().lower().strip()

            if asker not in returns_dict:
                print("Invalid input!\n")
            else:
                return returns_dict[asker]


    @staticmethod
    def ask_save_path() -> Path | None:
        original_path = Path.cwd()
        chdir(Askers.downloads_path)
        folder_selected = filedialog.askdirectory(title="Select download folder")
        chdir(original_path)
        if folder_selected == "":
            return

        folder_selected = Path(folder_selected)
        return folder_selected


    # ==========================================================================
    # ================================ METADATA ================================
    # ==========================================================================
    @staticmethod
    def ask_which_md_embed(
        md_to_emb: dict[Literal[
            "album",
            "artist",
            "date",
            "title",
            "tracknumber"]:bool],
        md_album_set:  bool,
        md_artist_set: bool,
        md_date_set:   bool) -> Literal[
            "all_legal",
            "change_set_album",
            "change_set_artist",
            "change_set_date",
            "change_set_title",
            "change_set_tracknumber",
            "return",
            "exit"]:

        returns_dict = {
            "e": "all_legal",
            "l": "change_set_album",
            "a": "change_set_artist",
            "d": "change_set_date",
            "n": "change_set_title",
            "t": "change_set_tracknumber",
            "r": "return",
            "x": "exit"}

        # I know I'm lazy
        md_album_set_msg_1       = str(md_to_emb["album"]      ).replace("True", "Disable").replace("False", "Enable ")
        md_artist_set_msg_1      = str(md_to_emb["artist"]     ).replace("True", "Disable").replace("False", "Enable ")
        md_date_set_msg_1        = str(md_to_emb["date"]       ).replace("True", "Disable").replace("False", "Enable ")
        md_title_set_msg_1       = str(md_to_emb["title"]      ).replace("True", "Disable").replace("False", "Enable ")
        md_tracknumber_set_msg_1 = str(md_to_emb["tracknumber"]).replace("True", "Disable").replace("False", "Enable ")

        # I'm sure You'd do it better <3
        md_album_set_msg_2       = md_album_set_msg_1.replace(   "Disable", "enabled").replace("Enable ", "disabled")
        md_artist_set_msg_2      = md_artist_set_msg_1.replace(  "Disable", "enabled").replace("Enable ", "disabled")
        md_date_set_msg_2        = md_date_set_msg_1.replace(    "Disable", "enabled").replace("Enable ", "disabled")
        md_title_set_msg_2       = md_title_set_msg_1.replace(    "Disable", "enabled").replace("Enable ", "disabled")
        md_tracknumber_set_msg_2 = md_tracknumber_set_msg_1.replace("Disable", "enabled").replace("Enable ", "disabled")

        legality_to_set = {
            "l": md_album_set,
            "a": md_artist_set,
            "d": md_date_set}

        while True:
            print("Choose metadata to be embedded:\n"
                  "e - Enable embedding all metadata with set value\n"
                 f"l - {md_album_set_msg_1      } embedding album metadata       (currently {md_album_set_msg_2})\n"
                 f"a - {md_artist_set_msg_1     } embedding artist metadata      (currently {md_artist_set_msg_2})\n"
                 f"d - {md_date_set_msg_1       } embedding date metadata        (currently {md_date_set_msg_2})\n"
                 f"n - {md_title_set_msg_1      } embedding title metadata       (currently {md_title_set_msg_2})\n"
                 f"t - {md_tracknumber_set_msg_1} embedding tracknumber metadata (currently {md_tracknumber_set_msg_2})\n"
                  "r - Return\n"
                  "x - Exit\n"
                  ">> ", end='')
            asker = input().strip().lower()

            if asker in legality_to_set:
                if legality_to_set[asker] is False:
                    print("Can't enable embedding; value has to be set first\n\n")
                    continue

            if asker in returns_dict:
                return returns_dict[asker]
            else:
                print("Invalid input\n\n")


    @staticmethod
    def ask_set_album(current_album: str | None) -> str:
        if current_album == None:
            current_album = "Not set"

        print(f"Current album: {current_album}\n"
                "Input new album (leave empty to return):\n>> ", end='')
        asker = input()
        return asker


    @staticmethod
    def ask_set_artist(current_artist: str | None) -> str:
        if current_artist == None:
            current_artist = "Not set"

        print(f"Current artist: {current_artist}\n"
                "Input new artist (leave empty to return):\n>> ", end='')
        asker = input()
        return asker


    @staticmethod
    def ask_set_date(current_date: str | None) -> str:
        if current_date == None:
            current_date = "Not set"

        while True:
            print(f"Current date: {current_date}\n"
                   "Input new date (leave empty to return):\n>> ", end='')
            asker = input().strip()

            if (asker.isdigit() and
                len(asker) == 4):
                return asker
            elif asker == "":
                return asker
            else:
                print("Invalid input\n\n")


    @staticmethod
    def ask_md_title_string(curr_title: str) -> str | None:
        while True:
            print(curr_title)
            print(f"Input new title metadata:\n"
                   "(leave empty to return)\n"
                   ">> ", end='')
            asker = input()

            if asker == "":
                return
            return asker


    @staticmethod
    def ask_md_tracknumber_string(curr_tracknumber: str) -> str | None:
        while True:
            print(f"Current number: {curr_tracknumber}")
            print(f"Input new tracknumber metadata:\n"
                   "(leave empty to return)\n"
                   ">> ", end='')
            asker = input()

            if asker == "":
                return
            if not asker.isdigit():
                print("Invalid input\n\n")
                continue

            return asker


    # ==========================================================================
    # ================================= SINGLE =================================
    # ==========================================================================
    @staticmethod
    def ask_single_menu(
            md_possible: bool = True,
            download_md: bool = False
            ) -> str:
        returns_dict = {
            "f": "change_format",
            "p": "change_save_path",
            "l": "change_link",
            "d": "download",
            "x": "exit"}
        if md_possible:
            returns_dict["m"] = "metadata_settings"

        download_string = (
            "(with metadata)"
            if download_md
            else "(no metadata)"
            if md_possible
            else "")

        while True:
            print("f - Change saving format\n"
                  "p - Change save path")
            if md_possible:
                print("m - Metadata settings")
            print("l - Change link\n"
                 f"d - Download {download_string}\n"
                  "x - Exit program\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_single_md(
        md_included: bool,
        md_to_emb:   dict[Literal["album", "artist", "date", "title", "tracknumber"]:bool],
        md_album_set:  bool,
        md_artist_set: bool,
        md_date_set:   bool,
        md_tracknum_set: bool
        ) -> Literal[
            "change_appending",
            "which_md_embedded",
            "set_album",
            "set_artist",
            "set_date",
            "set_title",
            "set_tracknumber",
            "return",
            "exit"]:
        returns_dict = {
            "a":  "change_appending",
            "e":  "which_md_embedded",
            "sl": "set_album",
            "sa": "set_artist",
            "sd": "set_date",
            "sn": "set_title",
            "st": "set_tracknumber",
            "r":  "return",
            "x":  "exit"}

        md_album_set_msg       = str(md_to_emb["album"]      ).replace("True", "True ")
        md_artist_set_msg      = str(md_to_emb["artist"]     ).replace("True", "True ")
        md_date_set_msg        = str(md_to_emb["date"]       ).replace("True", "True ")
        md_title_set_msg       = str(md_to_emb["title"]      ).replace("True", "True ")
        md_tracknumber_set_msg = str(md_to_emb["tracknumber"]).replace("True", "True ")
        able_msg = ("Disable metadata appending"
                    if md_included
                    else "Enable metadata appending")

        while True:
            print(f"a  - {able_msg}\n"
                   "e  - Specify which metadata will be embedded\n"
                  f"sl - Set album       (Embed: {md_album_set_msg      }) (Is set: {md_album_set})\n"
                  f"sa - Set artist      (Embed: {md_artist_set_msg     }) (Is set: {md_artist_set})\n"
                  f"sd - Set date        (Embed: {md_date_set_msg       }) (Is set: {md_date_set})\n"
                  f"sn - Set title       (Embed: {md_title_set_msg      }) (Is set: True)\n" #Troll!
                  f"st - Set tracknumber (Embed: {md_tracknumber_set_msg}) (Is set: {md_tracknum_set})\n"
                   "r  - Return\n"
                   "x  - Exit program\n"
                   ">> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n\n")
        return ""
