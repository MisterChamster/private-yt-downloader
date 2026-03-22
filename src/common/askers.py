from tkinter import filedialog
from pathlib import Path
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
    def ask_single_menu() -> str:
        returns_dict = {
            "f": "change_format",
            "p": "change_save_path",
            "l": "change_link",
            "d": "download",
            "e": "exit"}

        while True:
            print("f - Change saving format\n"
                  "p - Change save path\n"
                  "l - Change link\n"
                  "d - Download\n"
                  "e - Exit program\n>> ", end="")
            action = input().strip().lower()

            if action in returns_dict:
                return returns_dict[action]
            else:
                print("Incorrect input.\n")
