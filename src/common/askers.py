from tkinter import filedialog
import os



class Askers():
    @staticmethod
    def ask_url():
        print("Enter URL of YouTube video or playlist:\n" \
        "(input 'exit' to exit program)" \
        "\n>> ", end="")

        url = input()
        if '&list=' in url:
            url = url[:url.find('&list=')]
        return url


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
            asker = input()

            if asker not in returns_dict:
                print("Invalid input!\n")
            else:
                return returns_dict[asker]


    @staticmethod
    def ask_save_path():
        original_path = os.getcwd()
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        os.chdir(desktop_path)
        folder_selected = filedialog.askdirectory(title="Select download folder")
        os.chdir(original_path)
        return folder_selected
