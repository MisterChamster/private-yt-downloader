from typing  import Literal
from pathlib import Path
from tkinter import filedialog
from os import chdir



class Askers():
    downloads_path: Path

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


    @staticmethod
    def ask_single_menu(md_possible: bool = True) -> str:
        returns_dict = {
            "f": "change_format",
            "p": "change_save_path",
            "l": "change_link",
            "d": "download",
            "x": "exit"}
        if md_possible:
            returns_dict["m"] = "metadata_settings"

        while True:
            print("f - Change saving format\n"
                  "p - Change save path")
            if md_possible:
                print("m - Metadata settings")
            print("l - Change link\n"
                  "d - Download\n"
                  "x - Exit program\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n")


    @staticmethod
    def ask_single_md(
        md_included: bool,
        md_to_emb:     dict[Literal["album", "artist", "date", "title", "tracknumber"]:bool]
        ) -> Literal[
            "change_appending",
            "set_album",
            "set_artist",
            "set_date",
            "set_title",
            "set_tracknumber",
            "return",
            "exit"]:
        returns_dict = {
            "a": "change_appending",
            "sl": "set_album",
            "sa": "set_artist",
            "sd": "set_date",
            "sn": "set_title",
            "st": "set_tracknumber",
            "r": "return",
            "x": "exit"}
        
        md_album_set_msg       = str(md_to_emb["album"]      ).replace("True", "True ")
        md_artist_set_msg      = str(md_to_emb["artist"]     ).replace("True", "True ")
        md_date_set_msg        = str(md_to_emb["date"]       ).replace("True", "True ")
        md_title_set_msg       = str(md_to_emb["title"]      ).replace("True", "True ")
        md_tracknumber_set_msg = str(md_to_emb["tracknumber"]).replace("True", "True ")
        able_msg = ("Disable metadata appending"
                    if md_included
                    else "Enable metadata appending")

        while True:
            print(f"a - {able_msg}\n"
                   " - \n"
                  f"sl - Set album        (Embed: {md_album_set_msg      })\n"
                  f"sa - Set artist       (Embed: {md_artist_set_msg     })\n"
                  f"sd - Set date         (Embed: {md_date_set_msg       })\n"
                  f"sn - Set titles       (Embed: {md_title_set_msg      })\n"
                  f"st - Set tracknumbers (Embed: {md_tracknumber_set_msg})\n"
                   "r - Return\n"
                   "x - Exit program\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n\n")
        return ""
