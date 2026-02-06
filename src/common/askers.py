from tkinter import filedialog
import os



class Askers():
    downloads_path: str


    @staticmethod
    def ask_url() -> str | None:
        print("Enter URL of YouTube video or playlist:\n"
              "(input 'exit' to exit program)\n>> ", end="")
        asker = input().strip()

        #If user copies browser link when on vid from playlist
        #ID tracker lmao
        #A/B testing
        #How opened
        #Promotion
        #Time stamp
        bad_stuff = ['&list', '&si', '&ab_channel', '&feature', '&pp', '&t']

        if asker == "exit":
            return
        for el in bad_stuff:
            if el in asker:
                asker = asker[:asker.find(el)]

        return asker


    @staticmethod
    def ask_save_ext() -> str:
        returns_dict = {
            "4": "mp4",
            "3": "mp3",
            "f": "flac"}

        while True:
            print("Choose file format for saving:\n"
                  "4 - mp4\n"
                  "3 - mp3\n"
                  "f - flac\n>> ", end="")
            asker = input().lower().strip()

            if asker not in returns_dict:
                print("Invalid input!\n")
            else:
                return returns_dict[asker]


    @staticmethod
    def ask_save_path():
        original_path = os.getcwd()
        os.chdir(Askers.downloads_path)
        folder_selected = filedialog.askdirectory(title="Select download folder")
        os.chdir(original_path)
        return folder_selected
